import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    arr.append(temp)

for i in range(n):
    index=random.randint(0,m)
    arr[i][index]=1
for i in range(n):
    print(arr[i])
        
points=[
    [0,9],
    [1,8],
    [2,3]
]
#выбор точки и высчитать расстояние
0 -> [0,9]
2->[2,3]
