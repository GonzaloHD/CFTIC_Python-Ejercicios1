a = int(input("Introduce año: "))

d1 = int(input("Introduce dia primera fecha: "))
m1 = int(input("Introduce mes primera fecha: "))

d2 = int(input("Introduce dia segunda fecha: "))
m2 = int(input("Introduce mes segunda fecha: "))

feb = 0

if a % 400 == 0 or (a % 4 == 0 and a % 100 == 0):
    feb = 29
else:
    feb = 28

diasMes = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = False

while not result:
    if d1 < 0 or d1 > diasMes[m1] or m1 > 12 or d2 < 0 or d2 > diasMes[m2] or m2 > 12:
        print("Fecha no correcta")
        result = False
        a = int(input("Introduce año: "))
        d1 = int(input("Introduce dia primera fecha: "))
        m1 = int(input("Introduce mes primera fecha: "))

        d2 = int(input("Introduce dia segunda fecha: "))
        m2 = int(input("Introduce mes segunda fecha: "))
    else:
        result = True

diasMes = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dias1 = 0
dias2 = 0
dif = 0

for i in (1, m1):
    dias1 += diasMes[i]

dias1 = dias1 + d1

for i in (1, m1):
    dias2 += diasMes[i]

dias2 = dias2 + d2

if dias1 > dias2:
    dif = dias1 - dias2
else:
    dif = dias2 - dias1

print(dif)
