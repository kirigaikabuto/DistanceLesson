import random
n = int(input())
numbers=[random.randint(0,20) for i in range(n)]
print(numbers)
for i in range(n):
    for j in range(n):
        if numbers[i]<numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
unique={}
print(numbers)
counter=1
for i in range(n-1):
    if numbers[i]==numbers[i+1]:
        counter+=1
    else:
        unique[numbers[i]]=counter
        counter=1
for i in unique:
    print(i,":",unique[i])
