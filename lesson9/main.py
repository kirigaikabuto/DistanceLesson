import random
import math
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    arr.append(temp)

s = int(input())
for i in range(n):
    print("строка",i)
    for j in range(s):
        index=random.randint(0,m-1)
        arr[i][index]=1
        print("    столбец",index)
for i in range(n):
    print(arr[i])
import json
with open("game.json","w") as file:
    json.dump(arr,file,indent=2)
