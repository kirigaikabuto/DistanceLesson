import random
n = int(input())
numbers=[random.randint(0,20) for i in range(n)]
print(numbers)
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
d={}
for i in unique:
    d[i]=0
for i in unique:
    for j in numbers:
        if i==j:
            d[i]+=1
for i in d:
    print(i,":",d[i])