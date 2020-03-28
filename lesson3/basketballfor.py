sumia=0
sumib=0
for i in range(4):
    line = input()
    a,b = line.split(" ")
    a = int(a)
    b = int(b)
    sumia=sumia+a
    sumib=sumib+b
if sumia>sumib:
    print("1")
elif sumia<sumib:
    print("2")
else:
    print("DRAW")
