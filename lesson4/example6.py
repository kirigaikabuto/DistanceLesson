n = int(input("Count of number:"))
arr=[]
for i in range(n):
    arr.append(int(input("number:")))
find = int(input("find:"))
#code
k=0
for i in range(n):
    if arr[i]==find:
        k=1
if k==1:
    print("YES")
else:
    print("NO")