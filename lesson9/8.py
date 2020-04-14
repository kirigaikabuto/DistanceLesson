
n,m = input().split()
n = int(n)
m = int(m)
cars=[int(i) for i in input().split()]
for i in range(n):
    for j in range(n):
        if cars[i]<cars[j]:
            cars[i],cars[j] = cars[j],cars[i]
sumi=0
count=0
for i in range(n):
    if sumi+cars[i]<=m:
        sumi=sumi+cars[i]
        count=count+1
print(count)