""" some function libs """

import random

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
		if mxs.classOf(i) == mxs.Teapot and i.wireColor.B < 210: # use mxs.Teapot refer to Teapot keyword in maxscript, cause there is no such type in python
			mxs.delete(i) 


def convertObject():
	currentSelection = mxs.selection
	if len(currentSelection) > 0:
		for m in currentSelection:
			mxs.convertTo(m, mxs.editable_Poly)
			randomR = random.randint(10,200)			
			randomB = random.randint(10,200)
			randomG = random.randint(10,200)
			m.wireColor = mxs.color(randomR, randomG, randomB)
	else:
		mxs.messageBox("Nothing selected")
	mxs.completeRedraw()