import json
with open("table.json","r") as jsonFile:
    data = jsonFile.read()
    arr = json.loads(data)
print(arr[0])