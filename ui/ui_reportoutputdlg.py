# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportoutputdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_reportoutputdialog(object):
    def setupUi(self, reportoutputdialog):
        reportoutputdialog.setObjectName("reportoutputdialog")
        reportoutputdialog.resize(300, 60)
        self.verticalLayout = QtWidgets.QVBoxLayout(reportoutputdialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(reportoutputdialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(reportoutputdialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(reportoutputdialog)
        QtCore.QMetaObject.connectSlotsByName(reportoutputdialog)

    def retranslateUi(self, reportoutputdialog):
        _translate = QtCore.QCoreApplication.translate
        reportoutputdialog.setWindowTitle(_translate("reportoutputdialog", "Dialog"))
        self.label.setText(_translate("reportoutputdialog", "质检报告导出中，请稍候……"))

