# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:07:23 2020

@author: nick.viner
"""

#Generate opt files from template

import pandas as pd
import os

print(os.getcwd())

ignoreFile = ['CAL', 'DEM', 'NAV', 'OUTPUT', 'OPT', 'FOV_sn351020_20190530.txt', 'AisaFENIX_SN351020.lut', 'optGen.py']

def gen_opt(file_template):
    
    opt = pd.read_csv(file_template, header=None, sep = '\n')
    
    opt = opt[0].str.split('   ', expand = True)
    
    ignoreFile.append(file_template)
    
    fileList = [x for x in os.listdir('.') if x not in ignoreFile]
    
    cwd = os.getcwd()
    
    for x in fileList:
        
        tempDf = opt
        
        tempDf.iloc[0][1] = cwd + "\\" + x + "\\" + x + ".raw"
        tempDf.iloc[5][1] = cwd + "\\" + x + "\\" + x + ".nav"
        tempDf.iloc[23][1] = cwd + "\\OUTPUT\\" + x + "-rect.dat"
        
        tempDf.to_csv(cwd + "\\OPT\\" + x + ".opt", index = False, header = False, sep = " ")
        
    
gen_opt("2020-03-16_18-42-04_test.opt")


