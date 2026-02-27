import getpass
import os
import Cuenta_bancaria

intentos = 3
usuario = "XiroBear"
contraseña = "abc123"

nombre_archivo = f"Cliente_saldo_{usuario}.txt"
saldo_inicial = 0

while True:
    usu=input("Bienvenido al sistema bancario\nIngrese su usuario (Ingrese 'Salir' para dejar el sistema): ")
    if usu == "Salir":
        break
    con=getpass.getpass("Ingrese su contraseña: ")
    if intentos == 0:
        print("Se han agotado los intentos")
        break
    elif usu == usuario and con == contraseña:
        try:
            with open(nombre_archivo, 'r') as archivo:
                saldo_inicial = int(archivo.read())
        except FileNotFoundError:
            pass
        cuenta = Cuenta_bancaria.CuentaBancaria(usu,saldo_inicial)
        while True:
            os.system("cls")
            print("-"*50)
            print(f"Bienvenido a su cuenta bancaria {usu}")
            print("-"*50)
            try:
                opcion=int(input("1. Consultar Saldo\n2. Depositar\n3. Retirar\n4. Salir\nIngrese una opcion: "))
            except ValueError:
                input("Error: El valor ingresado debe ser un numero entero\nPresione Enter para continuar")
                continue
            if opcion == 1:
                os.system("cls")
                input(f"Su saldo es de {cuenta.obtener_saldo()}\nPresione Enter para continuar")
            elif opcion == 2:
                try:
                    os.system("cls")
                    cantidad=int(input("Ingrese la cantidad a depositar: "))
                    cuenta.depositar(cantidad)
                except ValueError:
                    input("Error: El valor ingresado debe ser un numero entero\nPresione Enter para continuar")
            elif opcion == 3:
                try:
                    os.system("cls")
                    cantidad=int(input("Ingrese la cantidad a retirar: "))
                    cuenta.retirar(cantidad)
                except ValueError:
                    input("Error: El valor ingresado debe ser un numero entero\nPresione Enter para continuar")
            elif opcion == 4:
                os.system("cls")
                break
    else:
        intentos -= 1
        input(f"Las credenciales son incorrectas, le quedan {intentos + 1} intentos\nPresione Enter para reintentar")
        os.system("cls")
os.system("cls")
print("Gracias por usar el sistema bancario")