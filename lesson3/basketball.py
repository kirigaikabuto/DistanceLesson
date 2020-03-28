line1 = input()
a1,b1 = line1.split(" ")
a1 = int(a1)
b1 = int(b1)
line2 = input()
a2,b2 = line2.split(" ")
a2 = int(a2)
b2 = int(b2)
line3 = input()
a3,b3 = line3.split(" ")
a3 = int(a3)
b3 = int(b3)
line4 = input()
a4,b4 = line4.split(" ")
a4 = int(a4)
b4 = int(b4)
sumia=a1+a2+a3+a4
sumib=b1+b2+b3+b4
if sumia>sumib:
    print("1")
elif sumia<sumib:
    print("2")
else:
    print("DRAW")