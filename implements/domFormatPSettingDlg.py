# -*- coding:utf-8 -*-
"""
domFormatPSettingDlg.py
~~~~~~~~~~~~~~~~~~~~~~~

DOM分辨率与坐标系检查时设置检查参数的对话框。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from PySide2 import QtWidgets,QtGui,QtCore
from ui import ui_formatparamsdlg
import os

class domformatpsettingdlg(QtWidgets.QDialog):
    domFormatTableItemDataSignal = QtCore.Signal(object)  # 发送参数信息的signal
    def __init__(self):
        super(domformatpsettingdlg, self).__init__(None)
        self.ui = ui_formatparamsdlg.Ui_formatparamsdlg()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.95)
        font = QtGui.QFont()
        font.setBold(True)
        self.ui.fomatTitle.setFont(font)

        self.paramsDict = {}

        self.ui.crsNameCBox.stateChanged.connect(self.crsNameStateChanged)
        self.ui.accCBox.stateChanged.connect(self.accStateChanged)
        # self.ui.xResCBox.stateChanged.connect(self.xResStateChanged)
        # self.ui.yResCBox.stateChanged.connect(self.yResStateChanged)
        self.ui.datumNameCBox.stateChanged.connect(self.datumNameStateChanged)
        self.ui.spNameCBox.stateChanged.connect(self.spNameStateChanged)
        self.ui.smajorCBox.stateChanged.connect(self.smajorStateChanged)
        self.ui.ieCBox.stateChanged.connect(self.ieStateChanged)
        self.ui.unitNameCBox.stateChanged.connect(self.unitNameStateChanged)
        self.ui.unitrpuCBox.stateChanged.connect(self.unitrpuStateChanged)
        self.ui.primemNameCBox.stateChanged.connect(self.primemNameStateChanged)
        self.ui.primemlonCBox.stateChanged.connect(self.primemlonStateChanged)

        self.ui.closeButton.clicked.connect(self.closeButtonClicked)
        self.ui.cancelButton.clicked.connect(self.cancelButtonClicked)
        self.ui.okButton.clicked.connect(self.okButtonClicked)

    def crsNameStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.crsNameLineEdit.setEnabled(True)
        else:
            self.ui.crsNameLineEdit.setEnabled(False)

    def accStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.accLineEdit.setEnabled(True)
            self.ui.xResLineEdit.setEnabled(True)
            self.ui.xResLineEdit2.setEnabled(True)
            self.ui.yResLineEdit.setEnabled(True)
            self.ui.yResLineEdit2.setEnabled(True)
        else:
            self.ui.accLineEdit.setEnabled(False)
            self.ui.xResLineEdit.setEnabled(False)
            self.ui.xResLineEdit2.setEnabled(False)
            self.ui.yResLineEdit.setEnabled(False)
            self.ui.yResLineEdit2.setEnabled(False)

    # def xResStateChanged(self,state):
    #     if state == QtCore.Qt.Checked:
    #         self.ui.xResLineEdit.setEnabled(True)
    #         self.ui.xResLineEdit2.setEnabled(True)
    #     else:
    #         self.ui.xResLineEdit.setEnabled(False)
    #         self.ui.xResLineEdit2.setEnabled(False)
    #
    # def yResStateChanged(self,state):
    #     if state == QtCore.Qt.Checked:
    #         self.ui.yResLineEdit.setEnabled(True)
    #         self.ui.yResLineEdit2.setEnabled(True)
    #     else:
    #         self.ui.yResLineEdit.setEnabled(False)
    #         self.ui.yResLineEdit2.setEnabled(False)

    def datumNameStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.datumNameLineEdit.setEnabled(True)
        else:
            self.ui.datumNameLineEdit.setEnabled(False)

    def spNameStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.spNameLineEdit.setEnabled(True)
        else:
            self.ui.spNameLineEdit.setEnabled(False)

    def smajorStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.smajorLineEdit.setEnabled(True)
        else:
            self.ui.smajorLineEdit.setEnabled(False)

    def ieStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.ieLineEdit.setEnabled(True)
        else:
            self.ui.ieLineEdit.setEnabled(False)

    def unitNameStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.unitNameLineEdit.setEnabled(True)
        else:
            self.ui.unitNameLineEdit.setEnabled(False)

    def unitrpuStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.unitrpuLineEdit.setEnabled(True)
        else:
            self.ui.unitrpuLineEdit.setEnabled(False)

    def primemNameStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.primemNameLineEdit.setEnabled(True)
        else:
            self.ui.primemNameLineEdit.setEnabled(False)

    def primemlonStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.ui.primemlonLineEdit.setEnabled(True)
        else:
            self.ui.primemlonLineEdit.setEnabled(False)

    def cancelButtonClicked(self):
        self.reject()

    def closeButtonClicked(self):
        self.reject()

    def okButtonClicked(self):
        self.paramsDict.clear()
        if self.ui.crsNameCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['坐标系名称'] = self.ui.crsNameLineEdit.currentText().__str__()
        if self.ui.accCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['分辨率'] = self.ui.accLineEdit.currentText().__str__()
            self.paramsDict['X分辨率min'] = self.ui.xResLineEdit.text().__str__()
            self.paramsDict['X分辨率max'] = self.ui.xResLineEdit2.text().__str__()
            self.paramsDict['Y分辨率min'] = self.ui.yResLineEdit.text().__str__()
            self.paramsDict['Y分辨率max'] = self.ui.yResLineEdit2.text().__str__()
        if self.ui.datumNameCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['基准面名称'] = self.ui.datumNameLineEdit.text().__str__()
        if self.ui.spNameCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['椭球体名称'] = self.ui.spNameLineEdit.text().__str__()
        if self.ui.smajorCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['椭球体长半轴'] = self.ui.smajorLineEdit.text().__str__()
        if self.ui.ieCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['椭球体反扁率'] = self.ui.ieLineEdit.text().__str__()
        if self.ui.unitNameCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['角度单位名称'] = self.ui.unitNameLineEdit.text().__str__()
        if self.ui.unitrpuCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['每单位弧度'] = self.ui.unitrpuLineEdit.text().__str__()
        if self.ui.primemNameCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['本初子午线名称'] = self.ui.primemNameLineEdit.text().__str__()
        if self.ui.primemlonCBox.checkState() == QtCore.Qt.Checked:
            self.paramsDict['本初子午线经度'] = self.ui.primemlonLineEdit.text().__str__()
        self.domFormatTableItemDataSignal.emit(self.paramsDict)
        self.accept()

    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton:
    #         self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
    #         event.accept()
    #
    # def mouseMoveEvent(self, event):
    #     if event.buttons() == QtCore.Qt.LeftButton:
    #         self.move(event.globalPos() - self.dragPosition)
    #         event.accept()

    def paintEvent(self, paintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtGui.QColor(61,174,233),1,QtCore.Qt.SolidLine))
        # painter.setRenderHint(QPainter.Antialiasing) ## 抗锯齿
        painter.drawRoundedRect(0,0,self.width()-1,self.height() -1,2,2)