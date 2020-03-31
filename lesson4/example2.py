arr = []
sumi=0
n = int(input("Write count of array:"))
#code
print(arr)
for i in range(n):
    number = int(input())
    arr.append(number)
    print(arr)
print(arr)
for i in range(n):
    sumi = sumi + arr[i]
print(sumi)
