import csv

iFile = open('train.csv')
temperatureFile = open('features.csv')
testReader = csv.reader(iFile)
temperatureReader = csv.reader(temperatureFile)
tempColumn = 2
oFile  = open('Output.csv', "w")
writer = csv.writer(oFile, delimiter=',', quotechar='"', lineterminator = '\n', quoting=csv.QUOTE_NONNUMERIC)

#Note that this is very very slow (~2 hours).  It could be optimized, but
#seeing as it only runs once for preprocessing, idk if it really matters

for tempInstance in temperatureReader:
    iFile.seek(0,0);
    for deptDate in testReader:
        if tempInstance[0] == deptDate[0]:
            if tempInstance[1] == deptDate[2]:
                if deptDate[4] != "TRUE":
                    writer.writerow([deptDate[0], deptDate[1], deptDate[2], deptDate[3], tempInstance[2]])
print("done")


#for row in testReader:
#    if row[4] != "TRUE":
#        writer.writerow([row[0], row[1], row[2], row[3]])
        
oFile.close()
iFile.close()
temperatureFile.close()
