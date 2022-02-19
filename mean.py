import csv
def mean(dataset):
    with open (str(dataset) , newline = "") as f:
        reader = csv.reader(f)
        fileData = list(reader)
    fileData.pop(0)
    newData = []
    for i in range(len(fileData)):
        Nnum = fileData[i][2]
        newData.append(float(Nnum))
    arrLength = len(newData)
    sum = 0
    for counter in newData:
        sum += counter
    mean = sum/arrLength
    print("The mean of the given dataSet is :"+ str(mean))
mean("data.csv")