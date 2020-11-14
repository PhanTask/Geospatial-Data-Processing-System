#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 20:10
# @Author  : Dutian
# @Site    : 
# @File    : propertyStdCheckImp.py
# @Software: PyCharm
# @license : Copyright(C), Dutian
# @Contact : free.du@qq.com
import re
import ogr
import shutil
from PySide2 import QtCore
import os
import multiprocessing as mp
from logger.logRcd import logRcd


class propertyStdCheckImp(QtCore.QThread):
    """
    时空专题数据规范性检查，对不同字段进行正则匹配
    """
    doneflag = QtCore.Signal(bool) # 是否成功完成
    stdTableItemDataSignal = QtCore.Signal(object) # std表格项signal
    dostop = False # 是否强制终止
    processValue = 0.0 # 进度
    indexPathList = []
    stdFileNum = 0
    def __init__(self,gdbInputDirPath,gdbDirOutputPath,reMatchDic,jsonDict):
        """
        初始化规范性检查类
        :param gdbInputDirPath: 输入专题数据gdb父级目录路径
        :param gdbDirOutputPath: 质检成果gdb文件父级目录路径
        :param reMatchDic: 正则匹配库，三层字典，第一层gdb名称，第二层lyr名称，第三层字段名，键值是正则表达式
        """
        super(propertyStdCheckImp, self).__init__()
        self.gdbInputDirPath = gdbInputDirPath
        self.gdbDirOutputPath = gdbDirOutputPath
        self.reMatchDic = reMatchDic
        self.jsonDict = jsonDict
        self.gdbInputDirPathNoExtList=[]
        self.gdbOutputDirPathNoExtList=[]
        self.stdGdbCount=0
        self.gdbCompleted=0
        self.logRcd = logRcd('时空专题大数据属性规范性检查日志')

    def emitFinish( self, isSuccessful ):
        self.doneflag.emit( isSuccessful )

    def emitStdTableItemData(self, StdTableItemData):
        self.stdTableItemDataSignal.emit(StdTableItemData)

    def run(self, *args, **kwargs):
        """
        主执行函数
        :param args:
        :param kwargs:
        :return:
        """

        try:
            self.stdGdbCount=self.getGdbInputPathList()
            self.startProcess()

        except Exception as e:
            print('ERROR ' + e.__str__())


    def getGdbInputPathList(self):
        """
        从所给的gdb文件夹路径中将所有gdb文件的路径提取出来。并复制到指定路径
        :return: feature数据数量
        """

        # 列表推导式  os.path.join()：  将多个路径组合后返回
        for dir in os.listdir(self.gdbInputDirPath + '/'):
            if dir[-3:] == 'gdb':
                # 复制为新的处理文件
                copyFilePath = self.gdbDirOutputPath + '/' + dir.replace('.gdb', '_P.gdb')
                dir=self.gdbInputDirPath+ '/' +dir
                #加入原始文件无后缀gdb路径列表
                self.gdbInputDirPathNoExtList.append(dir)
                try:
                    shutil.copytree(dir , copyFilePath)
                except Exception as e:
                    shutil.rmtree(copyFilePath)  # 递归删除文件夹
                    shutil.copytree(dir, copyFilePath)
                #处理后gdb文件_p路径列表
                self.gdbOutputDirPathNoExtList.append(copyFilePath)
        # self.domPathNoExtList = [os.path.join(self.domIndexDirPath, dir, '') for dir in os.listdir(self.domIndexDirPath+'/') if dir[:-3]=='gdb']
        # print(self.domPathList)
        return self.gdbOutputDirPathNoExtList.__len__()


    def startProcess(self):
        """
        主执行函数
        :return:
        """

        self.logRcd.emitInfo('[CONFIG] 任务项：时空专题大数据属性规范性检查')
        self.logRcd.emitInfo('[CONFIG] 输入目录：' + self.gdbInputDirPath)
        self.logRcd.emitInfo('[CONFIG] 输出目录：' + self.gdbDirOutputPath)
        self.logRcd.emitInfo('[CONFIG] 规则库设置：')

        for key in self.jsonDict:
            self.logRcd.emitInfo('[CONFIG]   - ' + key.__str__() + ' : ' + self.jsonDict[key].__str__())

        self.logRcd.emitInfo('\n[CONFIG] 检查模式：串行（核心数 ' + mp.cpu_count().__str__() + '）')
        self.logRcd.emitInfo('[INFO] 初始化...')
        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...\n')
        #每个文件生成一个一一对应的字典
        #多进程处理分gdb处理
        # domPool = mp.Pool(2)
        # 遍历gdbOutput数据，进行检查
        for gdbInputDir,gdbOutputDir  in zip(self.gdbInputDirPathNoExtList, self.gdbOutputDirPathNoExtList):
            # gdbFile = ogr.Open(gdbOutputDir, 1)
            self.eachProcess(gdbInputDir,gdbOutputDir,self.reMatchDic[os.path.split(gdbInputDir)[1]])
            # domPool.apply_async(self.eachProcess,
            #                     args=(gdbInputDir,gdbOutputDir,self.reMatchDic[os.path.split(gdbInputDir)[1]]),
            #                     callback=self.mpProcessCallBack)
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()
    # 静态函数标注
    # @staticmethod
    def eachProcess(self,gdbInputDirPath,gdbOuputDirPath, layerDefnVsReDic ):
        """
        多进程处理函数
        :param gdbOuputDirPath：待检查文件路径
        :param layerVsReDic:    各图层正则匹配字典,一级键是图层名称，二级键是字典或者字段名称,值是正则表达式
        :return:  返回可视化表格单行参数以及信号参数
        """

        def fieldCheck(keyPattern, keyType, strField):
            '''
            正则匹配实现算法
            :param keyPattern:
            :param keyType:
            :param strField:
            :return:
            '''
            if strField is None:
                return ''
            # if keyType[:-10] == 'OBJECTID':
            #     return ''
            try:
                keyPattern1 = re.compile(keyPattern, re.I | re.M)

                matchObj = re.match(keyPattern1, strField)

                fieldCheckResult = ''
                if matchObj:
                    #fieldCheckResult = keyType + 'success:' + matchObj.group().__str__()
                    fieldCheckResult=''
                else:
                    #fieldCheckResult = keyType + 'error：' + strField
                    fieldCheckResult= strField + ' 错误'
                return fieldCheckResult
            except Exception as e:
                print(e.__str__())

        def timeFieldCheck(workTimePattern, keyType, strField):
            # workTimePattern = r'\d{1,2}[:：.]\d{2}|\d{1,2}点\d{0,2}'
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

        self.gdbCompleted += 1
        #注册驱动
        driver = ogr.GetDriverByName('FileGDB')
        # 打开
        gdbOutputFile = driver.Open(gdbOuputDirPath, 1)

        #gdbOutputFile = ogr.Open(gdbOuputDirPath, 0)
        if gdbOutputFile == None:
            print("打开文件%s失败！" % gdbOuputDirPath)
            return
        print("打开文件%s成功！" % gdbOuputDirPath)
        # 错误统计字典
        oFeErrorNumDic={'feAllErrorNum':0}

        layerCount = 1
        layerNum = gdbOutputFile.GetLayerCount()
        for oLayer in gdbOutputFile:
            for key,value in layerDefnVsReDic[oLayer.GetName()].items():
                if value[0] == '不检查':
                    continue
                # oLayer.CreateField(ogr.FieldDefn(key + u'FieldCheck', ogr.OFTString))
                # 错误统计字典初始化
                oFeErrorNumDic[key+'ErrNum']=0
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
                for key, value in layerDefnVsReDic[oLayer.GetName()].items():
                    if value[0] == '不检查':
                        continue
                    tmpFieldC = key + u'FieldCheck'
                    if value[0] == '时间':
                        workTimePattern=value[1]
                        fieldCheckRes = timeFieldCheck(workTimePattern, u'workTimeFieldCheck',
                                                               oFeature.GetField(key))
                    else:
                        fieldCheckRes = fieldCheck(value[1], tmpFieldC,oFeature.GetField(key))
                    #写入与统计
                    if fieldCheckRes != '':
                        # oFeature.SetField(tmpFieldC, fieldCheckRes)
                        # oLayer.SetFeature(oFeature)
                        oFeErrorNumDic[key + u'ErrNum'] += 1
                        if isFeErrorRecorded == False:
                            oFeErrorNumDic[u'feAllErrorNum'] += 1
                            isFeErrorRecorded = True
                        # tempFeat = oLayer.GetFeature(oFeature.GetFID())
                        # print(u'------')
                        # print(tempFeat.GetField(tmpFieldC))
                        # tempFeat = None
                    else:
                        pass
                        # oFeature.SetField(tmpFieldC, fieldCheckRes)
                        # oLayer.SetFeature(oFeature)
                oFeature = None
                oFeature = oLayer.GetNextFeature()
            #stdProTableItemData 以图层为单位，图层名称，检查字段总个数，要素总个数，要素出错个数，输入路径，输出路径，
            stdProTableItemData=(oLayer.GetName(),
                                 oFeErrorNumDic.__len__().__str__(),
                                 oLayer.GetFeatureCount().__str__(),
                                 oFeErrorNumDic[u'feAllErrorNum'].__str__(),
                                 gdbInputDirPath,
                                 gdbOuputDirPath
            )
            self.emitStdTableItemData(stdProTableItemData)
            signalProcess= '[INFO] ' + oLayer.GetName()+'共检查'+oFeErrorNumDic.__len__().__str__() +'个字段'+'\n'
            for (key,value) in oFeErrorNumDic.items():
                signalProcess+= '[INFO] ' + key+' : '+value.__str__()+'\n'
            self.logRcd.emitInfo(signalProcess + '\n')
            # self.logRcd.emitProcessValue(int(100.0 * self.gdbCompleted / self.stdGdbCount))
            self.logRcd.emitProcessValue(int(100.0 * (((self.gdbCompleted - 1) / self.stdGdbCount) + layerCount / layerNum / self.stdGdbCount)))
            layerCount += 1