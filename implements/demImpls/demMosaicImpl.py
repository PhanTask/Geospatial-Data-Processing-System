# -*- coding:utf-8 -*-

"""
demMosaicImpl.py
~~~~~~~~~~~~~~~~

DEM模块接边检查功能实现。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from osgeo import gdal
from osgeo import ogr
import os
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import numpy as np
import shutil

class demMosaicImpl(QtCore.QThread):
    """
    处理dem接边检查任务。
    """
    # infomsgSignal = QtCore.Signal( str ) # 日志signal
    # processSignal = QtCore.Signal( int ) # 进度signal
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    demTableItemDataSignal = QtCore.Signal(object) # dem表格项signal
    dostop = False # 是否强制终止
    processValue = 0.0#mp.Value("d",0.0) # 进度
    demPathList = []
    shpPathList = []
    demFileNum = 0
    def __init__(self, demDirPath, demDirOutputPath, valueRange = (0,100), slopeThreshold = 80, fileType = "img"):
        """
        demMosaicImpl类。

        :param demDirPath: dem文件夹路径
        :param demDirOutputPath: 处理后异常值输出文件夹路径
        :param fileType: 指定的dem文件格式，默认为img
        """
        super(demMosaicImpl, self).__init__()
        self.demDirPath = demDirPath
        self.demDirOutputPath = demDirOutputPath
        self.valueRange = valueRange
        self.slopeThreshold = slopeThreshold
        self.fileType = fileType
        self.demCount = 0
        self.logRcd = logRcd('DEM接边检查日志')

    def emitFinish( self, isSuccessful):
        self.doneflag.emit( isSuccessful )

    def emitDemTableItemData(self, DemTableItemData):
        self.demTableItemDataSignal.emit(DemTableItemData)

    def run(self, *args, **kwargs):
        """
        在本线程中执行算法。

        :return: None
        """
        try:
            demFileNum = self.getDemPathList()
            self.demMosaicChecker(demFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getDemPathList(self):
        """
        从所给的dem文件夹路径中将所有dem的路径提取出来。

        :return: dem数据数量，即dem文件夹数量
        """
        self.demPathNoExtList = [ self.demDirPath + '/' + dir for dir in os.listdir(self.demDirPath) if dir[-3:] == self.fileType]
        #print(self.demPathList)
        return self.demPathNoExtList.__len__()

    @staticmethod
    def pyMosaicChecker(dstFilename,srcFilename,demFileNum,**kwargs):
        """
        执行dem接边检查与记录操作，为静态函数。

        :param dstFilename: 处理后数据文件路径名
        :param srcFilename: 原始数据文件路径名
        :param demFileNum: 原始数据个数
        :param kwargs: 自定义参数
        :return: (dstFilename,srcFilename,demFileNum)
        """

        #tempFilename = os.path.splitext(dstFilename)[0] + '.img'
        #srcFilename = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\dem_cs.img"
        slopeFilename = os.path.splitext(dstFilename)[0] + '_slope.img'
        aspectFilename = os.path.splitext(dstFilename)[0] + '_aspect.img'
        resultFilename = os.path.splitext(dstFilename)[0] + '_result.img'
        resultShpname = dstFilename # r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\result\dem_cs_result.shp"

        driver = gdal.GetDriverByName(kwargs['format'])

        demSrcDS = gdal.Open(srcFilename)

        # demSlopeDS = driver.Create(slopeFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
        #                          demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
        #
        demResultDS = driver.Create(resultFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
                                    demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])

        GeoTransform = demSrcDS.GetGeoTransform()
        Projection = demSrcDS.GetProjection()

        demResultDS.SetGeoTransform(GeoTransform)
        demResultDS.SetProjection(Projection)
        #
        # demAspectDS.SetGeoTransform(GeoTransform)
        # demAspectDS.SetProjection(Projection)

        demSlopeDS = gdal.DEMProcessing(slopeFilename, srcFilename, "slope", computeEdges=True)
        demAspectDS = gdal.DEMProcessing(aspectFilename, srcFilename, "aspect", computeEdges=True)

        rowNum = demSrcDS.RasterYSize
        columnNum = demSrcDS.RasterXSize

        rowblockNum = int((rowNum - 1) / 1024) + 1
        colblockNum = int((columnNum - 1) / 1024) + 1

        valueRange = kwargs['valueRange']
        slopeThreshold = kwargs['slopeThreshold']

        srcBand = demSrcDS.GetRasterBand(1)
        slopeBand = demSlopeDS.GetRasterBand(1)
        aspectBand = demAspectDS.GetRasterBand(1)
        resultBand = demResultDS.GetRasterBand(1)

        srcNoDataValue = srcBand.GetNoDataValue()

        for rowstep in range(rowblockNum):
            for colstep in range(colblockNum):
                rowpafNum = 1024
                colpafNum = 1024
                if (rowstep == rowblockNum - 1):
                    rowpafNum = int((rowNum - 1) % 1024) + 1
                if (colstep == colblockNum - 1):
                    colpafNum = int((columnNum - 1) % 1024) + 1

                srcArray = srcBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
                slopeArray = slopeBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
                aspectArray = aspectBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)

                aspectTemp = np.where(((aspectArray >= 0) & (aspectArray <= 1)) |
                                      ((aspectArray >= 89) & (aspectArray <= 91)) |
                                      ((aspectArray >= 179) & (aspectArray <= 181)) |
                                      ((aspectArray >= 269) & (aspectArray <= 271)) |
                                      ((aspectArray >= 359) & (aspectArray <= 360))
                                      , 0, 255)

                ssTemp = np.where((srcArray == srcNoDataValue) |
                                  ((srcArray <= valueRange[0]) & (srcArray >= valueRange[1])) |
                                  (slopeArray >= slopeThreshold)
                                  , 0, 255)

                aspectBand.WriteArray(aspectTemp, colstep * 1024, rowstep * 1024)
                resultBand.WriteArray(ssTemp, colstep * 1024, rowstep * 1024)

        gdal.SieveFilter(srcBand=aspectBand, maskBand=None, dstBand=aspectBand, threshold=(512))
        for rowstep in range(rowblockNum):
            for colstep in range(colblockNum):
                rowpafNum = 1024
                colpafNum = 1024
                if (rowstep == rowblockNum - 1):
                    rowpafNum = int((rowNum - 1) % 1024) + 1
                if (colstep == colblockNum - 1):
                    colpafNum = int((columnNum - 1) % 1024) + 1
                resultArray = resultBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
                aspectArray = aspectBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
                resultTemp = np.where(aspectArray == 0, 0, resultArray)
                resultBand.WriteArray(resultTemp, colstep * 1024, rowstep * 1024)

        dstLayername = "POLYGONIZED"
        drv = ogr.GetDriverByName("ESRI Shapefile")
        dst_ds = drv.CreateDataSource(resultShpname)
        dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

        fd = ogr.FieldDefn("Status", ogr.OFTInteger)
        dst_layer.CreateField(fd)
        dst_field = dst_layer.FindFieldIndex("Status", 1)

        gdal.Polygonize(resultBand, None, dst_layer, dst_field, [], callback=None)

        dst_ds = None
        demSrcDS = None
        demResultDS = None
        demSlopeDS = None
        demAspectDS = None

        return (dstFilename,srcFilename,demFileNum,resultFilename)

    def pyMosaicCheckerCallBack(self,res):
        """
        pyMosaicChecker的回调函数，用于记录日志和更新进度条。

        :param res: pyMosaicChecker的返回值，为(dstFilename,srcFilename,demFileNum)
        :return: None
        """
        try:
            self.demCount += 1
            self.logRcd.emitInfo('[INFO] '+'(' + self.demCount.__str__()  + '/' + res[2].__str__() + ') ' + res[1])
            self.logRcd.emitProcessValue(int(100.0 * self.demCount /res[2]))

            # 通过result文件统计总像元数量和异常像元数量
            tempDs = gdal.Open(res[3])
            tempList = tempDs.GetRasterBand(1).GetHistogram(-0.5,255.5,buckets = 256, include_out_of_range = 0,approx_ok = 0)
            tempDs = None

            if os.path.exists(res[3]):
                os.remove(res[3])
            if os.path.exists(res[3].replace('_result.img','_result.img.aux.xml')):
                os.remove(res[3].replace('_result.img','_result.img.aux.xml'))
            if os.path.exists(os.path.splitext(res[0])[0] + '_slope.img'):
                os.remove(os.path.splitext(res[0])[0] + '_slope.img')
            if os.path.exists(os.path.splitext(res[0])[0] + '_aspect.img'):
                os.remove(os.path.splitext(res[0])[0] + '_aspect.img')
            if os.path.exists(os.path.splitext(res[0])[0] + '_result.img'):
                os.remove(os.path.splitext(res[0])[0] + '_result.img')


            datanameItem = os.path.basename(res[1])

            datapathItem = res[1]

            rangeItem = self.valueRange.__str__()

            thresItem = self.slopeThreshold.__str__()

            totalItem = sum(tempList).__str__()

            errorItem = tempList[0].__str__()

            saveasItem = os.path.basename(res[0])

            saveaspathItem = res[0]

            demTableItemData = (datanameItem,datapathItem,rangeItem,thresItem,totalItem,errorItem,saveasItem,saveaspathItem)

            self.logRcd.emitInfo('[INFO] 总像元数量：' + totalItem + '；异常像元数量：' + errorItem + '\n')

            self.emitDemTableItemData(demTableItemData)
        except Exception as e:
            print(e.__str__())

    def demMosaicChecker(self,demFileNum):
        """
        寻找dem中异常值，并根据其对应位置制作shp掩膜文件。

        :return: None
        """
        gdal.AllRegister()
        format = 'HFA'

        self.logRcd.emitInfo('[CONFIG] 任务项：DEM接边检查')

        self.logRcd.emitInfo('[CONFIG] 输入目录：'+self.demDirPath)

        self.logRcd.emitInfo('[CONFIG] 输出目录：' + self.demDirOutputPath)

        self.logRcd.emitInfo('[CONFIG] DEM高程有效范围设置：'+self.valueRange.__str__())
        self.logRcd.emitInfo('[CONFIG] 高程突变阈值设置：' + self.slopeThreshold.__str__())
        coreNum = mp.cpu_count()
        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（CPU核心数 '+ coreNum.__str__() +  '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        demPool = mp.Pool(coreNum)

        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        for demPath in self.demPathNoExtList:
            srcFilename = demPath
            outputDir = self.demDirOutputPath
            dstFilename = outputDir + '/' + demPath.rsplit('/',1)[1] + ".shp"

            demPool.apply_async(self.pyMosaicChecker,
                                (dstFilename, srcFilename, demFileNum),
                                kwds={'format':'HFA',
                                      'valueRange':self.valueRange,
                                      'slopeThreshold':self.slopeThreshold
                                },callback=self.pyMosaicCheckerCallBack)
        demPool.close()
        demPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()