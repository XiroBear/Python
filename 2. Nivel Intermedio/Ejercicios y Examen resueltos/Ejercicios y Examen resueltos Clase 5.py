# Lista de Tareas (CRUD Básico)
import collections
import os
tareas = []

while True:
    os.system("cls")
    print("\nMenu:\n1. Agregar Tarea\n2. Ver todas las tareas\n3. Completar (eliminar) una tarea\n4. Eliminar una tarea en especifico\n5. Salir")
    ingreso = int(input("Ingrese una opcion: "))
    if ingreso == 1:
        os.system("cls")
        ntarea=input("Ingrese el nombre de la nueva tarea: ")
        tareas.append(ntarea)
        print(f"\nSe agrego la tarea {ntarea}")
        input("\nPresione enter para continuar...")
    elif ingreso == 2:
        os.system("cls")
        if len(tareas) == 0:
            print("No se encuentran tareas")
        else:
            print("\nTareas:")
            for i in tareas:
                print(i)
        input("\nPresione enter para continuar...")
    elif ingreso == 3:
        os.system("cls")
        if len(tareas) == 0:
            print("No se encuentran tareas")
        else:
            print("\nTareas:")
            for i in tareas:
                print(i)
            eliminar = input("\nDesea eliminar la ultima tarea? (s/n)")
            if eliminar == "s":
                tareas.pop()
                print("\nSe completo la tarea")
                input("\nPresione enter para continuar...")
            else:
                print("\nNo se completo la tarea")
                input("\nPresione enter para continuar...")
    elif ingreso == 4:
        os.system("cls")
        if len(tareas) == 0:
            print("No se encuentran tareas")
        else:
            print("\nTareas:")
            for i in tareas:
                print(i)
            eliminar = input("\nIngrese el nombre de la tarea a eliminar: ")
            if eliminar in tareas:
                tareas.remove(eliminar)
                print(f"\nSe completo la tarea {eliminar}")
                input("\nPresione enter para continuar...")
            else:
                print(f"\nNo se encontro la tarea {eliminar}")
                input("\nPresione enter para continuar...")
    elif ingreso == 5:
        break
    os.system("cls")
        
#El Analista de Datos

ventas = [150,300,50,20,100]

#Con un bucle for...
x = 0
for i in ventas:
    x = x + i
print(f"\nLa suma de las ventas es ${x}")

#con la funcion sum()
print(f"\nLa suma de las ventas es ${sum(ventas)}")

y = 0
for i in ventas:
    if i >= y:
        y = i
print(f"\nLa venta mas alta es ${y}")

#con la funcion max()
print(f"\nLa venta mas alta es ${max(ventas)}")

#Lo solicitado con funciones
print(f"\nTotal vendido ${sum(ventas)} y la venta mas alta es ${max(ventas)}")

#Lo solicitado con bucles
print(f"\nTotal vendido ${x} y la venta mas alta es ${y}")
