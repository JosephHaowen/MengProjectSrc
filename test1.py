import os
import re

workingDir="C:\\Users\\ht398\\eMODIS\\"
os.chdir(workingDir)
file = open('emodis.txt','r')
for line in file:
    line = line.strip('\n')
    line1 =line.split('/')
    fileName = line1[9]
    fileName1 = os.path.splitext(fileName)[0]
    os.chdir(workingDir+"staging\\"+fileName1+"\\")
    L = os.listdir(os.getcwd())

    match = re.compile(r'(US_eMTH_NDVI.\d\d\d\d.\d\d\d-\d\d\d.QKM.VI_NDVI.\d\d\d.\d\d\d\d\d\d\d\d\d\d\d\d\d.tif)')
    l = re.findall(match,str(L))[0]
    dataFileDir = workingDir + "staging\\" + fileName1 + "\\" + l
