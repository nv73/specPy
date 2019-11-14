# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specPy.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_specPy(object):
    def setupUi(self, specPy):
        specPy.setObjectName(_fromUtf8("specPy"))
        specPy.resize(1016, 650)
        self.centralwidget = QtGui.QWidget(specPy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 751, 531))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.hsImage = QtGui.QGridLayout(self.gridLayoutWidget)
        self.hsImage.setObjectName(_fromUtf8("hsImage"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(780, 350, 231, 211))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.hsPlot = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.hsPlot.setObjectName(_fromUtf8("hsPlot"))
        self.hsImageSlider = QtGui.QSlider(self.centralwidget)
        self.hsImageSlider.setGeometry(QtCore.QRect(950, 110, 22, 160))
        self.hsImageSlider.setMaximum(222)
        self.hsImageSlider.setProperty("value", 0)
        self.hsImageSlider.setOrientation(QtCore.Qt.Vertical)
        self.hsImageSlider.setObjectName(_fromUtf8("hsImageSlider"))
        self.pixLocal = QtGui.QLabel(self.centralwidget)
        self.pixLocal.setGeometry(QtCore.QRect(100, 570, 301, 16))
        self.pixLocal.setObjectName(_fromUtf8("pixLocal"))
        self.pixValue = QtGui.QLabel(self.centralwidget)
        self.pixValue.setGeometry(QtCore.QRect(480, 570, 281, 16))
        self.pixValue.setObjectName(_fromUtf8("pixValue"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 570, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 570, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.imageShape = QtGui.QLabel(self.centralwidget)
        self.imageShape.setGeometry(QtCore.QRect(790, 30, 151, 16))
        self.imageShape.setText(_fromUtf8(""))
        self.imageShape.setObjectName(_fromUtf8("imageShape"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(922, 80, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.bandNumber = QtGui.QLabel(self.centralwidget)
        self.bandNumber.setGeometry(QtCore.QRect(940, 280, 41, 16))
        self.bandNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.bandNumber.setObjectName(_fromUtf8("bandNumber"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(780, 550, 231, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(780, 340, 231, 21))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(770, 350, 20, 211))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1000, 350, 20, 211))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 600, 751, 541))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.procView = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.procView.setObjectName(_fromUtf8("procView"))
        specPy.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(specPy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        specPy.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(specPy)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        specPy.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(specPy)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.menuFile.addAction(self.actionImport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(specPy)
        QtCore.QMetaObject.connectSlotsByName(specPy)

    def retranslateUi(self, specPy):
        specPy.setWindowTitle(_translate("specPy", "specPy", None))
        self.pixLocal.setText(_translate("specPy", "0", None))
        self.pixValue.setText(_translate("specPy", "0", None))
        self.label.setText(_translate("specPy", "Pixel Value", None))
        self.label_2.setText(_translate("specPy", "Local X, Y", None))
        self.label_3.setText(_translate("specPy", "Change Band", None))
        self.bandNumber.setText(_translate("specPy", "0", None))
        self.menuFile.setTitle(_translate("specPy", "File", None))
        self.actionImport.setText(_translate("specPy", "Import...", None))

