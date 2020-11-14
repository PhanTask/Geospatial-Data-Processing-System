# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_ProcessDialog(object):
    def setupUi(self, ProcessDialog):
        ProcessDialog.setObjectName("ProcessDialog")
        ProcessDialog.resize(480, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProcessDialog.sizePolicy().hasHeightForWidth())
        ProcessDialog.setSizePolicy(sizePolicy)
        ProcessDialog.setMinimumSize(QtCore.QSize(480, 330))
        ProcessDialog.setMaximumSize(QtCore.QSize(480, 330))
        self.progressBar = QtWidgets.QProgressBar(ProcessDialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 40, 441, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.logText = QtWidgets.QTextEdit(ProcessDialog)
        self.logText.setGeometry(QtCore.QRect(20, 90, 441, 191))
        self.logText.setFrameShape(QtWidgets.QFrame.Box)
        self.logText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.label = QtWidgets.QLabel(ProcessDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName("label")
        self.finishButton = QtWidgets.QPushButton(ProcessDialog)
        self.finishButton.setGeometry(QtCore.QRect(370, 290, 91, 31))
        self.finishButton.setObjectName("finishButton")
        self.terminateButton = QtWidgets.QPushButton(ProcessDialog)
        self.terminateButton.setGeometry(QtCore.QRect(270, 290, 91, 31))
        self.terminateButton.setObjectName("terminateButton")

        self.retranslateUi(ProcessDialog)
        QtCore.QMetaObject.connectSlotsByName(ProcessDialog)
        self.initUIconfig()

    def initUIconfig(self):
        self.terminateButton.setEnabled(False)

    def retranslateUi(self, ProcessDialog):
        _translate = QtCore.QCoreApplication.translate
        ProcessDialog.setWindowTitle(_translate("ProcessDialog", "进度对话框"))
        self.label.setText(_translate("ProcessDialog", "处理进度"))
        self.finishButton.setText(_translate("ProcessDialog", "完成"))
        self.terminateButton.setText(_translate("ProcessDialog", "强制终止"))

