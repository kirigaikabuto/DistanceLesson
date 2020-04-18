import csv
import json
def save_csv_to_json(csv_file,json_file):
    arr=[]
    with open(csv_file) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for i in csvReader:
            arr.append(i)
    with open(json_file,"w") as jsonFile:
        json_arr= json.dumps(arr,indent=4)
        jsonFile.write(json_arr)
