# -*- coding:utf-8 -*-
"""
logRcd.py
~~~~~~~~~~

日志模块功能实现。

:copyright: (c) 2018 by Jinmeng Rao.
"""
from PySide2 import QtCore
import codecs
import time
import os

class logRcd(QtCore.QObject):
    infomsgSignal = QtCore.Signal( str ) # 日志signal
    processSignal = QtCore.Signal( int ) # 进度signal

    def emitInfo(self, msg ):
        try:
            self.logFile.write( msg + '\n' )
            self.logFile.flush()
            self.infomsgSignal.emit( msg )
        except Exception as e:
            print(e.__str__())

    def emitProcessValue(self,pValue):
        self.processSignal.emit( pValue)

    def logFileClose(self):
        self.logFile.close()

    def __init__(self,taskname):
        """
        初始化logRcd类。
        """
        super(logRcd, self).__init__()
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        self.logFile = open('.\\log\\' + taskname + time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time())) + '.txt','a+',encoding = 'utf-8')