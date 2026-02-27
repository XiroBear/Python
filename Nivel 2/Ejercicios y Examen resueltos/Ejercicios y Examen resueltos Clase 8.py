import os
while True:
    os.system("cls")
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        input("Entrada inválida. Ingrese un número entero.\nPresione enter para continuar")
input(f"Edad registrada: {edad}\nPresione Enter para continuar")

catalogo = ["TV","Radio","Laptop","Mouse"]

while True:
    os.system("cls")
    try:
        indice = int(input("Ingrese el indice del producto:"))
        input(f"El producto es: {catalogo[indice]}\nPresione enter para continuar")
        break
    except ValueError:
        input("Error: Debe ingresar un número entero.\nPresione enter para continuar")
    except IndexError:
        input("Error: El indice no existe.\nPresione enter para continuar")
    