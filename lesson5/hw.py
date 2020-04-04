arr=[1,2,3,4,5,0]
num = 3
diff=[]
for i in range(len(arr)):
    diff.append(num-arr[i])
mini=diff[0]
minindex=0
for i in range(diff):
    if diff[i]<mini:
        mini=diff[i]
        minindex=i
print(diff[minindex])