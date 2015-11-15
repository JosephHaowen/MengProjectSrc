import urllib2
import re
import os

def fileList():

    workingDir="C:\\Users\\ht398\\eMODIS\\"
    os.chdir(workingDir)
    weburl = "https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/"
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, weburl, "woodardjoshua@gmail.com", "USGSwoodard14")
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(weburl)
    urllib2.install_opener(opener)
    data = urllib2.urlopen(weburl).read()
    data = str(data)
    match = re.compile(r'(?<=href=["]).*?(?=["])')
    rawlv1 = re.findall(match,data)
    file = open('emodis1.txt','a')
    for raw in rawlv1:
        web = str(urllib2.urlopen(weburl+str(raw)).read())
        rawlv2 = re.findall(match,web)
        match1 = re.compile(r'(comp_\d\d\d/)')
        rawlv3 = re.findall(match1,str(rawlv2))
        for raw2 in rawlv3:
            web1 = str(urllib2.urlopen(weburl + str(raw) + str(raw2)).read())
            rawlv3 = re.findall(match,web1)
            match2 = re.compile(r'(\bUS_eMTH_NDVI.\d\d\d\d.\d\d\d-\d\d\d.QKM.COMPRES.\d\d\d.\d\d\d\d\d\d\d\d\d\d\d\d\d.zip\b)')
            rawlv4 = re.findall(match2,str(rawlv3))
            rawlv4 = list(set(rawlv4))  #remove the duplicates in rawlv4
            for raw4 in rawlv4:
                web2 = weburl + str(raw) + str(raw2) + str(raw4)  #the url address for every emodis file we want.
            # print(web2)
                file.writelines(web2+'\n')

    file.close()

if __name__ == "__main__":
    fileList()