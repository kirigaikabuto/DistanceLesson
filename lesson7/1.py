arr=[-2,45,0,11,-9]
# n=len(arr)
# for i in range(0,n):
#     for j in range(0,n):
#         print(arr[i])
#         if arr[i]<arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)


for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
print(arr)
#loop1 i=0,5 
#loop2 j=0,4 
#loop2 if -2>45 [-2,45,0,11,-9]
#loop2 j=1,4 
#loop2 if 45>0 [-2 0 45 11 -9]
#loop2 j=2,4
#loop2 if 45>11 [-2 0 11 45 -9]
#loop2 j=3,4
#loop2 if 45>-9 [-2 0 11 -9 45]
#loop1 i=1,5
#loop2 j=0,3
#loop2 if -2>0 [0 -2 11 -9 45]
