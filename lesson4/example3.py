arr=[]
nechet=[]
chet=[]
n = int(input("Count of numbers:"))
for i in range(n):
    number = int(input())
    arr.append(number)

for i in range(n):
    if arr[i]%2==0:
        chet.append(arr[i])
    else:
        nechet.append(arr[i])
print("Nechet",nechet)
print("Chet",chet)