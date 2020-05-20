# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:36:33 2020

@author: nickv
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navigationToolbar
from matplotlib.figure import Figure

from sklearn.cluster import KMeans as kmeans

import sys

import numpy as np
import pandas as pd
from math import radians, degrees

import spectral.io.envi as envi

import gdal
import pyproj

import specPy2_ui

from geoCanvas import geoCanvas

class specPy2_Form(QtWidgets.QMainWindow, specPy2_ui.Ui_specPy):
    
    def __init__(self, parent=None):
        
        super().__init__()
        
        self.setupUi(self)
        
        self.geoCanvas = geoCanvas()
        
        self.dataView.addWidget(self.geoCanvas)
        
        self.hsi = self.load_hsi('samson_1.img', 'samson_1.img.hdr')
        
        hsi_slice = self.hsi[:,:,45]
        x,y,z = hsi_slice.shape
        hsi_slice = np.reshape(hsi_slice, (x,y))
        
        self.geoCanvas.displayArray(hsi_slice)
        
        #self.geoCanvas.importGeoImage('cea.tif')
        
    def load_hsi(self, file, header):
        
        hsi_raw = envi.open(header, file)
        
        return(hsi_raw.load())
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    form = specPy2_Form()

    form.show()

    app.exec_()
