import csv
import json
csv_file = "table.csv"
json_file = "table.json"
arr=[]
with open(csv_file) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for i in csvReader:
        arr.append(i)
    
with open(json_file,"w") as jsonFile:
    json_arr= json.dumps(arr,indent=4)
    jsonFile.write(json_arr)
