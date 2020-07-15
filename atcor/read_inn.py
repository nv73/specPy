# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:29:21 2020

@author: nick.viner
"""
import pandas as pd
import csv

class pyInn(object):
    
    def __init__(self, filepath):
        
        self.filepath = filepath
        self.inn = pd.read_csv(self.filepath, header=None, sep="^")
        
        #Line 0
        self.date = self.inn.iloc[0][0][:8]
        
        #Line 1
        self.scaleFactor = [x for x in self.inn.iloc[1][0][0:17].split(" ") if x != ''][0]
        
        #Line 2
        self.pixelSize = [x for x in self.inn.iloc[2][0][0:17].split(" ") if x != ''][0]
        
        #Line 3
        self.sensor = self.inn.iloc[3][0]
        
        #Line 4
        self.gainSettings = self.inn.iloc[4][0][5:12]
        
        #Line 5
        self.calibrationFile = self.inn.iloc[5][0]
        
        #Line 6
        self.scanAngleFile = self.inn.iloc[6][0]
        
        #Line 7
        #0=[m], 1=[dm], 2=[cm]
        self.demUnit = self.inn.iloc[7][0][8:9]
        self.iemiss = self.inn.iloc[7][0][:6]
        
        #Line 8
        self.elevationFile = self.inn.iloc[8][0]
        
        #Line 9
        self.slopeFile = self.inn.iloc[9][0]
        
        #Line 10
        self.aspectFile = self.inn.iloc[10][0]
        
        #Line 11
        self.skyviewFile = self.inn.iloc[11][0]
        
        #Line 12
        self.aerosolType = self.inn.iloc[12][0]
        
        #Line 13
        self.adjacencyRange = [x for x in self.inn.iloc[13][0][0:17].split(" ") if x != ''][0]
        
        #Line 14
        self.visibility = [x for x in self.inn.iloc[14][0][0:17].split(" ") if x != ''][0]
        
        #Line 15
        self.meanGroundElevation= [x for x in self.inn.iloc[15][0][0:17].split(" ") if x != ''][0]
        
        #Line 16
        self.solarZenith = [x for x in self.inn.iloc[16][0][0:17].split(" ") if x != ''][0]
        self.solarAzimuth = [x for x in self.inn.iloc[16][0][0:17].split(" ") if x != ''][1]

        #Line 17
        self.flightAltitude = [x for x in self.inn.iloc[17][0][0:18].split(" ") if x != ''][0]
        self.flightHeading = [x for x in self.inn.iloc[17][0][0:18].split(" ") if x != ''][1]
        
        #Line 18
        #Image processing steps to be used
        #dtype: binary
        self.npref = self.inn.iloc[18][0][3]
        self.iwaterwv = self.inn.iloc[18][0][7]
        self.haze = self.inn.iloc[18][0][11]
        self.iwat_shd = self.inn.iloc[18][0][15]
        self.ksolflux = self.inn.iloc[18][0][19]
        self.ishadow = self.inn.iloc[18][0][23]
        self.icl_shadow = self.inn.iloc[18][0][27]
        
        #Line 19
        self.itriang =  self.inn.iloc[19][0][3]
        self.ratio_red_nirswir = self.inn.iloc[19][0][7:12]
        self.ratio_blue_red = self.inn.iloc[19][0][15:20]
                
        #Line 20
        self.ibrdf = self.inn.iloc[20][0][3]
        self.beta_thr = self.inn.iloc[20][0][8:12]
        self.thr_g = self.inn.iloc[20][0][16:21]
                
        #Line 21
        #lai model
        self.use_lai = self.inn.iloc[21][0][3]
        self.a0_vi = self.inn.iloc[21][0][7:12]
        self.a1_vi = self.inn.iloc[21][0][15:20]
        self.a2_vi = self.inn.iloc[21][0][23:28]
        
        #Line 22
        #FPAR model
        self.C = self.inn.iloc[22][0][7:12]
        self.A = self.inn.iloc[22][0][15:20]
        self.B = self.inn.iloc[22][0][23:28]
        
        #Line 23
        #flat terrain
        self.t_airF = self.inn.iloc[23][0][8:12]
        self.emiss_air = self.inn.iloc[23][0][15:20]
        
        #Line 24
        #rugged terrain
        self.t_airR = self.inn.iloc[24][0][1:5]
        self.z0_ref = self.inn.iloc[24][0][7:11]
        self.tgradient = self.inn.iloc[24][0][12:16]
        self.p_wv = self.inn.iloc[24][0][17:21]
        self.zh_pwv = self.inn.iloc[24][0][23:26]
        
        #Line 25
        self.ihot_mask = self.inn.iloc[25][0][3]
        self.ihot_dynr= self.inn.iloc[25][0][7]
        
        #Line 26
        self.iclshad_mask = self.inn.iloc[26][0][2]
        self.thr_shad = self.inn.iloc[26][0][4:11]
        self.phi_unscl_max = self.inn.iloc[26][0][12:19]
        self.phi_scl_min = self.inn.iloc[26][0][22:26]
        self.istretch_type = self.inn.iloc[26][0][29]
        
        #Line 27
        self.vapourRetrieval940 = [x for x in self.inn.iloc[27][0][0:31].split(" ") if x != '']
        
        #Line 28
        self.vapourRetrieval1130 = [x for x in self.inn.iloc[28][0][0:31].split(" ") if x != '']
        
        #Line 29
        self.thermalVapourRetrieval = [x for x in self.inn.iloc[29][0][0:31].split(" ") if x != '']
                
        #Line 30
        self.e_water = self.inn.iloc[30][0][2:7]
        self.e_veget = self.inn.iloc[30][0][9:14]
        self.e_soil = self.inn.iloc[30][0][16:21]
        self.e_sand = self.inn.iloc[30][0][23:28]
        
        #Line 31
        self.iwv_model = self.inn.iloc[31][0][5]
        
        #Line 32
        self.icirrus = self.inn.iloc[32][0][5]
        
        #Line 33
        self.irrad0 = self.inn.iloc[33][0][5]
        
        
def read_inn_file(filepath):
    
    inn = pd.read_csv(filepath, header=None, sep="^")



