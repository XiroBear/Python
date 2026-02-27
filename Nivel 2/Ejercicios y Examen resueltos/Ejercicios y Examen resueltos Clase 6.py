# Agenda Telefónica Inteligente
import os

agenda = {}

while True:
    os.system("cls")
    print("Agenda Telefonica\n1. Guardar\n2. Buscar\n3. Borrar\n4. Ver todos\n5. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        os.system("cls")
        print("Guardar contacto")
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono: ")
        agenda[nombre] = telefono
        input("Contacto guardado exitosamente.\n\nPresione enter para continuar")
    elif opcion == 2:
        os.system("cls")
        print("Buscador de contactos")
        busqueda = input("Ingrese el nombre que dese buscar: ")
        if busqueda in agenda:
            print(f"\nEl numero de {busqueda} es: {agenda[busqueda]}")
        else:
            print("\nContacto no encontrado")
        input("\nPresione enter para continuar...")
    elif opcion == 3:
        os.system("cls")
        nombre=input("\nIngrese el nombre del contacto que desea eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"\nSe ha eliminado el contacto {nombre}")
        else:
            print("\nContacto no encontrado")
        input("\nPresione enter para continuar...")
    elif opcion == 4:
        os.system("cls")
        print("Lista de contactos: ")
        if not agenda:
            print("\nNo se encuentran contactos en la agenda\n")
        else:
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Telefono: {telefono}")
        input("\nPresione enter para continuar...")
    elif opcion == 5:
        print("\nGracias por usar la agenda")
        break
    else:
        print("\nOpcion no valida")

#Contador de Frecuencias (Algoritmo Clásico)

texto = "manzana banana manzana fresa banana manzana uva"
lista = texto.split()
conteo ={}
#uso del diccionario con conteo

for i in lista:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1
print(f"\nresultado: {conteo}")
