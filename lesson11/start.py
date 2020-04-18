import json 
import csv
arr=[]
csv_file="table.csv"
json_file="table.json"
with open(csv_file) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for i in csvReader:
        arr.append(i)
for i in range(len(arr)):
    d = arr[i]
    d["EMPLOYEE_ID"]=int(d["EMPLOYEE_ID"])
    if d["DEPARTMENT_ID"] !=" - ":
        d["DEPARTMENT_ID"]=int(d["DEPARTMENT_ID"])
    d["SALARY"]=int(d['SALARY'])
with open(json_file,"w") as jsonFile:
    json_arr= json.dumps(arr,indent=4)
    jsonFile.write(json_arr)