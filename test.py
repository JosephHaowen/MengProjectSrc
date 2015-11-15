import os
import datetime
import urllib2


# 1) DateStart (first day of 10 year period, SQL FOmrat)
# 2) DateEnd (the last day of 10 day period SQL Format)
# 3) Year (int)
# 4) MonthNum (int)
# 5) DayOfMonth (int)
# 6) DayofYearStart (int, for example, Feb 1st would be 32)
# 7) DayofYearEnd
# 8) AggLevel (aggregation level: CLU, township, county, district, state)
# 9) CountyFIPS
# 10) StateFIPS
# 11) FIPS (5 digit FIPS if county AggLevel then = StateFIPS*1000+CountyFips; if State then StateFIPS*1000+999; if district, then StateFIPS*1000+District code (e.g. 010, 020, etc.); if township or CLU then the 5 digit fips of the county it is in)
# 12) Township ID (from Tiger Line Township boundary files)
# 13) CLU ID (from CLU files)
# 14) Value: The processed value (mean) that is generated from the spatial processing in the .py program
workingDir="C:\\Users\\ht398\\eMODIS\\"
os.chdir(workingDir)
file = open('emodis.txt','r')

file = open('emodis.txt','r')
year = "1999"
for line in file:
    line = line.strip('\n')
    line1 =line.split('/')
    fileName = line1[9]
    fileName1 = os.path.splitext(fileName)[0]
    print(fileName1)
    # req =urllib2.urlopen(line)
    # with open(workingDir +"staging\\"+fileName, 'wb') as fp:
    #     shutil.copyfileobj(req, fp)
    # fp.close()
    # with zipfile.ZipFile(workingDir +"staging\\"+fileName,'r') as z:
    #     z.extractall(workingDir +"staging\\"+fileName1)
    # os.remove(workingDir +"staging\\"+fileName)
    # z.close()
    #unzip using 7zip
    # uncompress the file (TODO: UPDATE SO LOOPS OVER FILE CORRECTLY)
    # title=fileName.split('.')
    # year1=title[1]
    # temday = title[2].split('-')
    # DateStart = temday[0]                                                   #DataStart is the attribute of DateStart
    # DateEnd = temday[1]
    # if year!=year1:
    #     year = year1
    #     DayYearStart = DateStart
    # temday = title[2].split('-')
    # DateStart = temday[0]                                                   #DataStart is the attribute of DateStart
    # DateEnd = temday[1]
    #
    # day = datetime.date(int(year),1,1) + datetime.timedelta(days = (int(DateStart) - 1) )
    # monthNum = day.month
    # DayOfMonth = day.day
    # print(day,monthNum,DayOfMonth)
    #
    # AggLevel = "CLU"