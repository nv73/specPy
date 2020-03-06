# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specPy2_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_specPy(object):
    def setupUi(self, specPy):
        specPy.setObjectName("specPy")
        specPy.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(specPy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.dataView = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.dataView.setContentsMargins(0, 0, 0, 0)
        self.dataView.setObjectName("dataView")
        specPy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(specPy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        specPy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(specPy)
        self.statusbar.setObjectName("statusbar")
        specPy.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(specPy)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(specPy)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(specPy)
        QtCore.QMetaObject.connectSlotsByName(specPy)

    def retranslateUi(self, specPy):
        _translate = QtCore.QCoreApplication.translate
        specPy.setWindowTitle(_translate("specPy", "MainWindow"))
        self.menuFile.setTitle(_translate("specPy", "File"))
        self.actionLoad.setText(_translate("specPy", "Load..."))
        self.actionSave.setText(_translate("specPy", "Save..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    specPy = QtWidgets.QMainWindow()
    ui = Ui_specPy()
    ui.setupUi(specPy)
    specPy.show()
    sys.exit(app.exec_())

