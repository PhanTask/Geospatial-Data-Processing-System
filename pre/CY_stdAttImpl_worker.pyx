#!/usr/bin/env python
# -*- coding: utf-8 -*-
# distutils: language=c++

import re
import ogr
import os
import cython
cimport cython
# import numpy as np
# cimport numpy as np
# from cpython cimport array
# import array
from openpyxl import Workbook

cdef class CY_stdAttImpl_worker():
    """
    时空专题数据规范性检查，对不同字段进行正则匹配
    """
    cdef str gdbInputDirPath,gdbDirOutputPath
    cdef dict reMatchDic,jsonDict
    cdef list gdbInputDirPathNoExtList
    cdef list gdbOutputDirPathNoExtList
    cdef int stdGdbCount, gdbCompleted
    def __init__(self,gdbInputDirPath,gdbDirOutputPath,reMatchDic,jsonDict):
        """
        初始化规范性检查类
        :param gdbInputDirPath: 输入专题数据gdb父级目录路径
        :param gdbDirOutputPath: 质检成果gdb文件父级目录路径
        :param reMatchDic: 正则匹配库，三层字典，第一层gdb名称，第二层lyr名称，第三层字段名，键值是正则表达式
        """
        self.gdbInputDirPath = gdbInputDirPath
        self.gdbDirOutputPath = gdbDirOutputPath
        self.reMatchDic = reMatchDic
        self.jsonDict = jsonDict
        self.gdbInputDirPathNoExtList=[]
        self.gdbOutputDirPathNoExtList=[]
        self.stdGdbCount=0
        self.gdbCompleted=0

    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    def getGdbInputPathList_Py(self):
        return self.getGdbInputPathList()
    #
    # def get_gdbInputDirPathNoExtList(self):
    #     return self.gdbInputDirPathNoExtList
    #
    # def get_gdbOutputDirPathNoExtList(self):
    #     return self.gdbOutputDirPathNoExtList

    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    cdef int getGdbInputPathList(self):
        """
        从所给的gdb文件夹路径中将所有gdb文件的路径提取出来。并复制到指定路径
        :return: feature数据数量
        """

        # 列表推导式  os.path.join()：  将多个路径组合后返回
        print('getGdbInputPathList')
        cdef list dirs = os.listdir(self.gdbInputDirPath + u'/')
        for dir in dirs:
            if dir[-3:] == u'gdb':
                # 复制为新的处理文件
                copyFilePath = self.gdbDirOutputPath + u'/' + dir.replace(u'.gdb', u'.xlsx')
                dir=self.gdbInputDirPath+ u'/' +dir
                #加入原始文件无后缀gdb路径列表
                self.gdbInputDirPathNoExtList.append(dir)
                self.gdbOutputDirPathNoExtList.append(copyFilePath)
        print('getGdbInputPathList pass')
        return self.gdbInputDirPathNoExtList.__len__()


    # cdef int startProcess(self):
    #     """
    #     主执行函数
    #     :return:
    #     """
    #
    #     # self.logRcd.emitInfo(u'[CONFIG] 任务项：时空专题大数据属性规范性检查')
    #     # self.logRcd.emitInfo(u'[CONFIG] 输入目录：' + self.gdbInputDirPath)
    #     # self.logRcd.emitInfo(u'[CONFIG] 输出目录：' + self.gdbDirOutputPath)
    #     # self.logRcd.emitInfo(u'[CONFIG] 规则库设置：')
    #     #
    #     # for key in self.jsonDict:
    #     #     self.logRcd.emitInfo(u'[CONFIG]   - ' + key.__str__() + u' : ' + self.jsonDict[key].__str__())
    #     #
    #     # self.logRcd.emitInfo(u'\n[CONFIG] 检查模式：串行（核心数 ' + mp.cpu_count().__str__() + u'）')
    #     # self.logRcd.emitInfo(u'[INFO] 初始化...')
    #     # self.logRcd.emitInfo(u'[INFO] 初始化成功，开始检查数据...\n')
    #     #每个文件生成一个一一对应的字典
    #     #多进程处理分gdb处理
    #     # domPool = mp.Pool(2)
    #     # 遍历gdbOutput数据，进行检查
    #     for gdbInputDir,gdbOutputDir in zip(self.gdbInputDirPathNoExtList, self.gdbOutputDirPathNoExtList):
    #         # gdbFile = ogr.Open(gdbOutputDir, 1)
    #         self.eachProcess(gdbInputDir,gdbOutputDir,self.reMatchDic[os.path.split(gdbInputDir)[1]])
    #         # domPool.apply_async(self.eachProcess,
    #         #                     args=(gdbInputDir,gdbOutputDir,self.reMatchDic[os.path.split(gdbInputDir)[1]]),
    #         #                     callback=self.mpProcessCallBack)
    #     # self.logRcd.emitProcessValue(100)
    #     # self.logRcd.emitInfo(u'[INFO] 检查完成')
    #     # self.logRcd.logFileClose()

    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    cdef str fieldCheck(self, str keyPattern, str keyType, str strField ):
        '''
        正则匹配实现算法
        :param keyPattern:
        :param keyType:
        :param strField:
        :return:
        '''

        cdef str fieldCheckResult
        cdef bint matchObj

        # print('fieldCheck')

        if strField is None:
            return ''
        # if keyType[:-10] == 'OBJECTID':
        #     return ''
        try:
            #keyPattern1 = re.compile(keyPattern, re.I | re.M)
            matchObj = re.match(re.compile(keyPattern, re.I | re.M), strField)

            fieldCheckResult = ''
            if matchObj:
                #fieldCheckResult = keyType + 'success:' + matchObj.group().__str__()
                fieldCheckResult=''
            else:
                #fieldCheckResult = keyType + 'error：' + strField
                fieldCheckResult = strField + ' 错误'
            return fieldCheckResult
        except Exception as e:
            print(e.__str__())

    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    cdef str timeFieldCheck(self, str workTimePattern, str keyType, str strField):
        cdef list matchList,matchReslutSplitList
        # workTimePattern = r'\d{1,2}[:：.]\d{2}|\d{1,2}点\d{0,2}'
        # print('timeFieldCheck')
        if strField == '' or strField is None:
            return '空值 错误'
        matchList = re.findall(workTimePattern, strField)
        for matchReslut in matchList:
            if ':' in matchReslut:
                matchReslutSplitList = matchReslut.split(':')
                if int(matchReslutSplitList[0]) < 0 or int(matchReslutSplitList[0]) > 24 \
                        or int(matchReslutSplitList[1]) < 0 or int(matchReslutSplitList[1]) > 60:
                    return strField + ' 错误'
                continue
            if '：' in matchReslut:
                matchReslutSplitList = matchReslut.split('：')
                if int(matchReslutSplitList[0]) < 0 or int(matchReslutSplitList[0]) > 24 \
                        or int(matchReslutSplitList[1]) < 0 or int(matchReslutSplitList[1]) > 60:
                    return strField + ' 错误'

                continue
            if '点' in matchReslut:
                matchReslutSplitList = matchReslut.split('点')
                if matchReslutSplitList.__len__() == 1 or matchReslutSplitList[1] == '':
                    if int(matchReslutSplitList[0]) < 0 or int(matchReslutSplitList[0]) > 24:
                        return strField + ' 错误'

                    continue
                try:
                    if int(matchReslutSplitList[0]) < 0 or int(matchReslutSplitList[0]) > 24 \
                            or int(matchReslutSplitList[1]) < 0 or int(matchReslutSplitList[1]) > 60:
                        return strField + ' 错误'

                    continue
                except Exception as e:
                    print(e.__str__())
        return ''

    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    def eachProcess_Py(self, index):
        return self.eachProcess(index)

    # 静态函数标注
    # @staticmethod
    @cython.boundscheck(False)  # Deactivate bounds checking
    @cython.wraparound(False)   # Deactivate negative indexing.
    cdef list eachProcess(self, int index):
        """
        多进程处理函数
        :param gdbOuputDirPath：待检查文件路径
        :param layerVsReDic:    各图层正则匹配字典,一级键是图层名称，二级键是字典或者字段名称,值是正则表达式
        :return:  返回可视化表格单行参数以及信号参数
        """
        cdef dict oFeErrorNumDic = {}
        cdef int layerCount = 0,layerNum = 0, dictCount = 0, dictNum = 0, oFeErrorNum = 0, ErrNum = 0, ErrCount = 0
        cdef str fieldCheckRes
        cdef str signalProcess = ''
        cdef str fieldCheckResTotal = ''
        cdef list itemDataList = []
        cdef list dictKeys
        cdef list dictValues = []
        cdef str gdbInputDirPath = self.gdbInputDirPathNoExtList[index]
        cdef str gdbOuputDirPath = self.gdbOutputDirPathNoExtList[index]
        cdef dict layerDefnVsReDic = self.reMatchDic[os.path.split(gdbInputDirPath)[1]]
        cdef list oFeErrorKeys
        cdef list oFeErrorValues
        # cdef int excelColCount = 4
        cdef int excelRowCount = 1

        layerName = ''

        self.gdbCompleted += 1

        wbk = Workbook()
        sheet = wbk.active
        sheet.title = '质检结果'
        sheet.cell(row = excelRowCount,column = 1,value="ObjectID")
        sheet.cell(row = excelRowCount,column = 2,value="名称")
        sheet.cell(row = excelRowCount,column = 3,value="所属图层")
        sheet.cell(row = excelRowCount,column = 4,value="质检结果详情")

        # print('pass')

        excelRowCount = 2

        #注册驱动
        driver = ogr.GetDriverByName('OpenFileGDB')
        # 打开
        gdbOutputFile = driver.Open(gdbInputDirPath, 0)

        #gdbOutputFile = ogr.Open(gdbOuputDirPath, 0)
        if gdbOutputFile == None:
            print("打开文件%s失败！" % gdbOuputDirPath)
            return 0
        print("打开文件%s成功！" % gdbOuputDirPath)

        layerNum = gdbOutputFile.GetLayerCount()

        # for oLayer in gdbOutputFile:
        for layerCount in range(layerNum):
            print('for layerCount in range(layerNum):')
            oFeErrorNum = 0
            ErrNum = 0

            oLayer = gdbOutputFile.GetLayer(layerCount)
            layerName = oLayer.GetName()
            print(layerName)
            dictKeys = list(layerDefnVsReDic[layerName].keys())
            dictValues = list(layerDefnVsReDic[layerName].values())
            dictNum = dictKeys.__len__()
            # layerDefnVsReDicNum = layerDefnVsReDic[layerName].__len__()
            # for key,value in layerDefnVsReDic[layerName].items():
            for dictCount in range(dictNum):
                key = dictKeys[dictCount]
                if dictValues[dictCount][0] == '不检查':
                    continue
                # oLayer.CreateField(ogr.FieldDefn(key + 'FieldCheck', ogr.OFTString))
                # 错误统计字典初始化
                oFeErrorNumDic[key+'ErrNum']=0
                ErrNum += 1
            # for key, value in layerDefnVsReDic[oLayer.GetName()].items():
            #     tmpFieldC = key + u'FieldCheck'
            #     oLayer.CreateField(ogr.FieldDefn(tmpFieldC, ogr.OFTString))
            #     # 错误统计字典初始化
            #     oFeErrorNumDic[key + 'ErrNum'] = 0
            # oLayer.ResetReading()
            oFeature = oLayer.GetNextFeature()
            fieldCheckRes = ''
            while oFeature is not None:
                isFeErrorRecorded = False
                # for key, value in layerDefnVsReDic[layerName].items():
                fieldCheckResTotal = ''
                for dictCount in range(dictNum):
                    key = dictKeys[dictCount]
                    value = dictValues[dictCount]
                    if value[0] == '不检查':
                        continue
                    tmpFieldC = key + 'FieldCheck'
                    if value[0] == '时间':
                        workTimePattern=value[1]
                        fieldCheckRes = self.timeFieldCheck(workTimePattern, 'workTimeFieldCheck',
                                                               oFeature.GetField(key))
                    else:
                        fieldCheckRes = self.fieldCheck(value[1], tmpFieldC,oFeature.GetField(key))
                    #写入与统计
                    if fieldCheckRes != '':
                        # oFeature.SetField(tmpFieldC, fieldCheckRes)
                        # oLayer.SetFeature(oFeature)
                        oFeErrorNumDic[key + 'ErrNum'] += 1
                        if isFeErrorRecorded == False:
                            sheet.cell(row = excelRowCount,column = 1,value=oFeature.GetFID().__str__())
                            sheet.cell(row = excelRowCount,column = 2,value=oFeature.GetField('name').__str__())
                            sheet.cell(row = excelRowCount,column = 3,value=layerName.__str__())
                            oFeErrorNum += 1
                            isFeErrorRecorded = True
                        fieldCheckResTotal += tmpFieldC.__str__() + ' : ' + fieldCheckRes.__str__() + ' ; '
                        # tempFeat = oLayer.GetFeature(oFeature.GetFID())
                        # print(u'------')
                        # print(tempFeat.GetField(tmpFieldC))
                        # tempFeat = None
                    # else:
                    #     pass
                        # oFeature.SetField(tmpFieldC, fieldCheckRes)
                        # oLayer.SetFeature(oFeature)
                if isFeErrorRecorded == True:
                    sheet.cell(row = excelRowCount,column = 4,value=fieldCheckResTotal.__str__())
                    excelRowCount += 1
                oFeature = None
                oFeature = oLayer.GetNextFeature()
            #stdProTableItemData 以图层为单位，图层名称，检查字段总个数，要素总个数，要素出错个数，输入路径，输出路径，
            stdProTableItemData=(layerName,
                                 ErrNum.__str__(),
                                 oLayer.GetFeatureCount().__str__(),
                                 oFeErrorNum.__str__(),
                                 gdbInputDirPath,
                                 gdbOuputDirPath
            )

            print('stdProTableItemData')

            itemDataList.append(stdProTableItemData)
            # self.emitStdTableItemData(stdProTableItemData)
            print('1')
            signalProcess +=  '[INFO] ' + layerName+'共检查'+ ErrNum.__str__() +'个字段\n'

            oFeErrorKeys = list(oFeErrorNumDic.keys())
            oFeErrorValues = list(oFeErrorNumDic.values())

            # for (key,value) in oFeErrorNumDic.items():
            print('2')
            for ErrCount in range(ErrNum):
                signalProcess += '[INFO] ' + oFeErrorKeys[ErrCount] +' : ' + oFeErrorValues[ErrCount].__str__() +'\n'
                print('3')

            # signalProcess = signalProcess + tempS
            # self.logRcd.emitInfo(signalProcess + u'\n')
            # self.logRcd.emitProcessValue(int(100.0 * self.gdbCompleted / self.stdGdbCount))
            # self.logRcd.emitProcessValue(int(100.0 * (((self.gdbCompleted - 1) / self.stdGdbCount) + layerCount / layerNum / self.stdGdbCount)))
            # layerCount += 1
            print('3 finished')
            oLayer = None
            print('4')
        print("before wbk save")
        wbk.save(gdbOuputDirPath)
        print("after wbk save")
        return [itemDataList,signalProcess]