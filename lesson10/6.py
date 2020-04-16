peoples=[
    {
        "name":"Yerassyl",
        "age":22,
        "balance":10000,
        "department_id":1,
    },
    {
        "name":"kirito",
        "age":21,
        "balance":1000,
        "department_id":1
    },
    {
        "name":"zoka",
        "age":19,
        "balance":5000,
        "department_id":2
    }
]
def print_data(arr):
    for i in arr:
        st="Name:{},Balance:{},Age:{}".format(i['name'],i['balance'],i['age'])
        print(st)

def getAverageBalance(arr):
    sumi=0
    avg=0
    for i in arr:
        sumi=sumi+i['balance']
    avg = sumi/len(arr)
    return avg
print_data(peoples)
avg = getAverageBalance(peoples)
print(avg)