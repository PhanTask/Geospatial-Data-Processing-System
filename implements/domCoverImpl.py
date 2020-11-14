#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 16:16
# @Author  : Dutian
# @Site    :
# @File    : coverCheckRun.py
# @Software: PyCharm
# @license : Copyright(C), Dutian
# @Contact : free.du@qq.com
"""
    数据质检覆盖检测模块
"""
import os

import shutil
from PySide2 import QtCore
import ogr
from osgeo import gdal
import multiprocessing as mp
import operator
from logger.logRcd import logRcd
import xml.etree.ElementTree as et


class cityInsection():
    '''
    市级行政区相交面积
    '''
    def __init__(self,cityName,indexFeatureName,insecArea):
        self.cityName=cityName
        self.indexFeatureName=indexFeatureName
        self.insecArea=insecArea

    def printAll(self):
        print(self.cityName,self.indexFeatureName,self.insecArea)
class couInsection():
    '''
    县行政区相交面积
    '''
    def __init__(self, cityName , couName, indexFeatureName, insecArea):
        self.cityName=cityName
        self.couName=couName
        self.indexFeatureName=indexFeatureName
        self.insecArea=insecArea

    def printAll(self):
        print(self.cityName,self.couName, self.indexFeatureName, self.insecArea)



class coverCheck(QtCore.QThread):
    """处理覆盖检测功能"""

    doneflag = QtCore.Signal(bool)  # 是否成功完成
    domTableItemDataSignal = QtCore.Signal(object)  # dom表格项signal
    dostop = False  # 是否强制终止
    processValue = 0.0  # mp.Value("d",0.0) # 进度
    domPathList = []
    shpPathList = []

    domFileNum = 0
    featureNum=0

    def __init__(self,domIndexDirPath,domCoverDirPath,domCoverOutputDirPath,fileType):
        """
        初始化coverCheck类
        :param domIndexDirPath: 索引数据路径
        :param domCoverDirPath: 行政区划数据
        :param Else: 补充数据
        """
        super(coverCheck, self).__init__()
        self.domIndexDirPath = domIndexDirPath
        self.domCoverDirPath = domCoverDirPath
        self.domCoverOutputDirPath=domCoverOutputDirPath
        self.domPathNoExtList=[]
        self.domOriginalPathNoExtList=[]
        self.fileType = fileType
        self.domCount = 0
        self.logRcd = logRcd('DOM覆盖检查日志')

    # 自定义信号发射函数
    # 任务完成信号
    def emitFinish(self, isSuccessful):
        self.doneflag.emit(isSuccessful)

    # 结果传输到列表信号
    def emitDomTableItemData(self, DomTableItemData):
        self.domTableItemDataSignal.emit(DomTableItemData)

    def run(self, *args, **kwargs):
        """
        算法执行函数
        :param args:
        :param kwargs:
        :return:
        """
        try:
            domFileNum = self.getDomPathList(self.domCoverOutputDirPath)
            self.startProcess(domFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getDomPathList(self,domCoverOutputDirPath):
        """
        从所给的索引文件夹路径中将所有索引文件的路径提取出来。并复制到指定路径
        :return: feature数据数量
        """

        # 列表推导式  os.path.join()：  将多个路径组合后返回
        for dir in os.listdir(self.domIndexDirPath + '/'):
            if dir[-3:] == 'gdb':
                # 复制为新的处理文件
                copyFilePath = domCoverOutputDirPath + '/' + dir.replace('.gdb', '_P.gdb')

                dir=self.domIndexDirPath+ '/' +dir
                self.domOriginalPathNoExtList.append(dir)
                try:
                    shutil.copytree(dir , copyFilePath)
                except Exception as e:
                    shutil.rmtree(copyFilePath)  # 递归删除文件夹
                    shutil.copytree(dir, copyFilePath)
                self.domPathNoExtList.append(copyFilePath)
        # self.domPathNoExtList = [os.path.join(self.domIndexDirPath, dir, '') for dir in os.listdir(self.domIndexDirPath+'/') if dir[:-3]=='gdb']
        # print(self.domPathList)
        return self.domPathNoExtList.__len__()

    # 静态函数标注
    @staticmethod
    def mpProcess(domPath,domOriginalPath,adDivisionFilePath):

        def intersectionCal(adDivisionFile, indexFeature):
            '''
            输入行政区划gdb，以及待求交面要素，输出相交面积排序列表
            :param adDivisionFile: 行政区划gdb文件，一打开
            :param indexFeature: 索引表单个面要素
            :return:
            '''
            cityInsectList = []
            couInsectList = []

            indexGeom = indexFeature.GetGeometryRef()
            for perLayer in adDivisionFile:
                print('正在处理图层：' + perLayer.GetName())
                # 对图层进行初始化，如果对图层进行了过滤操作，执行这句后，之前的过滤全部清空
                perLayer.ResetReading()
                perFeature = perLayer.GetNextFeature()
                while perFeature is not None:
                    # print("当前处理第%d个: \n" % perFeature.GetFID())
                    perGeom = perFeature.GetGeometryRef()
                    inSection = indexGeom.Intersection(perGeom)
                    inSectionArea = ogr.Geometry.Area(inSection)
                    if inSectionArea != 0:
                        if perLayer.GetName() == 'BOU_CIT_PY':
                            perCityClass = cityInsection(perFeature.GetField('NAME'),
                                                         indexFeature.GetField('影像名称'),
                                                         inSectionArea)
                            # perCityClass.printAll()
                            # 和之前元素对比，消除重复项
                            hasSame = False
                            for t in cityInsectList:
                                if perCityClass.cityName == t.cityName:
                                    t.insecArea += perCityClass.insecArea
                                    hasSame = True
                                    break
                            if hasSame == False: cityInsectList.append(perCityClass)

                        else:
                            if perLayer.GetName() == "BOU_COU_PY":
                                perCouClass = couInsection(perFeature.GetField('ADDRESS'),
                                                           perFeature.GetField('NAME'),
                                                           indexFeature.GetField('影像名称'),
                                                           inSectionArea)
                                # perCouClass.printAll()

                                hasSame = False
                                for t in couInsectList:
                                    if perCouClass.couName == t.couName:
                                        t.insecArea += perCityClass.insecArea
                                        hasSame = True
                                        break
                                if hasSame == False: couInsectList.append(perCouClass)

                        # print(perFeature.GetField('ADDRESS'), perFeature.GetField('NAME'),indexFeature.GetField('影像名称')+':'+str(inSectionArea))

                    perFeature = perLayer.GetNextFeature()
                # 排序输出

                cmpfun = operator.attrgetter('insecArea')  # 确定比较因子，
                # 排序输出市相交面积
                if perLayer.GetName() == 'BOU_CIT_PY':
                    print('排序输出市相交面积')
                    cityInsectList.sort(key=cmpfun, reverse=True)
                    [obj.printAll() for obj in cityInsectList]

                # 排序输出县相交面积
                if perLayer.GetName() == "BOU_COU_PY":
                    print('排序输出县相交面积')
                    couInsectList.sort(key=cmpfun, reverse=True)
                    # couInsectList=sorted(couInsectList, key=lambda x: x.insecArea)
                    [obj.printAll() for obj in couInsectList]
            intersecDic = {'cityInsectList': cityInsectList, 'couInsectList': couInsectList}
            return intersecDic

        def sortByDis(cityList, couList):
            '''
            输入市级区划和县级区划排序号的结果，生成按要求的字符串
            :param cityList:
            :param couList:
            :return:str
            '''
            returnStr = '浙江省 '
            for perCity in cityList:
                perCityStr = perCity.cityName + ':'
                for perCou in couList:
                    # 如果市名匹配
                    if perCou.cityName[3:] == perCity.cityName:
                        perCityStr = perCityStr + perCou.couName + ','
                    # 如果是最后一个县
                    if couList.index(perCou) == len(couList) - 1:
                        perCityStr = perCityStr[:-1]
                        perCityStr += ';'
                returnStr += perCityStr
            returnStr = returnStr[:-1]
            return returnStr

        try:

            domTableItemData = []
            signalProcessList = []

            print('before FileGDB')
            driver = ogr.GetDriverByName('FileGDB')
            print('after driver')
            indexFile = driver.Open(domPath, 1)
            print('after FileGDB')
            for oLayer in indexFile:
                oLayer.CreateField(ogr.FieldDefn(u"correct", 4))
                oFeature = oLayer.GetNextFeature()
                while oFeature is not None:
                    signalProcess = ''
                    adDivisionFile = ogr.Open(adDivisionFilePath, 0)
                    # 输出覆盖范围str并保存
                    # print(oFeature.GetField('imaCoverage'))
                    perFeatureIntersecDic = intersectionCal(adDivisionFile, oFeature)
                    # 输入排序结果，字符串匹配后输出 待比对字符串
                    sortResultStr = sortByDis(perFeatureIntersecDic['cityInsectList'],
                                              perFeatureIntersecDic['couInsectList'])
                    # print(sortResultStr)
                    oFeature.SetField(u"correct", sortResultStr)
                    oLayer.SetFeature(oFeature)
                    print(oFeature.GetField(u"correct"))

                    xmlPath = domOriginalPath.split(r':')[0] + r':/' + oFeature.GetField('地址').replace('\\','/')[:-3]+'xml'
                    xt = et.parse(xmlPath)
                    originalText = ''.join([i[-1].text for i in list(xt.getroot()) if i[0].text == 'imaCoverage'])
                    # for i in list(xt.getroot()):
                    #     if i[0].text == 'imaCoverage':
                    #         originalText = i[-1].text
                    # originalText = list(list(xt.getroot())[-3])[-1].text.__str__()

                    if sortResultStr == originalText: #oFeature.GetField(('imaCoverage')):
                        signalProcess += 'imaCoverage正确' + '\n'

                    else:
                        signalProcess += 'imaCoverage错误，正确值为：' + sortResultStr + '\n'

                    domTableItemDataItem = (oFeature.GetField('影像名称'),
                                            domOriginalPath,
                                            originalText,# oFeature.GetField('imaCoverage'),
                                            sortResultStr,
                                            domPath.rsplit('/',1)[1],
                                            domPath,
                                            )

                    domTableItemData.append(domTableItemDataItem)
                    signalProcessList.append(signalProcess)

                    oFeature=oLayer.GetNextFeature()
            return (domTableItemData, signalProcessList)
        except Exception as e:
            print(e.__str__())

    def mpProcessCallBack(self,res):
        """
        多进程回调函数
        :param res: 第一个为表格值，第二个为信号
        :return:
        """

        # 处理一份数据后，发送信号给信号窗体
        for item,desc in zip(res[0],res[1]):
            self.domCount += 1
            # 进度栏显示
            self.logRcd.emitInfo('[INFO] ' + '(' + self.domCount.__str__() +
                                 '/' + self.featureNum.__str__() + ')\n'
                                 + item[1] + '/' + item[0])
            self.logRcd.emitInfo(desc + '\n')
            self.logRcd.emitProcessValue(int(100.0 * self.domCount / self.featureNum))

            self.emitDomTableItemData(item)

    def startProcess(self,domFileNum):
        # 调用gdal 前准备
        # 为了支持中文路径，请添加下面这句代码
        #gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
        # 为了使属性表字段支持中文，请添加下面这句
        gdal.SetConfigOption("SHAPE_ENCODING", "")
        # 注册所有的驱动

        #ogr.RegisterAll()

        self.logRcd.emitInfo('[CONFIG] 任务项：DOM覆盖范围检查')
        self.logRcd.emitInfo('[CONFIG] 输入索引数据目录：' + self.domIndexDirPath)
        self.logRcd.emitInfo('[CONFIG] 输入行政区划数据目录：' + self.domCoverDirPath)
        self.logRcd.emitInfo('[CONFIG] 输出目录：' + self.domCoverOutputDirPath)
        #self.logRcd.emitInfo('[CONFIG] 异常值设置：' + self.outlierValue.__str__())
        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（进程数 ' + mp.cpu_count().__str__() + '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        domPool = mp.Pool(mp.cpu_count())
        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        # 测试打开行政区划数据
        adDivisionFilePath = self.domCoverDirPath
        #adDivisionFile = ogr.Open(adDivisionFilePath, 0)
        adDivisionFile = ogr.Open(adDivisionFilePath, 0)
        print(adDivisionFile)
        if adDivisionFile == None:
            print("打开文件%s失败！" % adDivisionFilePath)
            return
        print("打开文件%s成功！" % adDivisionFilePath)

        # 检查文件是否存在或打开，遍历索引数据，得到索引数据总个数
        for domPath in self.domPathNoExtList:

            indexFile = ogr.Open(domPath, 0)
            if indexFile == None:
                #print("打开文件%s失败！"% indexTableFilePath)
                #self.logRcd.emitInfo("打开文件%s失败！"% domPath)
                return
            #print("打开文件%s成功！"% indexTableFilePath)
            #self.logRcd.emitInfo("打开文件%s成功！"% domPath)
            for oLayer in indexFile:
                self.featureNum+=oLayer.GetFeatureCount()

        # 遍历索引数据，进行检查
        for domPath,domOriginalPath in zip(self.domPathNoExtList,self.domOriginalPathNoExtList):
            # 初始化进程池
            domPool.apply_async(self.mpProcess,
                                args=(domPath,domOriginalPath,adDivisionFilePath),
                                callback=self.mpProcessCallBack)
            # domPool.apply(self.mpProcess,
            #                     args=(domPath,domOriginalPath,adDivisionFilePath))
        domPool.close()
        domPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()