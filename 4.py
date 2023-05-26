USUARIO = "admin"
PASSWORD = "admin"

login = False

while not login:
    user = input("Introduce usuario: ")
    pss = input("Introduce contraseña: ")

    if user == USUARIO and PASSWORD == pss:
        print("Registro correcto: ")
        login = True

    else:
        print("Registro no correcto")


