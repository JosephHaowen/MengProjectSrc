import urllib2
import shutil
import os
import popen2
import zipfile
import datetime
import re
import us
import connDatabase
import subprocess
import arcpy
from arcpy import env


env.workspace = "E:\\ht398\\eMODIS"
workingDir="E:\\ht398\\eMODIS\\"
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("GeoStats")
os.chdir(workingDir)
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, "https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/", "woodardjoshua@gmail.com", "USGSwoodard14")
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
opener.open("https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/")
urllib2.install_opener(opener)

#TODO: now loop over all year directories for  *.US_eMTH_NDVI.YYYY.DDD-DDD.QKM.COMPRES...zip files
#for example .../TERRA/2014/US_eMTH_NDVI.2014.365-006.QKM.COMPRES.*
file = open('emodis.txt','r')
year = "1999"
DayYearEnd1 = ['363', '361', '360', '364', '363', '361', '360', '365', '364', '362', '361', '360', '366', '364', '363', '299']
for line in file:
    line = line.strip('\n')
    line1 =line.split('/')
    fileName = line1[9]
    fileName1 = os.path.splitext(fileName)[0]
    req =urllib2.urlopen(line)
    with open(workingDir +"staging\\"+fileName, 'wb') as fp:
        shutil.copyfileobj(req, fp)
    fp.close()
    with zipfile.ZipFile(workingDir +"staging\\"+fileName,'r') as z:
        z.extractall(workingDir +"staging\\"+fileName1)
    os.remove(workingDir +"staging\\"+fileName)
    z.close()

    title=fileName.split('.')
    year1=title[1]
    temday = title[2].split('-')
    DateStart = temday[0]                                                   #DataStart is the attribute of DateStart
    DateEnd = temday[1]

    if year!=year1:
        year = year1
        DayYearStart = DateStart
    DayYearEnd = DayYearEnd1[int(year)-2000]

    day = datetime.date(int(year),1,1) + datetime.timedelta(days = (int(DateStart) - 1) )
    monthNum = day.month
    DayOfMonth = day.day

    os.chdir(workingDir+"staging\\"+fileName1)
    L = os.listdir(os.getcwd())
    match = re.compile(r'(US_eMTH_NDVI.\d\d\d\d.\d\d\d-\d\d\d.QKM.VI_NDVI.\d\d\d.\d\d\d\d\d\d\d\d\d\d\d\d\d.tif)')
    l = re.findall(match,str(L))[0]
    dataFileDir = workingDir + "staging\\" + fileName1 + "\\" + l
    AggLevel = "CLU"
    os.chdir(workingDir+"clu\\")
    for dirpath,directories, filenames in os.walk(workingDir+"clu\\"):
        for filename in directories:
            if len(filename) == 18:
                county = (filename.split('_')[3])[0:2]
                countyFIPS = (filename.split('_')[3])[2:5]
                stateFIPS = us.states.lookup((filename.split('_')[3])[0:2]).fips
                FIPS = stateFIPS + countyFIPS
                shapefileDir = workingDir+"clu\\"+county+"\\"+"clu\\"+filename+"\\"+filename+".shp"
                

                Layer = arcpy.mapping.Layer(dataFileDir)
                arcpy.gp.ZonalStatisticsAsTable_sa(shapefileDir,"FID",dataFileDir,"ZonalStUS.dbf","DATA","MEAN")
                

                dbfpath = "E:\\ht398\\eMODIS\\ZonalStUS.dbf"
                db = dbf.Dbf(dbfpath, new = False)

                for tuple in db:
                   CLUID = tuple['FID_']
                   value = tuple['MEAN']
                   FIPS = FIPS + CLUID
                   connDatabase.loadData(year,DateStart,DateEnd,DayYearStart,DayYearEnd,monthNum,DayOfMonth,AggLevel,countyFIPS,stateFIPS,FIPS,CLUID,value)

                os.remove(workingDir+"ZonalStUS.dbf")



#now process by different levels of aggregation (state, county, district, township, CLU etc.) and pack in database
#Create and fill table "dbo.eMODIS_NDVI"
#fields of table eMODIS_NDVI should be Year, Month, Day, Date, AggLevel, Freq ("weekly"), Sensor ("Terra") , Value
#file to process is US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif

#Layer = arcpy.mapping.Layer( workingDir +"staging\US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif")
#Raster = arcpy.Raster(workingDir +"staging\US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif")


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "tl_2015_us_county", "US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif"
#arcpy.gp.ZonalStatisticsAsTable_sa(env.workspace +"\\tl_2015_us_county\\tl_2015_us_county.shp","GEOID",env.workspace +"\\staging\\US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif","ZonalStUS.dbf","DATA","MEAN")


#TODO: delete out stagig files then loop to next
#arcpy.Delete_management() #stuff to delete here


#TODO: stack and pack dbf results into database
