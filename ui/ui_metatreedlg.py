# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metatreedlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_metatreeDlg(object):
    def setupUi(self, metatreeDlg):
        metatreeDlg.setObjectName("metatreeDlg")
        metatreeDlg.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(metatreeDlg)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xmlNameLabel = QtWidgets.QLabel(metatreeDlg)
        self.xmlNameLabel.setObjectName("xmlNameLabel")
        self.horizontalLayout.addWidget(self.xmlNameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.xmlCloseButton = QtWidgets.QPushButton(metatreeDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmlCloseButton.sizePolicy().hasHeightForWidth())
        self.xmlCloseButton.setSizePolicy(sizePolicy)
        self.xmlCloseButton.setMinimumSize(QtCore.QSize(20, 20))
        self.xmlCloseButton.setMaximumSize(QtCore.QSize(20, 20))
        self.xmlCloseButton.setFlat(False)
        self.xmlCloseButton.setObjectName("xmlCloseButton")
        self.horizontalLayout.addWidget(self.xmlCloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.xmlTreeWidget = QtWidgets.QTreeWidget(metatreeDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmlTreeWidget.sizePolicy().hasHeightForWidth())
        self.xmlTreeWidget.setSizePolicy(sizePolicy)
        self.xmlTreeWidget.setObjectName("xmlTreeWidget")
        self.xmlTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.xmlTreeWidget)

        self.xmlTreeWidget.setColumnCount(2)
        self.xmlTreeWidget.setHeaderLabels([u'项',u'值'])
        self.xmlTreeWidget.expandAll()

        self.retranslateUi(metatreeDlg)
        QtCore.QMetaObject.connectSlotsByName(metatreeDlg)

    def retranslateUi(self, metatreeDlg):
        _translate = QtCore.QCoreApplication.translate
        metatreeDlg.setWindowTitle(_translate("metatreeDlg", "Dialog"))
        self.xmlNameLabel.setText(_translate("metatreeDlg", "TextLabel"))
        self.xmlCloseButton.setText(_translate("metatreeDlg", "×"))
