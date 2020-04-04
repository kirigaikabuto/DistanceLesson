import math
arr=[1,2,3,1,2,0]
num = 3
diff=[]
#math
for i in range(len(arr)):
    diff.append(num-arr[i])
print(diff)
mini=diff[0]
minindex=0
for i in range(len(diff)):
    if diff[i]<mini:
        mini=diff[i]
        minindex=i
print(diff[minindex])