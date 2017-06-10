""" Py3dsMaxDemo """
import sys
import os

try:
	import core
except ImportError:
	# append current path into PYTHONPATH, in case some import issue
	dirName = os.path.dirname(__file__)
	sys.path.append(dirName)
	import core


__version__ = "0.1.0"

core.launchGUI()