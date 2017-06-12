""" some function libs """

import random

from Py3dsMax import mxs


def create_teapot(offset=0):
    """docstring"""
    teapot = mxs.Teapot(radius=50, segments=10)
    teapot.pos = mxs.Point3(0, offset, offset * 2)
    mxs.completeRedraw()


def create_group():
    """ do sth """
    for i in range(10):
        create_teapot(i * 30)
    mxs.actionMan.executeAction(0, "310")  # Tools: Zoom Extents Selected


def delete_scene():
    """ pydoc """
    mxs.actionMan.executeAction(0, "40021")  # Selection: Select All
    for i in mxs.selection:
        # use mxs.Teapot refer to Teapot keyword in maxscript, cause there is
        # no such type in python
        if mxs.classOf(i) == mxs.Teapot and i.wireColor.B < 210:
            mxs.delete(i)


def convert_object():
    """ pydoc """
    current_selection = mxs.selection
    if len(current_selection) > 0:
        for m in current_selection:
            mxs.convertTo(m, mxs.editable_Poly)
            randomR = random.randint(10, 200)
            randomB = random.randint(10, 200)
            randomG = random.randint(10, 200)
            m.wireColor = mxs.color(randomR, randomG, randomB)
    else:
        mxs.messageBox("Nothing selected")
    mxs.completeRedraw()
