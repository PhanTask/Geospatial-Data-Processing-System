#!/usr/bin/env python
# -*- coding: utf-8 -*-
# distutils: language=c

import ogr
import cython
cimport cython
from openpyxl import Workbook

cdef class CY_stdCodeImpl_worker():
    """
    时空专题数据检查，对不同字段进行正则匹配
    """
    cdef str gdbDir
    cdef str outputPath
    cdef int indexFileNum
    def __init__(self):
        self.gdbDir = ''
        self.outputPath = ''
        self.indexFileNum = 0

    cpdef list pystdCodeChecker(self, str indexPath, str outputPath2, int indexFileNum):
        """
        执行编码一致性检查操作

        :param indexPath: 原始索引表文件路径名，为str
        :param indexFileNum: 原始索引表文件个数，为int
        :return resDict: 检查结果，为dict
        """

        cdef str layerName,featName,featCode
        cdef set nameSet = set()
        cdef set nameAndCodeSet = set()
        cdef dict featDifferCounterDict = {}  # 各要素的编码种类的数量，若为1则该要素再各个图层中出现的编码都是一致的，大于1则存在不一致的情况
        cdef dict resultDict = {}
        cdef int layerCount
        cdef int layerNum
        cdef dict basicItem
        cdef dict unconsistItem
        cdef list keys = []
        cdef int itemCount,itemNum,conCounter
        cdef int excelRowCount = 1

        self.gdbDir = indexPath
        self.outputPath = outputPath2
        self.indexFileNum = indexFileNum

        wbk = Workbook()
        sheet = wbk.active
        sheet.title = '质检结果'
        sheet.cell(row = excelRowCount,column = 1,value="要素名称")
        sheet.cell(row = excelRowCount,column = 2,value="所属图层")
        sheet.cell(row = excelRowCount,column = 3,value="要素编码")
        sheet.cell(row = excelRowCount,column = 4,value="是否一致")
        excelRowCount += 1

        driver = ogr.GetDriverByName('FileGDB')
        gdbFile = driver.Open(self.gdbDir, 0)

        # 读取所有要素属性信息
        layerNum = gdbFile.GetLayerCount()
        # for oLayer in gdbFile:
        for layerCount in range(layerNum):
            oLayer = gdbFile.GetLayer(layerCount)
            layerName = oLayer.GetName()
            oFeature = oLayer.GetNextFeature()
            # for oFeature in oLayer:
            while oFeature is not None:
                featName = oFeature.GetField('name')
                if featName not in nameSet:
                    featCode = oFeature.GetField('uuid')
                    nameSet.add(featName)
                    nameAndCodeSet.add(featName + '/' + featCode)
                    featDifferCounterDict[featName] = 1
                    resultDict[featName] = []
                    basicItem = {'name': featName,
                                 'code': featCode,
                                 'layerName': layerName,
                                 'gdbDir': self.gdbDir
                                 }
                    resultDict[featName].append(basicItem)
                else:
                    featCode = oFeature.GetField('uuid')
                    featNameAndCode = featName + '/' + featCode
                    if featNameAndCode not in nameAndCodeSet:  # 相同名称要素编码不一致，通常是第一次检查到不一致的情况
                        nameAndCodeSet.add(featNameAndCode)
                        featDifferCounterDict[featName] += 1
                        unconsistItem = {'name': featName,
                                         'code': featCode,
                                         'layerName': layerName,
                                         'gdbDir': self.gdbDir
                                         }
                        resultDict[featName].append(unconsistItem)
                    else:  # 存在相同名称要素编码一致的情况，但可能只是与部分要素的编码一致，整体还可能不一致
                        if featDifferCounterDict[featName] > 1:  # 若要素数量大于1，说明该要素编码本身就存在多个不一致情况，仍判作不一致
                            unconsistItem = {'name': featName,
                                             'code': featCode,
                                             'layerName': layerName,
                                             'gdbDir': self.gdbDir
                                             }
                            resultDict[featName].append(unconsistItem)
                        # else:  # 遇到了相同名称要素编码完全一致的理想情况，检查合格
                        #     pass
                oFeature = oLayer.GetNextFeature()

        # keys = list(resultDict.keys())
        # itemNum = keys.__len__()

        print('FINISHED 1')
        infoString = ''
        itemCount = 1
        for item in resultDict:
            print('itemCount')
            # time.sleep(0.005)
            infoString+='[INFO]   ' + itemCount.__str__() + '/' + itemNum.__str__() + '  ' + item.__str__() + '\n'
            if resultDict[item].__len__() == 1:
                # sheet.cell(row = excelRowCount,column = 1,value=resultDict[keys[itemCount]][0]['name'].__str__())
                # sheet.cell(row = excelRowCount,column = 2,value=resultDict[keys[itemCount]][0]['layerName'].__str__())
                # sheet.cell(row = excelRowCount,column = 3,value=resultDict[keys[itemCount]][0]['code'].__str__())
                # sheet.cell(row = excelRowCount,column = 4,value='一致')
                infoString +='[INFO] 该要素编码均一致\n'
                infoString +='[INFO] 要素编码：' + resultDict[item][0]['code'].__str__() + '\n\n'
                itemCount += 1
                excelRowCount+=1
                continue
            else:
                infoString += '[INFO] 共出现 ' + resultDict[item].__len__().__str__() + ' 处编码不一致的要素 \n'
                conCounter = 1
                for con in resultDict[item]:
                    # sheet.cell(row = excelRowCount,column = 1,value=resultDict[keys[itemCount]][0]['name'].__str__())
                    # sheet.cell(row = excelRowCount,column = 2,value=resultDict[keys[itemCount]][0]['layerName'].__str__())
                    # sheet.cell(row = excelRowCount,column = 3,value=resultDict[keys[itemCount]][0]['code'].__str__())
                    # sheet.cell(row = excelRowCount,column = 4,value='不一致')
                    infoString +='[INFO] ----第 ' + conCounter.__str__() + ' 处要素----' + '\n'
                    infoString +='[INFO] 要素所在图层名称：' + con['layerName'].__str__()+ '\n'
                    infoString +='[INFO] 要素编码：' + con['code'].__str__()+ '\n'
                    infoString +='[INFO] 要素所在文件路径：' + con['gdbDir'].__str__() + '\n\n'
                    conCounter += 1
                    excelRowCount+=1
                itemCount += 1
        print('FINISHED 2')
        wbk.save(self.outputPath)
        return [resultDict,self.gdbDir,self.indexFileNum,infoString]