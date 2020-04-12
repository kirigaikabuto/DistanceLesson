product={
    "name":"product3",
    "pruce":1000
}
import json
products=[]
with open("products.json","r") as file:
    data = file.read()
    products = json.loads(data)
print(products)
# products.append(product)
# with open("products.json","w") as file:
#     json.dump(products,file,indent=2)