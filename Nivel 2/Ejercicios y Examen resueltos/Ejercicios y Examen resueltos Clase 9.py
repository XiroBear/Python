import os
while True:
    os.system("cls")
    print(f"*" * 50)
    try:
        menu = int(input("1. Escribir Pensamiento\n2. Leer pensamientos\n3. Salir\nIngrese una opcion: "))
        if menu == 1:
            os.system("cls")
            print(f"*" * 50)
            pensamiento = input("Escribe un pensamiento: ")
            with open("diario.txt", 'a') as archivo:
                archivo.write(f"{pensamiento}\n")
                input("El pensamiento fue agregado al diario")
        elif menu == 2:
            os.system("cls")
            print(f"*" * 50)
            try:
                with open("diario.txt", 'r') as archivo:
                    input(f"Pensamientos:\n{archivo.read()}\nPresione Enter para continuar")
            except FileNotFoundError:
                input("Error: El diario aún no ha sido creado\nPresione Enter para continuar")
        elif menu == 3:
            os.system("cls")
            print(f"*" * 50)
            print("Gracias por usar el diario")
            break
        else:
            input("Opcion no valida, presione Enter para continuar")
    except ValueError:
        input("Error: Opcion no valida, presione Enter para continuar")