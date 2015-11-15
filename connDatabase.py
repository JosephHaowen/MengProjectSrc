import pyodbc

def loadData(year,DateStart,DateEnd,DayYearStart,DayYearEnd,monthNum,DayOfMonth,AggLevel,countyFIPS,stateFIPS,FIPS,CLUID,value):
    sqlServerInstance = "AG-AEM-BCRQYQ1\MSSQLAGDEV"
    #sqlServerInstance = "AG-AEM-1M9RBY1" #this way when it is not a SQL Server named instance)
    schema="dbo" #schema for processed data
    dbname="AgDB" #database name
    sqltablename = "TestCLU1"

    connectionStr = "DRIVER={SQL Server};SERVER="+sqlServerInstance+";DATABASE="+dbname+";Trusted_Connection=Yes"
    con = pyodbc.connect(connectionStr)
    cur = con.cursor()
    query = "INSERT INTO TestTable (DateStart, DateEnd, Year, Month, DayOfMonth, DayYearStart, DayYearEnd, AggLevel, countyFIPS, stateFIPS, FIPS, CLU_ID, Value)"
    query +=" VALUES ("
    query += str(DateStart)
    query += ", "
    query += str(DateEnd)
    query += ", "
    query += str(year)
    query += ", "
    query += str(monthNum)
    query += ", "
    query += str(DayOfMonth)
    query += ", "
    query += str(DayYearStart)                                                      #report error about agglevel, need to make change to aggreLevel
    query += ", "
    query += str(DayYearEnd)
    query += ", "
    query += str(AggLevel)
    query += ", "
    query += str(countyFIPS)
    query += ", "
    query += str(stateFIPS)
    query += ", ";
    query += str(FIPS)
    query += "," ;
    query += str(CLUID)
    query += "," ;
    query += str(value)
    query += ");"

    print query

    cur.execute(query)
    cur.commit()
