import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        rnum = random.randint(0,20)
        temp.append(rnum)
    arr.append(temp)
for i in range(n):
    print(arr[i])
# n-строк
# m-столбцы
# 3 4 5 6
# 1 2 3 4
# 4
# 4
# 1 2 3 4
# 5 5 6 7
# 7 4 3 1
# 2 3 4 5
# arr[строку][колонна]
for i in range(m):
    sumi=0
    for j in range(n):
        sumi = sumi+arr[j][i]
    print(sumi)
#создать массив sumi_arr
#если 4 столбца то 4 элемента
#индекс суммы 0 в массие значит это нулевой столбец
#найти максимальный эелмент в массиве sumi_arr и запомнить его индекс
#через индекс можно понять какой столбец
    