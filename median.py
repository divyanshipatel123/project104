import csv
def median(dataset):
    with open (str(dataset) , newline = "") as f:
        reader = csv.reader(f)
        fileData = list(reader)
    fileData.pop(0)
    newData = []
    for i in range(len(fileData)):
        Nnum = fileData[i][2]
        newData.append(float(Nnum))
    arrLength = len(newData)
    newData.sort()
    if arrLength % 2 == 0:
        median1 = float(newData[arrLength//2])
        median2 =  float(newData[arrLength//2 - 1])
        median = (median1+median2)/2   
    else:
        median = newData[arrLength//2]

    print("THe median of the DataSet is :" , median)
median("data.csv")