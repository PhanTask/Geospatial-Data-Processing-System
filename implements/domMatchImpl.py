# -*- coding:utf-8 -*-
"""
domMatchImpl.py
~~~~~~~~~~~~~~~~

DOM影像与索引匹配功能实现。

:copyright: (c) 2018 by Jinmeng Rao.
"""

import os
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import ogr
import gdal
import operator

class domMatchImpl(QtCore.QThread):
    """
    处理dom任务
    """
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    domTableItemDataSignal = QtCore.Signal(object) # dom表格项signal
    dostop = False # 是否强制终止
    processValue = 0.0 # 进度
    indexPathList = []
    domFileNum = 0
    def __init__(self, indexDirPath, panCap):
        """
        初始化domMatchImpl类

        :param indexDirPath: 索引文件夹路径，为str
        """
        super(domMatchImpl, self).__init__()
        self.indexDirPath = indexDirPath
        self.panCap = panCap
        self.logRcd = logRcd('DOM影像与索引匹配检查日志')
        self.domCount = 0

    def emitFinish( self, isSuccessful ):
        self.doneflag.emit( isSuccessful )

    def emitDomTableItemData(self, DomTableItemData):
        self.domTableItemDataSignal.emit(DomTableItemData)

    def run(self, *args, **kwargs):
        """
        在本线程中执行算法。

        :return: None
        """
        try:
            indexFileNum = self.getIndexPathList()
            self.domIndexMatcher(indexFileNum)
        except Exception as e:
            print('ERROR ' + e.__str__())

    def getIndexPathList(self):
        """
        从所给的索引文件夹路径中将所有索引的路径提取出来。

        :return: 索引数据数量，为int
        """
        self.indexPathList = [ self.indexDirPath + '/' + dir for dir in os.listdir(self.indexDirPath)]
        return self.indexPathList.__len__()

    @staticmethod
    def pyIndexMatch(indexPath,indexFileNum,panCap):
        """
        执行影像与索引匹配操作

        :param indexPath: 原始索引表文件路径名，为str
        :param indexFileNum: 原始索引表文件个数，为int
        :return resDict: 检查结果，为dict
        """

        # 储存检查结果的字典
        resDict = {}

        indexGDFrame = ogr.Open(indexPath)

        for layer in indexGDFrame:
            layerName = layer.GetName()
            for feature in layer:
                imgNameInFeature = feature.GetField(u'影像名称')
                imgPathInFeature = feature.GetField(u'地址').replace('\\','/')
                imgPathInFeature = panCap + ':/' + imgPathInFeature
                # imgName = [[ imgPath.rsplit('\\',1)[0] + '\\'+ filename
                #              for filename in os.listdir(imgPath.rsplit('\\',1)[0])
                #              if '.' in filename and filename.rsplit('.',1)[1]=='img']
                #            for imgPath in imgPathInIndex.__iter__()]
                # xmlName = [[ imgPath.rsplit('\\',1)[0] + '\\'+ filename
                #              for filename in os.listdir(imgPath.rsplit('\\',1)[0])
                #              if '.' in filename and 'img' not in filename and filename.rsplit('.',1)[1]=='xml']
                #            for imgPath in imgPathInIndex.__iter__()]

                if os.path.exists(imgPathInFeature.rsplit('/',1)[0]) == False:
                    # 数据地址路径不存在或有误
                    nameRes = '错误: "' + \
                                  os.path.basename(indexPath) + \
                                  '"索引文件中"' + \
                                  layerName + \
                                  '"索引表中"' + \
                                  imgNameInFeature + \
                                  '"对应地址的"' + \
                                  imgPathInFeature.rsplit('/', 1)[0] + \
                                  '"路径有误，请检查'
                    resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                     '名称一致性': nameRes,
                                                     '范围一致性': '-'}
                    continue

                imgPath = [ imgPathInFeature.rsplit('/',1)[0] + '/'+ filename
                                 for filename in os.listdir(imgPathInFeature.rsplit('/',1)[0])
                                 if '.' in filename and filename.rsplit('.',1)[1]=='img']
                xmlPath = [ imgPathInFeature.rsplit('/',1)[0] + '/'+ filename
                                 for filename in os.listdir(imgPathInFeature.rsplit('/',1)[0])
                                 if '.' in filename and 'img' not in filename and filename.rsplit('.',1)[1]=='xml']

                imgPathChosen = ''
                xmlPathChosen = ''

                if imgPath.__len__() == 0:
                    #影像数据不存在
                    nameRes = '错误: "' + \
                              os.path.basename(indexPath) + \
                              '"索引文件中"' + \
                              layerName + \
                              '"索引表中"' + \
                              imgNameInFeature + \
                              '"对应地址"' + \
                              imgPathInFeature.rsplit('/', 1)[0] + \
                              '"路径下无影像文件，请检查'
                    resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                 '名称一致性': nameRes,
                                                 '范围一致性': '-'}
                    continue
                elif imgPathInFeature not in imgPath:
                    #有多个影像数据，且没有一个是目标影像数据
                    imgPathChosen = imgPath[0]
                    pass
                else:
                    #有多个影像数据，且存在目标影像数据
                    imgPathChosen = imgPathInFeature
                    pass

                if xmlPath.__len__() == 0:
                    #元数据不存在
                    nameRes = '错误: "' + \
                              os.path.basename(indexPath) + \
                              '"索引文件中"' + \
                              layerName + \
                              '"索引表中"' + \
                              imgNameInFeature + \
                              '"对应地址"' + \
                              imgPathInFeature.rsplit('/', 1)[0] + \
                              '"路径下无元数据文件，请检查'
                    resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                 '名称一致性': nameRes,
                                                 '范围一致性': '-'}
                    continue
                elif imgPathInFeature.rsplit('.',1)[0]+'.xml' not in xmlPath:
                    #有多个元数据，且没有一个是目标元数据
                    xmlPathChosen = xmlPath[0]
                else:
                    #有多个元数据，且存在目标元数据
                    xmlPathChosen = imgPathInFeature.rsplit('.',1)[0]+'.xml'

                imgName = os.path.basename(imgPathChosen).rsplit('.',1)[0]
                xmlName = os.path.basename(xmlPathChosen).rsplit('.',1)[0]

                if imgNameInFeature != imgName or imgNameInFeature != xmlName or imgName != xmlName:
                    #名称不一致的情况，反馈后直接跳过范围检查
                    nameRes = '错误: "' + \
                                  os.path.basename(indexPath) + \
                                  '"索引文件中"' + \
                                  layerName + \
                                  '"索引表中"' + \
                                  imgNameInFeature + \
                                  '"对应地址"' + \
                                  imgPath[0] + \
                                  '"路径下，元数据名为"' + \
                                  xmlName.__str__() + \
                                  '"，影像名称为"' + \
                                  imgName.__str__() + \
                                  '"'
                    resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                     '名称一致性': nameRes,
                                                     '范围一致性': '-'}
                else:
                    #一致的情况，继续进行范围检查
                    envelope = feature.geometry().GetEnvelope()

                    #计算要素图廓的长宽
                    w = envelope[1] - envelope[0]
                    h = envelope[3] - envelope[2]

                    #获取要素图廓的左上角经纬度坐标
                    fCood = (envelope[0],envelope[3])
                    ds = gdal.Open(imgPath[0])
                    geot = ds.GetGeoTransform()

                    #获取影像的左上角经纬度坐标
                    iCood = (geot[0],geot[3])

                    #计算要素图廓与影像在经纬线方向上的偏移量
                    deltaW = abs(fCood[0] - iCood[0])
                    deltaH = abs(fCood[1] - iCood[1])

                    if deltaW >= w/2 or deltaH >= h/2:
                        #此时要素图廓与影像算作没有对应上
                        rangeRes = '"' + \
                                   imgNameInFeature + \
                                  '"矢量与影像的范围没有正确对应'
                        resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                     '名称一致性': '无误',
                                                     '范围一致性': rangeRes}
                    else:
                        #此时要素图廓与影像对应了
                        resDict[imgNameInFeature] = {'所属索引表': layerName,
                                                     '名称一致性': '无误',
                                                     '范围一致性': '无误'}

        #当前文件中所有索引表中所有记录项都已经检查完毕
        return (resDict,indexPath,indexFileNum)

    def pyIndexMatchCallBack(self,res):
        """
        pyIndexMatch的回调函数，用于记录日志和更新进度条。

        :param res: pyIndexMatch的返回值，为(resDict,indexPath,indexFileNum)
        :return: None
        """
        self.domCount += 1

        self.logRcd.emitInfo('[INFO] '+'(' + self.domCount.__str__()  + '/' + res[2].__str__() + ') ' + res[1])
        self.logRcd.emitProcessValue(int(100.0 * self.domCount /res[2]))

        itemCount = 1
        itemNum = res[0].__len__()
        for item in res[0]:
            self.logRcd.emitInfo('[INFO]   ' + itemCount.__str__() + '/' + itemNum.__str__() + '  ' + item)
            nameRes = res[0][item]['名称一致性']
            rangeRes = res[0][item]['范围一致性']
            self.logRcd.emitInfo('[INFO] 名称一致性：\n' + nameRes)
            self.logRcd.emitInfo('[INFO] 范围一致性：\n' + rangeRes + '\n')
            itemCount+=1

        self.emitDomTableItemData((res[0],res[1]))

    def domIndexMatcher(self,indexFileNum):
        """
        DOM影像与索引匹配检查

        :return: None
        """
        self.logRcd.emitInfo('[CONFIG] 任务项：DOM影像与索引匹配检查')
        self.logRcd.emitInfo('[CONFIG] 索引数据输入目录：' + self.indexDirPath)
        coreNum = mp.cpu_count()
        self.logRcd.emitInfo('[CONFIG] 检查模式：并行（CPU核心数 '+ coreNum.__str__() +  '）')
        self.logRcd.emitInfo('[INFO] 进程池初始化...')
        domPool = mp.Pool(coreNum)
        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')

        for indexPath in self.indexPathList:
            #domPool.apply(self.pyIndexMatch,(indexPath, indexFileNum))
            domPool.apply_async(self.pyIndexMatch,(indexPath, indexFileNum, self.panCap),callback=self.pyIndexMatchCallBack)
        domPool.close()
        domPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()