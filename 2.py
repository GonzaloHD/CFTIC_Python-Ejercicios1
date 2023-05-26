letra = input("Introduce letra: ")

cant = 0
for i in str(input("Introduce frase: ")):
    if letra == i:
        cant += 1
print("La cantidad de veces que aparece la letra es: " + str(cant))
