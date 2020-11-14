# -*- coding: utf-8 -*-
"""
mainui.py
~~~~~~~

界面文件。

:copyright: (c) 2018 by Jinmeng Rao.
"""
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from implements import processDlg,reportoutputDlg,metatreeDlg,domFormatPSettingDlg
import os
import json
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainHLayout = QtWidgets.QHBoxLayout()
        self.mainHLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.mainHLayout.setContentsMargins(5, 5, 5, 5)
        self.mainHLayout.setSpacing(5)
        self.mainHLayout.setObjectName("mainHLayout")
        self.modelScrollArea = QtWidgets.QScrollArea(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelScrollArea.sizePolicy().hasHeightForWidth())
        self.modelScrollArea.setSizePolicy(sizePolicy)
        self.modelScrollArea.setMinimumSize(QtCore.QSize(210, 0))
        self.modelScrollArea.setMaximumSize(QtCore.QSize(210, 16777215))
        self.modelScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.modelScrollArea.setWidgetResizable(True)
        self.modelScrollArea.setObjectName("modelScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 191, 521))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.modelVerticalLayout = QtWidgets.QVBoxLayout()
        self.modelVerticalLayout.setSpacing(2)
        self.modelVerticalLayout.setObjectName("modelVerticalLayout")
        self.domButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.domButton.setMinimumSize(QtCore.QSize(0, 80))
        self.domButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.domButton.setObjectName("domButton")
        self.modelVerticalLayout.addWidget(self.domButton)
        self.demButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.demButton.setMinimumSize(QtCore.QSize(0, 80))
        self.demButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.demButton.setObjectName("demButton")
        self.modelVerticalLayout.addWidget(self.demButton)
        self.stdataButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.stdataButton.setMinimumSize(QtCore.QSize(0, 80))
        self.stdataButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.stdataButton.setObjectName("stdataButton")
        self.modelVerticalLayout.addWidget(self.stdataButton)
        self.modelButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.modelButton.setMinimumSize(QtCore.QSize(0, 80))
        self.modelButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.modelButton.setObjectName("modelButton")
        self.modelVerticalLayout.addWidget(self.modelButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.modelVerticalLayout.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.modelVerticalLayout)
        self.modelScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mainHLayout.addWidget(self.modelScrollArea)
        self.mainContent = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContent.sizePolicy().hasHeightForWidth())
        self.mainContent.setSizePolicy(sizePolicy)
        self.mainContent.setTabBarAutoHide(False)
        self.mainContent.setObjectName("mainContent")
        self.domContentTab = QtWidgets.QWidget()
        self.domContentTab.setObjectName("domContentTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.domContentTab)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.domVLayout = QtWidgets.QVBoxLayout()
        self.domVLayout.setContentsMargins(5, 5, 5, 5)
        self.domVLayout.setSpacing(5)
        self.domVLayout.setObjectName("domVLayout")
        self.domContent = QtWidgets.QTabWidget(self.domContentTab)
        self.domContent.setObjectName("domContent")
        self.domWBTab = QtWidgets.QWidget()
        self.domWBTab.setObjectName("domWBTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.domWBTab)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.domWBVLayout = QtWidgets.QVBoxLayout()
        self.domWBVLayout.setContentsMargins(5, 5, 5, 5)
        self.domWBVLayout.setSpacing(5)
        self.domWBVLayout.setObjectName("domWBVLayout")
        self.domWBParamsVLayout = QtWidgets.QVBoxLayout()
        self.domWBParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.domWBParamsVLayout.setSpacing(5)
        self.domWBParamsVLayout.setObjectName("domWBParamsVLayout")
        self.domWBParamsIGLayout = QtWidgets.QGridLayout()
        self.domWBParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.domWBParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.domWBParamsIGLayout.setSpacing(5)
        self.domWBParamsIGLayout.setObjectName("domWBParamsIGLayout")
        self.domWBILabel = QtWidgets.QLabel(self.domWBTab)
        self.domWBILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBILabel.setObjectName("domWBILabel")
        self.domWBParamsIGLayout.addWidget(self.domWBILabel, 0, 0, 1, 1)
        self.domWBIBrowerButton = QtWidgets.QPushButton(self.domWBTab)
        self.domWBIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBIBrowerButton.setObjectName("domWBIBrowerButton")
        self.domWBParamsIGLayout.addWidget(self.domWBIBrowerButton, 0, 2, 1, 1)
        self.domWBILineEdit = QtWidgets.QLineEdit(self.domWBTab)
        self.domWBILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBILineEdit.setObjectName("domWBILineEdit")
        self.domWBParamsIGLayout.addWidget(self.domWBILineEdit, 0, 1, 1, 1)
        self.domWBParamsVLayout.addLayout(self.domWBParamsIGLayout)
        self.domWBParamsGBox = QtWidgets.QGroupBox(self.domWBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domWBParamsGBox.sizePolicy().hasHeightForWidth())
        self.domWBParamsGBox.setSizePolicy(sizePolicy)
        self.domWBParamsGBox.setMinimumSize(QtCore.QSize(0, 80))
        self.domWBParamsGBox.setMaximumSize(QtCore.QSize(16777215, 160))
        self.domWBParamsGBox.setObjectName("domWBParamsGBox")

        self.domGBoxVLayout = QtWidgets.QVBoxLayout(self.domWBParamsGBox)
        self.domGBoxVLayout.setContentsMargins(5, 5, 5, 5)
        self.domGBoxVLayout.setSpacing(5)
        self.domGBoxVLayout.setObjectName("domGBoxVLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.domWBParamsGBox)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(255)
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox_2.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(10)
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.label_3 = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox_3.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(10)
        self.horizontalLayout.addWidget(self.spinBox_3)

        self.label_4 = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_4 = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox_4.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setValue(4)
        self.horizontalLayout.addWidget(self.spinBox_4)

        spacerItema = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItema)

        self.domGBoxVLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_m = QtWidgets.QHBoxLayout(self.domWBParamsGBox)
        self.horizontalLayout_m.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_m.setSpacing(5)
        self.horizontalLayout_m.setObjectName("horizontalLayout_m")
        self.label_resform = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_resform.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resform.setObjectName("label_resform")
        self.horizontalLayout_m.addWidget(self.label_resform)
        self.resformComboBox = QtWidgets.QComboBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resformComboBox.sizePolicy().hasHeightForWidth())
        self.resformComboBox.setSizePolicy(sizePolicy)
        self.resformComboBox.setObjectName("resformComboBox")
        self.resformComboBox.addItem('img')
        self.resformComboBox.addItem('tif')
        self.resformComboBox.setMinimumSize(QtCore.QSize(20, 25))
        self.resformComboBox.setMaximumSize(QtCore.QSize(20, 25))
        self.horizontalLayout_m.addWidget(self.resformComboBox)
        self.label_ovr = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_ovr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ovr.setObjectName("label_ovr")
        self.horizontalLayout_m.addWidget(self.label_ovr)
        self.ovrCBox = QtWidgets.QCheckBox(self.domWBParamsGBox)
        self.ovrCBox.setChecked(True)
        self.ovrCBox.setObjectName("ovrCBox")
        self.horizontalLayout_m.addWidget(self.ovrCBox)
        self.label_nodata = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_nodata.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nodata.setObjectName("label_nodata")
        self.horizontalLayout_m.addWidget(self.label_nodata)
        self.nodataCBox = QtWidgets.QCheckBox(self.domWBParamsGBox)
        self.nodataCBox.setChecked(True)
        self.nodataCBox.setObjectName("nodataCBox")
        self.horizontalLayout_m.addWidget(self.nodataCBox)

        self.label_c254 = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_c254.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c254.setObjectName("label_c254")
        self.horizontalLayout_m.addWidget(self.label_c254)
        self.c254CBox = QtWidgets.QCheckBox(self.domWBParamsGBox)
        self.c254CBox.setChecked(True)
        self.c254CBox.setObjectName("c254CBox")
        self.horizontalLayout_m.addWidget(self.c254CBox)

        spacerItem_m = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_m.addItem(spacerItem_m)
        self.domGBoxVLayout.addLayout(self.horizontalLayout_m)

        self.horizontalLayout_e = QtWidgets.QHBoxLayout(self.domWBParamsGBox)
        self.horizontalLayout_e.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_e.setSpacing(5)
        self.horizontalLayout_e.setObjectName("horizontalLayout_e")

        self.label_easyKill = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_easyKill.setAlignment(QtCore.Qt.AlignCenter)
        self.label_easyKill.setObjectName("label_easyKill")
        self.horizontalLayout_e.addWidget(self.label_easyKill)
        self.easyKillCBox = QtWidgets.QCheckBox(self.domWBParamsGBox)
        self.easyKillCBox.setChecked(False)
        self.easyKillCBox.setObjectName("easyKillCBox")
        self.horizontalLayout_e.addWidget(self.easyKillCBox)

        self.label_easyColors = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_easyColors.setAlignment(QtCore.Qt.AlignCenter)
        self.label_easyColors.setObjectName("label_easyColors")
        self.horizontalLayout_e.addWidget(self.label_easyColors)
        self.spinBox_easyColors = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_easyColors.sizePolicy().hasHeightForWidth())
        self.spinBox_easyColors.setSizePolicy(sizePolicy)
        self.spinBox_easyColors.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox_easyColors.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox_easyColors.setMaximum(255)
        self.spinBox_easyColors.setObjectName("spinBox_easyColors")
        self.spinBox_easyColors.setValue(0)
        self.horizontalLayout_e.addWidget(self.spinBox_easyColors)

        self.label_easyNearDist = QtWidgets.QLabel(self.domWBParamsGBox)
        self.label_easyNearDist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_easyNearDist.setObjectName("label_easyNearDist")
        self.horizontalLayout_e.addWidget(self.label_easyNearDist)
        self.spinBox_easyNearDist = QtWidgets.QSpinBox(self.domWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_easyNearDist.sizePolicy().hasHeightForWidth())
        self.spinBox_easyNearDist.setSizePolicy(sizePolicy)
        self.spinBox_easyNearDist.setMinimumSize(QtCore.QSize(20, 25))
        self.spinBox_easyNearDist.setMaximumSize(QtCore.QSize(20, 25))
        self.spinBox_easyNearDist.setMaximum(255)
        self.spinBox_easyNearDist.setObjectName("spinBox_easyNearDist")
        self.spinBox_easyNearDist.setValue(5)
        self.horizontalLayout_e.addWidget(self.spinBox_easyNearDist)

        spacerItem_e = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_e.addItem(spacerItem_e)
        self.domGBoxVLayout.addLayout(self.horizontalLayout_e)

        self.domWBParamsVLayout.addWidget(self.domWBParamsGBox)
        self.domWBPraramsOGLayout = QtWidgets.QGridLayout()
        self.domWBPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.domWBPraramsOGLayout.setSpacing(5)
        self.domWBPraramsOGLayout.setObjectName("domWBPraramsOGLayout")
        self.domWBOLabel = QtWidgets.QLabel(self.domWBTab)
        self.domWBOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBOLabel.setObjectName("domWBOLabel")
        self.domWBPraramsOGLayout.addWidget(self.domWBOLabel, 0, 0, 1, 1)
        self.domWBOLineEdit = QtWidgets.QLineEdit(self.domWBTab)
        self.domWBOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBOLineEdit.setObjectName("domWBOLineEdit")
        self.domWBPraramsOGLayout.addWidget(self.domWBOLineEdit, 0, 1, 1, 1)
        self.domWBOBrowerButton = QtWidgets.QPushButton(self.domWBTab)
        self.domWBOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domWBOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domWBOBrowerButton.setObjectName("domWBOBrowerButton")
        self.domWBPraramsOGLayout.addWidget(self.domWBOBrowerButton, 0, 2, 1, 1)
        self.domWBParamsVLayout.addLayout(self.domWBPraramsOGLayout)
        self.line = QtWidgets.QFrame(self.domWBTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setObjectName("line")
        self.domWBParamsVLayout.addWidget(self.line)
        self.domWBOpHLayout = QtWidgets.QHBoxLayout()
        self.domWBOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.domWBOpHLayout.setSpacing(5)
        self.domWBOpHLayout.setObjectName("domWBOpHLayout")
        self.domWBReportButton = QtWidgets.QPushButton(self.domWBTab)
        self.domWBReportButton.setObjectName("domWBReportButton")
        self.domWBOpHLayout.addWidget(self.domWBReportButton)
        self.domWBLogButton = QtWidgets.QPushButton(self.domWBTab)
        self.domWBLogButton.setObjectName("domWBLogButton")
        self.domWBOpHLayout.addWidget(self.domWBLogButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.domWBOpHLayout.addItem(spacerItem1)
        self.domWBStartButton = QtWidgets.QPushButton(self.domWBTab)
        self.domWBStartButton.setObjectName("domWBStartButton")
        self.domWBOpHLayout.addWidget(self.domWBStartButton)
        self.domWBParamsVLayout.addLayout(self.domWBOpHLayout)
        self.domWBVLayout.addLayout(self.domWBParamsVLayout)
        self.domTableWidget = QtWidgets.QTableWidget(self.domWBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domTableWidget.sizePolicy().hasHeightForWidth())
        self.domTableWidget.setSizePolicy(sizePolicy)
        self.domTableWidget.setObjectName("domTableWidget")
        self.domTableWidget.setColumnCount(0)
        self.domTableWidget.setRowCount(0)
        self.domWBVLayout.addWidget(self.domTableWidget)
        self.verticalLayout_3.addLayout(self.domWBVLayout)
        self.domContent.addTab(self.domWBTab, "")
        """
        domCoverTab
        """
        self.domCoverTab = QtWidgets.QWidget()
        self.domCoverTab.setObjectName("domCoverTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.domCoverTab)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.domCVLayout = QtWidgets.QVBoxLayout()
        self.domCVLayout.setContentsMargins(5, 5, 5, 5)
        self.domCVLayout.setSpacing(5)
        self.domCVLayout.setObjectName("domCVLayout")
        self.domCParamsVLayout = QtWidgets.QVBoxLayout()
        self.domCParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.domCParamsVLayout.setSpacing(5)
        self.domCParamsVLayout.setObjectName("domCParamsVLayout")
        self.domCParamsIGLayout = QtWidgets.QGridLayout()
        self.domCParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.domCParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.domCParamsIGLayout.setSpacing(5)
        self.domCParamsIGLayout.setObjectName("domCParamsIGLayout")
        self.domCILabel = QtWidgets.QLabel(self.domCoverTab)
        self.domCILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domCILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCILabel.setObjectName("domCILabel")
        self.domCParamsIGLayout.addWidget(self.domCILabel, 0, 0, 1, 1)
        self.domCIBrowerButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domCIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCIBrowerButton.setObjectName("domCIBrowerButton")
        self.domCParamsIGLayout.addWidget(self.domCIBrowerButton, 0, 2, 1, 1)
        self.domCILineEdit = QtWidgets.QLineEdit(self.domCoverTab)
        self.domCILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domCILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCILineEdit.setObjectName("domCILineEdit")
        self.domCParamsIGLayout.addWidget(self.domCILineEdit, 0, 1, 1, 1)
        self.domCParamsVLayout.addLayout(self.domCParamsIGLayout)
        self.domCParamsADGLayout = QtWidgets.QGridLayout()
        self.domCParamsADGLayout.setContentsMargins(5, 5, 5, 5)
        self.domCParamsADGLayout.setSpacing(5)
        self.domCParamsADGLayout.setObjectName("domCParamsADGLayout")
        self.domCADLabel = QtWidgets.QLabel(self.domCoverTab)
        self.domCADLabel.setObjectName("domCADLabel")
        self.domCParamsADGLayout.addWidget(self.domCADLabel, 0, 0, 1, 1)
        self.domCADLineEdit = QtWidgets.QLineEdit(self.domCoverTab)
        self.domCADLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domCADLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCADLineEdit.setObjectName("domCADLineEdit")
        self.domCParamsADGLayout.addWidget(self.domCADLineEdit, 0, 1, 1, 1)
        self.domCADBrowerButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCADBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domCADBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCADBrowerButton.setObjectName("domCADBrowerButton")
        self.domCParamsADGLayout.addWidget(self.domCADBrowerButton, 0, 2, 1, 1)
        self.domCParamsVLayout.addLayout(self.domCParamsADGLayout)
        self.domCParamsGBox = QtWidgets.QGroupBox(self.domCoverTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domCParamsGBox.sizePolicy().hasHeightForWidth())
        self.domCParamsGBox.setSizePolicy(sizePolicy)
        self.domCParamsGBox.setMinimumSize(QtCore.QSize(0, 80))
        self.domCParamsGBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.domCParamsGBox.setObjectName("domCParamsGBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.domCParamsGBox)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.domCParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comCCityComboBox = QtWidgets.QComboBox(self.domCParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comCCityComboBox.sizePolicy().hasHeightForWidth())
        self.comCCityComboBox.setSizePolicy(sizePolicy)
        self.comCCityComboBox.setObjectName("comCCityComboBox")
        self.horizontalLayout_5.addWidget(self.comCCityComboBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.domCParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.domCCountyComboBox = QtWidgets.QComboBox(self.domCParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domCCountyComboBox.sizePolicy().hasHeightForWidth())
        self.domCCountyComboBox.setSizePolicy(sizePolicy)
        self.domCCountyComboBox.setObjectName("domCCountyComboBox")
        self.horizontalLayout_4.addWidget(self.domCCountyComboBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.domCParamsVLayout.addWidget(self.domCParamsGBox)
        self.domCPraramsOGLayout = QtWidgets.QGridLayout()
        self.domCPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.domCPraramsOGLayout.setSpacing(5)
        self.domCPraramsOGLayout.setObjectName("domCPraramsOGLayout")
        self.domCOLabel = QtWidgets.QLabel(self.domCoverTab)
        self.domCOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domCOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCOLabel.setObjectName("domCOLabel")
        self.domCPraramsOGLayout.addWidget(self.domCOLabel, 0, 0, 1, 1)
        self.domCOLineEdit = QtWidgets.QLineEdit(self.domCoverTab)
        self.domCOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domCOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCOLineEdit.setObjectName("domCOLineEdit")
        self.domCPraramsOGLayout.addWidget(self.domCOLineEdit, 0, 1, 1, 1)
        self.domCOBrowerButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domCOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domCOBrowerButton.setObjectName("domCOBrowerButton")
        self.domCPraramsOGLayout.addWidget(self.domCOBrowerButton, 0, 2, 1, 1)
        self.domCParamsVLayout.addLayout(self.domCPraramsOGLayout)
        self.line_2 = QtWidgets.QFrame(self.domCoverTab)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.domCParamsVLayout.addWidget(self.line_2)
        self.domCOpHLayout = QtWidgets.QHBoxLayout()
        self.domCOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.domCOpHLayout.setSpacing(5)
        self.domCOpHLayout.setObjectName("domCOpHLayout")
        self.domCReportButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCReportButton.setObjectName("domCReportButton")
        self.domCOpHLayout.addWidget(self.domCReportButton)
        self.domCLogButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCLogButton.setObjectName("domCLogButton")
        self.domCOpHLayout.addWidget(self.domCLogButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.domCOpHLayout.addItem(spacerItem3)
        self.domCStartButton = QtWidgets.QPushButton(self.domCoverTab)
        self.domCStartButton.setObjectName("domCStartButton")
        self.domCOpHLayout.addWidget(self.domCStartButton)
        self.domCParamsVLayout.addLayout(self.domCOpHLayout)
        self.domCVLayout.addLayout(self.domCParamsVLayout)
        self.domCTableWidget = QtWidgets.QTableWidget(self.domCoverTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domCTableWidget.sizePolicy().hasHeightForWidth())
        self.domCTableWidget.setSizePolicy(sizePolicy)
        self.domCTableWidget.setObjectName("domCTableWidget")
        self.domCTableWidget.setColumnCount(0)
        self.domCTableWidget.setRowCount(0)
        self.domCVLayout.addWidget(self.domCTableWidget)
        self.verticalLayout_8.addLayout(self.domCVLayout)
        self.domContent.addTab(self.domCoverTab, "")
        """
        domFormatTab
        """
        self.domFormatTab = QtWidgets.QWidget()
        self.domFormatTab.setObjectName("domFormatTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.domFormatTab)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.domFormatVLayout = QtWidgets.QVBoxLayout()
        self.domFormatVLayout.setContentsMargins(5, 5, 5, 5)
        self.domFormatVLayout.setSpacing(5)
        self.domFormatVLayout.setObjectName("domFormatVLayout")
        self.domFormatParamsVLayout = QtWidgets.QVBoxLayout()
        self.domFormatParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.domFormatParamsVLayout.setSpacing(5)
        self.domFormatParamsVLayout.setObjectName("domFormatParamsVLayout")
        self.domFormatParamsIGLayout = QtWidgets.QGridLayout()
        self.domFormatParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.domFormatParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.domFormatParamsIGLayout.setSpacing(5)
        self.domFormatParamsIGLayout.setObjectName("domFormatParamsIGLayout")
        self.domFormatILabel = QtWidgets.QLabel(self.domFormatTab)
        self.domFormatILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domFormatILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domFormatILabel.setObjectName("domFormatILabel")
        self.domFormatParamsIGLayout.addWidget(self.domFormatILabel, 0, 0, 1, 1)
        self.domFormatIBrowerButton = QtWidgets.QPushButton(self.domFormatTab)
        self.domFormatIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domFormatIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domFormatIBrowerButton.setObjectName("domFormatIBrowerButton")
        self.domFormatParamsIGLayout.addWidget(self.domFormatIBrowerButton, 0, 2, 1, 1)
        self.domFormatILineEdit = QtWidgets.QLineEdit(self.domFormatTab)
        self.domFormatILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domFormatILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domFormatILineEdit.setObjectName("domFormatILineEdit")
        self.domFormatParamsIGLayout.addWidget(self.domFormatILineEdit, 0, 1, 1, 1)
        self.domFormatParamsVLayout.addLayout(self.domFormatParamsIGLayout)
        self.domFormatParamsGBox = QtWidgets.QGroupBox(self.domFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domFormatParamsGBox.sizePolicy().hasHeightForWidth())
        self.domFormatParamsGBox.setSizePolicy(sizePolicy)
        self.domFormatParamsGBox.setMinimumSize(QtCore.QSize(0, 80))
        self.domFormatParamsGBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.domFormatParamsGBox.setObjectName("domFormatParamsGBox")
        self.gridLayout = QtWidgets.QGridLayout(self.domFormatParamsGBox)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(6)















        self.gridLayout.setObjectName("gridLayout")
        self.domFormatPButtonVLayout = QtWidgets.QVBoxLayout()
        self.domFormatPButtonVLayout.setContentsMargins(5, 5, 5, 5)
        self.domFormatPButtonVLayout.setSpacing(5)
        self.domFormatPButtonVLayout.setObjectName("domFormatPButtonVLayout")
        self.domFormatPSettingButton = QtWidgets.QPushButton(self.domFormatParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domFormatPSettingButton.sizePolicy().hasHeightForWidth())
        self.domFormatPSettingButton.setSizePolicy(sizePolicy)
        self.domFormatPSettingButton.setObjectName("domFormatPSettingButton")
        self.domFormatPButtonVLayout.addWidget(self.domFormatPSettingButton)
        self.domFormatPResetButton = QtWidgets.QPushButton(self.domFormatParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domFormatPResetButton.sizePolicy().hasHeightForWidth())
        self.domFormatPResetButton.setSizePolicy(sizePolicy)
        self.domFormatPResetButton.setObjectName("domFormatPResetButton")
        self.domFormatPButtonVLayout.addWidget(self.domFormatPResetButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.domFormatPButtonVLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.domFormatPButtonVLayout, 0, 1, 1, 1)
        self.domFormatParamsTWidget = QtWidgets.QTableWidget(self.domFormatParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domFormatParamsTWidget.sizePolicy().hasHeightForWidth())
        self.domFormatParamsTWidget.setSizePolicy(sizePolicy)
        self.domFormatParamsTWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.domFormatParamsTWidget.setObjectName("domFormatParamsTWidget")
        self.gridLayout.addWidget(self.domFormatParamsTWidget, 0, 0, 1, 1)
        self.domFormatParamsVLayout.addWidget(self.domFormatParamsGBox)
        self.line_4 = QtWidgets.QFrame(self.domFormatTab)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.domFormatParamsVLayout.addWidget(self.line_4)
        self.domFormatOpHLayout = QtWidgets.QHBoxLayout()
        self.domFormatOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.domFormatOpHLayout.setSpacing(5)
        self.domFormatOpHLayout.setObjectName("domFormatOpHLayout")
        self.domFormatReportButton = QtWidgets.QPushButton(self.domFormatTab)
        self.domFormatReportButton.setObjectName("domFormatReportButton")
        self.domFormatOpHLayout.addWidget(self.domFormatReportButton)
        self.domFormatLogButton = QtWidgets.QPushButton(self.domFormatTab)
        self.domFormatLogButton.setObjectName("domFormatLogButton")
        self.domFormatOpHLayout.addWidget(self.domFormatLogButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.domFormatOpHLayout.addItem(spacerItem3)
        self.domFormatStartButton = QtWidgets.QPushButton(self.domFormatTab)
        self.domFormatStartButton.setObjectName("domFormatStartButton")
        self.domFormatOpHLayout.addWidget(self.domFormatStartButton)
        self.domFormatParamsVLayout.addLayout(self.domFormatOpHLayout)
        self.domFormatVLayout.addLayout(self.domFormatParamsVLayout)
        self.domFormatTableWidget = QtWidgets.QTableWidget(self.domFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domFormatTableWidget.sizePolicy().hasHeightForWidth())
        self.domFormatTableWidget.setSizePolicy(sizePolicy)
        self.domFormatTableWidget.setObjectName("domFormatTableWidget")
        self.domFormatTableWidget.setColumnCount(0)
        self.domFormatTableWidget.setRowCount(0)
        self.domFormatVLayout.addWidget(self.domFormatTableWidget)
        self.verticalLayout_6.addLayout(self.domFormatVLayout)
        self.domContent.addTab(self.domFormatTab, "")
        """
        domMatchTab
        """
        self.domMatchTab = QtWidgets.QWidget()
        self.domMatchTab.setObjectName("domMatchTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.domMatchTab)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.domMatchVLayout = QtWidgets.QVBoxLayout()
        self.domMatchVLayout.setContentsMargins(5, 5, 5, 5)
        self.domMatchVLayout.setSpacing(5)
        self.domMatchVLayout.setObjectName("domMatchVLayout")
        self.domMatchParamsVLayout = QtWidgets.QVBoxLayout()
        self.domMatchParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.domMatchParamsVLayout.setSpacing(5)
        self.domMatchParamsVLayout.setObjectName("domMatchParamsVLayout")
        # self.domMatchParamsIGLayout = QtWidgets.QGridLayout()
        # self.domMatchParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        # self.domMatchParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        # self.domMatchParamsIGLayout.setSpacing(5)
        # self.domMatchParamsIGLayout.setObjectName("domMatchParamsIGLayout")
        # self.domMatchIBrowerButton = QtWidgets.QPushButton(self.domMatchTab)
        # self.domMatchIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        # self.domMatchIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.domMatchIBrowerButton.setObjectName("domMatchIBrowerButton")
        # self.domMatchParamsIGLayout.addWidget(self.domMatchIBrowerButton, 0, 2, 1, 1)
        # self.domMatchILineEdit = QtWidgets.QLineEdit(self.domMatchTab)
        # self.domMatchILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        # self.domMatchILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.domMatchILineEdit.setObjectName("domMatchILineEdit")
        # self.domMatchParamsIGLayout.addWidget(self.domMatchILineEdit, 0, 1, 1, 1)
        # self.domMatchILabel = QtWidgets.QLabel(self.domMatchTab)
        # self.domMatchILabel.setMinimumSize(QtCore.QSize(0, 24))
        # self.domMatchILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.domMatchILabel.setObjectName("domMatchILabel")
        # self.domMatchParamsIGLayout.addWidget(self.domMatchILabel, 0, 0, 1, 1)
        # self.domMatchParamsVLayout.addLayout(self.domMatchParamsIGLayout)
        self.domMatchParamsIndexGLayout = QtWidgets.QGridLayout()
        self.domMatchParamsIndexGLayout.setContentsMargins(5, 5, 5, 5)
        self.domMatchParamsIndexGLayout.setSpacing(5)
        self.domMatchParamsIndexGLayout.setObjectName("domMatchParamsIndexGLayout")
        self.domMatchIndexLabel = QtWidgets.QLabel(self.domMatchTab)
        self.domMatchIndexLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domMatchIndexLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domMatchIndexLabel.setObjectName("domMatchIndexLabel")
        self.domMatchParamsIndexGLayout.addWidget(self.domMatchIndexLabel, 0, 0, 1, 1)
        self.domMatchIndexBrowerButton = QtWidgets.QPushButton(self.domMatchTab)
        self.domMatchIndexBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.domMatchIndexBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domMatchIndexBrowerButton.setObjectName("domMatchIndexBrowerButton")
        self.domMatchParamsIndexGLayout.addWidget(self.domMatchIndexBrowerButton, 0, 2, 1, 1)
        self.domMatchIndexLineEdit = QtWidgets.QLineEdit(self.domMatchTab)
        self.domMatchIndexLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domMatchIndexLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domMatchIndexLineEdit.setObjectName("domMatchIndexLineEdit")
        self.domMatchParamsIndexGLayout.addWidget(self.domMatchIndexLineEdit, 0, 1, 1, 1)
        self.domMatchParamsVLayout.addLayout(self.domMatchParamsIndexGLayout)

        self.domMatchPanHLayout = QtWidgets.QHBoxLayout()
        self.domMatchPanHLayout.setContentsMargins(5, 5, 5, 5)
        self.domMatchPanHLayout.setSpacing(5)
        self.domMatchPanHLayout.setObjectName("domMatchPanHLayout")
        self.domMatchPanLabel = QtWidgets.QLabel(self.domMatchTab)
        self.domMatchPanLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.domMatchPanLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.domMatchPanLabel.setObjectName("domMatchPanLabel")
        self.domMatchPanHLayout.addWidget(self.domMatchPanLabel)
        self.domMatchPanLineEdit = QtWidgets.QLineEdit(self.domMatchTab)
        self.domMatchPanLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.domMatchPanLineEdit.setMaximumSize(QtCore.QSize(40, 24))
        self.domMatchPanLineEdit.setObjectName("domMatchPanLineEdit")
        self.domMatchPanHLayout.addWidget(self.domMatchPanLineEdit)
        self.spacerItem_0803 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.domMatchPanHLayout.addItem(self.spacerItem_0803)
        self.domMatchParamsVLayout.addLayout(self.domMatchPanHLayout)

        self.line_6 = QtWidgets.QFrame(self.domMatchTab)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.domMatchParamsVLayout.addWidget(self.line_6)
        self.domMatchOpHLayout = QtWidgets.QHBoxLayout()
        self.domMatchOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.domMatchOpHLayout.setSpacing(5)
        self.domMatchOpHLayout.setObjectName("domMatchOpHLayout")
        self.domMatchReportButton = QtWidgets.QPushButton(self.domMatchTab)
        self.domMatchReportButton.setObjectName("domMatchReportButton")
        self.domMatchOpHLayout.addWidget(self.domMatchReportButton)
        self.domMatchLogButton = QtWidgets.QPushButton(self.domMatchTab)
        self.domMatchLogButton.setObjectName("domMatchLogButton")
        self.domMatchOpHLayout.addWidget(self.domMatchLogButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.domMatchOpHLayout.addItem(spacerItem4)
        self.domMatchStartButton = QtWidgets.QPushButton(self.domMatchTab)
        self.domMatchStartButton.setObjectName("domMatchStartButton")
        self.domMatchOpHLayout.addWidget(self.domMatchStartButton)
        self.domMatchParamsVLayout.addLayout(self.domMatchOpHLayout)
        self.domMatchVLayout.addLayout(self.domMatchParamsVLayout)
        self.domMatchTableWidget = QtWidgets.QTableWidget(self.domMatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domMatchTableWidget.sizePolicy().hasHeightForWidth())
        self.domMatchTableWidget.setSizePolicy(sizePolicy)
        self.domMatchTableWidget.setObjectName("domMatchTableWidget")
        self.domMatchTableWidget.setColumnCount(0)
        self.domMatchTableWidget.setRowCount(0)
        self.domMatchVLayout.addWidget(self.domMatchTableWidget)
        self.verticalLayout_7.addLayout(self.domMatchVLayout)
        self.domContent.addTab(self.domMatchTab, "")


        self.domVLayout.addWidget(self.domContent)
        self.verticalLayout_2.addLayout(self.domVLayout)
        self.mainContent.addTab(self.domContentTab, "")
        """
        demContentTab
        """
        self.demContentTab = QtWidgets.QWidget()
        self.demContentTab.setObjectName("demContentTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.demContentTab)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.demVLayout = QtWidgets.QVBoxLayout()
        self.demVLayout.setSpacing(5)
        self.demVLayout.setContentsMargins(5, 5, 5, 5)
        self.demVLayout.setObjectName("demVLayout")
        self.demContent = QtWidgets.QTabWidget(self.demContentTab)
        self.demContent.setObjectName("demContent")
        self.demWBTab = QtWidgets.QWidget()
        self.demWBTab.setObjectName("demWBTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.demWBTab)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.demWBLayout = QtWidgets.QVBoxLayout()
        self.demWBLayout.setSpacing(5)
        self.demWBLayout.setContentsMargins(5, 5, 5, 5)
        self.demWBLayout.setObjectName("demWBLayout")
        self.demWBParamsVLayout = QtWidgets.QVBoxLayout()
        self.demWBParamsVLayout.setSpacing(5)
        self.demWBParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.demWBParamsVLayout.setObjectName("demWBParamsVLayout")
        self.demWBParamsIGLayout = QtWidgets.QGridLayout()
        self.demWBParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.demWBParamsIGLayout.setSpacing(5)
        self.demWBParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.demWBParamsIGLayout.setObjectName("demWBParamsIGLayout")
        self.demWBILabel = QtWidgets.QLabel(self.demWBTab)
        self.demWBILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBILabel.setObjectName("demWBILabel")
        self.demWBParamsIGLayout.addWidget(self.demWBILabel, 0, 0, 1, 1)
        self.demWBIBrowerButton = QtWidgets.QPushButton(self.demWBTab)
        self.demWBIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBIBrowerButton.setObjectName("demWBIBrowerButton")
        self.demWBParamsIGLayout.addWidget(self.demWBIBrowerButton, 0, 2, 1, 1)
        self.demWBILineEdit = QtWidgets.QLineEdit(self.demWBTab)
        self.demWBILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBILineEdit.setObjectName("demWBILineEdit")
        self.demWBParamsIGLayout.addWidget(self.demWBILineEdit, 0, 1, 1, 1)
        self.demWBParamsVLayout.addLayout(self.demWBParamsIGLayout)
        self.demWBParamsGBox = QtWidgets.QGroupBox(self.demWBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demWBParamsGBox.sizePolicy().hasHeightForWidth())
        self.demWBParamsGBox.setSizePolicy(sizePolicy)
        self.demWBParamsGBox.setMinimumSize(QtCore.QSize(0, 80))
        self.demWBParamsGBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.demWBParamsGBox.setObjectName("demWBParamsGBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.demWBParamsGBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_demvalue = QtWidgets.QLabel(self.demWBParamsGBox)
        self.label_demvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_demvalue.setObjectName("label_demvalue")
        self.horizontalLayout_2.addWidget(self.label_demvalue)
        self.spinBox_4d = QtWidgets.QSpinBox(self.demWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4d.sizePolicy().hasHeightForWidth())
        self.spinBox_4d.setSizePolicy(sizePolicy)
        self.spinBox_4d.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_4d.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_4d.setMaximum(10000)
        self.spinBox_4d.setMinimum(-1000)
        self.spinBox_4d.setObjectName("spinBox_4d")
        self.horizontalLayout_2.addWidget(self.spinBox_4d)
        self.label_7 = QtWidgets.QLabel(self.demWBParamsGBox)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.spinBox_5d = QtWidgets.QSpinBox(self.demWBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_5d.sizePolicy().hasHeightForWidth())
        self.spinBox_5d.setSizePolicy(sizePolicy)
        self.spinBox_5d.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_5d.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_5d.setMaximum(10000)
        self.spinBox_5d.setMinimum(-1000)
        self.spinBox_5d.setObjectName("spinBox_5d")
        self.horizontalLayout_2.addWidget(self.spinBox_5d)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.demWBParamsVLayout.addWidget(self.demWBParamsGBox)
        self.demWBPraramsOGLayout = QtWidgets.QGridLayout()
        self.demWBPraramsOGLayout.setSpacing(5)
        self.demWBPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.demWBPraramsOGLayout.setObjectName("demWBPraramsOGLayout")
        self.demWBOLabel = QtWidgets.QLabel(self.demWBTab)
        self.demWBOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBOLabel.setObjectName("demWBOLabel")
        self.demWBPraramsOGLayout.addWidget(self.demWBOLabel, 0, 0, 1, 1)
        self.demWBOLineEdit = QtWidgets.QLineEdit(self.demWBTab)
        self.demWBOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBOLineEdit.setObjectName("demWBOLineEdit")
        self.demWBPraramsOGLayout.addWidget(self.demWBOLineEdit, 0, 1, 1, 1)
        self.demWBOBrowerButton = QtWidgets.QPushButton(self.demWBTab)
        self.demWBOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.demWBOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demWBOBrowerButton.setObjectName("demWBOBrowerButton")
        self.demWBPraramsOGLayout.addWidget(self.demWBOBrowerButton, 0, 2, 1, 1)
        self.demWBParamsVLayout.addLayout(self.demWBPraramsOGLayout)
        self.line_3 = QtWidgets.QFrame(self.demWBTab)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.demWBParamsVLayout.addWidget(self.line_3)
        self.demWBOpHLayout = QtWidgets.QHBoxLayout()
        self.demWBOpHLayout.setSpacing(5)
        self.demWBOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.demWBOpHLayout.setObjectName("demWBOpHLayout")
        self.demWBReportButton = QtWidgets.QPushButton(self.demWBTab)
        self.demWBReportButton.setObjectName("demWBReportButton")
        self.demWBOpHLayout.addWidget(self.demWBReportButton)
        self.demWBLogButton = QtWidgets.QPushButton(self.demWBTab)
        self.demWBLogButton.setObjectName("demWBLogButton")
        self.demWBOpHLayout.addWidget(self.demWBLogButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.demWBOpHLayout.addItem(spacerItem8)
        self.demWBStartButton = QtWidgets.QPushButton(self.demWBTab)
        self.demWBStartButton.setObjectName("demWBStartButton")
        self.demWBOpHLayout.addWidget(self.demWBStartButton)
        self.demWBParamsVLayout.addLayout(self.demWBOpHLayout)
        self.demWBLayout.addLayout(self.demWBParamsVLayout)
        self.demTableWidget = QtWidgets.QTableWidget(self.demWBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demTableWidget.sizePolicy().hasHeightForWidth())
        self.demTableWidget.setSizePolicy(sizePolicy)
        self.demTableWidget.setObjectName("demTableWidget")
        self.demWBLayout.addWidget(self.demTableWidget)
        self.verticalLayout_11.addLayout(self.demWBLayout)
        self.demContent.addTab(self.demWBTab, "")
        self.demJBTab = QtWidgets.QWidget()
        self.demJBTab.setObjectName("demJBTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.demJBTab)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.demJBLayout = QtWidgets.QVBoxLayout()
        self.demJBLayout.setSpacing(5)
        self.demJBLayout.setContentsMargins(5, 5, 5, 5)
        self.demJBLayout.setObjectName("demJBLayout")
        self.demJBParamsVLayout = QtWidgets.QVBoxLayout()
        self.demJBParamsVLayout.setSpacing(5)
        self.demJBParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.demJBParamsVLayout.setObjectName("demJBParamsVLayout")
        self.demJBParamsIGLayout = QtWidgets.QGridLayout()
        self.demJBParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.demJBParamsIGLayout.setSpacing(5)
        self.demJBParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.demJBParamsIGLayout.setObjectName("demJBParamsIGLayout")
        self.demJBILabel_ = QtWidgets.QLabel(self.demJBTab)
        self.demJBILabel_.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBILabel_.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBILabel_.setObjectName("demJBILabel_")
        self.demJBParamsIGLayout.addWidget(self.demJBILabel_, 0, 0, 1, 1)
        self.demJBIBrowerButton = QtWidgets.QPushButton(self.demJBTab)
        self.demJBIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBIBrowerButton.setObjectName("demJBIBrowerButton")
        self.demJBParamsIGLayout.addWidget(self.demJBIBrowerButton, 0, 2, 1, 1)
        self.demJBILineEdit = QtWidgets.QLineEdit(self.demJBTab)
        self.demJBILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBILineEdit.setObjectName("demJBILineEdit")
        self.demJBParamsIGLayout.addWidget(self.demJBILineEdit, 0, 1, 1, 1)
        self.demJBParamsVLayout.addLayout(self.demJBParamsIGLayout)
        self.demJBParamsGBox = QtWidgets.QGroupBox(self.demJBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demJBParamsGBox.sizePolicy().hasHeightForWidth())
        self.demJBParamsGBox.setSizePolicy(sizePolicy)
        self.demJBParamsGBox.setMinimumSize(QtCore.QSize(0, 80))
        self.demJBParamsGBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.demJBParamsGBox.setObjectName("demJBParamsGBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.demJBParamsGBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.demJBParamsGBox)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.spinBox_6 = QtWidgets.QSpinBox(self.demJBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_6.setMaximum(10000)
        self.spinBox_6.setMinimum(-1000)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_7.addWidget(self.spinBox_6)
        self.label_12 = QtWidgets.QLabel(self.demJBParamsGBox)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.spinBox_7 = QtWidgets.QSpinBox(self.demJBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy)
        self.spinBox_7.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_7.setMaximum(10000)
        self.spinBox_7.setMinimum(-1000)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_7.addWidget(self.spinBox_7)
        self.label_13 = QtWidgets.QLabel(self.demJBParamsGBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.spinBox_8 = QtWidgets.QSpinBox(self.demJBParamsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy)
        self.spinBox_8.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_8.setMaximum(10000)
        self.spinBox_8.setMinimum(-1000)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_7.addWidget(self.spinBox_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.demJBParamsVLayout.addWidget(self.demJBParamsGBox)
        self.demJBPraramsOGLayout = QtWidgets.QGridLayout()
        self.demJBPraramsOGLayout.setSpacing(5)
        self.demJBPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.demJBPraramsOGLayout.setObjectName("demJBPraramsOGLayout")
        self.demJBOLabel = QtWidgets.QLabel(self.demJBTab)
        self.demJBOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBOLabel.setObjectName("demJBOLabel")
        self.demJBPraramsOGLayout.addWidget(self.demJBOLabel, 0, 0, 1, 1)
        self.demJBOLineEdit = QtWidgets.QLineEdit(self.demJBTab)
        self.demJBOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBOLineEdit.setObjectName("demJBOLineEdit")
        self.demJBPraramsOGLayout.addWidget(self.demJBOLineEdit, 0, 1, 1, 1)
        self.demJBOBrowerButton = QtWidgets.QPushButton(self.demJBTab)
        self.demJBOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.demJBOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.demJBOBrowerButton.setObjectName("demJBOBrowerButton")
        self.demJBPraramsOGLayout.addWidget(self.demJBOBrowerButton, 0, 2, 1, 1)
        self.demJBParamsVLayout.addLayout(self.demJBPraramsOGLayout)
        self.line_5 = QtWidgets.QFrame(self.demJBTab)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.demJBParamsVLayout.addWidget(self.line_5)
        self.demJBOpHLayout = QtWidgets.QHBoxLayout()
        self.demJBOpHLayout.setSpacing(5)
        self.demJBOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.demJBOpHLayout.setObjectName("demJBOpHLayout")
        self.demJBReportButton = QtWidgets.QPushButton(self.demJBTab)
        self.demJBReportButton.setObjectName("demJBReportButton")
        self.demJBOpHLayout.addWidget(self.demJBReportButton)
        self.demJBLogButton = QtWidgets.QPushButton(self.demJBTab)
        self.demJBLogButton.setObjectName("demJBLogButton")
        self.demJBOpHLayout.addWidget(self.demJBLogButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.demJBOpHLayout.addItem(spacerItem10)
        self.demJBStartButton = QtWidgets.QPushButton(self.demJBTab)
        self.demJBStartButton.setObjectName("demJBStartButton")
        self.demJBOpHLayout.addWidget(self.demJBStartButton)
        self.demJBParamsVLayout.addLayout(self.demJBOpHLayout)
        self.demJBLayout.addLayout(self.demJBParamsVLayout)
        self.demJBTableWidget = QtWidgets.QTableWidget(self.demJBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demJBTableWidget.sizePolicy().hasHeightForWidth())
        self.demJBTableWidget.setSizePolicy(sizePolicy)
        self.demJBTableWidget.setObjectName("demJBTableWidget")
        self.demJBLayout.addWidget(self.demJBTableWidget)
        self.verticalLayout_9.addLayout(self.demJBLayout)
        self.demContent.addTab(self.demJBTab, "")
        self.demVLayout.addWidget(self.demContent)
        self.verticalLayout_10.addLayout(self.demVLayout)
        self.mainContent.addTab(self.demContentTab, "")
        self.stdataContentTab = QtWidgets.QWidget()
        self.stdataContentTab.setObjectName("stdataContentTab")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.stdataContentTab)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.mainContent.addTab(self.demContentTab, "")


        """
        stdataContentTab
        """
        self.stdataContentTab = QtWidgets.QWidget()
        self.stdataContentTab.setObjectName("stdataContentTab")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.stdataContentTab)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stdVLayout = QtWidgets.QVBoxLayout()
        self.stdVLayout.setSpacing(5)
        self.stdVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdVLayout.setObjectName("stdVLayout")
        self.stdContent = QtWidgets.QTabWidget(self.stdataContentTab)
        self.stdContent.setObjectName("stdContent")
        self.stdAttTab = QtWidgets.QWidget()
        self.stdAttTab.setObjectName("stdAttTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.stdAttTab)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stdAttVLayout = QtWidgets.QVBoxLayout()
        self.stdAttVLayout.setSpacing(5)
        self.stdAttVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttVLayout.setObjectName("stdAttVLayout")
        self.stdAttParamsVLayout = QtWidgets.QVBoxLayout()
        self.stdAttParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttParamsVLayout.setObjectName("stdAttParamsVLayout")
        self.stdAttParamsIGLayout = QtWidgets.QHBoxLayout()
        self.stdAttParamsIGLayout.setSpacing(5)
        self.stdAttParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttParamsIGLayout.setObjectName("stdAttParamsIGLayout")
        self.stdAttILabel = QtWidgets.QLabel(self.stdAttTab)
        self.stdAttILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttILabel.setObjectName("stdAttILabel")
        self.stdAttParamsIGLayout.addWidget(self.stdAttILabel)
        self.stdAttILineEdit = QtWidgets.QLineEdit(self.stdAttTab)
        self.stdAttILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttILineEdit.setObjectName("stdAttILineEdit")
        self.stdAttParamsIGLayout.addWidget(self.stdAttILineEdit)
        self.stdAttIBrowerButton = QtWidgets.QPushButton(self.stdAttTab)
        self.stdAttIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttIBrowerButton.setObjectName("stdAttIBrowerButton")
        self.stdAttParamsIGLayout.addWidget(self.stdAttIBrowerButton)
        self.stdAttParamsVLayout.addLayout(self.stdAttParamsIGLayout)
        self.stdAttSelectIGLayout = QtWidgets.QHBoxLayout()
        self.stdAttSelectIGLayout.setSpacing(5)
        self.stdAttSelectIGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttSelectIGLayout.setObjectName("stdAttSelectIGLayout")
        self.stdAttSelectLayersGBox = QtWidgets.QGroupBox(self.stdAttTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.stdAttSelectLayersGBox.sizePolicy().hasHeightForWidth())
        self.stdAttSelectLayersGBox.setSizePolicy(sizePolicy)
        self.stdAttSelectLayersGBox.setMinimumSize(QtCore.QSize(20, 30))
        self.stdAttSelectLayersGBox.setObjectName("stdAttSelectLayersGBox")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.stdAttSelectLayersGBox)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.stdAttSelectLayersComboBox = QtWidgets.QComboBox(self.stdAttSelectLayersGBox)
        self.stdAttSelectLayersComboBox.setObjectName("stdAttSelectLayersComboBox")
        self.verticalLayout_17.addWidget(self.stdAttSelectLayersComboBox)
        self.stdAttSelectIGLayout.addWidget(self.stdAttSelectLayersGBox)
        self.stdAttSelectGdbGBox = QtWidgets.QGroupBox(self.stdAttTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.stdAttSelectGdbGBox.sizePolicy().hasHeightForWidth())
        self.stdAttSelectGdbGBox.setSizePolicy(sizePolicy)
        self.stdAttSelectGdbGBox.setMinimumSize(QtCore.QSize(20, 30))
        self.stdAttSelectGdbGBox.setObjectName("stdAttSelectGdbGBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.stdAttSelectGdbGBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.stdAttSelectGdbComboBox = QtWidgets.QComboBox(self.stdAttSelectGdbGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stdAttSelectGdbComboBox.sizePolicy().hasHeightForWidth())
        self.stdAttSelectGdbComboBox.setSizePolicy(sizePolicy)
        self.stdAttSelectGdbComboBox.setObjectName("stdAttSelectGdbComboBox")
        self.verticalLayout_10.addWidget(self.stdAttSelectGdbComboBox)
        self.stdAttSelectIGLayout.addWidget(self.stdAttSelectGdbGBox)
        self.stdAttParamsVLayout.addLayout(self.stdAttSelectIGLayout)
        self.stdAttSelectGBox = QtWidgets.QGroupBox(self.stdAttTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.stdAttSelectGBox.sizePolicy().hasHeightForWidth())
        self.stdAttSelectGBox.setSizePolicy(sizePolicy)
        self.stdAttSelectGBox.setMinimumSize(QtCore.QSize(20, 10))
        self.stdAttSelectGBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stdAttSelectGBox.setObjectName("stdAttSelectGBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.stdAttSelectGBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.stdAttSelectGBoxLayout = QtWidgets.QHBoxLayout()
        self.stdAttSelectGBoxLayout.setSpacing(5)
        self.stdAttSelectGBoxLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttSelectGBoxLayout.setObjectName("stdAttSelectGBoxLayout")
        self.stdAttSelectGBoxTableWidget = QtWidgets.QTableWidget(self.stdAttSelectGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.stdAttSelectGBoxTableWidget.sizePolicy().hasHeightForWidth())
        self.stdAttSelectGBoxTableWidget.setSizePolicy(sizePolicy)
        self.stdAttSelectGBoxTableWidget.setMinimumSize(QtCore.QSize(0, 20))
        self.stdAttSelectGBoxTableWidget.setObjectName("stdAttSelectGBoxTableWidget")
        self.stdAttSelectGBoxTableWidget.setColumnCount(0)
        self.stdAttSelectGBoxTableWidget.setRowCount(0)
        self.stdAttSelectGBoxLayout.addWidget(self.stdAttSelectGBoxTableWidget)
        self.stdAttSelectGBoxPushButton = QtWidgets.QPushButton(self.stdAttSelectGBox)
        self.stdAttSelectGBoxPushButton.setObjectName("stdAttSelectGBoxPushButton")
        self.stdAttSelectGBoxLayout.addWidget(self.stdAttSelectGBoxPushButton)
        self.horizontalLayout_10.addLayout(self.stdAttSelectGBoxLayout)
        self.stdAttParamsVLayout.addWidget(self.stdAttSelectGBox)
        self.stdAttPraramsOGLayout = QtWidgets.QHBoxLayout()
        self.stdAttPraramsOGLayout.setSpacing(5)
        self.stdAttPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttPraramsOGLayout.setObjectName("stdAttPraramsOGLayout")
        self.stdAttOLabel = QtWidgets.QLabel(self.stdAttTab)
        self.stdAttOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttOLabel.setObjectName("stdAttOLabel")
        self.stdAttPraramsOGLayout.addWidget(self.stdAttOLabel)
        self.stdAttOLineEdit = QtWidgets.QLineEdit(self.stdAttTab)
        self.stdAttOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttOLineEdit.setObjectName("stdAttOLineEdit")
        self.stdAttPraramsOGLayout.addWidget(self.stdAttOLineEdit)
        self.stdAttOBrowerButton = QtWidgets.QPushButton(self.stdAttTab)
        self.stdAttOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdAttOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdAttOBrowerButton.setObjectName("stdAttOBrowerButton")
        self.stdAttPraramsOGLayout.addWidget(self.stdAttOBrowerButton)
        self.stdAttParamsVLayout.addLayout(self.stdAttPraramsOGLayout)
        self.line_8 = QtWidgets.QFrame(self.stdAttTab)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.stdAttParamsVLayout.addWidget(self.line_8)
        self.stdAttOpHLayout = QtWidgets.QHBoxLayout()
        self.stdAttOpHLayout.setSpacing(5)
        self.stdAttOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.stdAttOpHLayout.setObjectName("stdAttOpHLayout")
        self.stdAttReportButton = QtWidgets.QPushButton(self.stdAttTab)
        self.stdAttReportButton.setObjectName("stdAttReportButton")
        self.stdAttOpHLayout.addWidget(self.stdAttReportButton)
        self.stdAttLogButton = QtWidgets.QPushButton(self.stdAttTab)
        self.stdAttLogButton.setObjectName("stdAttLogButton")
        self.stdAttOpHLayout.addWidget(self.stdAttLogButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stdAttOpHLayout.addItem(spacerItem11)
        self.stdAttStartButton = QtWidgets.QPushButton(self.stdAttTab)
        self.stdAttStartButton.setObjectName("stdAttStartButton")
        self.stdAttOpHLayout.addWidget(self.stdAttStartButton)
        self.stdAttParamsVLayout.addLayout(self.stdAttOpHLayout)
        self.stdAttVLayout.addLayout(self.stdAttParamsVLayout)
        self.stdAttTableWidget = QtWidgets.QTableWidget(self.stdAttTab)
        self.stdAttTableWidget.setObjectName("stdAttTableWidget")
        self.stdAttTableWidget.setColumnCount(0)
        self.stdAttTableWidget.setRowCount(0)
        self.stdAttVLayout.addWidget(self.stdAttTableWidget)
        self.verticalLayout_9.addLayout(self.stdAttVLayout)
        self.stdContent.addTab(self.stdAttTab, "")
        self.stdCodeTab = QtWidgets.QWidget()
        self.stdCodeTab.setObjectName("stdCodeTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.stdCodeTab)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stdCodeVLayout = QtWidgets.QVBoxLayout()
        self.stdCodeVLayout.setSpacing(5)
        self.stdCodeVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdCodeVLayout.setObjectName("stdCodeVLayout")
        self.stdCodeParamsVLayout = QtWidgets.QVBoxLayout()
        self.stdCodeParamsVLayout.setSpacing(5)
        self.stdCodeParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdCodeParamsVLayout.setObjectName("stdCodeParamsVLayout")
        self.stdCodeParamsIGLayout = QtWidgets.QHBoxLayout()
        self.stdCodeParamsIGLayout.setSpacing(5)
        self.stdCodeParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdCodeParamsIGLayout.setObjectName("stdCodeParamsIGLayout")
        self.stdCodeILabel = QtWidgets.QLabel(self.stdCodeTab)
        self.stdCodeILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeILabel.setObjectName("stdCodeILabel")
        self.stdCodeParamsIGLayout.addWidget(self.stdCodeILabel)
        self.stdCodeILineEdit = QtWidgets.QLineEdit(self.stdCodeTab)
        self.stdCodeILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeILineEdit.setObjectName("stdCodeILineEdit")
        self.stdCodeParamsIGLayout.addWidget(self.stdCodeILineEdit)
        self.stdCodeIBrowerButton = QtWidgets.QPushButton(self.stdCodeTab)
        self.stdCodeIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeIBrowerButton.setObjectName("stdCodeIBrowerButton")
        self.stdCodeParamsIGLayout.addWidget(self.stdCodeIBrowerButton)
        self.stdCodeParamsVLayout.addLayout(self.stdCodeParamsIGLayout)
        self.stdCodePraramsOGLayout = QtWidgets.QHBoxLayout()
        self.stdCodePraramsOGLayout.setSpacing(5)
        self.stdCodePraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdCodePraramsOGLayout.setObjectName("stdCodePraramsOGLayout")
        self.stdCodeOLabel = QtWidgets.QLabel(self.stdCodeTab)
        self.stdCodeOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeOLabel.setObjectName("stdCodeOLabel")
        self.stdCodePraramsOGLayout.addWidget(self.stdCodeOLabel)
        self.stdCodeOLineEdit = QtWidgets.QLineEdit(self.stdCodeTab)
        self.stdCodeOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeOLineEdit.setObjectName("stdCodeOLineEdit")
        self.stdCodePraramsOGLayout.addWidget(self.stdCodeOLineEdit)
        self.stdCodeOBrowerButton = QtWidgets.QPushButton(self.stdCodeTab)
        self.stdCodeOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdCodeOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdCodeOBrowerButton.setObjectName("stdCodeOBrowerButton")
        self.stdCodePraramsOGLayout.addWidget(self.stdCodeOBrowerButton)
        self.stdCodeParamsVLayout.addLayout(self.stdCodePraramsOGLayout)
        self.line_9 = QtWidgets.QFrame(self.stdCodeTab)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.stdCodeParamsVLayout.addWidget(self.line_9)
        self.stdCodeOpHLayout = QtWidgets.QHBoxLayout()
        self.stdCodeOpHLayout.setSpacing(5)
        self.stdCodeOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.stdCodeOpHLayout.setObjectName("stdCodeOpHLayout")
        self.stdCodeReportButton = QtWidgets.QPushButton(self.stdCodeTab)
        self.stdCodeReportButton.setObjectName("stdCodeReportButton")
        self.stdCodeOpHLayout.addWidget(self.stdCodeReportButton)
        self.stdCodeLogButton = QtWidgets.QPushButton(self.stdCodeTab)
        self.stdCodeLogButton.setObjectName("stdCodeLogButton")
        self.stdCodeOpHLayout.addWidget(self.stdCodeLogButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stdCodeOpHLayout.addItem(spacerItem12)
        self.stdCodeStartButton = QtWidgets.QPushButton(self.stdCodeTab)
        self.stdCodeStartButton.setObjectName("stdCodeStartButton")
        self.stdCodeOpHLayout.addWidget(self.stdCodeStartButton)
        self.stdCodeParamsVLayout.addLayout(self.stdCodeOpHLayout)
        self.stdCodeVLayout.addLayout(self.stdCodeParamsVLayout)
        self.stdCodeTableWidget = QtWidgets.QTableWidget(self.stdCodeTab)
        self.stdCodeTableWidget.setObjectName("stdCodeTableWidget")
        self.stdCodeTableWidget.setColumnCount(0)
        self.stdCodeTableWidget.setRowCount(0)
        self.stdCodeVLayout.addWidget(self.stdCodeTableWidget)
        self.verticalLayout_11.addLayout(self.stdCodeVLayout)
        self.stdContent.addTab(self.stdCodeTab, "")
        self.stdRepeatTab = QtWidgets.QWidget()
        self.stdRepeatTab.setObjectName("stdRepeatTab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.stdRepeatTab)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.stdRepeatVLayout = QtWidgets.QVBoxLayout()
        self.stdRepeatVLayout.setSpacing(5)
        self.stdRepeatVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatVLayout.setObjectName("stdRepeatVLayout")
        self.stdRepeatParamsVLayout = QtWidgets.QVBoxLayout()
        self.stdRepeatParamsVLayout.setSpacing(5)
        self.stdRepeatParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatParamsVLayout.setObjectName("stdRepeatParamsVLayout")
        self.stdRepeatParamsIGLayout = QtWidgets.QHBoxLayout()
        self.stdRepeatParamsIGLayout.setSpacing(5)
        self.stdRepeatParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatParamsIGLayout.setObjectName("stdRepeatParamsIGLayout")
        self.stdRepeatILabel = QtWidgets.QLabel(self.stdRepeatTab)
        self.stdRepeatILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatILabel.setObjectName("stdRepeatILabel")
        self.stdRepeatParamsIGLayout.addWidget(self.stdRepeatILabel)
        self.stdRepeatILineEdit = QtWidgets.QLineEdit(self.stdRepeatTab)
        self.stdRepeatILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatILineEdit.setObjectName("stdRepeatILineEdit")
        self.stdRepeatParamsIGLayout.addWidget(self.stdRepeatILineEdit)
        self.stdRepeatIBrowerButton = QtWidgets.QPushButton(self.stdRepeatTab)
        self.stdRepeatIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatIBrowerButton.setObjectName("stdRepeatIBrowerButton")
        self.stdRepeatParamsIGLayout.addWidget(self.stdRepeatIBrowerButton)
        self.stdRepeatParamsVLayout.addLayout(self.stdRepeatParamsIGLayout)
        self.stdRepeatGroupBox = QtWidgets.QGroupBox(self.stdRepeatTab)
        self.stdRepeatGroupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.stdRepeatGroupBox.setObjectName("stdRepeatGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.stdRepeatGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stdRepeatGroupBoxLayout = QtWidgets.QHBoxLayout()
        self.stdRepeatGroupBoxLayout.setSpacing(5)
        self.stdRepeatGroupBoxLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatGroupBoxLayout.setObjectName("stdRepeatGroupBoxLayout")
        self.stdRepeatGroupBoxlabel = QtWidgets.QLabel(self.stdRepeatGroupBox)
        self.stdRepeatGroupBoxlabel.setObjectName("stdRepeatGroupBoxlabel")
        self.stdRepeatGroupBoxLayout.addWidget(self.stdRepeatGroupBoxlabel)
        self.stdRepeatGroupBoxspinBox = QtWidgets.QSpinBox(self.stdRepeatGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stdRepeatGroupBoxspinBox.sizePolicy().hasHeightForWidth())
        self.stdRepeatGroupBoxspinBox.setSizePolicy(sizePolicy)
        self.stdRepeatGroupBoxspinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.stdRepeatGroupBoxspinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.stdRepeatGroupBoxspinBox.setMaximum(100)
        self.stdRepeatGroupBoxspinBox.setMinimum(0)
        self.stdRepeatGroupBoxspinBox.setObjectName("stdRepeatGroupBoxspinBox")
        self.stdRepeatGroupBoxLayout.addWidget(self.stdRepeatGroupBoxspinBox)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stdRepeatGroupBoxLayout.addItem(spacerItem13)
        self.horizontalLayout_8.addLayout(self.stdRepeatGroupBoxLayout)
        self.stdRepeatParamsVLayout.addWidget(self.stdRepeatGroupBox)
        self.stdRepeatPraramsOGLayout = QtWidgets.QHBoxLayout()
        self.stdRepeatPraramsOGLayout.setSpacing(5)
        self.stdRepeatPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatPraramsOGLayout.setObjectName("stdRepeatPraramsOGLayout")
        self.stdRepeatOLabel = QtWidgets.QLabel(self.stdRepeatTab)
        self.stdRepeatOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatOLabel.setObjectName("stdRepeatOLabel")
        self.stdRepeatPraramsOGLayout.addWidget(self.stdRepeatOLabel)
        self.stdRepeatOLineEdit = QtWidgets.QLineEdit(self.stdRepeatTab)
        self.stdRepeatOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatOLineEdit.setObjectName("stdRepeatOLineEdit")
        self.stdRepeatPraramsOGLayout.addWidget(self.stdRepeatOLineEdit)
        self.stdRepeatOBrowerButton = QtWidgets.QPushButton(self.stdRepeatTab)
        self.stdRepeatOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stdRepeatOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.stdRepeatOBrowerButton.setObjectName("stdRepeatOBrowerButton")
        self.stdRepeatPraramsOGLayout.addWidget(self.stdRepeatOBrowerButton)
        self.stdRepeatParamsVLayout.addLayout(self.stdRepeatPraramsOGLayout)
        self.line_10 = QtWidgets.QFrame(self.stdRepeatTab)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.stdRepeatParamsVLayout.addWidget(self.line_10)
        self.stdRepeatOpHLayout = QtWidgets.QHBoxLayout()
        self.stdRepeatOpHLayout.setSpacing(5)
        self.stdRepeatOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.stdRepeatOpHLayout.setObjectName("stdRepeatOpHLayout")
        self.stdRepeatReportButton = QtWidgets.QPushButton(self.stdRepeatTab)
        self.stdRepeatReportButton.setObjectName("stdRepeatReportButton")
        self.stdRepeatOpHLayout.addWidget(self.stdRepeatReportButton)
        self.stdRepeatLogButton = QtWidgets.QPushButton(self.stdRepeatTab)
        self.stdRepeatLogButton.setObjectName("stdRepeatLogButton")
        self.stdRepeatOpHLayout.addWidget(self.stdRepeatLogButton)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stdRepeatOpHLayout.addItem(spacerItem14)
        self.stdRepeatStartButton = QtWidgets.QPushButton(self.stdRepeatTab)
        self.stdRepeatStartButton.setObjectName("stdRepeatStartButton")
        self.stdRepeatOpHLayout.addWidget(self.stdRepeatStartButton)
        self.stdRepeatParamsVLayout.addLayout(self.stdRepeatOpHLayout)
        self.stdRepeatVLayout.addLayout(self.stdRepeatParamsVLayout)
        self.stdRepeatTableWidget = QtWidgets.QTableWidget(self.stdRepeatTab)
        self.stdRepeatTableWidget.setObjectName("stdRepeatTableWidget")
        self.stdRepeatTableWidget.setColumnCount(0)
        self.stdRepeatTableWidget.setRowCount(0)
        self.stdRepeatVLayout.addWidget(self.stdRepeatTableWidget)
        self.verticalLayout_12.addLayout(self.stdRepeatVLayout)
        self.stdContent.addTab(self.stdRepeatTab, "")
        self.stdVLayout.addWidget(self.stdContent)
        self.verticalLayout_15.addLayout(self.stdVLayout)
        self.mainContent.addTab(self.stdataContentTab, "")

        """
        modelContentTab
        """
        self.modelContentTab = QtWidgets.QWidget()
        self.modelContentTab.setObjectName("modelContentTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.modelContentTab)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.thrDVLayout = QtWidgets.QVBoxLayout()
        self.thrDVLayout.setSpacing(5)
        self.thrDVLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDVLayout.setObjectName("thrDVLayout")
        self.thrDContent = QtWidgets.QTabWidget(self.modelContentTab)
        self.thrDContent.setObjectName("thrDContent")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.thrDTexVLayout = QtWidgets.QVBoxLayout()
        self.thrDTexVLayout.setSpacing(5)
        self.thrDTexVLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDTexVLayout.setObjectName("thrDTexVLayout")
        self.thrDTexParamsVLayout = QtWidgets.QVBoxLayout()
        self.thrDTexParamsVLayout.setSpacing(5)
        self.thrDTexParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDTexParamsVLayout.setObjectName("thrDTexParamsVLayout")
        self.thrDTexParamsIGLayout = QtWidgets.QGridLayout()
        self.thrDTexParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.thrDTexParamsIGLayout.setSpacing(5)
        self.thrDTexParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDTexParamsIGLayout.setObjectName("thrDTexParamsIGLayout")
        self.thrDTexILabel = QtWidgets.QLabel(self.tab_3)
        self.thrDTexILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexILabel.setObjectName("thrDTexILabel")
        self.thrDTexParamsIGLayout.addWidget(self.thrDTexILabel, 0, 0, 1, 1)
        self.thrDTexIBrowerButton = QtWidgets.QPushButton(self.tab_3)
        self.thrDTexIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexIBrowerButton.setObjectName("thrDTexIBrowerButton")
        self.thrDTexParamsIGLayout.addWidget(self.thrDTexIBrowerButton, 0, 2, 1, 1)
        self.thrDTexILineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.thrDTexILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexILineEdit.setObjectName("thrDTexILineEdit")
        self.thrDTexParamsIGLayout.addWidget(self.thrDTexILineEdit, 0, 1, 1, 1)
        self.thrDTexParamsVLayout.addLayout(self.thrDTexParamsIGLayout)
        self.thrDTexPraramsTELayout = QtWidgets.QGridLayout()
        self.thrDTexPraramsTELayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.thrDTexPraramsTELayout.setSpacing(5)
        self.thrDTexPraramsTELayout.setContentsMargins(5, 5, 5, 5)
        self.thrDTexPraramsTELayout.setObjectName("thrDTexPraramsTELayout")
        self.thrDTexTLabel = QtWidgets.QLabel(self.tab_3)
        self.thrDTexTLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexTLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexTLabel.setObjectName("thrDTexTLabel")
        self.thrDTexPraramsTELayout.addWidget(self.thrDTexTLabel, 0, 0, 1, 1)
        self.thrDTexTBrowerButton = QtWidgets.QPushButton(self.tab_3)
        self.thrDTexTBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexTBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexTBrowerButton.setObjectName("thrDTexTBrowerButton")
        self.thrDTexPraramsTELayout.addWidget(self.thrDTexTBrowerButton, 0, 2, 1, 1)
        self.thrDTexTLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.thrDTexTLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDTexTLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDTexTLineEdit.setObjectName("thrDTexTLineEdit")
        self.thrDTexPraramsTELayout.addWidget(self.thrDTexTLineEdit, 0, 1, 1, 1)
        self.thrDTexParamsVLayout.addLayout(self.thrDTexPraramsTELayout)
        # self.thrDTexPraramsOGLayout = QtWidgets.QGridLayout()
        # self.thrDTexPraramsOGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        # self.thrDTexPraramsOGLayout.setSpacing(5)
        # self.thrDTexPraramsOGLayout.setContentsMargins(5, 5, 5, 5)
        # self.thrDTexPraramsOGLayout.setObjectName("thrDTexPraramsOGLayout")
        # self.thrDTexOLabel = QtWidgets.QLabel(self.tab_3)
        # self.thrDTexOLabel.setMinimumSize(QtCore.QSize(0, 24))
        # self.thrDTexOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.thrDTexOLabel.setObjectName("thrDTexOLabel")
        # self.thrDTexPraramsOGLayout.addWidget(self.thrDTexOLabel, 0, 0, 1, 1)
        # self.thrDTexOBrowerButton = QtWidgets.QPushButton(self.tab_3)
        # self.thrDTexOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        # self.thrDTexOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.thrDTexOBrowerButton.setObjectName("thrDTexOBrowerButton")
        # self.thrDTexPraramsOGLayout.addWidget(self.thrDTexOBrowerButton, 0, 2, 1, 1)
        # self.thrDTexOLineEdit = QtWidgets.QLineEdit(self.tab_3)
        # self.thrDTexOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        # self.thrDTexOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        # self.thrDTexOLineEdit.setObjectName("thrDTexOLineEdit")
        # self.thrDTexPraramsOGLayout.addWidget(self.thrDTexOLineEdit, 0, 1, 1, 1)
        # self.thrDTexParamsVLayout.addLayout(self.thrDTexPraramsOGLayout)
        self.line_7 = QtWidgets.QFrame(self.tab_3)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.thrDTexParamsVLayout.addWidget(self.line_7)
        self.thrDTexOpHLayout = QtWidgets.QHBoxLayout()
        self.thrDTexOpHLayout.setSpacing(5)
        self.thrDTexOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDTexOpHLayout.setObjectName("thrDTexOpHLayout")
        self.thrDTexReportButton = QtWidgets.QPushButton(self.tab_3)
        self.thrDTexReportButton.setObjectName("thrDTexReportButton")
        self.thrDTexOpHLayout.addWidget(self.thrDTexReportButton)
        self.thrDTexLogButton = QtWidgets.QPushButton(self.tab_3)
        self.thrDTexLogButton.setObjectName("thrDTexLogButton")
        self.thrDTexOpHLayout.addWidget(self.thrDTexLogButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.thrDTexOpHLayout.addItem(spacerItem15)
        self.thrDTexStartButton = QtWidgets.QPushButton(self.tab_3)
        self.thrDTexStartButton.setObjectName("thrDTexStartButton")
        self.thrDTexOpHLayout.addWidget(self.thrDTexStartButton)
        self.thrDTexParamsVLayout.addLayout(self.thrDTexOpHLayout)
        self.thrDTexVLayout.addLayout(self.thrDTexParamsVLayout)
        self.thrDTexTableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.thrDTexTableWidget.setObjectName("thrDTexTableWidget")
        self.thrDTexTableWidget.setColumnCount(0)
        self.thrDTexTableWidget.setRowCount(0)
        self.thrDTexVLayout.addWidget(self.thrDTexTableWidget)
        self.verticalLayout_10.addLayout(self.thrDTexVLayout)
        self.thrDContent.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.thrDDevVLayout = QtWidgets.QVBoxLayout()
        self.thrDDevVLayout.setSpacing(5)
        self.thrDDevVLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevVLayout.setObjectName("thrDDevVLayout")
        self.thrDDevParamsVLayout = QtWidgets.QVBoxLayout()
        self.thrDDevParamsVLayout.setSpacing(5)
        self.thrDDevParamsVLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevParamsVLayout.setObjectName("thrDDevParamsVLayout")
        self.thrDDevParamsIGLayout = QtWidgets.QGridLayout()
        self.thrDDevParamsIGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.thrDDevParamsIGLayout.setSpacing(5)
        self.thrDDevParamsIGLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevParamsIGLayout.setObjectName("thrDDevParamsIGLayout")
        self.thrDDevILabel = QtWidgets.QLabel(self.tab_4)
        self.thrDDevILabel.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevILabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevILabel.setObjectName("thrDDevILabel")
        self.thrDDevParamsIGLayout.addWidget(self.thrDDevILabel, 0, 0, 1, 1)
        self.thrDDevIBrowerButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevIBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevIBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevIBrowerButton.setObjectName("thrDDevIBrowerButton")
        self.thrDDevParamsIGLayout.addWidget(self.thrDDevIBrowerButton, 0, 2, 1, 1)
        self.thrDDevILineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.thrDDevILineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevILineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevILineEdit.setObjectName("thrDDevILineEdit")
        self.thrDDevParamsIGLayout.addWidget(self.thrDDevILineEdit, 0, 1, 1, 1)
        self.thrDDevParamsVLayout.addLayout(self.thrDDevParamsIGLayout)
        self.thrDDevParamsRELayout = QtWidgets.QGridLayout()
        self.thrDDevParamsRELayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.thrDDevParamsRELayout.setSpacing(5)
        self.thrDDevParamsRELayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevParamsRELayout.setObjectName("thrDDevParamsRELayout")
        self.thrDDevRLabel = QtWidgets.QLabel(self.tab_4)
        self.thrDDevRLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevRLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevRLabel.setObjectName("thrDDevRLabel")
        self.thrDDevParamsRELayout.addWidget(self.thrDDevRLabel, 0, 0, 1, 1)
        self.thrDDevRBrowerButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevRBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevRBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevRBrowerButton.setObjectName("thrDDevRBrowerButton")
        self.thrDDevParamsRELayout.addWidget(self.thrDDevRBrowerButton, 0, 2, 1, 1)
        self.thrDDevRLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.thrDDevRLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevRLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevRLineEdit.setObjectName("thrDDevRLineEdit")
        self.thrDDevParamsRELayout.addWidget(self.thrDDevRLineEdit, 0, 1, 1, 1)
        self.thrDDevParamsVLayout.addLayout(self.thrDDevParamsRELayout)
        self.thrDDevParamsOGLayout = QtWidgets.QGridLayout()
        self.thrDDevParamsOGLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.thrDDevParamsOGLayout.setSpacing(5)
        self.thrDDevParamsOGLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevParamsOGLayout.setObjectName("thrDDevParamsOGLayout")
        self.thrDDevOLabel = QtWidgets.QLabel(self.tab_4)
        self.thrDDevOLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevOLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevOLabel.setObjectName("thrDDevOLabel")
        self.thrDDevParamsOGLayout.addWidget(self.thrDDevOLabel, 0, 0, 1, 1)
        self.thrDDevOBrowerButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevOBrowerButton.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevOBrowerButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevOBrowerButton.setObjectName("thrDDevOBrowerButton")
        self.thrDDevParamsOGLayout.addWidget(self.thrDDevOBrowerButton, 0, 2, 1, 1)
        self.thrDDevOLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.thrDDevOLineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.thrDDevOLineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.thrDDevOLineEdit.setObjectName("thrDDevOLineEdit")
        self.thrDDevParamsOGLayout.addWidget(self.thrDDevOLineEdit, 0, 1, 1, 1)
        self.thrDDevParamsVLayout.addLayout(self.thrDDevParamsOGLayout)
        self.line_11 = QtWidgets.QFrame(self.tab_4)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.thrDDevParamsVLayout.addWidget(self.line_11)
        self.thrDDevOpHLayout = QtWidgets.QHBoxLayout()
        self.thrDDevOpHLayout.setSpacing(5)
        self.thrDDevOpHLayout.setContentsMargins(5, 5, 5, 5)
        self.thrDDevOpHLayout.setObjectName("thrDDevOpHLayout")
        self.thrDDevReportButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevReportButton.setObjectName("thrDDevReportButton")
        self.thrDDevOpHLayout.addWidget(self.thrDDevReportButton)
        self.thrDDevLogButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevLogButton.setObjectName("thrDDevLogButton")
        self.thrDDevOpHLayout.addWidget(self.thrDDevLogButton)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.thrDDevOpHLayout.addItem(spacerItem16)
        self.thrDDevStartButton = QtWidgets.QPushButton(self.tab_4)
        self.thrDDevStartButton.setObjectName("thrDDevStartButton")
        self.thrDDevOpHLayout.addWidget(self.thrDDevStartButton)
        self.thrDDevParamsVLayout.addLayout(self.thrDDevOpHLayout)
        self.thrDDevVLayout.addLayout(self.thrDDevParamsVLayout)
        self.thrDDevTableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.thrDDevTableWidget.setObjectName("thrDDevTableWidget")
        self.thrDDevTableWidget.setColumnCount(0)
        self.thrDDevTableWidget.setRowCount(0)
        self.thrDDevVLayout.addWidget(self.thrDDevTableWidget)
        self.verticalLayout_11.addLayout(self.thrDDevVLayout)
        self.thrDContent.addTab(self.tab_4, "")
        self.thrDVLayout.addWidget(self.thrDContent)
        self.verticalLayout_9.addLayout(self.thrDVLayout)
        self.mainContent.addTab(self.modelContentTab, "")


        self.mainHLayout.addWidget(self.mainContent)
        self.verticalLayout.addLayout(self.mainHLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.mainContent.setCurrentIndex(0)
        self.domContent.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.initUiconfig()

    def thrDDevTableWidgetMenu(self, pos):
        """
        为thrDDevTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.thrDDevTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开模型所在文件位置")
        item2 = menu.addAction(u"打开参照数据位置")
        item3 = menu.addAction(u"打开输出数据位置")
        action = menu.exec_(self.thrDDevTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.thrDDevTableWidget.item(row_num, 3).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.thrDDevTableWidget.item(row_num, 4).text().__str__()))
        elif action == item3:
            os.startfile(os.path.dirname(self.thrDDevTableWidget.item(row_num, 5).text().__str__()))
        else:
            return

    def thrDTexTableWidgetMenu(self, pos):
        """
        为thrDTexTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.thrDTexTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开模型所在文件位置")
        item2 = menu.addAction(u"打开贴图文件夹位置")
        action = menu.exec_(self.thrDTexTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.thrDTexTableWidget.item(row_num, 3).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.thrDTexTableWidget.item(row_num, 4).text().__str__()))
        else:
            return

    def stdCodeTableWidgetMenu(self, pos):
        """
        为stdCodeTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.stdCodeTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开要素所在文件位置")
        action = menu.exec_(self.stdCodeTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.stdCodeTableWidget.item(row_num, 3).text().__str__()))
        else:
            return

    def demJBTableWidgetMenu(self, pos):
        """
        为demJBTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.demJBTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开原始DEM所在位置")
        item2 = menu.addAction(u"打开处理后矢量文件所在位置")
        action = menu.exec_(self.demJBTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.demJBTableWidget.item(row_num, 1).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.demJBTableWidget.item(row_num, 7).text().__str__()))
        else:
            return

    def demTableWidgetMenu(self, pos):
        """
        为demTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.demTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开原始DEM所在位置")
        item2 = menu.addAction(u"打开处理后矢量文件所在位置")
        action = menu.exec_(self.demTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.demTableWidget.item(row_num, 1).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.demTableWidget.item(row_num, 6).text().__str__()))
        else:
            return

    def domTableWidgetMenu(self, pos):
        """
        为domTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.domTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开原始影像所在位置")
        item2 = menu.addAction(u"打开处理后影像所在位置")
        item3 = menu.addAction(u"查看元数据")
        action = menu.exec_(self.domTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.domTableWidget.item(row_num, 1).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.domTableWidget.item(row_num, 7).text().__str__()))
        elif action == item3:
            xmlPath,_ = os.path.splitext(self.domTableWidget.item(row_num, 7).text().__str__())
            if os.path.exists(xmlPath +'.xml'):
                self.mdlg = metatreeDlg.metatreeDlg(xmlPath+'.xml')
                self.mdlg.exec_()
            else:
                QtWidgets.QMessageBox.information(self.domContentTab, u"元数据不存在",
                                                  u"所选数据的元数据文件不存在，请检查。",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            return

    def domFormatTableWidgetMenu(self, pos):
        """
        为domFormatTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.domFormatTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开影像所在位置")
        item2 = menu.addAction(u"查看元数据")
        action = menu.exec_(self.domFormatTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.domFormatTableWidget.item(row_num, 1).text().__str__()))
        elif action == item2:
            xmlPath,_ = os.path.splitext(self.domFormatTableWidget.item(row_num, 1).text().__str__())
            if os.path.exists(xmlPath):
                self.mdlg = metatreeDlg.metatreeDlg(xmlPath+'.xml')
                self.mdlg.exec_()
            else:
                QtWidgets.QMessageBox.information(self.domContentTab, u"元数据不存在",
                                                  u"所选数据的元数据文件不存在，请检查。",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            return

    def domMatchTableWidgetMenu(self, pos):
        """
        为domMatchTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.domMatchTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开索引文件所在位置")
        action = menu.exec_(self.domMatchTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.domMatchTableWidget.item(row_num, 2).text().__str__()))
        else:
            return

    def domCTableWidgetMenu(self, pos):
        """
        为domCTableWidget添加右键Menu菜单。

        :param pos: 鼠标位置。
        :return:
        """
        row_num = -1
        for i in self.domCTableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1: #没数据或没选中时返回
            return
        menu = QtWidgets.QMenu()
        item1 = menu.addAction(u"打开原始索引文件所在位置")
        item2 = menu.addAction(u"打开处理后索引文件所在位置")
        action = menu.exec_(self.domCTableWidget.mapToGlobal(pos))
        if action == item1:
            os.startfile(os.path.dirname(self.domCTableWidget.item(row_num, 1).text().__str__()))
        elif action == item2:
            os.startfile(os.path.dirname(self.domCTableWidget.item(row_num, 5).text().__str__()))
        else:
            return

    def selectWBInputPath(self):
        """
        选择异常值检查输入数据路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectWBInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.domWBILineEdit.setText(InputDir)

    def selectWBOutputPath(self):
        """
        选择异常值检查输出数据路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectWBOutputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.domWBOLineEdit.setText(OutputDir)

    def selectFormatInputPath(self):
        """
        选择分辨率与坐标系检查输入数据路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectWBInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.domFormatILineEdit.setText(InputDir)

    def domFormatPSettingButtonClicked(self):
        self.fpdlg.exec_()

    def initUiconfig(self):
        """
        对界面中的widgets进行初始化设置。

        :return: None.
        """

        self.enToChnDict = {
            'szs': '所在设区市',
            'szqx': '所在区县',
            'szz' : '所在乡镇街道',
            'dz' : '地址',
            'yzbm': '邮政编码',
            'lxdh': '公开电话',
            'wz' : '网址',
            'email': '电子邮箱',
            'gzsj' : '时间'
        }

        self.gdbDict = {}
        self.jsonDict = {}

        #fpdlg初始化与信号槽连接
        self.formatParamsDict = {}
        self.fpdlg = domFormatPSettingDlg.domformatpsettingdlg()
        self.fpdlg.domFormatTableItemDataSignal.connect(self.slot_setDomFormatParamsTItem)

        #对mainContent的初始化设置
        self.mainContent.tabBar().hide() # 隐藏tabBar，准备用按钮控制
        self.domButton.setChecked(True)
        self.demButton.setChecked(False)
        self.stdataButton.setChecked(False)
        self.modelButton.setChecked(False)
        self.mainContent.setCurrentIndex(0)

        """
        对DOM中的widgets进行初始化设置
        """

        """对影像边缘异常值Tab中的widgets进行初始化设置"""
        #对domWBlineEdit的初始化设置
        self.domWBILineEdit.setEnabled(False) # 不允许用户手动输入地址
        self.domWBOLineEdit.setEnabled(False) # 不允许用户手动输入地址
        self.domWBILineEdit.setStyleSheet("color:white") # 修改颜色
        self.domWBOLineEdit.setStyleSheet("color:white") # 修改颜色

        #对domWBBrowerButton的初始化设置
        self.domWBIBrowerButton.clicked.connect(self.selectWBInputPath)
        self.domWBOBrowerButton.clicked.connect(self.selectWBOutputPath)

        self.ovrCBox.stateChanged.connect(self.ovrStateChanged)

        self.nodataCBox.stateChanged.connect(self.nodataStateChanged)

        self.c254CBox.stateChanged.connect(self.c254StateChanged)

        #对domWBStartButton的初始化设置
        self.domWBStartButton.clicked.connect(self.domWBStartButtonClicked)

        #对domWBLogButton的初始化设置
        self.domWBLogButton.clicked.connect(self.domWBLogButtonClicked)

        #对domWBReportButton的初始化设置
        self.domWBReportButton.clicked.connect(self.domWBReportButtonClicked)
        self.domWBReportButton.setEnabled(False) #初始不开启，domTableWidget中有数据时才enabled

        #对domTableWidget的初始化设置
        self.domTableWidget.setColumnCount(8) # 设定表格列数
        #self.domTableWidget.setRowCount(2)
        horizontalHeader = [u"影像名称", u"影像路径", u"异常类型", u"总像元数量", u"异常像元数量", u"处理结果", u"另存为名称", u"另存为路径"] # 表格头名称
        self.domTableWidget.setHorizontalHeaderLabels(horizontalHeader) # 将表格头名称添加到表格中
        self.domTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # 不允许编辑表格
        self.domTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection) # 只允许单选
        self.domTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # 只允许行选
        # self.domTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.domTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.domTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.domTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # 允许右键产生子菜单
        self.domTableWidget.customContextMenuRequested.connect(self.domTableWidgetMenu) # 右键菜单
        self.domTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionClicked) # 连接排序用的槽
        self.domTableWidget.setSortingEnabled(True)

        """对覆盖范围检查Tab中的widgets进行初始化设置"""
        self.domCILineEdit.setEnabled(False) # 索引数据路径 不允许用户手动输入地址
        self.domCADLineEdit.setEnabled(False) # 行政区划数据路径 不允许用户手动输入地址
        self.domCOLineEdit.setEnabled(False) # 输出路径 不允许用户手动输入地址
        self.domCILineEdit.setStyleSheet("color:white")
        self.domCADLineEdit.setStyleSheet("color:white")
        self.domCOLineEdit.setStyleSheet("color:white")

        self.domCIBrowerButton.clicked.connect(self.selectCIInputPath)
        self.domCADBrowerButton.clicked.connect(self.selectCADInputPath)
        self.domCOBrowerButton.clicked.connect(self.selectCOutputPath)

        # 对domCStartButton的初始化设置
        self.domCStartButton.clicked.connect(self.domCStartButtonClicked)
        # 对domCLogButton的初始化设置
        self.domCLogButton.clicked.connect(self.domCLogButtonClicked)
        # 对domCReportButton的初始化设置
        self.domCReportButton.clicked.connect(self.domCReportButtonClicked)
        self.domCReportButton.setEnabled(False)  # 初始不开启，TableWidget中有数据时才enabled

        self.domCCountyComboBox.addItem('县级')
        self.comCCityComboBox.addItem('市级')

        self.domCTableWidget.setColumnCount(6)  # 设定表格列数

        domCHorizontalHeader = [u"影像名称", u"索引数据路径", u"原始值", u"正确结果", u"索引数据另存为名称", u"索引数据另存为路径"]  # 表格头名称
        self.domCTableWidget.setHorizontalHeaderLabels(domCHorizontalHeader)  # 将表格头名称添加到表格中
        self.domCTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.domCTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.domCTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        # self.domTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.domCTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.domCTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.domCTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.domCTableWidget.customContextMenuRequested.connect(self.domCTableWidgetMenu)  # 右键菜单
        self.domCTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionCClicked)  # 连接排序用的槽
        self.domCTableWidget.setSortingEnabled(True)


        """对分辨率与坐标系检查Tab中的widgets进行初始化设置"""
        #对domFormatLineEdit的初始化设置
        self.domFormatILineEdit.setEnabled(False) # 不允许用户手动输入地址
        self.domFormatILineEdit.setStyleSheet("color:white") # 修改颜色

        #对domWBBrowerButton的初始化设置
        self.domFormatIBrowerButton.clicked.connect(self.selectFormatInputPath)

        # 对domFormatPSettingButton的初始化设置
        self.domFormatPSettingButton.clicked.connect(self.domFormatPSettingButtonClicked)

        #对domFormatParamsTWidget的初始化设置
        self.domFormatParamsTWidget.setColumnCount(2) # 设定表格列数

        #对domFormatStartButton的初始化设置
        self.domFormatStartButton.clicked.connect(self.domFormatStartButtonClicked)

        #对domFormatLogButton的初始化设置
        self.domFormatLogButton.clicked.connect(self.domFormatLogButtonClicked)

        #对domFormatReportButton的初始化设置
        self.domFormatReportButton.clicked.connect(self.domFormatReportButtonClicked)
        self.domFormatReportButton.setEnabled(False) #初始不开启，domFormatTableWidget中有数据时才enabled

        domFormatHorizontalHeader = [u"参数项", u"参数值"] # 表格头名称
        self.domFormatParamsTWidget.setHorizontalHeaderLabels(domFormatHorizontalHeader) # 将表格头名称添加到表格中
        self.domFormatParamsTWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # 不允许编辑表格
        self.domFormatParamsTWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection) # 只允许单选
        self.domFormatParamsTWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # 只允许行选
        self.domFormatParamsTWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.domFormatParamsTWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动

        #对domFormatTableWidget的初始化设置
        self.domFormatTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # 不允许编辑表格
        self.domFormatTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection) # 只允许单选
        self.domFormatTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # 只允许行选
        self.domFormatTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.domFormatTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.domFormatTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # 允许右键产生子菜单
        self.domFormatTableWidget.customContextMenuRequested.connect(self.domFormatTableWidgetMenu) # 右键菜单
        self.domFormatTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionFormatClicked) # 连接排序用的槽
        self.domFormatTableWidget.setSortingEnabled(True)

        """对索引与影像匹配检查Tab中的widgets进行初始化设置"""
        # 对domMatchIndexLineEdit的初始化设置
        self.domMatchIndexLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.domMatchIndexLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对domMatchIndexBrowerButton的初始化设置
        self.domMatchIndexBrowerButton.clicked.connect(self.selectMatchIndexInputPath)

        # 对domMatchStartButton的初始化设置
        self.domMatchStartButton.clicked.connect(self.domMatchStartButtonClicked)

        # 对domMatchLogButton的初始化设置
        self.domMatchLogButton.clicked.connect(self.domMatchLogButtonClicked)

        # 对domMatchReportButton的初始化设置
        self.domMatchReportButton.clicked.connect(self.domMatchReportButtonClicked)
        self.domMatchReportButton.setEnabled(False)  # 初始不开启，domMatchTableWidget中有数据时才enabled

        domMatchHorizontalHeader = [u"索引表项", u"所属索引表", u"所属文件地址", u"名称一致性", u"范围一致性"]  # 表格头名称

        # 对domMatchTableWidget的初始化设置
        self.domMatchTableWidget.setColumnCount(5)  # 设定表格列数
        self.domMatchTableWidget.setHorizontalHeaderLabels(domMatchHorizontalHeader)  # 将表格头名称添加到表格中
        self.domMatchTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.domMatchTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.domMatchTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        self.domMatchTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.domMatchTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.domMatchTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.domMatchTableWidget.customContextMenuRequested.connect(self.domMatchTableWidgetMenu)  # 右键菜单
        self.domMatchTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionMatchClicked)  # 连接排序用的槽
        self.domMatchTableWidget.setSortingEnabled(True)

        """
        对DEM中的widgets进行初始化设置
        """

        """对高程异常值检查Tab中的widgets进行初始化设置"""
        # 对demWBLineEdit的初始化设置
        self.demWBILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.demWBOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.demWBILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.demWBOLineEdit.setStyleSheet("color:white")  # 修改颜色

        #对demWBBrowerButton的初始化设置
        self.demWBIBrowerButton.clicked.connect(self.selectDemWBInputPath)
        self.demWBOBrowerButton.clicked.connect(self.selectDemWBOnputPath)

        #对domWBStartButton的初始化设置
        self.demWBStartButton.clicked.connect(self.demWBStartButtonClicked)

        #对demWBLogButton的初始化设置
        self.demWBLogButton.clicked.connect(self.demWBLogButtonClicked)

        #对demWBReportButton的初始化设置
        self.demWBReportButton.clicked.connect(self.demWBReportButtonClicked)
        self.demWBReportButton.setEnabled(False) #初始不开启，demTableWidget中有数据时才enabled

        #对demTableWidget的初始化设置
        self.demTableWidget.setColumnCount(7) # 设定表格列数
        horizontalHeader = [u"影像名称", u"影像路径", u"有效值范围", u"总像元数量", u"异常像元数量", u"另存为名称", u"另存为路径"] # 表格头名称
        self.demTableWidget.setHorizontalHeaderLabels(horizontalHeader) # 将表格头名称添加到表格中
        self.demTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # 不允许编辑表格
        self.demTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection) # 只允许单选
        self.demTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.demTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.demTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.demTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # 允许右键产生子菜单
        self.demTableWidget.customContextMenuRequested.connect(self.demTableWidgetMenu) # 右键菜单
        self.demTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionDemWBClicked) # 连接排序用的槽
        self.demTableWidget.setSortingEnabled(True)

        """对接边检查Tab中的widgets进行初始化设置"""
        # 对demJBLineEdit的初始化设置
        self.demJBILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.demJBOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.demJBILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.demJBOLineEdit.setStyleSheet("color:white")  # 修改颜色

        #对demJBBrowerButton的初始化设置
        self.demJBIBrowerButton.clicked.connect(self.selectDemJBInputPath)
        self.demJBOBrowerButton.clicked.connect(self.selectDemJBOnputPath)

        #对domJBStartButton的初始化设置
        self.demJBStartButton.clicked.connect(self.demJBStartButtonClicked)

        #对demJBLogButton的初始化设置
        self.demJBLogButton.clicked.connect(self.demJBLogButtonClicked)

        #对demJBReportButton的初始化设置
        self.demJBReportButton.clicked.connect(self.demJBReportButtonClicked)
        self.demJBReportButton.setEnabled(False) #初始不开启，demJBTableWidget中有数据时才enabled

        #对demJBTableWidget的初始化设置
        self.demJBTableWidget.setColumnCount(8) # 设定表格列数
        horizontalHeader = [u"影像名称", u"影像路径", u"有效值范围", u"高程突变阈值", u"总像元数量", u"异常像元数量", u"另存为名称", u"另存为路径"] # 表格头名称
        self.demJBTableWidget.setHorizontalHeaderLabels(horizontalHeader) # 将表格头名称添加到表格中
        self.demJBTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # 不允许编辑表格
        self.demJBTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection) # 只允许单选
        self.demJBTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.demJBTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.demJBTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel) # 圆润地滑动
        self.demJBTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # 允许右键产生子菜单
        self.demJBTableWidget.customContextMenuRequested.connect(self.demJBTableWidgetMenu) # 右键菜单
        self.demJBTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionDemJBClicked) # 连接排序用的槽
        self.demJBTableWidget.setSortingEnabled(True)

        """
        对STD中的widgets进行初始化设置
        """
        """对属性规范性检查Tab中的widgets进行初始化设置"""
        # 对stdAttLineEdit的初始化设置
        self.stdAttILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdAttOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdAttILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.stdAttOLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对stdAttBrowerButton的初始化设置
        self.stdAttIBrowerButton.clicked.connect(self.selectStdAttInputPath)
        self.stdAttOBrowerButton.clicked.connect(self.selectStdAttOutputPath)

        # 对stdComboBox的初始化设置
        self.stdAttSelectGdbComboBox.currentIndexChanged.connect(self.stdAttGdbUpdate)
        self.stdAttSelectLayersComboBox.currentIndexChanged.connect(self.stdAttLayerUpdate)

        # 对stdAttSelectGBoxPushButton的初始化设置
        self.stdAttSelectGBoxPushButton.clicked.connect(self.loadPatternJson)
        self.stdAttSelectGBoxPushButton.setEnabled(False)

        # 对stdAttStartButton的初始化设置
        self.stdAttStartButton.clicked.connect(self.stdAttStartButtonClicked)

        # 对stdAttLogButton的初始化设置
        self.stdAttLogButton.clicked.connect(self.stdAttLogButtonClicked)

        # 对stdAttReportButton的初始化设置
        self.stdAttReportButton.clicked.connect(self.stdAttReportButtonClicked)
        self.stdAttReportButton.setEnabled(False)  # 初始不开启，stdAttTableWidget中有数据时才enabled

        # 对stdAttSelectGBoxTableWidget的初始化设置
        self.stdAttSelectGBoxTableWidget.setColumnCount(3)  # 设定表格列数
        horizontalHeader = [u"字段编码", u"字段检查规则", u"字段检查规则选择"]  # 表格头名称
        self.stdAttSelectGBoxTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.stdAttSelectGBoxTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.stdAttSelectGBoxTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.stdAttSelectGBoxTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        self.stdAttSelectGBoxTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdAttSelectGBoxTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdAttSelectGBoxTableWidget.setSortingEnabled(False)

        # 对stdAttTableWidget的初始化设置
        self.stdAttTableWidget.setColumnCount(6)  # 设定表格列数
        horizontalHeader = [u"图层名称",u"图层检查字段总数量",u"图层要素总数量",u"出错要素总数量",u"图层所在文件路径",u"输出文件路径"]  # 表格头名称
        self.stdAttTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.stdAttTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.stdAttTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.stdAttTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.stdAttTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdAttTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdAttTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        # self.stdAttTableWidget.customContextMenuRequested.connect(self.stdAttTableWidgetMenu)  # 右键菜单
        self.stdAttTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionStdAttClicked)  # 连接排序用的槽
        self.stdAttTableWidget.setSortingEnabled(True)

        """对编码一致性检查Tab中的widgets进行初始化设置"""
        # 对stdCodeLineEdit的初始化设置
        self.stdCodeILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdCodeOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdCodeILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.stdCodeOLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对stdCodeBrowerButton的初始化设置
        self.stdCodeIBrowerButton.clicked.connect(self.selectStdCodeInputPath)
        self.stdCodeOBrowerButton.clicked.connect(self.selectStdCodeOutputPath)

        # 对stdCodeStartButton的初始化设置
        self.stdCodeStartButton.clicked.connect(self.stdCodeStartButtonClicked)

        # 对stdCodeLogButton的初始化设置
        self.stdCodeLogButton.clicked.connect(self.stdCodeLogButtonClicked)

        # 对stdCodeReportButton的初始化设置
        self.stdCodeReportButton.clicked.connect(self.stdCodeReportButtonClicked)
        self.stdCodeReportButton.setEnabled(False)  # 初始不开启，stdAttTableWidget中有数据时才enabled

        # 对stdCodeTableWidget的初始化设置
        self.stdCodeTableWidget.setColumnCount(4)  # 设定表格列数
        horizontalHeader = [u"要素名称", u"要素所在图层名称", u"要素编码", u"要素所在文件路径"]  # 表格头名称
        self.stdCodeTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.stdCodeTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.stdCodeTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.stdCodeTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.stdCodeTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdCodeTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdCodeTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.stdCodeTableWidget.customContextMenuRequested.connect(self.stdCodeTableWidgetMenu)  # 右键菜单
        self.stdCodeTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionStdCodeClicked)  # 连接排序用的槽
        self.stdCodeTableWidget.setSortingEnabled(True)

        """对名称重复性检查Tab中的widgets进行初始化设置"""
        # 对stdRepeatLineEdit的初始化设置
        self.stdRepeatILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdRepeatOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.stdRepeatILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.stdRepeatOLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对stdRepeatBrowerButton的初始化设置
        self.stdRepeatIBrowerButton.clicked.connect(self.selectStdRepeatInputPath)
        self.stdRepeatOBrowerButton.clicked.connect(self.selectStdRepeatOutputPath)

        # 对stdRepeatStartButton的初始化设置
        self.stdRepeatStartButton.clicked.connect(self.stdRepeatStartButtonClicked)

        # 对stdRepeatLogButton的初始化设置
        self.stdRepeatLogButton.clicked.connect(self.stdRepeatLogButtonClicked)

        # 对stdRepeatReportButton的初始化设置
        self.stdRepeatReportButton.clicked.connect(self.stdRepeatReportButtonClicked)
        self.stdRepeatReportButton.setEnabled(False)  # 初始不开启，stdAttTableWidget中有数据时才enabled

        # 对stdRepeatTableWidget的初始化设置
        self.stdRepeatTableWidget.setColumnCount(6)  # 设定表格列数
        horizontalHeader = [u"图层名称",u"图层要素总数量",u"重名要素数量",u"重名要素FID字符串",u"图层所在文件路径",u"输出文件路径"]  # 表格头名称
        self.stdRepeatTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.stdRepeatTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.stdRepeatTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.stdRepeatTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.stdRepeatTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdRepeatTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.stdRepeatTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        # self.stdRepeatTableWidget.customContextMenuRequested.connect(self.stdRepeatTableWidgetMenu)  # 右键菜单
        self.stdRepeatTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionStdRepeatClicked)  # 连接排序用的槽
        self.stdRepeatTableWidget.setSortingEnabled(True)

        """
        对model中的widgets进行初始化设置
        """
        """对贴图完整性检查Tab中的widgets进行初始化设置"""
        # 对thrDTexLineEdit的初始化设置
        self.thrDTexILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.thrDTexTLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        # self.thrDTexOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.thrDTexILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.thrDTexTLineEdit.setStyleSheet("color:white")  # 修改颜色
        # self.thrDTexOLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对thrDTexBrowerButton的初始化设置
        self.thrDTexIBrowerButton.clicked.connect(self.selectThrDTexInputPath)
        self.thrDTexTBrowerButton.clicked.connect(self.selectThrDTexTexturePath)
        # self.thrDTexOBrowerButton.clicked.connect(self.selectThrDTexOutputPath)

        # 对thrDTexStartButton的初始化设置
        self.thrDTexStartButton.clicked.connect(self.thrDTexStartButtonClicked)

        # 对thrDTexLogButton的初始化设置
        self.thrDTexLogButton.clicked.connect(self.thrDTexLogButtonClicked)

        # 对thrDTexReportButton的初始化设置
        self.thrDTexReportButton.clicked.connect(self.thrDTexReportButtonClicked)
        self.thrDTexReportButton.setEnabled(False)  # 初始不开启，thrDTexTableWidget中有数据时才enabled

        # 对thrDTexTableWidget的初始化设置
        self.thrDTexTableWidget.setColumnCount(5)  # 设定表格列数
        horizontalHeader = [u"3D模型名称", u"贴图名称", u"是否缺失", u"模型所在文件路径", u"贴图文件夹路径"] # 表格头名称
        self.thrDTexTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.thrDTexTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.thrDTexTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.thrDTexTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        self.thrDTexTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.thrDTexTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.thrDTexTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.thrDDevTableWidget.customContextMenuRequested.connect(self.thrDTexTableWidgetMenu)  # 右键菜单
        self.thrDTexTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionThrDTexClicked)  # 连接排序用的槽
        self.thrDTexTableWidget.setSortingEnabled(True)

        """对平面位置精度检查Tab中的widgets进行初始化设置"""
        # 对ThrDTexLineEdit的初始化设置
        self.thrDDevILineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.thrDDevRLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.thrDDevOLineEdit.setEnabled(False)  # 不允许用户手动输入地址
        self.thrDDevILineEdit.setStyleSheet("color:white")  # 修改颜色
        self.thrDDevRLineEdit.setStyleSheet("color:white")  # 修改颜色
        self.thrDDevOLineEdit.setStyleSheet("color:white")  # 修改颜色

        # 对thrDDevBrowerButton的初始化设置
        self.thrDDevIBrowerButton.clicked.connect(self.selectThrDDevInputPath)
        self.thrDDevRBrowerButton.clicked.connect(self.selectThrDDevReferencePath)
        self.thrDDevOBrowerButton.clicked.connect(self.selectThrDDevOutputPath)

        # 对thrDDevStartButton的初始化设置
        self.thrDDevStartButton.clicked.connect(self.thrDDevStartButtonClicked)

        # 对stdCodeLogButton的初始化设置
        self.thrDDevLogButton.clicked.connect(self.thrDDevLogButtonClicked)

        # 对stdCodeReportButton的初始化设置
        self.thrDDevReportButton.clicked.connect(self.thrDDevReportButtonClicked)
        self.thrDDevReportButton.setEnabled(False)  # 初始不开启，thrDDevTableWidget中有数据时才enabled

        # 对thrDDevTableWidget的初始化设置
        self.thrDDevTableWidget.setColumnCount(6)  # 设定表格列数
        horizontalHeader = [u"3D模型名称", u"匹配要素ID", u"偏差值", u"模型所在文件路径", u"参照数据路径", u"输出数据路径"]  # 表格头名称
        self.thrDDevTableWidget.setHorizontalHeaderLabels(horizontalHeader)  # 将表格头名称添加到表格中
        self.thrDDevTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 不允许编辑表格
        self.thrDDevTableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)  # 只允许单选
        self.thrDDevTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 只允许行选
        # self.demTableWidget.resizeColumnToContents() # 列的宽度适应于内容
        self.thrDDevTableWidget.setHorizontalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.thrDDevTableWidget.setVerticalScrollMode(QtWidgets.QTableWidget.ScrollPerPixel)  # 圆润地滑动
        self.thrDDevTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.thrDDevTableWidget.customContextMenuRequested.connect(self.thrDDevTableWidgetMenu)  # 右键菜单
        self.thrDDevTableWidget.verticalHeader().sectionClicked.connect(self.VerSectionThrDDevClicked)  # 连接排序用的槽
        self.thrDDevTableWidget.setSortingEnabled(True)

        # 用按钮控制mainContent的Tab切换
        self.domButton.clicked.connect(self.domButtonClicked)
        self.demButton.clicked.connect(self.demButtonClicked)
        self.stdataButton.clicked.connect(self.stdataButtonClicked)
        self.modelButton.clicked.connect(self.modelButtonClicked)

    def domButtonClicked(self):
        self.domButton.setChecked(True)
        self.demButton.setChecked(False)
        self.stdataButton.setChecked(False)
        self.modelButton.setChecked(False)
        self.mainContent.setCurrentIndex(0)

    def demButtonClicked(self):
        self.domButton.setChecked(False)
        self.demButton.setChecked(True)
        self.stdataButton.setChecked(False)
        self.modelButton.setChecked(False)
        self.mainContent.setCurrentIndex(1)

    def stdataButtonClicked(self):
        self.domButton.setChecked(False)
        self.demButton.setChecked(False)
        self.stdataButton.setChecked(True)
        self.modelButton.setChecked(False)
        self.mainContent.setCurrentIndex(2)

    def modelButtonClicked(self):
        self.domButton.setChecked(False)
        self.demButton.setChecked(False)
        self.stdataButton.setChecked(False)
        self.modelButton.setChecked(True)
        self.mainContent.setCurrentIndex(3)

    def stdAttGdbUpdate(self):
        if self.stdAttSelectGdbComboBox.count() == 0:
            return
        self.stdAttSelectLayersComboBox.clear()
        for layerName in self.gdbDict[self.stdAttSelectGdbComboBox.currentText()]:
            self.stdAttSelectLayersComboBox.addItem(layerName)
        self.stdAttSelectLayersComboBox.setCurrentIndex(0)

    def stdAttLayerUpdate(self):
        if self.stdAttSelectLayersComboBox.count() == 0:
            return
        self.stdAttSelectGBoxTableWidget.clearContents()
        self.stdAttSelectGBoxTableWidget.setRowCount(0)

        currGdb = self.stdAttSelectGdbComboBox.currentText()
        currLayer = self.stdAttSelectLayersComboBox.currentText()
        rowCount = 0
        for fieldName in self.gdbDict[currGdb][currLayer]:
            patternCombo = QtWidgets.QComboBox(self.stdAttSelectGBoxTableWidget)
            if self.jsonDict:  # 若非空
                for key in self.jsonDict:
                    patternCombo.addItem(key)
                patternCombo.addItem('不检查')
                patternCombo.setCurrentText(self.gdbDict[currGdb][currLayer][fieldName][0])
                self.stdAttSelectGBoxTableWidget.insertRow(rowCount)
                self.stdAttSelectGBoxTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(fieldName))
                self.stdAttSelectGBoxTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(self.gdbDict[currGdb][currLayer][fieldName][1]))
                self.stdAttSelectGBoxTableWidget.setCellWidget(rowCount, 2, patternCombo)
                x = patternCombo.frameGeometry().x()
                y = patternCombo.frameGeometry().y()
                index = self.stdAttSelectGBoxTableWidget.indexAt(QtCore.QPoint(x, y))
                row = index.row()
                column = index.column()
                patternCombo.currentIndexChanged.connect(self.stdPatternUpdate(row, column, currGdb, currLayer, fieldName))
                rowCount += 1
            else:
                self.stdAttSelectGBoxTableWidget.insertRow(rowCount)
                self.stdAttSelectGBoxTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(fieldName))
                self.stdAttSelectGBoxTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(self.gdbDict[currGdb][currLayer][fieldName][1]))
                self.stdAttSelectGBoxTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem('规则库未导入'))
                rowCount += 1
            self.stdAttSelectGBoxTableWidget.resizeColumnsToContents()

    def selectStdRepeatOutputPath(self):
        """
        选择名称重复性检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdRepeatOutputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.stdRepeatOLineEdit.setText(OutputDir)

    def selectStdRepeatInputPath(self):
        """
        选择名称重复性检查数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdRepeatInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.stdRepeatILineEdit.setText(InputDir)

    def selectThrDDevOutputPath(self):
        """
        选择平面精度检查输出数据路径

        :return: None
        """
        try:
            outputFileName,_ = QtWidgets.QFileDialog.getSaveFileName(self.modelContentTab, u"保存输出数据", None, u".shp(*.shp)")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.modelContentTab, u"错误",
                                              u"输出数据路径指定错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectThrDDevOutputPath error: ' + e.__str__())
            return
        if outputFileName is None:
            return
        self.thrDDevOLineEdit.setText(outputFileName)

    def selectThrDDevReferencePath(self):
        """
        选择平面精度检查参照数据路径

        :return: None
        """
        try:
            referFileName,_ = QtWidgets.QFileDialog.getOpenFileName(self.modelContentTab, u"选择参照数据", None, "All Files (*);;ESRI Shapefile 文件 (*.shp)")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.modelContentTab, u"错误",
                                              u"参照数据选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectThrDDevReferencePath error: ' + e.__str__())
            return
        if referFileName is None:
            return
        self.thrDDevRLineEdit.setText(referFileName)

    def selectThrDDevInputPath(self):
        """
        选择平面精度检查数据输入路径

        :return: None
        """
        try:
            # InputFileName,_ = QtWidgets.QFileDialog.getOpenFileName(self.modelContentTab, u"选择模型文件", None, "All Files (*);;DirectX 文件 (*.X)")
            InputFileName = QtWidgets.QFileDialog.getExistingDirectory(self.modelContentTab, u"选择模型文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.modelContentTab, u"错误",
                                              u"模型文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectThrDDevInputPath error: ' + e.__str__())
            return
        if InputFileName is None:
            return
        self.thrDDevILineEdit.setText(InputFileName)

    def selectThrDTexTexturePath(self):
        """
        选择贴图完整性检查贴图数据路径

        :return: None
        """
        try:
            textureDir = QtWidgets.QFileDialog.getExistingDirectory(self.modelContentTab, u"选择贴图数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.modelContentTab, u"错误",
                                              u"贴图文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectThrDTexTexturePath error: ' + e.__str__())
            return
        if textureDir is None:
            return
        self.thrDTexTLineEdit.setText(textureDir)

    def selectThrDTexInputPath(self):
        """
        选择贴图完整性检查数据输入路径

        :return: None
        """
        try:
            #InputFileName,_ = QtWidgets.QFileDialog.getOpenFileName(self.modelContentTab, u"选择模型文件", None, "All Files (*);;DirectX 文件 (*.X)")
            InputFileName = QtWidgets.QFileDialog.getExistingDirectory(self.modelContentTab, u"选择模型文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.modelContentTab, u"错误",
                                              u"模型文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectThrDTexInputPath error: ' + e.__str__())
            return
        if InputFileName is None:
            return
        self.thrDTexILineEdit.setText(InputFileName)

    def selectStdCodeOutputPath(self):
        """
        选择编码一致性检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdCodeOutputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.stdCodeOLineEdit.setText(OutputDir)

    def selectStdCodeInputPath(self):
        """
        选择编码一致性检查数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdCodeInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.stdCodeILineEdit.setText(InputDir)

    def selectStdAttOutputPath(self):
        """
        选择属性规范性检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdAttOutputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.stdAttOLineEdit.setText(OutputDir)

    def selectStdAttInputPath(self):
        """
        选择属性规范性检查数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.stdataContentTab, u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdAttInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.stdAttILineEdit.setText(InputDir)
        self.loadGdb(InputDir)
        for gdb in self.gdbDict:
            self.stdAttSelectGdbComboBox.addItem(gdb)
        self.stdAttSelectGdbComboBox.setCurrentIndex(0)
        self.stdAttSelectGBoxPushButton.setEnabled(True)

    def loadPatternJson_Impl(self):
        """
        加载规则库的实现

        :return:
        """
        for gdb in self.gdbDict:
            for layerName in self.gdbDict[gdb]:
                for fieldName in self.gdbDict[gdb][layerName]:
                    if fieldName in self.enToChnDict:
                        key = self.enToChnDict[fieldName]
                        self.gdbDict[gdb][layerName][fieldName][0] = key
                        self.gdbDict[gdb][layerName][fieldName][1] = self.jsonDict[key]
                    else:
                        self.gdbDict[gdb][layerName][fieldName][0] = '不检查'
                        self.gdbDict[gdb][layerName][fieldName][1] = '不检查'

        currGdb = self.stdAttSelectGdbComboBox.currentText()
        currLayer = self.stdAttSelectLayersComboBox.currentText()
        rowCount = 0
        for fieldName in self.gdbDict[currGdb][currLayer]:
            patternCombo = QtWidgets.QComboBox(self.stdAttSelectGBoxTableWidget)
            for key in self.jsonDict:
                patternCombo.addItem(key)
            patternCombo.addItem('不检查')
            patternCombo.setCurrentText(self.gdbDict[currGdb][currLayer][fieldName][0])
            self.stdAttSelectGBoxTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(fieldName))
            self.stdAttSelectGBoxTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(self.gdbDict[currGdb][currLayer][fieldName][1]))
            self.stdAttSelectGBoxTableWidget.setCellWidget(rowCount, 2, patternCombo)
            x = patternCombo.frameGeometry().x()
            y = patternCombo.frameGeometry().y()
            index = self.stdAttSelectGBoxTableWidget.indexAt(QtCore.QPoint(x, y))
            row = index.row()
            column = index.column()
            # print(row.__str__())
            patternCombo.currentIndexChanged.connect(self.stdPatternUpdate(row, column, currGdb, currLayer, fieldName))
            rowCount += 1
        self.stdAttSelectGBoxTableWidget.resizeColumnsToContents()

    def loadPatternJson(self):
        """
        选择并加载规则库

        :return: None
        """
        try:
            InputJson,_ = QtWidgets.QFileDialog.getOpenFileName(self.stdataContentTab, u"选择规则库文件", None, "All Files (*);;规则库文件 (*.json)")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.stdataContentTab, u"错误",
                                              u"规则库选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectStdAttInputPath error: ' + e.__str__())
            return
        if InputJson is None:
            return
        with open(InputJson, 'r', encoding= 'utf-8') as f:
            self.jsonDict = json.load(f)
        self.loadPatternJson_Impl()
        # for gdb in self.gdbDict:
        #     for layerName in self.gdbDict[gdb]:
        #         for fieldName in self.gdbDict[gdb][layerName]:
        #             for patternName in self.jsonDict:
        #                 if self.jsonDict:  # 若非空
        #                     patternCombo.addItem(key)
        #                     patternCombo.setCurrentText(self.gdbDict[currGdb][currLayer][fieldName][0])

    def stdPatternUpdate(self,row,column,gdb,layerName,fieldName):
        def calluser():
            currentPatternName = self.stdAttSelectGBoxTableWidget.cellWidget(row, 2).currentText()
            self.gdbDict[gdb][layerName][fieldName][0] = currentPatternName
            patternStr = '不检查'
            if currentPatternName != '不检查':
                patternStr = self.jsonDict[self.gdbDict[gdb][layerName][fieldName][0]]
            self.gdbDict[gdb][layerName][fieldName][1] = patternStr
            patternItem = QtWidgets.QTableWidgetItem(patternStr)
            self.stdAttSelectGBoxTableWidget.setItem(row, 1, patternItem)
        return calluser

    def loadGdb(self,InputDir):
        try:
            self.gdbDict = {}
            self.stdAttSelectGdbComboBox.clear()
            self.stdAttSelectLayersComboBox.clear()
            for gdb in os.listdir(InputDir):
                import ogr
                driver = ogr.GetDriverByName('openFileGDB')
                if gdb[-4:] != '.gdb':
                    continue
                gdbFile = driver.Open(InputDir + '/' + gdb, 0)
                self.gdbDict[gdb] = {}
                for layer in gdbFile:
                    layerName = layer.GetName()
                    self.gdbDict[gdb][layerName] = {}
                    layerdef = layer.GetLayerDefn()
                    for i in range(layerdef.GetFieldCount()):
                        defn = layerdef.GetFieldDefn(i)
                        fieldName = defn.GetName()
                        patternStr = '-'
                        self.gdbDict[gdb][layerName][fieldName] = ['-',patternStr]
                gdbFile = None
            if self.jsonDict.__len__() != 0:
                self.loadPatternJson_Impl()
        except Exception as e:
            print(e.__str__())
            return

    def selectDemJBOnputPath(self):
        """
        选择DEM接边检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.demContentTab,u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.demContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectDemJBOnputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.demJBOLineEdit.setText(OutputDir)

    def selectDemJBInputPath(self):
        """
        选择DEM接边数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.demContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.demContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectDemJBInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.demJBILineEdit.setText(InputDir)


    def selectDemWBOnputPath(self):
        """
        选择DEM高程检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.demContentTab,u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.demContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectDemWBOnputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.demWBOLineEdit.setText(OutputDir)

    def selectDemWBInputPath(self):
        """
        选择DEM高程数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.demContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.demContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectDemWBInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.demWBILineEdit.setText(InputDir)

    def selectCIInputPath(self):
        """
        选择覆盖范围检查索引数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectCIInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.domCILineEdit.setText(InputDir)

    def selectCADInputPath(self):
        """
        选择覆盖范围检查行政区划数据输入路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectCADInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.domCADLineEdit.setText(InputDir)

    def selectCOutputPath(self):
        """
        选择覆盖范围检查输出路径

        :return: None
        """
        try:
            OutputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输出数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输出数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectCOutputPath error: ' + e.__str__())
            return
        if OutputDir is None:
            return
        self.domCOLineEdit.setText(OutputDir)


    def selectMatchIndexInputPath(self):
        """
        选择索引与影像匹配检查输入数据路径

        :return: None
        """
        try:
            InputDir = QtWidgets.QFileDialog.getExistingDirectory(self.domContentTab,u"选择输入数据文件夹")
        except Exception as e:
            QtWidgets.QMessageBox.information(self.domContentTab, u"错误",
                                              u"输入数据文件夹选取错误，请重试。",
                                              QtWidgets.QMessageBox.Ok)
            print('selectMatchIndexInputPath error: ' + e.__str__())
            return
        if InputDir is None:
            return
        self.domMatchIndexLineEdit.setText(InputDir)


    def slot_setThrDTexTableItem(self,modelTableItemData):
        """
        槽，用于添加贴图完整性检查表格项 [u"3D模型名称", u"贴图名称", u"是否缺失", u"模型所在文件路径", u"贴图文件夹路径"]

        :param modelTableItemData: model表格项数据，为列表，元素为元组(贴图名称, 是否缺失, 模型名称, 模型路径, 贴图路径)
        :return: None
        """
        rowCount = self.thrDTexTableWidget.rowCount()
        for item in modelTableItemData:
            self.thrDTexTableWidget.insertRow(rowCount)
            self.thrDTexTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item[2]))
            self.thrDTexTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(item[0]))
            self.thrDTexTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(item[1]))
            self.thrDTexTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(item[3]))
            self.thrDTexTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(item[4]))
            rowCount += 1
        self.thrDTexTableWidget.resizeColumnsToContents()

    def slot_setThrDDevTableItem(self,modelTableItemData):
        """
        槽，用于添加平面精度检查表格项

        :param modelTableItemData: model表格项数据
        :return: None
        """
        rowCount = self.thrDDevTableWidget.rowCount()
        self.thrDDevTableWidget.insertRow(rowCount)
        self.thrDDevTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(modelTableItemData[0]))
        self.thrDDevTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(modelTableItemData[1]))
        self.thrDDevTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(modelTableItemData[2]))
        self.thrDDevTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(modelTableItemData[3]))
        self.thrDDevTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(modelTableItemData[4]))
        self.thrDDevTableWidget.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(modelTableItemData[5]))
        rowCount += 1
        self.thrDDevTableWidget.resizeColumnsToContents()


    def slot_setDomCoverTableItem(self,domTableItemData):
        """
        槽，用于添加覆盖检测表格项

        :param domTableItemData: dom表格项数据，为元组
        :return: None
        """
        rowCount = self.domCTableWidget.rowCount()
        self.domCTableWidget.insertRow(rowCount)
        datanameItem = QtWidgets.QTableWidgetItem(domTableItemData[0])
        datapathItem = QtWidgets.QTableWidgetItem(domTableItemData[1])
        typeItem = QtWidgets.QTableWidgetItem(domTableItemData[2])
        totalItem = QtWidgets.QTableWidgetItem(domTableItemData[3])
        errorItem = QtWidgets.QTableWidgetItem(domTableItemData[4])
        resultItem = QtWidgets.QTableWidgetItem(domTableItemData[5])
        self.domCTableWidget.setItem(rowCount, 0, datanameItem)
        self.domCTableWidget.setItem(rowCount, 1, datapathItem)
        self.domCTableWidget.setItem(rowCount, 2, typeItem)
        self.domCTableWidget.setItem(rowCount, 3, totalItem)
        self.domCTableWidget.setItem(rowCount, 4, errorItem)
        self.domCTableWidget.setItem(rowCount, 5, resultItem)
        self.domCTableWidget.resizeColumnsToContents()

    def slot_setStdAttTableItem(self,stdTableItemData):
        """
        槽，用于添加std表格项

        :param stdTableItemData: std表格项数据，为字典
        :return: None
        """
        items = stdTableItemData
        rowCount = self.stdAttTableWidget.rowCount()
        for item in items:
            self.stdAttTableWidget.insertRow(rowCount)
            self.stdAttTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item[0]))
            self.stdAttTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(item[1]))
            self.stdAttTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(item[2]))
            self.stdAttTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(item[3]))
            self.stdAttTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(item[4]))
            self.stdAttTableWidget.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(item[5]))
            self.stdAttTableWidget.resizeColumnsToContents()
            rowCount+=1
        # item = stdTableItemData
        # rowCount = self.stdAttTableWidget.rowCount()
        # self.stdAttTableWidget.insertRow(rowCount)
        # self.stdAttTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item[0]))
        # self.stdAttTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(item[1]))
        # self.stdAttTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(item[2]))
        # self.stdAttTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(item[3]))
        # self.stdAttTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(item[4]))
        # self.stdAttTableWidget.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(item[5]))
        # self.stdAttTableWidget.resizeColumnsToContents()

    def slot_setStdCodeTableItem(self,stdTableItemData):
        """
        槽，用于添加std表格项

        :param stdTableItemData: std表格项数据，为字典
        :return: None
        """
        rowCount = self.stdCodeTableWidget.rowCount()
        for item in stdTableItemData:
            if stdTableItemData[item].__len__() == 1:
                continue
            for con in stdTableItemData[item]:
                self.stdCodeTableWidget.insertRow(rowCount)
                self.stdCodeTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(con['name']))
                self.stdCodeTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(con['layerName']))
                self.stdCodeTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(con['code']))
                self.stdCodeTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(con['gdbDir']))
                rowCount += 1
        self.stdCodeTableWidget.resizeColumnsToContents()

    def slot_setStdRepeatTableItem(self,stdTableItemData):
        """
        槽，用于添加std表格项

        :param stdTableItemData: std表格项数据，为列表
        :return: None
        """
        rowCount = self.stdRepeatTableWidget.rowCount()
        for item in stdTableItemData:
            self.stdRepeatTableWidget.insertRow(rowCount)
            self.stdRepeatTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item[0]))
            self.stdRepeatTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(item[1]))
            self.stdRepeatTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(item[2]))
            self.stdRepeatTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(item[3]))
            self.stdRepeatTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(item[4]))
            self.stdRepeatTableWidget.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(item[5]))
            rowCount += 1
        self.stdRepeatTableWidget.resizeColumnsToContents()


    def slot_setDemTableItem(self,demTableItemData):
        """
        槽，用于添加demWB表格项

        :param demTableItemData: dem表格项数据，为元组
        :return: None
        """
        rowCount = self.demTableWidget.rowCount()
        self.demTableWidget.insertRow(rowCount)
        datanameItem = QtWidgets.QTableWidgetItem(demTableItemData[0])
        datapathItem = QtWidgets.QTableWidgetItem(demTableItemData[1])
        rangeItem = QtWidgets.QTableWidgetItem(demTableItemData[2])
        totalItem = QtWidgets.QTableWidgetItem(demTableItemData[3])
        errorItem = QtWidgets.QTableWidgetItem(demTableItemData[4])
        saveasItem = QtWidgets.QTableWidgetItem(demTableItemData[5])
        saveaspathItem = QtWidgets.QTableWidgetItem(demTableItemData[6])
        self.demTableWidget.setItem(rowCount, 0, datanameItem)
        self.demTableWidget.setItem(rowCount, 1, datapathItem)
        self.demTableWidget.setItem(rowCount, 2, rangeItem)
        self.demTableWidget.setItem(rowCount, 3, totalItem)
        self.demTableWidget.setItem(rowCount, 4, errorItem)
        self.demTableWidget.setItem(rowCount, 5, saveasItem)
        self.demTableWidget.setItem(rowCount, 6, saveaspathItem)
        self.demTableWidget.resizeColumnsToContents()

    def slot_setDemJBTableItem(self,demTableItemData):
        """
        槽，用于添加demWB表格项

        :param demTableItemData: dem表格项数据，为元组
        :return: None
        """
        rowCount = self.demJBTableWidget.rowCount()
        self.demJBTableWidget.insertRow(rowCount)
        datanameItem = QtWidgets.QTableWidgetItem(demTableItemData[0])
        datapathItem = QtWidgets.QTableWidgetItem(demTableItemData[1])
        rangeItem = QtWidgets.QTableWidgetItem(demTableItemData[2])
        thresItem = QtWidgets.QTableWidgetItem(demTableItemData[3])
        totalItem = QtWidgets.QTableWidgetItem(demTableItemData[4])
        errorItem = QtWidgets.QTableWidgetItem(demTableItemData[5])
        saveasItem = QtWidgets.QTableWidgetItem(demTableItemData[6])
        saveaspathItem = QtWidgets.QTableWidgetItem(demTableItemData[7])
        self.demJBTableWidget.setItem(rowCount, 0, datanameItem)
        self.demJBTableWidget.setItem(rowCount, 1, datapathItem)
        self.demJBTableWidget.setItem(rowCount, 2, rangeItem)
        self.demJBTableWidget.setItem(rowCount, 3, thresItem)
        self.demJBTableWidget.setItem(rowCount, 4, totalItem)
        self.demJBTableWidget.setItem(rowCount, 5, errorItem)
        self.demJBTableWidget.setItem(rowCount, 6, saveasItem)
        self.demJBTableWidget.setItem(rowCount, 7, saveaspathItem)
        self.demJBTableWidget.resizeColumnsToContents()

    def slot_setdomTableItem(self,domTableItemData):
        """
        槽，用于添加dom表格项

        :param domTableItemData: dom表格项数据，为元组
        :return: None
        """
        rowCount = self.domTableWidget.rowCount()
        self.domTableWidget.insertRow(rowCount)
        datanameItem = QtWidgets.QTableWidgetItem(domTableItemData[0])
        datapathItem = QtWidgets.QTableWidgetItem(domTableItemData[1])
        typeItem = QtWidgets.QTableWidgetItem(domTableItemData[2])
        totalItem = QtWidgets.QTableWidgetItem(domTableItemData[3])
        errorItem = QtWidgets.QTableWidgetItem(domTableItemData[4])
        resultItem = QtWidgets.QTableWidgetItem(domTableItemData[5])
        saveasItem = QtWidgets.QTableWidgetItem(domTableItemData[6])
        saveaspathItem = QtWidgets.QTableWidgetItem(domTableItemData[7])
        self.domTableWidget.setItem(rowCount, 0, datanameItem)
        self.domTableWidget.setItem(rowCount, 1, datapathItem)
        self.domTableWidget.setItem(rowCount, 2, typeItem)
        self.domTableWidget.setItem(rowCount, 3, totalItem)
        self.domTableWidget.setItem(rowCount, 4, errorItem)
        self.domTableWidget.setItem(rowCount, 5, resultItem)
        self.domTableWidget.setItem(rowCount, 6, saveasItem)
        self.domTableWidget.setItem(rowCount, 7, saveaspathItem)
        self.domTableWidget.resizeColumnsToContents()

    def slot_setDomMatchTableItem(self,domTableItemDataWithIndexPath):
        """
        槽，用于添加dom表格项

        :param domTableItemData: dom表格项数据，为元组
        :return: None
        """
        domTableItemData = domTableItemDataWithIndexPath[0]
        indexPath = domTableItemDataWithIndexPath[1]
        rowCount = self.domMatchTableWidget.rowCount()
        for item in domTableItemData:
            self.domMatchTableWidget.insertRow(rowCount)
            self.domMatchTableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item))
            self.domMatchTableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(domTableItemData[item]['所属索引表']))
            self.domMatchTableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(indexPath))
            self.domMatchTableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(domTableItemData[item]['名称一致性']))
            self.domMatchTableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(domTableItemData[item]['范围一致性']))
            rowCount += 1
        self.domMatchTableWidget.resizeColumnsToContents()

    def slot_setDomFormatParamsTItem(self,paramsDict):
        """
        槽，用于设置分辨率与坐标系质检项

        :param paramsDict: 质检项参数，为字典
        :return:
        """
        self.formatParamsDict = paramsDict
        # self.domFormatParamsTWidget.clearContents()
        self.domFormatParamsTWidget.setRowCount(0)
        rowIndex = 0
        for param in paramsDict:
            self.domFormatParamsTWidget.insertRow(rowIndex)
            datanameItem = QtWidgets.QTableWidgetItem(param)
            datapathItem = QtWidgets.QTableWidgetItem(paramsDict[param])
            self.domFormatParamsTWidget.setItem(rowIndex, 0, datanameItem)
            self.domFormatParamsTWidget.setItem(rowIndex, 1, datapathItem)
            rowIndex += 1
        self.domFormatParamsTWidget.resizeColumnsToContents()

    def slot_setDomFormatTableItem(self,resultList):
        """
        槽，用于设置分辨率与坐标系质检结果表格项

        :param paramsDict: 质检结果项参数，为列表
        :return:
        """
        rowCount = self.domFormatTableWidget.rowCount()
        if rowCount == 0:
            #还没放入数据，所以设置表格头
            self.domFormatTableWidget.setColumnCount(resultList.__len__()) # 设定表格列数
            horizontalHeader = [h[0] for h in resultList]
            self.domFormatTableWidget.setHorizontalHeaderLabels(horizontalHeader) # 将表格头名称添加到表格中
        self.domFormatTableWidget.insertRow(rowCount)
        colIndex = 0
        for res in resultList:
            datanameItem = QtWidgets.QTableWidgetItem(res[1])
            self.domFormatTableWidget.setItem(rowCount, colIndex, datanameItem)
            colIndex += 1
        self.domFormatTableWidget.resizeColumnsToContents()

    def thrDDevStartButtonClicked(self):
        """
        thrDDevStartButton点击事件，开始质检

        :return:
        """
        self.thrDDevTableWidget.clearContents()
        self.thrDDevTableWidget.setRowCount(0)
        thrDDevInputPath = self.thrDDevILineEdit.text().__str__()
        thrDDevReferencePath = self.thrDDevRLineEdit.text().__str__()
        thrDDevOutputPath = self.thrDDevOLineEdit.text().__str__()

        kwd = {'thrDDevInputPath': thrDDevInputPath, 'thrDDevReferencePath': thrDDevReferencePath, 'thrDDevOutputPath': thrDDevOutputPath
               }

        self.pdlg = processDlg.processdlg(taskType = 11, kwd = kwd)
        self.pdlg.t.modelTableItemDataSignal.connect(self.slot_setThrDDevTableItem)
        self.pdlg.exec_()
        if self.thrDDevTableWidget.rowCount() > 0:
            self.thrDDevReportButton.setEnabled(True)

    def thrDDevLogButtonClicked(self):
        """
        thrDDevLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def thrDDevReportButtonClicked(self):
        """
        thrDDevReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.modelContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.thrDDevTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->thrDDevReportButtonClicked ERROR] ' + e.__str__())
            return

    def thrDTexStartButtonClicked(self):
        """
        thrDTexStartButton点击事件，开始质检

        :return:
        """
        self.thrDTexTableWidget.clearContents()
        self.thrDTexTableWidget.setRowCount(0)
        thrDTexInputPath = self.thrDTexILineEdit.text().__str__()
        thrDTexTexturePath = self.thrDTexTLineEdit.text().__str__()

        kwd = {'thrDTexInputPath': thrDTexInputPath, 'thrDTexTexturePath': thrDTexTexturePath
               }

        self.pdlg = processDlg.processdlg(taskType = 10, kwd = kwd)
        self.pdlg.t.modelTableItemDataSignal.connect(self.slot_setThrDTexTableItem)
        self.pdlg.exec_()
        if self.thrDTexTableWidget.rowCount() > 0:
            self.thrDTexReportButton.setEnabled(True)

    def thrDTexLogButtonClicked(self):
        """
        thrDTexLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def thrDTexReportButtonClicked(self):
        """
        thrDTexReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.modelContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.thrDTexTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->thrDTexReportButtonClicked ERROR] ' + e.__str__())
            return

    def stdRepeatStartButtonClicked(self):
        """
        stdRepeatStartButton点击事件，开始质检

        :return:
        """
        self.stdRepeatTableWidget.clearContents()
        self.stdRepeatTableWidget.setRowCount(0)
        gdbDirInputPath = self.stdRepeatILineEdit.text().__str__()
        gdbDirOutputPath = self.stdRepeatOLineEdit.text().__str__()
        matchDegree = self.stdRepeatGroupBoxspinBox.value()

        kwd = {'gdbDirInputPath': gdbDirInputPath, 'gdbDirOutputPath': gdbDirOutputPath,
               'matchDegree': matchDegree
               }

        self.pdlg = processDlg.processdlg(taskType = 9, kwd = kwd)
        self.pdlg.t.stdTableItemDataSignal.connect(self.slot_setStdRepeatTableItem)
        self.pdlg.exec_()
        if self.stdRepeatTableWidget.rowCount() > 0:
            self.stdRepeatReportButton.setEnabled(True)

    def stdRepeatLogButtonClicked(self):
        """
        stdRepeatLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def stdRepeatReportButtonClicked(self):
        """
        stdRepeatReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.stdataContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.stdRepeatTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->stdRepeatReportButtonClicked ERROR] ' + e.__str__())
            return

    def stdCodeStartButtonClicked(self):
        """
        stdCodeStartButton点击事件，开始质检

        :return:
        """
        self.stdCodeTableWidget.clearContents()
        self.stdCodeTableWidget.setRowCount(0)
        indexDirPath = self.stdCodeILineEdit.text().__str__()
        outputDirPath = self.stdCodeOLineEdit.text().__str__()
        kwd = {'indexDirPath' : indexDirPath,'outputDirPath' : outputDirPath}
        self.pdlg = processDlg.processdlg(taskType = 8, kwd = kwd)
        self.pdlg.t.stdTableItemDataSignal.connect(self.slot_setStdCodeTableItem)
        self.pdlg.exec_()
        if self.stdCodeTableWidget.rowCount() > 0:
            self.stdCodeReportButton.setEnabled(True)

    def stdCodeLogButtonClicked(self):
        """
        stdCodeLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def stdCodeReportButtonClicked(self):
        """
        stdCodeReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.stdataContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.stdCodeTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->stdCodeReportButtonClicked ERROR] ' + e.__str__())
            return

    def stdAttStartButtonClicked(self):
        """
        stdAttStartButton点击事件，开始质检

        :return:
        """
        self.stdAttTableWidget.clearContents()
        self.stdAttTableWidget.setRowCount(0)

        gdbInputDirPath = self.stdAttILineEdit.text().__str__()
        gdbDirOutputPath = self.stdAttOLineEdit.text().__str__()
        # minDemValue = self.spinBox_6.value()
        # maxDemValue = self.spinBox_7.value()
        # slopeThreshold = self.spinBox_8.value()
        kwd = {'gdbInputDirPath' : gdbInputDirPath,
               'gdbDirOutputPath' : gdbDirOutputPath,
               'reMatchDic' : self.gdbDict,
               'jsonDict': self.jsonDict
               }
        self.pdlg = processDlg.processdlg(taskType = 7, kwd = kwd)
        self.pdlg.t.stdTableItemDataSignal.connect(self.slot_setStdAttTableItem)
        self.pdlg.exec_()
        if self.stdAttTableWidget.rowCount() > 0:
            self.stdAttReportButton.setEnabled(True)

    def stdAttLogButtonClicked(self):
        """
        stdAttLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def stdAttReportButtonClicked(self):
        """
        stdAttReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.stdataContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.stdAttTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->stdAttReportButtonClicked ERROR] ' + e.__str__())
            return


    def demJBStartButtonClicked(self):
        """
        demJBStartButton点击事件，开始质检

        :return:
        """
        self.demJBTableWidget.clearContents()
        self.demJBTableWidget.setRowCount(0)
        demDirPath = self.demJBILineEdit.text().__str__()
        demDirOutputPath=self.demJBOLineEdit.text().__str__()
        minDemValue = self.spinBox_6.value()
        maxDemValue = self.spinBox_7.value()
        slopeThreshold = self.spinBox_8.value()
        kwd = {'demDirPath' : demDirPath,'demDirOutputPath' : demDirOutputPath,
               'valueRange' : (minDemValue, maxDemValue),
               'slopeThreshold' : slopeThreshold,
               'fileType' : 'img'}
        self.pdlg = processDlg.processdlg(taskType = 6, kwd = kwd)
        self.pdlg.t.demTableItemDataSignal.connect(self.slot_setDemJBTableItem)
        self.pdlg.exec_()
        if self.demJBTableWidget.rowCount() > 0:
            self.demJBReportButton.setEnabled(True)

    def demJBLogButtonClicked(self):
        """
        demJBLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def demJBReportButtonClicked(self):
        """
        demJBReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.demContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.demJBTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->demJBReportButtonClicked ERROR] ' + e.__str__())
            return

    def demWBStartButtonClicked(self):
        """
        demWBStartButton点击事件，开始质检

        :return:
        """
        self.demTableWidget.clearContents()
        self.demTableWidget.setRowCount(0)
        demDirPath = self.demWBILineEdit.text().__str__()
        demDirOutputPath=self.demWBOLineEdit.text().__str__()
        minDemValue = self.spinBox_4d.value()
        maxDemValue = self.spinBox_5d.value()
        kwd = {'demDirPath' : demDirPath,'demDirOutputPath' : demDirOutputPath,
               'valueRange' : (minDemValue, maxDemValue),
               'fileType' : 'img'}
        self.pdlg = processDlg.processdlg(taskType = 5, kwd = kwd)
        self.pdlg.t.demTableItemDataSignal.connect(self.slot_setDemTableItem)
        self.pdlg.exec_()
        if self.demTableWidget.rowCount() > 0:
            self.demWBReportButton.setEnabled(True)

    def demWBLogButtonClicked(self):
        """
        demWBLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def demWBReportButtonClicked(self):
        """
        demWBReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.demContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.demTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->demWBReportButtonClicked ERROR] ' + e.__str__())
            return

    def domCStartButtonClicked(self):
        """
        domCStartButton点击事件，开始质检

        :return:
        """
        self.domCTableWidget.clearContents()
        self.domCTableWidget.setRowCount(0)
        domIndexDirPath = self.domCILineEdit.text().__str__()
        domCoverOutputDirPath=self.domCOLineEdit.text().__str__()
        domCoverDirPath=self.domCADLineEdit.text().__str__()
        kwd = {'domIndexDirPath' : domIndexDirPath,'domCoverDirPath' : domCoverDirPath,
               'domCoverOutputDirPath':domCoverOutputDirPath,
               'fileType' : '.gdb'}
        self.pdlg = processDlg.processdlg(taskType = 2,kwd = kwd)
        self.pdlg.t.domTableItemDataSignal.connect(self.slot_setDomCoverTableItem)
        self.pdlg.exec_()
        if self.domCTableWidget.rowCount() > 0:
            self.domCReportButton.setEnabled(True)

    def domCLogButtonClicked(self):
        """
        domCLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def domCReportButtonClicked(self):
        """
        domCReportButtonClicked点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.domContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.domCTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->domCReportButtonClicked ERROR] ' + e.__str__())
            return

    def domMatchStartButtonClicked(self):
        """
        domMatchStartButton点击事件，开始质检

        :return:
        """
        self.domMatchTableWidget.clearContents()
        self.domMatchTableWidget.setRowCount(0)
        indexDirPath = self.domMatchIndexLineEdit.text().__str__()
        panCap = self.domMatchPanLineEdit.text().__str__()
        kwd = {'indexDirPath': indexDirPath, 'panCap': panCap}
        self.pdlg = processDlg.processdlg(taskType = 4,kwd = kwd)
        self.pdlg.t.domTableItemDataSignal.connect(self.slot_setDomMatchTableItem)
        self.pdlg.exec_()
        if self.domMatchTableWidget.rowCount() > 0:
            self.domMatchReportButton.setEnabled(True)

    def domMatchLogButtonClicked(self):
        """
        domMatchLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def domMatchReportButtonClicked(self):
        """
        domMatchReportButton点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.domContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.domMatchTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->domMatchReportButtonClicked ERROR] ' + e.__str__())
            return

    def domWBStartButtonClicked(self):
        """
        domWBStartButton点击事件，开始质检

        :return:
        """
        self.domTableWidget.clearContents()
        self.domTableWidget.setRowCount(0)
        domDirPath = self.domWBILineEdit.text().__str__()
        outlierValue = self.spinBox.value()
        nearDist = self.spinBox_2.value()
        maxNonBlack = self.spinBox_3.value()
        delNum = self.spinBox_4.value()
        domDirOutputPath = self.domWBOLineEdit.text().__str__()
        fileType = self.resformComboBox.currentText().__str__()
        ovrBuild = True
        nodataFill = True
        c254 = True
        easyKill = False
        easyNearDist = self.spinBox_easyNearDist.value()
        easyColors = self.spinBox_easyColors.value()
        if self.ovrCBox.checkState() != QtCore.Qt.Checked:
            ovrBuild = False
        if self.nodataCBox.checkState() != QtCore.Qt.Checked:
            nodataFill = False
        if self.c254CBox.checkState() != QtCore.Qt.Checked:
            c254 = False
        if self.easyKillCBox.checkState() == QtCore.Qt.Checked:
            easyKill = True

        kwd = {'domDirPath' : domDirPath,
               'domDirOutputPath': domDirOutputPath,
               'outlierValue' : outlierValue,
               'nearDist' : nearDist,
               'maxNonBlack' : maxNonBlack,
               'delNum' : delNum,
               'fileType' : fileType,
               'ovrBuild' : ovrBuild,
               'nodataFill' : nodataFill,
               'c254': c254,
               'easyKill' : easyKill,
               'easyNearDist' : easyNearDist,
               'easyColors' : easyColors,
               }
        self.pdlg = processDlg.processdlg(taskType = 1,kwd = kwd)
        self.pdlg.t.domTableItemDataSignal.connect(self.slot_setdomTableItem)
        self.pdlg.exec_()
        if self.domTableWidget.rowCount() > 0:
            self.domWBReportButton.setEnabled(True)

    def domFormatStartButtonClicked(self):
        """
        domFormatStartButton点击事件，开始质检

        :return:
        """
        self.domFormatTableWidget.clear()
        self.domFormatTableWidget.setColumnCount(0)
        self.domFormatTableWidget.setRowCount(0)
        domDirPath = self.domFormatILineEdit.text().__str__()
        paramsDict = self.formatParamsDict
        kwd = {'domDirPath': domDirPath, 'paramsDict': paramsDict}
        self.pdlg = processDlg.processdlg(taskType = 3,kwd = kwd)
        self.pdlg.t.domTableItemDataSignal.connect(self.slot_setDomFormatTableItem)
        self.pdlg.exec_()
        if self.domFormatTableWidget.rowCount() > 0:
            self.domFormatReportButton.setEnabled(True)

    def domFormatLogButtonClicked(self):
        """
        domFormatLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def domFormatReportButtonClicked(self):
        """
        domFormatReportButton点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.domContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.domFormatTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->domFormatReportButtonClicked ERROR] ' + e.__str__())
            return


    def domWBLogButtonClicked(self):
        """
        domWBLogButton点击事件，保存日志用

        :return:None
        """
        if os.path.exists('.\\log\\') is False:
            os.mkdir('.\\log\\')
        os.startfile('.\\log\\')

    def domWBReportButtonClicked(self):
        """
        domWBReportButton点击事件，导出质检报告用

        :return: None
        """
        try:
            reportOutputPath = QtWidgets.QFileDialog.getSaveFileName(self.domContentTab, u'导出质检报告', None, u".xlsx(*.xlsx)")
            if reportOutputPath[0] == '':
                return
            self.rdlg = reportoutputDlg.reportoutputdlg(self.domTableWidget,reportOutputPath[0])
            self.rdlg.exec_()
        except Exception as e:
            print('[mainui->domWBReportButtonClicked ERROR] ' + e.__str__())
            return

    def VerSectionThrDTexClicked(self, index):
        """
        根据所选column对thrDTexTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.thrDTexTableWidget.sortByColumn(index)

    def VerSectionThrDDevClicked(self, index):
        """
        根据所选column对thrDDevTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.thrDDevTableWidget.sortByColumn(index)

    def VerSectionStdRepeatClicked(self, index):
        """
        根据所选column对stdRepeatTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.stdRepeatTableWidget.sortByColumn(index)

    def VerSectionStdCodeClicked(self, index):
        """
        根据所选column对stdCodeTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.stdCodeTableWidget.sortByColumn(index)

    def VerSectionStdAttClicked(self, index):
        """
        根据所选column对stdAttTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.stdAttTableWidget.sortByColumn(index)

    def VerSectionDemJBClicked(self, index):
        """
        根据所选column对demTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.demJBTableWidget.sortByColumn(index)

    def VerSectionDemWBClicked(self, index):
        """
        根据所选column对demTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.demTableWidget.sortByColumn(index)

    def VerSectionClicked(self, index):
        """
        根据所选column对domTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.domTableWidget.sortByColumn(index)

    def VerSectionCClicked(self, index):
        """
        根据所选column对domCTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.domCTableWidget.sortByColumn(index)

    def VerSectionFormatClicked(self, index):
        """
        根据所选column对domFormatTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.domFormatTableWidget.sortByColumn(index)

    def VerSectionMatchClicked(self, index):
        """
        根据所选column对domMatchTableWidget进行排序

        :param index: 选定column的索引
        :return: None
        """
        self.domMatchTableWidget.sortByColumn(index)

    def ovrStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.label_ovr.setEnabled(True)
        else:
            self.label_ovr.setEnabled(False)

    def nodataStateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.label_nodata.setEnabled(True)
        else:
            self.label_nodata.setEnabled(False)

    def c254StateChanged(self,state):
        if state == QtCore.Qt.Checked:
            self.label_c254.setEnabled(True)
        else:
            self.label_c254.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "空间地理大数据整理与质检系统 -Alpha v0.2.0"))
        self.domButton.setText(_translate("MainWindow", "DOM质检模块"))
        self.demButton.setText(_translate("MainWindow", "DEM质检模块"))
        self.stdataButton.setText(_translate("MainWindow", "时空专题数据质检模块"))
        self.modelButton.setText(_translate("MainWindow", "3D模型质检模块"))
        self.domWBILabel.setText(_translate("MainWindow", "数据路径"))
        self.domWBIBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domWBParamsGBox.setTitle(_translate("MainWindow", "参数设置"))
        self.label.setText(_translate("MainWindow", "影像异常值设置"))
        self.label_2.setText(_translate("MainWindow", "近似异常值距离"))
        self.label_3.setText(_translate("MainWindow", "边缘修正因子"))
        self.label_4.setText(_translate("MainWindow", "内扩距离"))
        self.label_resform.setText(_translate("MainWindow", "影像输出格式为"))
        self.label_ovr.setText(_translate("MainWindow", "生成影像金字塔"))
        self.label_nodata.setText(_translate("MainWindow", "填充NoData区域为0值"))
        self.label_c254.setText(_translate("MainWindow", "只转换255至254（不做剔除任务）"))
        self.label_easyKill.setText(_translate("MainWindow", "简单去边模式"))
        self.label_easyColors.setText(_translate("MainWindow", "简单去边值"))
        self.label_easyNearDist.setText(_translate("MainWindow", "简单去边距离"))
        self.domWBOLabel.setText(_translate("MainWindow", "输出路径"))
        self.domWBOBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domWBReportButton.setText(_translate("MainWindow", "导出质检报告"))
        self.domWBLogButton.setText(_translate("MainWindow", "打开日志目录"))
        self.domWBStartButton.setText(_translate("MainWindow", "开始检查"))
        self.domContent.setTabText(self.domContent.indexOf(self.domWBTab), _translate("MainWindow", "边缘异常值检查"))
        self.domCILabel.setText(_translate("MainWindow", "索引数据路径"))
        self.domCIBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domCADLabel.setText(_translate("MainWindow", "行政区划路径"))
        self.domCADBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domCParamsGBox.setTitle(_translate("MainWindow", "参数设置"))
        self.label_6.setText(_translate("MainWindow", "市级行政区图层"))
        self.label_5.setText(_translate("MainWindow", "县级行政区图层"))
        self.domCOLabel.setText(_translate("MainWindow", "输出路径"))
        self.domCOBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domCReportButton.setText(_translate("MainWindow", "导出质检报告"))
        self.domCLogButton.setText(_translate("MainWindow", "打开日志目录"))
        self.domCStartButton.setText(_translate("MainWindow", "开始检查"))
        self.domContent.setTabText(self.domContent.indexOf(self.domCoverTab), _translate("MainWindow", "覆盖范围检查"))
        self.domFormatILabel.setText(_translate("MainWindow", "数据路径"))
        self.domFormatIBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domFormatParamsGBox.setTitle(_translate("MainWindow", "分辨率与坐标系参数"))
        self.domFormatPSettingButton.setText(_translate("MainWindow", "参数设置"))
        self.domFormatPResetButton.setText(_translate("MainWindow", "重置"))
        self.domFormatReportButton.setText(_translate("MainWindow", "导出质检报告"))
        self.domFormatLogButton.setText(_translate("MainWindow", "打开日志目录"))
        self.domFormatStartButton.setText(_translate("MainWindow", "开始检查"))
        self.domContent.setTabText(self.domContent.indexOf(self.domFormatTab), _translate("MainWindow", "分辨率与坐标系检查"))
        # self.domMatchIBrowerButton.setText(_translate("MainWindow", "浏览..."))
        # self.domMatchILabel.setText(_translate("MainWindow", "数据路径"))
        self.domMatchIndexLabel.setText(_translate("MainWindow", "索引路径"))
        self.domMatchPanLabel.setText(_translate("MainWindow", "影像数据所在盘符(输入大写字母即可)"))
        self.domMatchIndexBrowerButton.setText(_translate("MainWindow", "浏览..."))
        self.domMatchReportButton.setText(_translate("MainWindow", "导出质检报告"))
        self.domMatchLogButton.setText(_translate("MainWindow", "打开日志目录"))
        self.domMatchStartButton.setText(_translate("MainWindow", "开始检查"))
        self.domContent.setTabText(self.domContent.indexOf(self.domMatchTab), _translate("MainWindow", "影像与索引匹配检查"))
        self.demWBILabel.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.demWBIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.demWBParamsGBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "参数设置", None, -1))
        self.label_demvalue.setText(QtWidgets.QApplication.translate("MainWindow", "DEM有效值范围", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "到", None, -1))
        self.demWBOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        self.demWBOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.demWBReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.demWBLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.demWBStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.demContent.setTabText(self.demContent.indexOf(self.demWBTab),
                                   QtWidgets.QApplication.translate("MainWindow", "高程异常值检查", None, -1))
        self.demJBILabel_.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.demJBIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.demJBParamsGBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "参数设置", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "DEM有效值范围", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "到", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "高程突变阈值", None, -1))
        self.demJBOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        self.demJBOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.demJBReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.demJBLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.demJBStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.demContent.setTabText(self.demContent.indexOf(self.demJBTab),
                                   QtWidgets.QApplication.translate("MainWindow", "接边检查", None, -1))
        self.mainContent.setTabText(self.mainContent.indexOf(self.domContentTab), _translate("MainWindow", "DOM"))
        self.mainContent.setTabText(self.mainContent.indexOf(self.demContentTab), _translate("MainWindow", "DEM"))
        self.mainContent.setTabText(self.mainContent.indexOf(self.stdataContentTab), _translate("MainWindow", "STD"))
        self.stdAttILabel.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.stdAttIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdAttSelectLayersGBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "选择图层", None, -1))
        self.stdAttSelectGdbGBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "选择Gdb文件", None, -1))
        self.stdAttSelectGBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "选择字段验证规则", None, -1))
        self.stdAttSelectGBoxPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "导入规则库", None, -1))
        self.stdAttOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        self.stdAttOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdAttReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.stdAttLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.stdAttStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.stdContent.setTabText(self.stdContent.indexOf(self.stdAttTab),
                                   QtWidgets.QApplication.translate("MainWindow", "属性规范性检查", None, -1))
        self.stdCodeILabel.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.stdCodeIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdCodeOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        self.stdCodeOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdCodeReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.stdCodeLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.stdCodeStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.stdContent.setTabText(self.stdContent.indexOf(self.stdCodeTab),
                                   QtWidgets.QApplication.translate("MainWindow", "编码一致性检查", None, -1))
        self.stdRepeatILabel.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.stdRepeatIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdRepeatGroupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "图层字段参数设置", None, -1))
        self.stdRepeatGroupBoxlabel.setText(QtWidgets.QApplication.translate("MainWindow", "设置字段模糊匹配值", None, -1))
        self.stdRepeatOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        self.stdRepeatOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.stdRepeatReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.stdRepeatLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.stdRepeatStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.stdContent.setTabText(self.stdContent.indexOf(self.stdRepeatTab),
                                   QtWidgets.QApplication.translate("MainWindow", "名称重复性检查", None, -1))
        self.mainContent.setTabText(self.mainContent.indexOf(self.modelContentTab), _translate("MainWindow", "3D"))
        self.thrDTexILabel.setText(QtWidgets.QApplication.translate("MainWindow", "数据路径", None, -1))
        self.thrDTexIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.thrDTexTLabel.setText(QtWidgets.QApplication.translate("MainWindow", "贴图路径", None, -1))
        self.thrDTexTBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        # self.thrDTexOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出路径", None, -1))
        # self.thrDTexOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.thrDTexReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.thrDTexLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.thrDTexStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.thrDContent.setTabText(self.thrDContent.indexOf(self.tab_3),
                                    QtWidgets.QApplication.translate("MainWindow", "贴图完整性检查", None, -1))
        self.thrDDevILabel.setText(QtWidgets.QApplication.translate("MainWindow", "模型数据路径", None, -1))
        self.thrDDevIBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.thrDDevRLabel.setText(QtWidgets.QApplication.translate("MainWindow", "参照数据路径", None, -1))
        self.thrDDevRBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.thrDDevOLabel.setText(QtWidgets.QApplication.translate("MainWindow", "输出数据路径", None, -1))
        self.thrDDevOBrowerButton.setText(QtWidgets.QApplication.translate("MainWindow", "浏览...", None, -1))
        self.thrDDevReportButton.setText(QtWidgets.QApplication.translate("MainWindow", "导出质检报告", None, -1))
        self.thrDDevLogButton.setText(QtWidgets.QApplication.translate("MainWindow", "打开日志目录", None, -1))
        self.thrDDevStartButton.setText(QtWidgets.QApplication.translate("MainWindow", "开始检查", None, -1))
        self.thrDContent.setTabText(self.thrDContent.indexOf(self.tab_4),
                                    QtWidgets.QApplication.translate("MainWindow", "模型偏差检查", None, -1))
