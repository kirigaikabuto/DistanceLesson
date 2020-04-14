import random
def getMax(array):
    maxi=array[0]
    for i in array:
        if maxi<i:
            maxi = i
    print(maxi)
def print_arr(arr):
    for i in arr:
        print(i,end=" ")
    print("\n")
n = int(input())
arr=[random.randint(0,20) for i in range(n)]
print_arr(arr)
getMax(arr)