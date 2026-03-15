import Calculadora_Modular
import Verificador_de_Palíndromos
import Conversor_de_Temperatura
import os

while True:
    os.system("cls")
    print("*" * 20)
    print("Bienvenido al menu")
    opcion = int(input("\n1. Calculadora Modular\n2. Verificador de Palíndromos\n3. Conversor de Temperatura\n4. Salir \nIngrese una opcion: "))
    if opcion == 1:
        while True:
            os.system("cls")
            print("*" * 20)
            opcion = int(input("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Volver al menu anterior: "))
            if opcion == 1:
                os.system("cls")
                numero1 = input("ingrese el primer numero a sumar: ")
                numero2 = input("Ingerse el segundo numero a sumar: ")
                if numero1.isdigit() and numero2.isdigit():
                    input(f"\nLa suma de {numero1} y {numero2} es: {Calculadora_Modular.sumar(int(numero1),int(numero2))}\nPresione Enter para continuar")
                else:
                    input("\nLos datos ingresados debe ser numeros, presione Enter para continuar")
            elif opcion == 2:
                os.system("cls")
                numero1 = input("ingrese el primer numero a restar: ")
                numero2 = input("ingrese el segundo numero a restar: ")
                if numero1.isdigit() and numero2.isdigit():
                    input(f"\nLa resta de {numero1} y {numero2} es: {Calculadora_Modular.restar(int(numero1),int(numero2))}\nPresione Enter para continuar")
                else:
                    input("\nLos datos ingresados debe ser numeros, presione Enter para continuar")
            elif opcion == 3:
                os.system("cls")
                numero1 = input("ingrese el primer numero a multiplicar: ")
                numero2 = input("ingrese el segundo numero a multiplicar: ")
                if numero1.isdigit() and numero2.isdigit():
                    input(f"\nLa multiplicacion de {numero1} y {numero2} es: {Calculadora_Modular.multiplicar(int(numero1),int(numero2))}\nPresione Enter para continuar")
                else:
                    input("\nLos datos ingresados debe ser numeros, presione Enter para continuar")
            elif opcion == 4:
                os.system("cls")
                numero1 = input("ingrese el primer numero a dividir: ")
                numero2 = input("ingrese el segundo numero a dividir: ")
                
                if numero1.isdigit() and numero2.isdigit():
                    if numero2 == "0":
                        input("\nError: No se puede dividir por cero\nPresione Enter para continuar")
                    else:
                        input(f"\nLa division de {numero1} y {numero2} es: {Calculadora_Modular.dividir(int(numero1),int(numero2))}\nPresione Enter para continuar")
                else:
                    input("\nLos datos ingresados debe ser numeros, presione Enter para continuar")
            elif opcion == 5:
                break
    elif opcion == 2:
        os.system("cls")
        print("*" * 20 + "\nVerificador de Palíndromos")
        palabra = input("Ingrese la palabra para saber si es un palíndromo: ")
        if Verificador_de_Palíndromos.palindromo(palabra):
            input("\nLa palabra es un palíndromo\nPresione Enter para continuar")
        else:
            input("\nLa palabra no es un palíndromo\nPresione Enter para continuar")
    elif opcion == 3:
        os.system("cls")
        print("*" * 20 + "\nConversor de Temperatura")
        numero = input("Ingrese la temperatura en grados Celsius: ")
        if numero.isdigit():
            input(f"\nLa temperatura en grados Fahrenheit es: {Conversor_de_Temperatura.celsius_a_fahrenheit(int(numero))}\nPresione Enter para continuar")
        else:
            input("\nLos datos ingresados debe ser numeros, presione Enter para continuar")
    elif opcion == 4:
        print("\nGracias por usar el programa")
        break
    else:
        input("\nOpcion no valida, por favor, ingrese una opcion valida, presione Enter para reintentar")
    