import csv 
import numpy as np

def getdatasource(datapath):
    cups=[]
    time=[]
    with open(datapath) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            cups.append(float(row["Marks In Percentage"]))
            time.append(float(row["Days Present"]))
    return {"x":cups,"y":time}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("CORRELATION BEETWEEN CUPS AND TIME = ",correlation[0,1])

def setup():
    datapath="StudentsAndDays.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup() 