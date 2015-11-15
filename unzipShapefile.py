import os
import zipfile


workingDir = "C:\\Users\\ht398\\emodis\\clu\\"
os.chdir(workingDir)
for dirpath,directories, filenames in os.walk(workingDir):
    for filename in filenames:
        file=filename.split('_')
        foldername=file[3]
        foldername1 = filename.split('.zip')[0]
        foldername2 = foldername[0:2]
        print(workingDir +foldername2+"\\"+"clu\\"+foldername)
        with zipfile.ZipFile(workingDir +foldername2+"\\"+"clu\\"+filename,'r') as z:
            z.extractall(workingDir +foldername2+"\\"+"clu\\"+foldername1)
        os.remove(workingDir +foldername2+"\\"+"clu\\"+filename)

