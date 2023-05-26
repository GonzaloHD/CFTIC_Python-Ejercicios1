letra = input("Introduce letra: ")

while letra != "a" and letra != "b" and letra != "c":
    print("Letra equivocada")
    letra = input("Introduce letra: ")

if letra == "a":
    print("7")
elif letra == "b":
    print("9")
elif letra == "c":
    print("101")


