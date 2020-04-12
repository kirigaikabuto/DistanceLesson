import json
products=[]
with open("products.json","r") as file:
    data = file.read()
    products = json.loads(data)
#deleting
products = products[1:]
with open("products.json","w") as file:
    json.dump(products,file,indent=2)