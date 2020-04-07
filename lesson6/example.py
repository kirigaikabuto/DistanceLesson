arr=[
    [1,2,3,5,5],
    [4,5,6,4,5],
    [7,8,9,4,5],
    [4,5,6,4,5],
    [4,5,6,4,5],
]
n = len(arr)
sumi=0
for i in range(n):
    m = len(arr[i])
    for j in range(m):
        if i+j+1<n:
            sumi=sumi+arr[i][j]
print(sumi)

        