n = int(input())
arr=[]
sumi=0
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    sumi=sumi+arr[i]
print(sumi/n)