# -*- coding:utf-8 -*-
"""
reportoutputDlg.py
~~~~~~~~~~~~~~~~~~

质检报告导出时提示进度的对话框。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from PySide2 import QtWidgets,QtCore
from ui import ui_reportoutputdlg
from implements import roImpl

class reportoutputdlg(QtWidgets.QDialog):
    def __init__(self,TableWidget,reportOutputPath):
        super(reportoutputdlg, self).__init__(None)
        self.ui = ui_reportoutputdlg.Ui_reportoutputdialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.t = roImpl.roImpl(TableWidget,reportOutputPath)
        self.t.processSignal.connect(self.onSetProcessBarValue)
        self.t.isfinishedSignal.connect(self.onIsFinished)
        self.t.start()

    def onSetProcessBarValue(self,pValue):
        self.ui.progressBar.setValue(pValue)

    def onIsFinished(self,isSuccessful):
        if isSuccessful:
            self.ui.progressBar.setValue(100)
            QtWidgets.QMessageBox.information(self, u"提示",
                                              u"质检报告导出成功！",
                                              QtWidgets.QMessageBox.Ok)
        else:
            self.ui.progressBar.setValue(0)
            QtWidgets.QMessageBox.information(self, u"提示",
                                              u"质检报告导出失败！",
                                              QtWidgets.QMessageBox.Ok)
        self.accept()