arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#сумма четных и нечетных числе вывести
chet=0
nechet=0
for i in range(len(arr)):
    for j in arr[i]:
        if j%2==0:
            chet+=1
        else:
            nechet+=1
print(chet)
print(nechet)
