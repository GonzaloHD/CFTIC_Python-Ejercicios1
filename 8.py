d1 = int(input("Introduce dia primera fecha: "))
m1 = int(input("Introduce mes primera fecha: "))
a1 = int(input("Introduce año primera fecha: "))

d2 = int(input("Introduce dia segunda fecha: "))
m2 = int(input("Introduce mes segunda fecha: "))
a2 = int(input("Introduce año primera fecha: "))

feb1 = 0
feb2 = 0

if a1 % 400 == 0 or (a1 % 4 == 0 and a1 % 100 == 0):
    feb1 = 29
else:
    feb1 = 28

if a2 % 400 == 0 or (a2 % 4 == 0 and a2 % 100 == 0):
    feb2 = 29
else:
    feb2 = 28

diasMes1 = [31, feb1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diasMes2 = [31, feb2, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = False

while not result:
    if d1 < 0 or d1 > diasMes1[m1] or m1 > 12 or d2 < 0 or d2 > diasMes2[m2] or m2 > 12:
        print("Fecha no correcta")
        result = False
        d1 = int(input("Introduce dia primera fecha: "))
        m1 = int(input("Introduce mes primera fecha: "))
        a1 = int(input("Introduce año primera fecha: "))

        d2 = int(input("Introduce dia segunda fecha: "))
        m2 = int(input("Introduce mes segunda fecha: "))
        a2 = int(input("Introduce año primera fecha: "))
    else:
        result = True

dias1 = 0
dias2 = 0
dif = 0

for i in (1, m1):
    dias1 += diasMes1[i]

dias1 = dias1 + d1

for i in (1, m2):
    dias2 += diasMes2[i]

dias2 = dias2 + d2

if dias1 > dias2:
    dif = dias1 - dias2
else:
    dif = dias2 - dias1

print(dif)
