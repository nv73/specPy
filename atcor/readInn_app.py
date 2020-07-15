# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:08:25 2020

@author: nick.viner
"""

from read_inn import pyInn
from PyQt5 import QtCore, QtGui, QtWidgets
import readInn_ui
import sys
import os 

class readInn_Form(QtWidgets.QMainWindow, readInn_ui.Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super().__init__()
        
        self.setupUi(self)
        
        self.inn = None
        
        self.atm_databases = []
        
        self.get_atm_database()
        
        self.actionLoad_inn.triggered.connect(self.import_inn_file)
        
    def import_inn_file(self):
        
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select INN file...', '', ".inn(*.inn)")
        
        inn = pyInn(str(fname[0]))
        
        self.inn = inn
        
        self.set_gui_params()
    
    def set_gui_params(self):
        
        self.fileNameEdit.setText(self.inn.filepath)
        
        self.fileDateEdit.setText(self.inn.date)
        
        self.sensorFileEdit.setText(self.inn.sensor)
        
        self.calibrationFileEdit.setText(self.inn.calibrationFile)
        
        self.scanAngleFileEdit.setText(self.inn.scanAngleFile)
        
        self.elevationFileEdit.setText(self.inn.elevationFile)
        
        self.slopeFileEdit.setText(self.inn.slopeFile)
        
        self.aspectFileEdit.setText(self.inn.aspectFile)
        
        self.skyviewFileEdit.setText(self.inn.skyviewFile)
        
        self.solarZenithEdit.setText(self.inn.solarZenith)
        
        self.solarAzimuthEdit.setText(self.inn.solarAzimuth)
        
        self.pixelSizeEdit.setText(self.inn.pixelSize)
        
        self.scaleFactorEdit.setText(self.inn.scaleFactor)
        
        self.gainEdit.setText(self.inn.gainSettings)
        
        self.heightUnitEdit.setText(self.inn.demUnit)
        
        self.surfEmissivityEdit.setText(self.inn.iemiss)
        
        self.adjacencyRangeEdit.setText(self.inn.adjacencyRange)
        
        self.visibilityEdit.setText(self.inn.visibility)
        
        self.meanElevationEdit.setText(self.inn.meanGroundElevation)
        
        self.flightAltitudeEdit.setText(self.inn.flightAltitude)
        
        self.flightHeadingEdit.setText(self.inn.flightHeading)
        
        self._set_combo_index(self.visibilityCombo, self.inn.npref)
        
        self._set_combo_index(self.vapourCorrectionCombo, self.inn.iwaterwv)
        
        self._set_combo_index(self.hazeRemovalCombo, self.inn.haze)
        
        self._set_combo_index(self.waterShadowsCombo, self.inn.iwat_shd)
        
        self._set_combo_index(self.cloudShadowsCombo, self.inn.icl_shadow)
        
        self._set_combo_index(self.solarFluxCombo, self.inn.ksolflux)
        
        self._set_combo_index(self.castShadowCombo, self.inn.ishadow)
        
        self._set_combo_index(self.visInterpCombo, self.inn.itriang)
        
        self.surRefRedThermEdit.setText(self.inn.ratio_red_nirswir)
        
        self.surfRefBlueRedEdit.setText(self.inn.ratio_blue_red)
        
        brdfTypes = {'0':0, '1':1, '2':2, '11':3, '12':4, 
                     '21':5, '22':6, '30':7, '40':8, '40':9, 
                     '41':10, '50':11, '51':12, '52':13}
        
        self.brdfCorrectionCombo.setCurrentIndex(brdfTypes[self.inn.ibrdf])
        
        self.iluAngleEdit.setText(self.inn.beta_thr)
        
        self.brdfCorrBoundsEdit.setText(self.inn.thr_g)
        
        self._set_combo_index(self.useLaiCombo, self.inn.use_lai)
        
        self.a0Edit.setText(self.inn.a0_vi)
        
        self.a1Edit.setText(self.inn.a1_vi)
        
        self.a2Edit.setText(self.inn.a2_vi)
        
        self.aEdit.setText(self.inn.A)
        
        self.bEdit.setText(self.inn.B)
        
        self.cEdit.setText(self.inn.C)
                
        self._set_combo_index(self.wvModelCombo, self.inn.iwv_model) 
        
        self._set_combo_index(self.useLaiCombo, self.inn.use_lai)
        
        wv_model_params = {'0':"0 - None",
                           '1':"1 - No Band Regression",
                           '2':"2 - Band Regression"}
        
        self._set_combo_index(self.wvModelCombo, wv_model_params[self.inn.iwv_model])
        
        print(self.inn.vapourRetrieval940)
        print(self.inn.vapourRetrieval1130)
        
        #I accidentally set the variable names to 830 rather than 940.
        #It is an error I don't feel like fixing
        self.wv830LeftWindow1Edit.setText(self.inn.vapourRetrieval940[0])
        self.wv830RightWindow1Edit.setText(self.inn.vapourRetrieval940[1])
        self.wv830AbsorptionRightEdit.setText(self.inn.vapourRetrieval940[2])
        self.wv830AbsorptionLeftEdit.setText(self.inn.vapourRetrieval940[3])
        self.wv830LeftWindow2Edit.setText(self.inn.vapourRetrieval940[4])
        self.wv830RightWindow2Edit.setText(self.inn.vapourRetrieval940[5])
        
        self.wv1130LeftWindow1Edit.setText(self.inn.vapourRetrieval1130[0])
        self.wv1130RightWindow1Edit.setText(self.inn.vapourRetrieval1130[1])
        self.wv1130AbsorptionRightEdit.setText(self.inn.vapourRetrieval1130[2])
        self.wv1130AbsorptionLeftEdit.setText(self.inn.vapourRetrieval1130[3])
        self.wv1130LeftWindow2Edit.setText(self.inn.vapourRetrieval1130[4])
        self.wv1130RightWindow2Edit.setText(self.inn.vapourRetrieval1130[5])
        
        self.sandEmissEdit.setText(self.inn.e_sand)
        self.waterEmissEdit.setText(self.inn.e_water)
        self.soilEmissEdit.setText(self.inn.e_soil)
        self.vegEmissEdit.setText(self.inn.e_veget)
        
        self.aTempEdit.setText(self.inn.t_airR)
        self.refEleEdit.setText(self.inn.z0_ref)
        self.tempGradEdit.setText(self.inn.tgradient)
        self.wvpEdit.setText(self.inn.p_wv)
        self.scaleHeightEdit.setText(self.inn.zh_pwv)
        
    def get_atm_database(self):
        
        fpath = r"C:\Program Files (x86)\ReSe_Software_Win64\atcor_4\atm_database"
        
        for f in os.listdir(fpath):
            
            if ".bp7" in f:
            
                self.atm_databases.append(f)
                
                self.atmDatabaseCombo.addItem(f)
        
    def _set_combo_index(self, combobox, value):
        
        index = combobox.findText(str(value), QtCore.Qt.MatchFixedString)
            
        combobox.setCurrentIndex(index)
        
app = QtWidgets.QApplication(sys.argv)

window = readInn_Form()

window.show()

app.exec_()
