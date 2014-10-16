import csv

iFile = open('train.csv')
testReader = csv.reader(iFile)
oFile  = open('Output.csv', "w")
writer = csv.writer(oFile, delimiter=',', quotechar='"', lineterminator = '\n', quoting=csv.QUOTE_NONNUMERIC)

for row in testReader:
    if row[4] != "TRUE":
        writer.writerow([row[0], row[1], row[2], row[3]])
        
oFile.close()
iFile.close()
