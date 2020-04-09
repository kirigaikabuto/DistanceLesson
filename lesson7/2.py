import random
n = int(input())
arr=[]
for i in range(n):
    arr.append(random.randint(0,1000))
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
print(arr)
print("Min",arr[0],"Max",arr[n-1])