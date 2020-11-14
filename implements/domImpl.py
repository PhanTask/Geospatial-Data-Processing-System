# -*- coding:utf-8 -*-
"""
domImpl.py
~~~~~~~~~~

DOM模块功能实现。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from osgeo import gdal
import ogr
import os
import time
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import numpy as np
from shapely.geometry import shape,Polygon
from shapely.ops import cascaded_union, unary_union
import json
import shutil

class domImpl(QtCore.QThread):
    """
    处理dom任务。
    """
    # infomsgSignal = QtCore.Signal( str ) # 日志signal
    # processSignal = QtCore.Signal( int ) # 进度signal
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    domTableItemDataSignal = QtCore.Signal(object) # dom表格项signal
    dostop = False # 是否强制终止
    processValue = 0.0#mp.Value("d",0.0) # 进度
    domPathList = []
    shpPathList = []
    domFileNum = 0
    def __init__(self, domDirPath, domDirOutputPath, outlierValue = 0, nearDist = 0, maxNonBlack = 0, delNum = 0, fileType = "img", ovrBuild = True, nodataFill = True, c254 = True, easyKill = False, easyColors = 0, easyNearDist = 5):
        """
        初始化domImpl类。

        :param domDirPath: dom文件夹路径
        :param outlierValue: 指定的异常值，如白边为255，黑边为0
        :param nearDist: 距离指定异常值相差指定值的像元也当做异常值。如outlierValue = 250，nearDist = 5，则246~255都算异常值
        :param maxNonBlack: 边缘修正因子，用于改善边缘渗透问题
        :param delNum: 内扩距离，可指定为int
        :param fileType: 指定输出的dom文件格式，默认为img，可指定为img或tif
        :param ovrBuild: 指定是否生成ovr格式影像金字塔文件，默认为True，可指定为Boolean值
        :param nodataFill: 指定是否将结果影像中的NoData区域填充为0值，默认为True，可指定为Boolean值
        """
        super(domImpl, self).__init__()
        self.domDirPath = domDirPath
        self.domDirOutputPath = domDirOutputPath
        self.outlierValue = outlierValue
        self.nearDist = nearDist
        self.maxNonBlack = maxNonBlack
        self.delNum = delNum
        self.fileType = fileType
        self.ovrBuild = ovrBuild
        self.nodataFill = nodataFill
        self.c254 = c254
        self.easyColors = easyColors
        self.easyNearDist = easyNearDist
        self.easyKill = easyKill
        self.domCount = 0
        self.logRcd = logRcd('DOM影像异常值检查日志')

    def emitFinish( self, isSuccessful):
        self.doneflag.emit( isSuccessful )

    def emitDomTableItemData(self, DomTableItemData):
        self.domTableItemDataSignal.emit(DomTableItemData)

    def run(self, *args, **kwargs):
        """
        在本线程中执行算法。

        :return: None
        """
        try:
            domFileNum = self.getDomPathList()
            self.domOutlierRemover(domFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getDomPathList(self):
        """
        从所给的dom文件夹路径中将所有dom的路径提取出来。

        :return: dom数据数量，即dom文件夹数量
        """
        self.domPathExtList = []
        for item in os.listdir(self.domDirPath):
            path = self.domDirPath + '/' + item
            if os.path.isdir(path):
                pathTemp = path + '/' + item
                if os.path.exists(pathTemp + '.img'):
                    self.domPathExtList.append(pathTemp + '.img')
                elif os.path.exists(pathTemp + '.tif'):
                    self.domPathExtList.append(pathTemp + '.tif')
                else:
                    print("There is no .img or .tif images in this dir: " + path.__str__())
            else:
                if path.rsplit('.',1)[1] == 'img' or path.rsplit('.',1)[1] == 'tif':
                    self.domPathExtList.append(path)
        # self.domPathNoExtList = [ self.domDirPath + '/' + dir + '/' + dir  for dir in os.listdir(self.domDirPath)]
        # #print(self.domPathList)
        # self.domPathNoExtList += [ self.domDirPath + '/' + dir for dir in os.listdir(self.domDirPath)]
        return self.domPathExtList.__len__()

    @staticmethod
    def pyNearBlack(dstFilename,srcFilename,domFileNum,**kwargs):
        """
        执行剔除异常值操作，为静态函数，是对gdal.Nearblack的封装。

        :param dstFilename: 处理后数据文件路径名
        :param srcFilename: 原始数据文件路径名
        :param domFileNum: 原始数据个数
        :param kwargs: 参数
        :return: (dstFilename,srcFilename,domFileNum,mskList)
        """
        try:
            blockSize = 2048
            gdal.AllRegister()
            gdal.SetConfigOption('TIFF_USE_OVR', 'YES')
            gdal.SetConfigOption('HFA_USE_RRD', 'YES')
            # gdal.SetConfigOption('JPEG_QUALITY_OVERVIEW', '50')
            # gdal.SetConfigOption('HFA_COMPRESS_OVR', 'YES')
            imgdriver = gdal.GetDriverByName('HFA')
            driver = gdal.GetDriverByName(kwargs['format'])
            domSrcDS = gdal.Open(srcFilename)

            COMPRESSoptions = ['COMPRESS=RLE']
            if kwargs['ext'] != 'img':
                COMPRESSoptions = ['COMPRESS=LZW','TFW=YES','GEOTIFF_KEYS_FLAVOR=ESRI_PE']# ,'PREDICTOR=2'

            domDstDS = driver.Create(dstFilename, domSrcDS.RasterXSize, domSrcDS.RasterYSize,
                                     domSrcDS.RasterCount, gdal.GDT_Byte, options=COMPRESSoptions)

            GeoTransform = domSrcDS.GetGeoTransform()
            Projection = domSrcDS.GetProjection()
            domDstDS.SetGeoTransform(GeoTransform)
            domDstDS.SetProjection(Projection)

            #简单去边模式#改成convex
                # rowNum = domDstDS.RasterYSize
                # columnNum = domDstDS.RasterXSize
                #
                # vRowNum = rowNum/10
                # hColNum = columnNum/10
                #
                # for i in range(domDstDS.RasterCount):
                #     srcband = domSrcDS.GetRasterBand(i + 1)
                #     band = domDstDS.GetRasterBand(i + 1)
                #     upArray = srcband.ReadAsArray(0, 0, columnNum, vRowNum)
                #     downArray = srcband.ReadAsArray(0, 9 * vRowNum, columnNum, rowNum)
                #     leftArray = srcband.ReadAsArray(0, vRowNum, hColNum, 9 * vRowNum)
                #     rightArray = srcband.ReadAsArray(9 * hColNum, vRowNum, columnNum, 9 * vRowNum)
                #
                #     # temparray = np.where(temparray == 255, 254, temparray)
                #     # temp = np.where(tempmask == 0, 255, temparray)
                #     # band.WriteArray(temp, colstep * blockSize, rowstep * blockSize)

                # for rowstep in range(rowblockNum):
                #     for colstep in range(colblockNum):
                #         rowpafNum = blockSize
                #         colpafNum = blockSize
                #         if (rowstep == rowblockNum - 1):
                #             rowpafNum = int((rowNum - 1) % blockSize) + 1
                #         if (colstep == colblockNum - 1):
                #             colpafNum = int((columnNum - 1) % blockSize) + 1
                #         for i in range(domDstDS.RasterCount):
                #             srcband = domSrcDS.GetRasterBand(i + 1)
                #             band = domDstDS.GetRasterBand(i + 1)
                #             band.SetNoDataValue(255)
                #             temparray = srcband.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                #             tempmask = mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                #             temparray = np.where(temparray == 255, 254, temparray)
                #             temp = np.where(tempmask == 0, 255, temparray)
                #             band.WriteArray(temp, colstep * blockSize, rowstep * blockSize)
                #

                # ====================================================================================

                # rowNum = domDstDS.RasterYSize
                # columnNum = domDstDS.RasterXSize
                #
                # rowblockNum = int((rowNum - 1) / blockSize) + 1
                # colblockNum = int((columnNum - 1) / blockSize) + 1
                #
                # gdal.Nearblack(domDstDS,
                #                domSrcDS,
                #                    format=kwargs['format'],
                #                    colors=[tuple(kwargs['easyColors'] for i in range(domSrcDS.RasterCount))],
                #                    nearDist=kwargs['easyNearDist'],
                #                    maxNonBlack=1,
                #                    setMask=True,
                #                    )
                # domDstDS = None
                # domDstDS = gdal.Open(dstFilename,gdal.GA_Update)
                #
                # # 通过msk文件统计总像元数量和异常像元数量
                # mskDs = gdal.Open(dstFilename + '.msk')
                # mskBand = mskDs.GetRasterBand(1)
                # mskList = mskBand.GetHistogram(-0.5,255.5,buckets = 256, include_out_of_range = 0,approx_ok = 0)
                # for rowstep in range(rowblockNum):
                #     for colstep in range(colblockNum):
                #         rowpafNum = blockSize
                #         colpafNum = blockSize
                #         if (rowstep == rowblockNum - 1):
                #             rowpafNum = int((rowNum - 1) % blockSize) + 1
                #         if (colstep == colblockNum - 1):
                #             colpafNum = int((columnNum - 1) % blockSize) + 1
                #         for i in range(domDstDS.RasterCount):
                #             srcband = domSrcDS.GetRasterBand(i + 1)
                #             band = domDstDS.GetRasterBand(i + 1)
                #             band.SetNoDataValue(255)
                #             temparray = srcband.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                #             tempmask = mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                #             # temparray = np.where(temparray == 255, 254, temparray)
                #             temp = np.where(tempmask == 0, 254, temparray)
                #             band.WriteArray(temp, colstep * blockSize, rowstep * blockSize)
                #
                # if kwargs['ovrBuild'] is True:
                #     domDstDS.BuildOverviews("NEAREST", [2, 4, 8])
                #
                # domSrcDS = None
                # domDstDS = None
                # mskDs = None
                #
                # # ====================================================================================
                #
                # # print('easyKill == True')
                # # rowNum = domDstDS.RasterYSize
                # # columnNum = domDstDS.RasterXSize
                # #
                # # rowblockNum = int((rowNum - 1) / blockSize) + 1
                # # colblockNum = int((columnNum - 1) / blockSize) + 1
                # #
                # # # mskDS = gdal.Open(dstFilename + '.msk',gdal.GA_Update)
                # #
                # # # 分块检查异常值手动生成掩膜的方案
                # # mskDS = imgdriver.Create(dstFilename.replace('.' + kwargs['ext'], '_M.img'), domSrcDS.RasterXSize,
                # #                          domSrcDS.RasterYSize,
                # #                          1, gdal.GDT_Byte, options=['COMPRESS=RLE'])
                # #
                # # mskDS.SetGeoTransform(GeoTransform)
                # # mskDS.SetProjection(Projection)
                # #
                # # delNum = kwargs['delNum']
                # #
                # # mskBand = mskDS.GetRasterBand(1)
                # #
                # # for rowstep in range(rowblockNum):
                # #     for colstep in range(colblockNum):
                # #         rowpafNum = blockSize
                # #         colpafNum = blockSize
                # #         if (rowstep == rowblockNum - 1):
                # #             rowpafNum = int((rowNum - 1) % blockSize) + 1
                # #         if (colstep == colblockNum - 1):
                # #             colpafNum = int((columnNum - 1) % blockSize) + 1
                # #         mskArray = np.zeros((rowpafNum, colpafNum),
                # #                             dtype=np.int8)  # np.ones(rowpafNum, colpafNum) * 255 # mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                # #         for i in range(domSrcDS.RasterCount):
                # #             band = domSrcDS.GetRasterBand(i + 1)
                # #             domSrcNoData = band.GetNoDataValue()
                # #             tempArray = band.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                # #             mskArray = np.where((mskArray == 0) & ((tempArray <= kwargs['easyColors'] + kwargs['easyNearDist']) &
                # #                                                     (tempArray >= kwargs['easyColors'] - kwargs['easyNearDist'])), 0, 255)
                # #             band = None
                # #         mskBand.WriteArray(mskArray, colstep * blockSize, rowstep * blockSize)
                # # gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=(1024))
                # #
                # # mskDS = None
                # # # 通过msk文件统计总像元数量和异常像元数量
                # # mskDS = gdal.Open(dstFilename.replace('.' + kwargs['ext'], '_M.img'))
                # # mskBand = mskDS.GetRasterBand(1)
                # # mskList = mskBand.GetHistogram(-0.5, 255.5, buckets=256, include_out_of_range=0, approx_ok=0)
                # #
                # # for rowstep in range(rowblockNum):
                # #     for colstep in range(colblockNum):
                # #         rowpafNum = blockSize
                # #         colpafNum = blockSize
                # #         if (rowstep == rowblockNum - 1):
                # #             rowpafNum = int((rowNum - 1) % blockSize) + 1
                # #         if (colstep == colblockNum - 1):
                # #             colpafNum = int((columnNum - 1) % blockSize) + 1
                # #         for i in range(domDstDS.RasterCount):
                # #             srcband = domSrcDS.GetRasterBand(i + 1)
                # #             band = domDstDS.GetRasterBand(i + 1)
                # #             band.SetNoDataValue(255)
                # #             temparray = srcband.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                # #             tempmask = mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                # #             temparray = np.where(temparray == 255, 254, temparray)
                # #             temp = np.where(tempmask == 0, 255, temparray)
                # #             band.WriteArray(temp, colstep * blockSize, rowstep * blockSize)
                # #
                # # if kwargs['ovrBuild'] is True:
                # #     domDstDS.BuildOverviews("NEAREST", [2, 4, 8])
                # #
                # # domSrcDS = None
                # # domDstDS = None
                # # mskDS = None
                #
                # return (dstFilename, srcFilename, domFileNum, mskList, kwargs['ext'])

            # print('easyKill == False')
            # gdal.Nearblack(domDstDS,
            #                domSrcDS,
            #                    format=kwargs['format'],
            #                    colors=[tuple(kwargs['colors'] for i in range(domSrcDS.RasterCount))],
            #                    nearDist=kwargs['nearDist'],
            #                    maxNonBlack=kwargs['maxNonBlack'],
            #                    setMask=kwargs['setMask'],
            #                    )

            # 这里不关闭数据集的话，msk数据将不能保存，下一步没法用。不用nearblack及其msk的话就不用考虑了
            # domDstDS = None
            # domDstDS = gdal.Open(dstFilename,gdal.GA_Update)

            rowNum = domDstDS.RasterYSize
            columnNum = domDstDS.RasterXSize

            rowblockNum=int((rowNum-1)/blockSize)+1
            colblockNum=int((columnNum-1)/blockSize)+1

            c254 = kwargs['c254']
            if c254 == True:
                for rowstep in range(rowblockNum):
                    for colstep in range(colblockNum):
                        rowpafNum = blockSize
                        colpafNum = blockSize
                        if (rowstep == rowblockNum - 1):
                            rowpafNum = int((rowNum - 1) % blockSize) + 1
                        if (colstep == colblockNum - 1):
                            colpafNum = int((columnNum - 1) % blockSize) + 1
                        for i in range(domDstDS.RasterCount):
                            srcband = domSrcDS.GetRasterBand(i + 1)
                            band = domDstDS.GetRasterBand(i + 1)
                            band.SetNoDataValue(255)
                            temparray = srcband.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                            temparray = np.where(temparray >= 255, 254, temparray)
                            band.WriteArray(temparray, colstep * blockSize, rowstep * blockSize)
                if kwargs['ovrBuild'] is True:
                    domDstDS.BuildOverviews("NEAREST", [2, 4, 8])
                domSrcDS = None
                domDstDS = None
                return (dstFilename, srcFilename, domFileNum, None, kwargs['ext'])

            # mskDS = gdal.Open(dstFilename + '.msk',gdal.GA_Update)

            # 分块检查异常值手动生成掩膜的方案
            mskDS = imgdriver.Create(dstFilename.replace('.' + kwargs['ext'], '_M.img'), domSrcDS.RasterXSize,
                                  domSrcDS.RasterYSize,
                                      1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

            mskDS.SetGeoTransform(GeoTransform)
            mskDS.SetProjection(Projection)

            delNum = kwargs['delNum']

            mskBand = mskDS.GetRasterBand(1)

            for rowstep in range(rowblockNum):
                for colstep in range(colblockNum):
                    rowpafNum = blockSize
                    colpafNum = blockSize
                    if (rowstep == rowblockNum - 1):
                        rowpafNum = int((rowNum - 1) % blockSize) + 1
                    if (colstep == colblockNum - 1):
                        colpafNum = int((columnNum - 1) % blockSize) + 1
                    mskArray = np.zeros((rowpafNum, colpafNum), dtype=np.int8) # np.ones(rowpafNum, colpafNum) * 255 # mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                    for i in range(domSrcDS.RasterCount):
                        band = domSrcDS.GetRasterBand(i + 1)
                        domSrcNoData = band.GetNoDataValue()
                        tempArray = band.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
                        mskArray = np.where((mskArray == 0) & (((tempArray <= kwargs['colors'] + kwargs['nearDist']) &
                                                                 (tempArray >= kwargs['colors'] - kwargs['nearDist'])) |
                                                               (tempArray == domSrcNoData)), 0, 255)
                        band = None
                    mskBand.WriteArray(mskArray, colstep * blockSize, rowstep * blockSize)
            gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=(1024))

            #if delNum != 0:
            unit = abs(GeoTransform[5])
            mskLessDS = imgdriver.Create(dstFilename.replace('.' + kwargs['ext'], '_N.img'), domSrcDS.RasterXSize,
                                      domSrcDS.RasterYSize,1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

            mskLessDS.SetGeoTransform(GeoTransform)
            mskLessDS.SetProjection(Projection)

            #mskLessBand = mskLessDS.GetRasterBand(1)

            shpFilename = dstFilename.replace('.' + kwargs['ext'],'_N.shp')
            dstLayername = "POLYGONIZED"
            drv = ogr.GetDriverByName("ESRI Shapefile")
            dst_ds = drv.CreateDataSource(shpFilename)
            dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

            fd = ogr.FieldDefn("Status", ogr.OFTInteger)
            dst_layer.CreateField(fd)
            dst_field = dst_layer.FindFieldIndex("Status", 1)

            gdal.Polygonize(mskBand, None, dst_layer, dst_field, [], callback=None)

            dst_ds = None
            dst_ds = ogr.Open(shpFilename,1)
            dst_layer2 = dst_ds.GetLayer(0)

            maxAreaFID = None
            maxTempArea = 0
            delIndexList = []
            mergeIndexList = []
            mergePolyList = []
            f = dst_layer2.GetNextFeature()
            while f is not None:
                # for f in dst_layer2:
                if f.GetField('status') == 0:
                    delIndexList.append(f.GetFID())
                else:
                    mergeIndexList.append(f.GetFID())
                    mergePolyList.append(shape(json.loads(f.geometry().ExportToJson())))
                f = None
                f = dst_layer2.GetNextFeature()

            [dst_layer2.DeleteFeature(i) for i in delIndexList]
            [dst_layer2.DeleteFeature(i) for i in mergeIndexList[1:]]
            feat = dst_layer2.GetFeature(mergeIndexList[0])

            reducePolyList = []
            print(mergePolyList)
            # 以下代码存在的问题：当区域被完全分割成几个子区域后，缓冲区无法修复已经被区分的子区域之间的裂痕（如白色道路）。
            # 解决方法是对整体进行级联合并，并对整体进行缓冲区和内扩操作。
            # for simplePoly in mergePolyList:
            #     if simplePoly.geom_type == 'Polygon':
            #         simplePoly = Polygon(simplePoly.exterior)
            #     else:
            #         maxArea = 0
            #         maxExt = None
            #         for p in simplePoly:
            #             if (p.area > maxArea):
            #                 maxArea = p.area
            #                 maxExt = p.exterior
            #         simplePoly = Polygon(maxExt)
            #     fx = simplePoly.buffer(distance=kwargs['maxNonBlack'] * unit, cap_style=1, join_style=2).buffer(
            #         distance=-(kwargs['maxNonBlack'] * unit), cap_style=1, join_style=2)
            #     reducefx = fx
            #     if delNum != 0:
            #         reducefx = fx.buffer(distance=-(delNum * unit), cap_style=1, join_style=3)
            #     if reducefx.geom_type == 'Polygon':
            #         reducefx = Polygon(reducefx.exterior)
            #     else:
            #         maxArea = 0
            #         maxExt = None
            #         for p in reducefx:
            #             if (p.area > maxArea):
            #                 maxArea = p.area
            #                 maxExt = p.exterior
            #         reducefx = Polygon(maxExt)
            #     reducePolyList.append(reducefx)

            for simplePoly in mergePolyList:
                if simplePoly.geom_type == 'Polygon':
                    simplePoly = Polygon(simplePoly.exterior)
                else:
                    maxArea = 0
                    maxExt = None
                    for p in simplePoly:
                        if (p.area > maxArea):
                            maxArea = p.area
                            maxExt = p.exterior
                    simplePoly = Polygon(maxExt)
                reducePolyList.append(simplePoly)

            poly = cascaded_union(reducePolyList)

            if kwargs['easyKill'] == True:
                poly = poly.convex_hull

            # 对整体poly进行边缘修正与内扩
            poly = poly.buffer(0)
            poly = poly.buffer(distance=kwargs['maxNonBlack'] * unit, cap_style=2, join_style=1).buffer(
                distance=-(kwargs['maxNonBlack'] * unit), cap_style=2, join_style=2)
            if delNum != 0:
                poly = poly.buffer(distance=-(delNum * unit), cap_style=2, join_style=1)

            # 消除内部冗余几何形态
            finalPolyList = []
            if poly.geom_type == 'Polygon':
                poly = Polygon(poly.exterior)
            else:
                for p in poly:
                    maxExt = p.exterior
                    subPoly = Polygon(maxExt)
                    finalPolyList.append(subPoly)
                poly = cascaded_union(finalPolyList)

            geobf = ogr.CreateGeometryFromWkb(poly.wkb)

            feat.SetGeometry(geobf)
            dst_layer2.SetFeature(feat)
            dst_ds = None

            gdal.Rasterize(mskLessDS, shpFilename, attribute='status')

            # 如果注释这里，则最终使用阈值法
            mskBand = None
            mskBand = mskLessDS.GetRasterBand(1)

            # 废弃
            # gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=1024)

            mskList = mskBand.GetHistogram(-0.5, 255.5, buckets=256, include_out_of_range=0, approx_ok=0)

            nodataFill = kwargs['nodataFill']

            for rowstep in range(rowblockNum):
                for colstep in range(colblockNum):
                    rowpafNum = blockSize
                    colpafNum = blockSize
                    if (rowstep==rowblockNum-1):
                        rowpafNum=int((rowNum-1)%blockSize)+1
                    if (colstep==colblockNum-1):
                        colpafNum=int((columnNum-1)%blockSize)+1
                    for i in range(domDstDS.RasterCount):
                        srcband = domSrcDS.GetRasterBand(i+1)
                        band = domDstDS.GetRasterBand(i+1)
                        band.SetNoDataValue(255)
                        temparray = srcband.ReadAsArray(colstep*blockSize,rowstep*blockSize,colpafNum,rowpafNum)
                        tempmask = mskBand.ReadAsArray(colstep*blockSize,rowstep*blockSize,colpafNum,rowpafNum)
                        temparray = np.where(temparray==255,254,temparray)
                        if nodataFill is True:
                            temp = np.where(tempmask == 0, 0, temparray)
                        else:
                            temp = np.where(tempmask==0,255,temparray)
                        band.WriteArray(temp,colstep*blockSize,rowstep*blockSize)

            if kwargs['ovrBuild'] is True:
                domDstDS.BuildOverviews("NEAREST",[2,4,8])

            domSrcDS = None
            domDstDS = None
            mskLessDS = None
            mskDS = None

            return (dstFilename,srcFilename,domFileNum,mskList,kwargs['ext'])
        except Exception as e:
            print(e.__str__())
            return (False, e.__str__())

    def pyNearBlackCallBack(self,res):
        """
        pyNearBlack的回调函数，用于记录日志和更新进度条。

        :param res: pyNearBlack的返回值，为(dstFilename,srcFilename,domFileNum,mskList,ext)
        :return: None
        """
        # print(res[0])
        # print(res[1])
        # print(res[2])
        # print(res[3])
        if res[0] is False:
            self.logRcd.emitInfo('[INFO] ERROR：' + res[1] + '\n')
            return

        # time.sleep(0.005)
        try:
            self.domCount += 1
            self.logRcd.emitInfo('[INFO] '+'(' + self.domCount.__str__()  + '/' + res[2].__str__() + ') ' + res[1])
            self.logRcd.emitProcessValue(int(100.0 * self.domCount /res[2]))

            # 通过msk文件统计总像元数量和异常像元数量
            # mskDs = gdal.Open(res[0] + '.msk')
            # mskList = mskDs.GetRasterBand(1).GetHistogram(-0.5,255.5,buckets = 256, include_out_of_range = 0,approx_ok = 0)
            # mskDs = None

            if os.path.exists(res[0] + '.msk'):
                os.remove(res[0] + '.msk')
            if os.path.exists(res[0] + '.aux.xml'):
                os.remove(res[0] + '.aux.xml')
            if os.path.exists(res[0] + '.msk.aux.xml'):
                os.remove(res[0] + '.msk.aux.xml')
            if os.path.exists(res[0] + '.msk.aux.xml'):
                os.remove(res[0] + '.msk.aux.xml')
            if os.path.exists(res[0].replace('.' + res[4],'_N.dbf')):
                os.remove(res[0].replace('.' + res[4],'_N.dbf'))
            if os.path.exists(res[0].replace('.' + res[4],'_N.shp')):
                os.remove(res[0].replace('.' + res[4],'_N.shp'))
            if os.path.exists(res[0].replace('.' + res[4],'_N.shx')):
                os.remove(res[0].replace('.' + res[4],'_N.shx'))
            if os.path.exists(res[0].replace('.' + res[4],'_M.img')):
                os.remove(res[0].replace('.' + res[4],'_M.img'))
            if os.path.exists(res[0].replace('.' + res[4],'_N.img')):
                os.remove(res[0].replace('.' + res[4],'_N.img'))
            if os.path.exists(res[0].replace('.' + res[4],'_N.img.aux.xml')):
                os.remove(res[0].replace('.' + res[4],'_N.img.aux.xml'))
            if os.path.exists(res[0].replace('.' + res[4],'_M.img.aux.xml')):
                os.remove(res[0].replace('.' + res[4],'_M.img.aux.xml'))

            datanameItem = os.path.basename(res[1])
            datapathItem = res[1]
            typeItem = ''
            if self.outlierValue == 255:
                typeItem = '去白边(255)'
            elif self.outlierValue == 0:
                typeItem = '去黑边(0)'
            else:
                typeItem = '自定义(' + self.outlierValue.__str__() +')'

            if self.easyKill == True:
                typeItem = '简单剔除模式(' + self.easyColors.__str__() + ')'

            if self.c254 == True:
                typeItem = '255转254'

            totalItem = ''
            errorItem = ''
            if res[3] is not None:
                totalItem = sum(res[3]).__str__()
                errorItem = res[3][0].__str__()
            else:
                totalItem = '未统计(255-254转换任务)'
                errorItem = '未统计(255-254转换任务)'

            resultItem = '成功'

            saveasItem = os.path.basename(res[0])

            saveaspathItem = res[0]

            domTableItemData = (datanameItem,datapathItem,typeItem,totalItem,errorItem,
                                resultItem,saveasItem,saveaspathItem)

            self.logRcd.emitInfo('[INFO] 总像元数量：' + totalItem + '；异常像元数量：' + errorItem + '\n')

            self.emitDomTableItemData(domTableItemData)

            if os.path.exists(os.path.splitext(datapathItem)[0]+'.xml'):
                shutil.copyfile(os.path.splitext(datapathItem)[0]+'.xml', os.path.splitext(res[0])[0]+'.xml')
        except Exception as e:
            print(e.__str__())
            self.logRcd.emitInfo('[INFO] ERROR：' + e.__str__() + '\n')

    def domOutlierRemover(self,domFileNum):
        """
        将异常值移除，即设为NoData。

        :return: None
        """
        gdal.AllRegister()
        #format = 'HFA'

        self.logRcd.emitInfo('[CONFIG] 任务项：DOM影像异常值检查')

        self.logRcd.emitInfo('[CONFIG] 输入目录：'+self.domDirPath)

        if self.domDirOutputPath != '':
            self.logRcd.emitInfo('[CONFIG] 输出目录：' + self.domDirOutputPath)
        else:
            self.logRcd.emitInfo('[CONFIG] 输出目录：缺省（数据原目录下）')

        self.logRcd.emitInfo('[CONFIG] 影像异常值设置：'+self.outlierValue.__str__())
        self.logRcd.emitInfo('[CONFIG] 近似异常值距离：' + self.nearDist.__str__())
        self.logRcd.emitInfo('[CONFIG] 边缘修正因子：' + self.maxNonBlack.__str__())
        self.logRcd.emitInfo('[CONFIG] 内扩距离：' + self.delNum.__str__())
        self.logRcd.emitInfo('[CONFIG] 影像输出格式为：' + self.fileType.__str__())
        self.logRcd.emitInfo('[CONFIG] 生成影像金字塔：' + self.ovrBuild.__str__())
        self.logRcd.emitInfo('[CONFIG] 填充NoData区域为0值：' + self.nodataFill.__str__())
        self.logRcd.emitInfo('[CONFIG] 只转换255至254（不做剔除任务）：' + self.c254.__str__())
        self.logRcd.emitInfo('[CONFIG] 简单去边模式：' + self.easyKill.__str__())
        self.logRcd.emitInfo('[CONFIG] 简单去边值：' + self.easyColors.__str__())
        self.logRcd.emitInfo('[CONFIG] 简单去边距离：' + self.easyNearDist.__str__())

        coreNum = 4
        coreNum = mp.cpu_count()
        if coreNum > 4:
            coreNum = 4

        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（进程数 '+ coreNum.__str__() +  '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        domPool = mp.Pool(coreNum)

        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        for domPath in self.domPathExtList:
            try:
                srcFilename = domPath # + "." + self.fileType
                dstFilename = ''
                if self.domDirOutputPath != '':
                    print("---------------------")
                    outputDirSub = srcFilename.rsplit(self.domDirPath,1)[1]
                    outputDir = os.path.dirname(self.domDirOutputPath + outputDirSub) # self.domDirOutputPath + '/' + domPath.rsplit('/',1)[1] # + "_P"
                    print("OUTPUTPATH: " + self.domDirOutputPath.__str__() + outputDirSub.__str__())
                    if os.path.exists(outputDir) is False:
                        print("MAKING SUBDIR: " + outputDir.__str__())
                        os.mkdir(outputDir)
                    else:
                        print("NO NEED TO MAKE SUBDIR: " + outputDir.__str__())
                    dstFilename = self.domDirOutputPath + outputDirSub.rsplit('.',1)[0] + '.' + self.fileType # outputDir + '/' + domPath.rsplit('/',1)[1] + "." +self.fileType

                format = 'HFA'
                ext = 'img'
                if dstFilename.rsplit('.',1)[1] == 'tif':
                    format = 'GTiff'
                    ext = 'tif'

                domPool.apply_async(self.pyNearBlack,
                                    (dstFilename, srcFilename, domFileNum),
                                    kwds={'ext':ext,
                                          'format':format,
                                          'colors':self.outlierValue,
                                          'nearDist':self.nearDist,
                                          'maxNonBlack':self.maxNonBlack,
                                          'delNum':self.delNum,
                                          'fileType':self.fileType,
                                          'ovrBuild':self.ovrBuild,
                                          'setMask': True,
                                          'nodataFill' : self.nodataFill,
                                          'c254': self.c254,
                                          'easyKill' : self.easyKill,
                                          'easyColors' : self.easyColors,
                                          'easyNearDist' : self.easyNearDist
                                    },callback=self.pyNearBlackCallBack)

                # domPool.apply(self.pyNearBlack,
                #                     (dstFilename, srcFilename, domFileNum),
                #                     kwds={'ext':ext,
                #                           'format':format,
                #                           'colors':self.outlierValue,
                #                           'nearDist':self.nearDist,
                #                           'maxNonBlack':self.maxNonBlack,
                #                           'delNum':self.delNum,
                #                           'fileType':self.fileType,
                #                           'ovrBuild':self.ovrBuild,
                #                           'setMask': True
                #                     })
            except Exception as e:
                print(e.__str__())
                self.logRcd.emitInfo('[INFO] ERROR：' + e.__str__() + '\n')
        domPool.close()
        domPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()