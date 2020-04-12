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

for i in range(n):
    index=random.randint(0,m-1)
    arr[i][index]=1
for i in range(n):
    print(arr[i])
points=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            point=[i,j]
            points.append(point)
for i in range(len(points)):
    print(i,points[i])
index1 = int(input("First point:"))
index2 = int(input("Second point:"))
point1 = points[index1]
point2 = points[index2]
print(point1,point2)
x =point1[0]-point2[0]
y =point1[1]-point2[1]
distance = math.sqrt(x*x+y*y)
print("Distance between points:",distance)