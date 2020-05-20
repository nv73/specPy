import subprocess
import os.path

idlpath = "C:\\Program Files (x86)\\ReSe_Software_Win64\\IDL87\\bin\\bin.x86_64\\idlrt.exe"
atcorpath = "C:\\Program Files (x86)\\ReSe_Software_Win64\\atcor_4\\bin\\atcor4.sav"
inputfile = "D:\\Hyperspectral\\HSI_Test\\D076_MetroVan_TEST\\sess1\\2020-03-16_18-54-36_test\\2020-03-16_18-54-36_test-rect_img.bsq"
outputfile = "D:\\Hyperspectral\\HSI_Test\\D076_MetroVan_TEST\\sess1\\OUTPUT\\BatchTest\\testout.bsq"
logfile = "D:\\Hyperspectral\\HSI_Test\\D076_MetroVan_TEST\\sess1\\OUTPUT\\BatchTest\\log.txt"
elefile = "D:\\Hyperspectral\\HSI_Test\\D076_MetroVan_TEST\\sess1\\2020-03-16_18-54-36_test\\2020-03-16_18-54-36_test_img_res_ele.bsq"
factor = "2"

filecheck = [idlpath, atcorpath, inputfile, elefile]

for x in filecheck:
    
    if os.path.isfile(x):
        
        print("%s exists" % str(os.path.basename(x)))
        
    else:
        
        print("%s does not exist" % str(os.path.basename(x)))


b = "%s\idlrt.exe -rt='%s' -args %s R %s %s %s %s" % (idlpath, atcorpath, inputfile, outputfile, logfile, elefile, factor)

print(b)

