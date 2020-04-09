import random
n = int(input("колво элементов в массиве:"))

arr=[]
for i in range(n):
    arr.append(random.randint(0,1000))
#step sorting
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
print(arr) 
find = int(input("число для поиска:"))
mid=n//2
left=0
right=n-1
while arr[mid]!=find and left<=right:
    if find>arr[mid]:
        left = mid+1
    else:
        right = mid-1
    mid = (left+right)//2
if left>right:
    print("Not find")
else:
    print(mid)





# 1 2 3 4 5 6 7 8 9 10
# n=10
# mid = 5
# left = 0
# right = 9
# find = 2
# arr[9]
# left = 0
# right=mid-1 4