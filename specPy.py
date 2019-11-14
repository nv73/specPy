#With pip, install the following libraries:
#python -m pip install PyQt4, OpenGL, PIL, matplotlib, numpy, pandas, spectral

#Qt Libraries
import specPy_ui
from PyQt4 import QtCore, QtGui, QtOpenGL
from OpenGL import GL
from PIL import Image, ImageQt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvasQt
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

#System
import sys

#Data management
import numpy as np
import pandas as pd
from math import radians, degrees

#Spectral libraries
import spectral.io.envi as envi

class specPy_Form(QtGui.QMainWindow, specPy_ui.Ui_specPy):

    def __init__(self, parent=None):

        super(specPy_Form, self).__init__(parent)

        #Initialize various widgets in the UI

        self.setupUi(self)

        self.figure = Figure()
        
        self.figureCanvas = FigureCanvasQt(self.figure)

        self.drawArea = canvas(plot=self.figureCanvas, figure=self.figure)
        
        self.hsImage.addWidget(self.drawArea)

        self.hsPlot.addWidget(self.figureCanvas)

        self.actionImport.triggered.connect(self.importSpectralData)

        #Other stuff

        self.active_band = 0

        #self.hsImageSlider.valueChanged.connect(self.set_band)
        self.hsImageSlider.sliderReleased.connect(self.set_band)
        
        self.hsArray = None

        self.hsImage = None
        
        self.hsGeo = {}

        isEmpty = True
        

    #Change the class variable responsible for which band is being displayed in the GUI
    #This function is called whenever the qslider is released
    def set_band(self):

        #Assign the band value to the slider value
        self.active_band = int(self.hsImageSlider.value())

        #Display the current band value on a label
        self.bandNumber.setText(str(self.active_band))

        #Only change the active band if there is an image present
        if self.isEmpty == False:

            self.changeBand(self.active_band)

    #Runs 2 qfiledialogs allowing for the selection of both a
    #hyperspectral header and img file.
    def importSpectralData(self):

        headerFilePath = QtGui.QFileDialog.getOpenFileName(self, 'Select header file to open...',
                                                           '', ".hdr(*.hdr)")
        
        imageFilePath = QtGui.QFileDialog.getOpenFileName(self, 'Select image file to open...',
                                                          '', "all(*);;.img(*.img);;.bip(*.bip)")

        self.hsImage = envi.open(str(headerFilePath), str(imageFilePath))


        #Generate a numpy nd array of the hyperspectral dataset.
        hsArray = self.hsImage.load()

        #Assign a class variable to the array
        self.hsArray = hsArray

        #Also provide the child graphicsview widget with access to the array
        self.drawArea.img = hsArray

        #get the dimensions of the nd array.
        x,y,z = hsArray.shape

        #Slice the array to retrieve the band 0 layer
        hsArray = hsArray[:,:,0]

        hsArray = np.reshape(hsArray, (x,y))

        self.drawArea.display_Image_From_Array(hsArray, True)

        self.isEmpty = False

    #Change the currently displayed band
    def changeBand(self, band=0):

        hsArray = self.hsArray[:,:,band]
        
        x,y,z = hsArray.shape
        
        self.imageShape.setText(str(x) + ', ' + str(y) + ', ' + str(z))
        
        hsArray = np.reshape(hsArray, (x,y))

        self.drawArea.display_Image_From_Array(hsArray, True)

class canvas(QtGui.QGraphicsView):

    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, img=None, plot=None, figure=None):

        super(canvas, self).__init__()

        self.img = img

        self.band = 0

        self.arr = None

        self.photo = QtGui.QGraphicsPixmapItem()

        self.scene = QtGui.QGraphicsScene(self)

        self.scene.addItem(self.photo)

        self.setScene(self.scene)

        self.zoom = 0

        self.empty = True

        self.plot = plot
        
        self.figure = figure

        self.setMouseTracking(True)
        
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)

    def plot_band(self, xval, yval, figureCanvas, figure, arr):

        ax = figure.add_subplot(111)
        
        ax.clear()
        
        ax.plot(arr[int(xval),int(yval)])

        ax.axvline(x=self.parent().parent().parent().active_band,color='r')

        figureCanvas.draw()
            
    def wheelEvent(self, event):

        if not self.empty:

            oldPos = self.mapToScene(event.pos())

            if event.delta() > 0:

                factor = 1.25
                self.zoom += 1

            else:

                factor = 0.8

                self.zoom -= 1

            self.scale(factor, factor)

            newPos = self.mapToScene(event.pos())

            delta = newPos - oldPos

            self.translate(delta.x(), delta.y())

    def mousePressEvent(self, event):

        if self.photo.isUnderMouse():

            self.photoClicked.emit(QtCore.QPoint(event.pos()))

        coords = self.mapToScene(event.x(), event.y())

        x= int(coords.x())

        y=int(coords.y())

        super(canvas, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):

        coords = self.mapToScene(event.x(), event.y())

        x = int(coords.x())
        y = int(coords.y())

        self.parent().parent().parent().pixLocal.setText(str(coords.x()) + ', ' + str(coords.y()))

        try:

            if self.photo.isUnderMouse():

                self.plot_band(int(coords.y()), int(coords.x()), self.plot, self.figure, self.img)

                self.parent().parent().parent().pixValue.setText(str(self.arr[int(coords.y()), int(coords.x())]))

        except Exception as e:

            pass

        super(canvas, self).mouseMoveEvent(event)

    def enable_Drag(self, enabled=True):

        if enabled == True:

            self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)

        else:

            self.setDragMode(QtGui.QGraphicsView.NoDrag)

    def image_to_Pixmap(self, img):

        imgQt = QtGui.QImage(ImageQt.ImageQt(img))

        Qpm = QtGui.QPixmap.fromImage(imgQt)

        return(Qpm)

    def display_Image_From_Array(self, arr, normalized=False):

        self.arr = arr
        a = arr

        if normalized == True:

            a = self.normalize(a)

        #Modes:
        #RGB = 3x8 bit pixels, full colour
        #L = 8 bit pixels, B&W
        img = Image.fromarray((a * 255).astype('uint8'), mode='L')
        #img = Image.fromarray((a * 255).astype('uint8'), mode='RGB')

        qpm = self.image_to_Pixmap(img)

        self.photo.setPixmap(qpm)

        self.enable_Drag()

        self.empty = False
        
    def normalize(self, inputArr):

        arr = inputArr
        
        arr_min, arr_max = np.amin(arr), np.amax(arr)

        for i, val in enumerate(arr):

            arr[i] = (val - arr_min) / (arr_max - arr_min)

        return(arr)

    def draw_Point(self, x, y):

        pointItem = QtGui.QGraphicsTextItem()
        pointItem.setPlainText('+')
        pointItem.setPos(x, y)
        self.scene.addItem(pointItem)

    
app = QtGui.QApplication(sys.argv)

form = specPy_Form()

form.show()

app.exec_()
