from collections import Counter
import csv
def mode(dataset):
    with open (str(dataset) , newline = "") as f:
        reader = csv.reader(f)
        fileData = list(reader)
    fileData.pop(0)
    newData = []
    for i in range(len(fileData)):
        Nnum = fileData[i][2]
        newData.append(float(Nnum))
    data = Counter(newData)
    modeData = {
        "60-70":0,
        "70-80":0,
        "80-90":0,
        "90-100":0,
        "100-110":0,
        "110-120":0,
        "120-130":0,
        "130-140":0,
        "140-150":0,
        "150-160":0,
        "160-170":0,
        "170-180":0,
        "180-190":0,
        "190-200":0,
    }
    for weight, occurance in data.items():
        if 60 < float(weight) < 70:
            modeData["60-70"] += occurance
        elif 70 < float(weight) < 80:
            modeData["70-80"] += occurance
        elif 80 < float(weight) < 90:
            modeData["80-90"] += occurance
        elif 90 < float(weight) < 100:
            modeData["90-100"] += occurance
        elif 100 < float(weight) < 110:
            modeData["100-110"] += occurance
        elif 110 < float(weight) < 120:
            modeData["110-120"] += occurance
        elif 120 < float(weight) < 130:
            modeData["120-130"] += occurance
        elif 130 < float(weight) < 140:
            modeData["130-140"] += occurance
        elif 140 < float(weight) < 150:
            modeData["140-150"] += occurance
        elif 150 < float(weight) < 160:
            modeData["150-160"] += occurance
        elif 160 < float(weight) < 170:
            modeData["160-170"] += occurance
        elif 170 < float(weight) < 180:
            modeData["170-180"] += occurance
        elif 180 < float(weight) < 190:
            modeData["180-190"] += occurance
        elif 190 < float(weight) < 200:
            modeData["190-200"] += occurance

    modeRange , modeOccurance = 0,0
    for Range , occurance in modeData.items():
        if occurance > modeOccurance:
            modeRange,modeOccurance = [int(Range.split("-")[0]),int(Range.split("-")[1])] , occurance
    mode = float((modeRange[0]+ modeRange[1])/2)
    print(f"mode is : {mode:2f}")

mode("data.csv")