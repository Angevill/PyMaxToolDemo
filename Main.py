#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from blurdev import gui
import blurdev

from Py3dsMax import mxs

def createTeapot(offset=0):
	teapot = mxs.Teapot(radius=50, segments=10)
	teapot.pos = mxs.Point3(0, offset, offset*2)
	mxs.completeRedraw()



def createGroup():
	""" do sth """
	for i in range(10):
		createTeapot(i*30)
	mxs.actionMan.executeAction(0, "310") # Tools: Zoom Extents Selected

def deleteScene():
	mxs.actionMan.executeAction(0, "40021") # Selection: Select All
	for i in mxs.selection: 
		if mxs.classOf(i) == mxs.Teapot and i.wireColor.B < 50: # use mxs.Teapot refer to Teapot keyword in maxscript, cause there is no such type in python
			mxs.delete(i) 


def convertObject():
	currentSelection = mxs.selection
	if len(currentSelection) > 0:
		for m in currentSelection:
			mxs.convertTo(m, mxs.editable_Poly)
			m.wireColor = mxs.color(0,50,50)
	else:
		mxs.messageBox("Nothing selected")


class MyToolWindow(gui.Window):
	"""docstring for MyToolWindow"""
	def __init__(self, parent=None):
		super(MyToolWindow, self).__init__()
		self.initUI()

	def initUI(self):
		
		btnOne = QtGui.QPushButton("One")
		btnOne.setToolTip(u"这是用来干嘛的？") #unicode test
		btnOne.clicked.connect(createGroup)
		btnTwo = QtGui.QPushButton("Two")
		btnTwo.clicked.connect(deleteScene)
		btnThree = QtGui.QPushButton("Three")
		btnThree.clicked.connect(convertObject)


		
		vBox = QtGui.QVBoxLayout()
		vBox.addWidget(btnOne)
		vBox.addWidget(btnTwo)
		vBox.addWidget(btnThree)


		groupBox = QtGui.QGroupBox("Group Title")
		groupBox.setAlignment(Qt.AlignHCenter)
		groupBox.setLayout(vBox)

		self.resize(200,50)
		self.setWindowTitle("PyQtDemo")
		#self.setLayout(groupBox)
		self.setCentralWidget(groupBox)


def launchGUI():
	# maybe there was a better way to avoid multiple instance ?
	for w in QtGui.QApplication.instance().topLevelWidgets():
		if w.__class__.__name__ == "MyToolWindow":
			w.close()

	initedWindow = MyToolWindow.instance()
	initedWindow.show()

	# if we use blurdev.launch method, it will crash Qt window when we minimum 3dsMax window
	#blurdev.launch(MyToolWindow)
	

if __name__ == '__main__':
	launchGUI()
	




		