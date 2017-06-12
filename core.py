#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Init 3dsMax GUI """

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from blurdev import gui

import funlibs


def launch_gui():
    """docstring"""
    # maybe there was a better way to avoid multiple instance ?
    for w in QtGui.QApplication.instance().topLevelWidgets():
        if w.__class__.__name__ == "MyToolWindow":
            w.close()

    inited_window = MyToolWindow.instance()
    inited_window.show()

    # if we use blurdev.launch method,
    # it will crash Qt window when we minimum 3dsMax window

    # blurdev.launch(MyToolWindow)


class MyToolWindow(gui.Window):
    """docstring for MyToolWindow"""

    def __init__(self, parent=None):
        super(MyToolWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        """docstring"""

        btnOne = QtGui.QPushButton("One")
        btnOne.setToolTip(u"这是用来干嘛的？")  # unicode test
        btnOne.clicked.connect(funlibs.create_group)
        btnTwo = QtGui.QPushButton("Two")
        btnTwo.clicked.connect(funlibs.delete_scene)
        btnThree = QtGui.QPushButton("Three")
        btnThree.clicked.connect(funlibs.convert_object)

        vBox = QtGui.QVBoxLayout()
        vBox.addWidget(btnOne)
        vBox.addWidget(btnTwo)
        vBox.addWidget(btnThree)

        groupBox = QtGui.QGroupBox("Group Title")
        groupBox.setAlignment(Qt.AlignHCenter)
        groupBox.setLayout(vBox)

        self.resize(200, 50)
        self.setWindowTitle("PyQtDemo")
        # self.setLayout(groupBox)
        self.setCentralWidget(groupBox)


if __name__ == '__main__':
    launch_gui()

    