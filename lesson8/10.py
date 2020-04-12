products=[
    {
        "name":"tovar1",
        "price":100,
    },
    {
        "name":"tovar2",
        "price":150,
    }
]
import json
with open("products.json","w") as file:
    json.dump(products,file,indent=2)