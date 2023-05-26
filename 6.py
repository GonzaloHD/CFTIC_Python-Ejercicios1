

H = int(input("Introduce hora: "))
M = int(input("Introduce minutos: "))
S = int(input("Introduce segundos: "))

result = False

while not result:
    if H % 24 < 24 and M % 60 < 60 and S < 60:
        print("La hora es valida")
        result = True
    else:
        print("La hora no es valida")
        H = int(input("Introduce hora: "))
        M = int(input("Introduce minutos: "))
        S = int(input("Introduce segundos: "))
