arr=[
    [1, 2, 3, 4,  5],
    [6, 7, 8 ,9 ,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]
num = int(input())
n = len(arr)
x=-1
y=-1
for i in range(n):
    m = len(i)
    for j in range(m):
        if arr[i][j]==num:
            x,y=i,j

if x!=-1 and y!=-1:
    if x+y+1<n:
        print("TOP TRIANGLE")
    elif x+y+1==n:
        print("IN THE MIDDLE")
    else:
        print("BOTTOM TRIANGLE")
else:
    print("ERROR")

        