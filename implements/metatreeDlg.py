# -*- coding:utf-8 -*-
"""
metatreeDlg.py
~~~~~~~~~~~~~~

质检报告导出时提示进度的对话框。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from PySide2 import QtWidgets,QtGui,QtCore
from ui import ui_metatreedlg
import xml.etree.ElementTree as et
import os

class metatreeDlg(QtWidgets.QDialog):
    def __init__(self,xmlMetaPath):
        super(metatreeDlg, self).__init__(None)
        self.ui = ui_metatreedlg.Ui_metatreeDlg()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.xmlCloseButton.clicked.connect(self.xmlCloseButtonClicked)
        self.setWindowOpacity(0.95)
        self.ui.xmlNameLabel.setText(os.path.basename(xmlMetaPath).__str__())
        font = QtGui.QFont()
        font.setBold(True)
        self.ui.xmlNameLabel.setFont(font)
        self.xmlLoad(xmlMetaPath)

    def xmlLoad(self,xmlMetaPath):
        root = et.parse(xmlMetaPath).getroot()
        rootItem = QtWidgets.QTreeWidgetItem(self.ui.xmlTreeWidget)
        rootItem.setText(0,root.tag)
        self.xmlTreeTraversal(root,rootItem)
        self.ui.xmlTreeWidget.addTopLevelItem(rootItem)
        self.ui.xmlTreeWidget.expandAll()
        self.ui.xmlTreeWidget.resizeColumnToContents(0)

    def xmlTreeTraversal(self,xmlItem,treeItem):
        if xmlItem.getchildren().__len__() != 0:
            for xmlChild in xmlItem:
                treeChild = QtWidgets.QTreeWidgetItem(treeItem)
                treeChild.setText(0,xmlChild.tag)
                self.xmlTreeTraversal(xmlChild,treeChild)
        else:
            treeItem.setText(1,xmlItem.text)
            return


    def xmlCloseButtonClicked(self):
        self.accept()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def paintEvent(self, paintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtGui.QColor(61,174,233),1,QtCore.Qt.SolidLine))
        # painter.setRenderHint(QPainter.Antialiasing) ## 抗锯齿
        painter.drawRoundedRect(0,0,self.width()-1,self.height() -1,2,2)