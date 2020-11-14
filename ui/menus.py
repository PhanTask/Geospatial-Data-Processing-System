# -*- coding:utf-8 -*-
"""
menus.py
~~~~~~~~

界面中用到的菜单栏集合。

:copyright: (c) 2018 by Jinmeng Rao.
"""
from PySide2.QtWidgets import QMenu

def domTableWidgetMenu(domTableWidget, pos):
    row_num = -1
    for i in domTableWidget.selectionModel().selection().indexes():
        row_num = i.row()
    menu = QMenu()
    item1 = menu.addAction(u"打开文件所在位置")
    item2 = menu.addAction(u"选项二")
    action = menu.exec_(domTableWidget.mapToGlobal(pos))
    if action == item1:
        print
        u'您选了选项一，当前行文字内容是：', domTableWidget.item(row_num, 1).text()

    elif action == item2:
        print
        u'您选了选项二，当前行文字内容是：', domTableWidget.item(row_num, 1).text()
    else:
        return