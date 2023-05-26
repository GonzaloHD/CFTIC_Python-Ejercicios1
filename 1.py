n1=input("Introduce primer número: ")
n2=input("Introduce segundo número: ")
n3=input("Introduce tercer número: ")

if n1 >= n2 and n1 >= n3:
    print("El mayor número es: " + str(n1))

else:
    if n2 >= n1 and n2 >= n3:
        print("El mayor número es: " + str(n2))

    else:
        print("El mayor número es: " + str(n3))
