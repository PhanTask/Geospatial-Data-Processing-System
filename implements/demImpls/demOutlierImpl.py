# -*- coding:utf-8 -*-
"""
demOutlierImpl.py
~~~~~~~~~~~~~~~~~

DEM模块异常值检查功能实现。

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

class demOutlierImpl(QtCore.QThread):
    """
    处理dem异常值检查任务。
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
    def __init__(self, demDirPath, demDirOutputPath, valueRange = (0,100), fileType = "img"):
        """
        demOutlierImpl类。

        :param demDirPath: dem文件夹路径
        :param demDirOutputPath: 处理后异常值输出文件夹路径
        :param valueRange: dem有效值范围，为tuple，第一个值为高程下限，第二个值为高程上限，在此范围外的都是异常值
        :param fileType: 指定的dem文件格式，默认为img
        """
        super(demOutlierImpl, self).__init__()
        self.demDirPath = demDirPath
        self.demDirOutputPath = demDirOutputPath
        self.valueRange = valueRange
        self.fileType = fileType
        self.demCount = 0
        self.logRcd = logRcd('DEM异常值检查日志')

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
            self.demOutlierChecker(demFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getDemPathList(self):
        """
        从所给的dem文件夹路径中将所有dem的路径提取出来。

        :return: dem数据数量，即dem文件夹数量
        """
        self.demPathNoExtList = [ self.demDirPath + '/'  + dir for dir in os.listdir(self.demDirPath) if dir[-3:] == self.fileType]
        #print(self.demPathList)
        return self.demPathNoExtList.__len__()

    @staticmethod
    def pyOutlierChecker(dstFilename,srcFilename,demFileNum,**kwargs):
        """
        执行dem异常值检查与记录操作，为静态函数。

        :param dstFilename: 处理后数据文件路径名
        :param srcFilename: 原始数据文件路径名
        :param demFileNum: 原始数据个数
        :param kwargs: 自定义参数，目前包括valueRange
        :return: (dstFilename,srcFilename,demFileNum)
        """

        tempFilename = os.path.splitext(dstFilename)[0] + '.img'

        driver = gdal.GetDriverByName(kwargs['format'])
        demSrcDS = gdal.Open(srcFilename)
        demDstDS = driver.Create(tempFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
                                 demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
        GeoTransform = demSrcDS.GetGeoTransform()
        Projection = demSrcDS.GetProjection()
        demDstDS.SetGeoTransform(GeoTransform)
        demDstDS.SetProjection(Projection)

        rowNum = demDstDS.RasterYSize
        columnNum = demDstDS.RasterXSize

        rowblockNum=int((rowNum-1)/1024)+1
        colblockNum=int((columnNum-1)/1024)+1

        valueRange = kwargs['valueRange']

        for rowstep in range(rowblockNum):
            for colstep in range(colblockNum):
                rowpafNum = 1024
                colpafNum = 1024
                if (rowstep==rowblockNum-1):
                    rowpafNum=int((rowNum-1)%1024)+1
                if (colstep==colblockNum-1):
                    colpafNum=int((columnNum-1)%1024)+1
                for i in range(demDstDS.RasterCount):
                    dstBand = demDstDS.GetRasterBand(i+1)
                    srcBand = demSrcDS.GetRasterBand(i+1)
                    srcArray = srcBand.ReadAsArray(colstep*1024,rowstep*1024,colpafNum,rowpafNum)
                    temp = np.where((srcArray >= valueRange[0]) & (srcArray <= valueRange[1]), 0, 255)
                    dstBand.WriteArray(temp,colstep*1024,rowstep*1024)

        demSrcDS = None
        demDstDS = None

        dstLayername = "POLYGONIZED"
        drv = ogr.GetDriverByName("ESRI Shapefile")
        dst_ds = drv.CreateDataSource(dstFilename)
        dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

        fd = ogr.FieldDefn("Status", ogr.OFTInteger)
        dst_layer.CreateField(fd)
        dst_field = dst_layer.FindFieldIndex("Status",1)

        demDstDS = gdal.Open(tempFilename)
        dstBand = demDstDS.GetRasterBand(1)
        gdal.Polygonize(dstBand, None, dst_layer, dst_field, [], callback=None)

        dst_ds = None
        demDstDS = None

        return (dstFilename,srcFilename,demFileNum,tempFilename)

    def pyOutlierCheckerCallBack(self,res):
        """
        pyOutlierChecker的回调函数，用于记录日志和更新进度条。

        :param res: pyOutlierChecker的返回值，为(dstFilename,srcFilename,demFileNum)
        :return: None
        """
        try:
            self.demCount += 1
            self.logRcd.emitInfo('[INFO] '+'(' + self.demCount.__str__()  + '/' + res[2].__str__() + ') ' + res[1])
            self.logRcd.emitProcessValue(int(100.0 * self.demCount /res[2]))

            # 通过temp文件统计总像元数量和异常像元数量
            tempDs = gdal.Open(res[3])
            tempList = tempDs.GetRasterBand(1).GetHistogram(-0.5,255.5,buckets = 256, include_out_of_range = 0,approx_ok = 0)
            tempDs = None

            if os.path.exists(res[3]):
                os.remove(res[3])
            if os.path.exists(res[3].replace('.img.img','.img.img.aux.xml')):
                os.remove(res[3].replace('.img.img','.img.img.aux.xml'))

            datanameItem = os.path.basename(res[1])

            datapathItem = res[1]

            rangeItem = self.valueRange.__str__()

            totalItem = sum(tempList).__str__()

            errorItem = tempList[255].__str__()

            saveasItem = os.path.basename(res[0])

            saveaspathItem = res[0]

            demTableItemData = (datanameItem,datapathItem,rangeItem,totalItem,errorItem,saveasItem,saveaspathItem)

            self.logRcd.emitInfo('[INFO] 总像元数量：' + totalItem + '；异常像元数量：' + errorItem + '\n')

            self.emitDemTableItemData(demTableItemData)
        except Exception as e:
            print(e.__str__())

    def demOutlierChecker(self,demFileNum):
        """
        寻找dem中异常值，并根据其对应位置制作shp掩膜文件。

        :return: None
        """
        gdal.AllRegister()
        format = 'HFA'

        self.logRcd.emitInfo('[CONFIG] 任务项：DEM异常值检查')

        self.logRcd.emitInfo('[CONFIG] 输入目录：'+self.demDirPath)

        self.logRcd.emitInfo('[CONFIG] 输出目录：' + self.demDirOutputPath)

        self.logRcd.emitInfo('[CONFIG] DEM高程有效范围设置：'+self.valueRange.__str__())
        coreNum = mp.cpu_count()
        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（CPU核心数 '+ coreNum.__str__() +  '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        demPool = mp.Pool(coreNum)

        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        for demPath in self.demPathNoExtList:
            srcFilename = demPath
            outputDir = self.demDirOutputPath
            dstFilename = outputDir + '/' + demPath.rsplit('/',1)[1] + ".shp"

            demPool.apply_async(self.pyOutlierChecker,
                                (dstFilename, srcFilename, demFileNum),
                                kwds={'format':'HFA',
                                      'valueRange':self.valueRange
                                },callback=self.pyOutlierCheckerCallBack)
        demPool.close()
        demPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()