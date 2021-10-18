import csv 
import numpy as np

def getdatasource(datapath):
    students=[]
    days=[]
    with open(datapath) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            students.append(float(row["STUDENTS"]))
            days.append(float(row["DAYS"]))
    return {"x":students,"y":days}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("CORRELATION BEETWEEN STUDENTS AND DAYS = ",correlation[0,1])

def setup():
    datapath="STUDENTSANDDAYS.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup() 