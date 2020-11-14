# -*- coding:utf-8 -*-
"""
main.py
~~~~~~~

主文件。

:copyright: (c) 2018 by Jinmeng Rao.
"""

import logging
import sys
from PySide2 import QtWidgets, QtGui
import multiprocessing as mp

from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

import qdarkstyle
import ui.mainui as mainui
import time


def main():
    """
    Application entry point
    """
    logging.basicConfig(level=logging.DEBUG)
    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)

    #splash
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("splash/splash_img.png"))
    splash.show()
    app.processEvents()
    time.sleep(3)
    window = QtWidgets.QMainWindow()
    # setup ui
    ui = mainui.Ui_MainWindow()
    ui.setupUi(window)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("splash/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    window.setWindowIcon(icon)
    window.setWindowTitle("空间地理大数据整理与质检系统 - Beta v 0.5.0")
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))
    # run
    window.show()
    splash.finish(window)
    app.exec_()


if __name__ == "__main__":
    mp.freeze_support()
    main()