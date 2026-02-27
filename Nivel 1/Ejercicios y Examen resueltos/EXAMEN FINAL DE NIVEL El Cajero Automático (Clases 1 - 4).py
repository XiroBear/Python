# Requerimientos del Sistema:

Clavesecreta = "1234"
intentos = 2

while True:
    clave = input("Ingrese su clave secreta: ")
    if clave == Clavesecreta:
        print("Bienvenido al menu")
        # El Menú Principal y logica de opciones
        saldo = 1000
        while True:
            print("\nMenu\n1. Mostrar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")
            opcion = int(input("Ingrese la opcion deseada: "))
            if opcion == 1:
                print(f"sua saldo es de ${saldo}")
            elif opcion == 2:
                retiro=float(input("Ingrese la cantidad deseada: "))
                if retiro > saldo:
                    print("Saldo insuficiente")
                elif retiro < 0 :
                    print("Error")
                else:
                    saldo = saldo - retiro
                    print(f"Retiro exitoso, su saldo es de ${saldo}")
            elif opcion == 3:
                deposito = float(input("Ingrese la cantidad a depositar: "))
                if deposito < 0:
                    print("Error")
                else:
                    saldo = saldo + deposito
                    print(f"Deposito exitoso, su saldo es de ${saldo}")
            elif opcion == 4:
                print("Gracias por usar nuestro banco")
                break
            else:
                print("Opcion no valida, debe ingresar una opcion del menu")
        break
    else:
        if intentos == 0:
            print("Tarjeta bloqueada")
            break
        print(f"Contraseña incorrecta, le quedan {intentos} restantes")
        intentos = intentos - 1

