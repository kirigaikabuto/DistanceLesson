arr=[42,123,3894,212,422]
arr1=[]
arr2=[]
for i in range(0,3):
    arr1.append(arr[i])
for i in range(3,len(arr)):
    arr2.append(arr[i])
print(arr)
print(arr1)
print(arr2)
arr3=arr1+arr2
print(arr3)