import pyodbc 

 
sqlServerInstance = "AG-AEM-BCRQYQ1\MSSQLAGDEV"
#sqlServerInstance = "AG-AEM-1M9RBY1"
schema="dbo" #schema for processed data 
dbname="AgDB" #database name 
sqltablename = "TestCLU1"                                                       
 
 
connectionStr = "DRIVER={SQL Server};SERVER="+sqlServerInstance+";DATABASE="+dbname+";Trusted_Connection=Yes" 
con = pyodbc.connect(connectionStr) 
cur = con.cursor() 
 
 
workingDir="E:\\ht398\\eMODIS\\" 

 
try: 
     f = open(workingDir + "createTABLE.txt", 'r') 
     query = " ".join(f.readlines()) 
     query ="Create Table ["+dbname+"].["+ schema +"].["+sqltablename+"]"+query 
     cursor = con.cursor() 
     cursor.execute(query) 
     cursor.commit() 
     print "Created table for CLU data storage " 
     f.close 

except pyodbc.ProgrammingError: 
     print "there is a error" 
     string = "DROP TABLE [dbo].[TestTable]" 
     cur.execute(string) 
     con.commit() 
 
 
     f = open(workingDir + "CreateTABLE.txt", 'r') 
     query = " ".join(f.readlines()) 
     query ="Create Table ["+dbname+"].["+ schema +"].["+sqltablename+"]"+query 
     cursor = con.cursor() 
     cursor.execute(query) 
     cursor.commit() 
     print "Created table for CLU data storage " 
     f.close 
