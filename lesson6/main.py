arr=[
    [1,2,3,5],
    [4,5,6,4],
    [7,8,9,4],
    [4,5,6,4],
]
n = len(arr)
equal=n-1
sumi=0
for i in range(n):
    m = len(arr[i])
    for j in range(m):
        if i+j==equal:
            sumi=sumi+arr[i][j]
print(sumi)

        