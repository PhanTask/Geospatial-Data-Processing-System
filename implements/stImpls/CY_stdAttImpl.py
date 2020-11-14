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
from implements.stImpls.CY_stdAttImpl_worker import CY_stdAttImpl_worker
import threading


# class workerThread(QtCore.QThread):
#     resultListEmitter = QtCore.Signal(object)  # 信号
#
#     def __init__(self, gdbInputDirPath,gdbDirOutputPath,reMatchDic,jsonDict):
#         super(workerThread, self).__init__()
#         self.worker = CY_stdAttImpl_worker(gdbInputDirPath, gdbDirOutputPath, reMatchDic, jsonDict)
#
#     def setIndex(self, index):
#         self.index = index
#
#     def run(self):
#         resultList = self.worker.eachProcess_Py(self.index)
#         self.resultListEmitter.emit(resultList)


class propertyStdCheckImp(QtCore.QThread):
    """
    时空专题数据规范性检查，对不同字段进行正则匹配
    """
    doneflag  = QtCore.Signal(bool) # 是否成功完成
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
        # self.workerThread = workerThread(gdbInputDirPath,gdbDirOutputPath,reMatchDic,jsonDict)
        self.workerThread = CY_stdAttImpl_worker(gdbInputDirPath,gdbDirOutputPath,reMatchDic,jsonDict)
        self.stdGdbCount = 0
        self.gdbInputDirPath = gdbInputDirPath
        self.gdbDirOutputPath = gdbDirOutputPath
        self.reMatchDic = reMatchDic
        self.jsonDict = jsonDict
        # self.gdbInputDirPathNoExtList=[]
        # self.gdbOutputDirPathNoExtList=[]
        # self.stdGdbCount=0
        # self.gdbCompleted=0
        self.gdbCompleted = 0
        self.logRcd = logRcd('时空专题大数据属性规范性检查日志')
        # self.workerThread.resultListEmitter.connect(self.emitResult)

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
            self.stdGdbCount = self.workerThread.getGdbInputPathList_Py()
            self.startProcess()
        except Exception as e:
            print('ERROR ' + e.__str__())


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

        self.logRcd.emitInfo('\n[CONFIG] 检查模式：并行（核心数 ' + mp.cpu_count().__str__() + '）')
        self.logRcd.emitInfo('[INFO] 初始化...')
        self.logRcd.emitInfo('[INFO] 初始化成功，开始检查数据...')

        # self.worker.startProcess()
        #每个文件生成一个一一对应的字典
        #多进程处理分gdb处理
        domPool = mp.Pool(4)
        # 遍历gdbOutput数据，进行检查
        self.logRcd.emitProcessValue(10)
        # for gdbInputDir,gdbOutputDir in zip(self.worker.get_gdbInputDirPathNoExtList(), self.worker.get_gdbOutputDirPathNoExtList()):
        for i in range(self.stdGdbCount):
            # gdbFile = ogr.Open(gdbOutputDir, 1)
            # self.workerThread.setIndex(i)
            # self.workerThread.start()
            # self.workerThread.wait()
            # self.logRcd.emitProcessValue(10 + int((i+1)*90/self.stdGdbCount))
            # self.emitStdTableItemData(resultList[0])
            # self.logRcd.emitInfo(resultList[1])
            domPool.apply_async(self.workerThread.eachProcess_Py,
                                args=(i,),
                                callback=self.emitResult)
            self.logRcd.emitInfo('[INFO] (' + (i + 1).__str__() + '/' + self.stdGdbCount.__str__() + ') 文件已加载，质检结果将批量返回，请稍候...\n')
            # domPool.apply(self.workerThread.eachProcess_Py,
            #                     args=(i,),)
        domPool.close()
        domPool.join()
        self.logRcd.emitProcessValue(100)
        self.logRcd.emitInfo('[INFO] 检查完成')
        self.logRcd.logFileClose()

    def emitResult(self, resultList):
        self.logRcd.emitInfo('\n[INFO] ' + resultList[0][0][4].__str__() + ' 检查结果：')
        self.gdbCompleted += 1
        self.logRcd.emitProcessValue(10 + 90 * self.gdbCompleted / self.stdGdbCount)
        self.emitStdTableItemData(resultList[0])
        self.logRcd.emitInfo(resultList[1])