from PyQt4 import QtGui,QtCore

from templates import ui_plotTemplate as plotTemplate
from utilities.expeyesWidgets import expeyesWidgets


import sys,time,functools

class AppWindow(QtGui.QWidget, plotTemplate.Ui_Form,expeyesWidgets):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.p = kwargs.get('handler',None)
		self.widgetLayout.setAlignment(QtCore.Qt.AlignTop)

		
		# ADD AN OSCILLOSCOPE PLOT TO THE plotLayout
		# This assumes self.plotLayout, and makes a dictionary self.curves with keys 'A1','A2','A3','MIC'
		#You should be able to access after executing this function. self.myCurves is a dictionary of curves with 4 Elements
		self.SCOPEPLOT(['A1','A2','A3','MIC','A1+A2'])   #You can also make up your own curve names.

		#Add a spacer
		self.SPACER(20)

		# ADD A SINE WIDGET SLIDER WITH NUMBERIC INPUT to the widgetLayout
		self.SINE()
		
		
		self.setInterval(100,self.tmp)
		#self.setTimeout(1000,functools.partial(self.capture,'A1',200,3),self.update)

	def tmp(self):
		self.CAPTURE()
		print ('capturing')
	
