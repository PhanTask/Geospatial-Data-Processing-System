# -*- coding:utf-8 -*-
"""
domFormatImpl.py
~~~~~~~~~~~~~~~~

DOM模块分辨率与坐标系检查功能实现。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from osgeo import gdal
import os
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import shutil
from implements import crsWktParser
import operator

class domFormatImpl(QtCore.QThread):
    """
    处理dom任务
    """
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    domTableItemDataSignal = QtCore.Signal(object) # dom表格项signal
    dostop = False # 是否强制终止
    processValue = 0.0#mp.Value("d",0.0) # 进度
    domPathList = []
    shpPathList = []
    domFileNum = 0
    def __init__(self, domDirPath, paramsDict):
        """
        初始化domFormatImpl类

        :param domDirPath: dom文件夹路径，为字符串
        :param paramsDict: 分辨率与坐标系参数，为字典
        """
        super(domFormatImpl, self).__init__()
        self.domDirPath = domDirPath
        self.paramsDict = paramsDict
        self.logRcd = logRcd('DOM分辨率与坐标系检查日志')
        self.domCount = 0

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
            self.domParamsChecker(domFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getDomPathList(self):
        """
        从所给的dom文件夹路径中将所有dom的路径提取出来。

        :return: dom数据数量，即dom文件夹数量
        """
        self.domPathNoExtList = [ self.domDirPath+ '/' +dir+ '/' +dir for dir in os.listdir(self.domDirPath)]
        #print(self.domPathList)
        return self.domPathNoExtList.__len__()

    @staticmethod
    def pyParamsMatch(srcFilename,domFileNum,paramsDict):
        """
        执行分辨率与坐标系的参数匹配操作

        :param srcFilename: 原始数据文件路径名，为str
        :param domFileNum: 原始数据个数，为int
        :param domFileNum: 需要检查的参数，为dict
        :return: (resultDict,srcFilename,domFileNum,errorFlag)
        """
        ds = gdal.Open(srcFilename)
        crsWktStr = ds.GetProjectionRef()
        parser = crsWktParser.CrsWkt1Parser()
        crsWktDict = parser.parse_text(crsWktStr).as_dict()

        geoTransformTuple = ds.GetGeoTransform()
        xRes = abs(geoTransformTuple[1])
        yRes = abs(geoTransformTuple[5])

        resultDict = {}
        errorFlag = 0

        for item in paramsDict:
            if item == '坐标系名称':
                resultDict['坐标系名称'] = paramsDict[item]
                if paramsDict[item] == crsWktDict['GEOGCS']['name']:
                    resultDict['坐标系名称检查结果'] = '正确'
                else:
                    resultDict['坐标系名称检查结果'] = '错误'
                    errorFlag += 1
            elif item == '分辨率':
                resultDict['分辨率要求'] = paramsDict['分辨率'].__str__()
                resultDict['分辨率x值'] = xRes.__format__('.20f').rstrip('0').__str__()
                resultDict['分辨率y值'] = yRes.__format__('.20f').rstrip('0').__str__()
                if abs(xRes) <= float(paramsDict['X分辨率max']) and abs(xRes) >= float(paramsDict['X分辨率min']) and\
                    abs(yRes) <= float(paramsDict['Y分辨率max']) and abs(yRes) >= float(paramsDict['Y分辨率min']):
                    resultDict['分辨率检查结果'] = '正确'
                else:
                    resultDict['分辨率检查结果'] = '错误'
                    errorFlag += 1
            elif item == '基准面名称':
                resultDict['基准面名称'] = crsWktDict['GEOGCS']['DATUM']['name']
                if paramsDict[item] == crsWktDict['GEOGCS']['DATUM']['name']:
                    resultDict['基准面名称检查结果'] = '正确'
                else:
                    resultDict['基准面名称检查结果'] = '错误'
                    errorFlag += 1
            elif item == '椭球体名称':
                resultDict['椭球体名称'] = crsWktDict['GEOGCS']['DATUM']['SPHEROID']['name']
                if paramsDict[item] == crsWktDict['GEOGCS']['DATUM']['SPHEROID']['name']:
                    resultDict['椭球体名称检查结果'] = '正确'
                else:
                    resultDict['椭球体名称检查结果'] = '错误'
                    errorFlag += 1
            elif item == '椭球体长半轴':
                resultDict['椭球体长半轴'] = crsWktDict['GEOGCS']['DATUM']['SPHEROID']['semi_major_axis'].__str__()
                if abs(float(paramsDict[item]) - crsWktDict['GEOGCS']['DATUM']['SPHEROID']['semi_major_axis'])<=0.000001:
                    resultDict['椭球体长半轴检查结果'] = '正确'
                else:
                    resultDict['椭球体长半轴检查结果'] = '错误'
                    errorFlag += 1
            elif item == '椭球体反扁率':
                resultDict['椭球体反扁率'] = crsWktDict['GEOGCS']['DATUM']['SPHEROID']['inverse_flattening'].__str__()
                if abs(float(paramsDict[item]) - crsWktDict['GEOGCS']['DATUM']['SPHEROID']['inverse_flattening'])<=0.000001:
                    resultDict['椭球体反扁率检查结果'] = '正确'
                else:
                    resultDict['椭球体反扁率检查结果'] = '错误'
                    errorFlag += 1
            elif item == '角度单位名称':
                resultDict['角度单位名称'] = crsWktDict['GEOGCS']['UNIT']['name']
                if paramsDict[item] == crsWktDict['GEOGCS']['UNIT']['name']:
                    resultDict['角度单位名称检查结果'] = '正确'
                else:
                    resultDict['角度单位名称检查结果'] = '错误'
                    errorFlag += 1
            elif item == '每单位弧度':
                resultDict['每单位弧度'] = crsWktDict['GEOGCS']['UNIT']['conversion_factor'].__str__()
                if abs(float(paramsDict[item]) - crsWktDict['GEOGCS']['UNIT']['conversion_factor'])<=0.000001:
                    resultDict['每单位弧度检查结果'] = '正确'
                else:
                    resultDict['每单位弧度检查结果'] = '错误'
                    errorFlag += 1
            elif item == '本初子午线名称':
                resultDict['本初子午线名称'] = crsWktDict['GEOGCS']['PRIMEM']['name']
                if paramsDict[item] == crsWktDict['GEOGCS']['PRIMEM']['name']:
                    resultDict['本初子午线名称检查结果'] = '正确'
                else:
                    resultDict['本初子午线名称检查结果'] = '错误'
                    errorFlag += 1
            elif item == '本初子午线经度':
                resultDict['本初子午线经度'] = crsWktDict['GEOGCS']['PRIMEM']['longitude'].__str__()
                if float(paramsDict[item]) == crsWktDict['GEOGCS']['PRIMEM']['longitude']:
                    resultDict['本初子午线经度检查结果'] = '正确'
                else:
                    resultDict['本初子午线经度检查结果'] = '错误'
                    errorFlag += 1
            else:
                pass
        return (resultDict,srcFilename,domFileNum,errorFlag)


    def pyParamsMatchCallBack(self,res):
        """
        pyNearBlack的回调函数，用于记录日志和更新进度条。

        :param res: pyParamsMatch的返回值，为(resultDict,srcFilename,domFileNum,errorFlag)
        :return: None
        """
        self.domCount += 1
        self.logRcd.emitInfo('[INFO] '+'(' + self.domCount.__str__()  + '/' + res[2].__str__() + ') ' + res[1])

        self.logRcd.emitInfo('[INFO] 错误参数个数：' + res[3].__str__() + '\n')

        self.logRcd.emitProcessValue(int(100.0 * self.domCount /res[2]))

        self.emitDomTableItemData([('影像名称',os.path.basename(res[1])),('影像路径',res[1]),('错误参数个数', res[3].__str__())] + sorted(res[0].items(),key=operator.itemgetter(0)))

    def domParamsChecker(self,domFileNum):
        """
        DOM分辨率与坐标系检查

        :return: None
        """
        gdal.AllRegister()

        self.logRcd.emitInfo('[CONFIG] 任务项：DOM分辨率与坐标系检查')
        self.logRcd.emitInfo('[CONFIG] 输入目录：'+self.domDirPath)
        paramsStr = ''
        for param in self.paramsDict:
            paramsStr += '          -' + param.__str__()
            paramsStr += '\n'
        self.logRcd.emitInfo('[CONFIG] 质检项：\n\n'+paramsStr)
        coreNum = mp.cpu_count()
        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（CPU核心数 '+ coreNum.__str__() +  '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        domPool = mp.Pool(coreNum)
        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        for domPath in self.domPathNoExtList:
            srcFilename = domPath+".img"
            domPool.apply_async(self.pyParamsMatch,
                                (srcFilename, domFileNum, self.paramsDict),callback=self.pyParamsMatchCallBack)
            # domPool.apply(self.pyParamsMatch,
            #                     (srcFilename, domFileNum, self.paramsDict))
        domPool.close()
        domPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()