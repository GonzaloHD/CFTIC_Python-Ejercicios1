operacion = input("Introduce S para sumar o R para restar: ")
result = 0

while operacion != 'S' and operacion != 'R':
    print(operacion)
    operacion = input("Introduce S para sumar o R para restar: ")


if operacion == 'S':
    print("Esta en S")
    num1 = float(input("Introduce primer numero: "))
    num2 = float(input("Introduce segundo numero: "))
    result = num1 + num2

else:
    if operacion == 'R':
        print("Esta en R")

        num1 = float(input("Introduce primer numero: "))
        num2 = float(input("Introduce segundo numero: "))
        result = num1 - num2
    else:
        print("Operacion no correcta: ")


print("El resultado es: " + str(result))