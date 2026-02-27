🚀 BIENVENIDO AL NIVEL INTERMEDIO
Aquí es donde Python se vuelve verdaderamente poderoso. Dejamos de jugar con variables sueltas (a, b, c) y empezamos a manejar Estructuras de Datos y Arquitectura de Software.

Nueva Ruta de Aprendizaje (Intermedio):

Colecciones I: Listas y Tuplas (Manejo de grandes volúmenes de datos).

Colecciones II: Diccionarios (Bases de datos en memoria).

Funciones: Modularización y reutilización de código profesional.

Manejo de Errores: try, except (Hacer programas a prueba de balas).

# Clase 5: Listas (El poder de las colecciones)
Hasta ahora, si querías guardar los nombres de 100 alumnos, necesitabas 100 variables (alumno1, alumno2...). Eso es insostenible.

Una Lista es una variable que puede almacenar múltiples elementos ordenados.

## 1. Sintaxis Básica
Se usan corchetes [] y los elementos se separan por comas.

    # Una lista de strings
    frutas = ["Manzana", "Banana", "Cereza"]

    # Una lista mixta (Python permite mezclar tipos, aunque no se recomienda abusar)
    datos = ["Juan", 31, 1.75, True]

    # Una lista vacía (para llenarla luego)
    carrito_compras = []

## 2. Acceder a los datos (Índices)
Las listas en Python empiezan a contar desde 0.

    frutas[0] es "Manzana".

    frutas[1] es "Banana".

    frutas[-1] es el último elemento ("Cereza").

## 3. Métodos Fundamentales (Las herramientas de la lista)
Las listas son objetos y tienen "poderes" (métodos) integrados:

    append(item): Agrega un elemento al final de la lista.
    pop(): Elimina y devuelve el último elemento.
    remove(valor): Busca el valor y elimina la primera aparición.
    len(lista): Devuelve el tamaño (cantidad de elementos) de la lista.

💻 Ejemplo Práctico: Gestión de Inventario

    inventario = ["Espada", "Escudo", "Poción"]

    print(f"Inventario inicial: {inventario}")

    # Agregamos un item
    print("Has encontrado un Mapa.")
    inventario.append("Mapa") 

    # Mostramos el primer objeto
    print(f"Arma equipada: {inventario[0]}")

    # Eliminamos la poción porque la usamos
    inventario.remove("Poción")

    # Verificamos cuántos items quedan
    cantidad = len(inventario)
    print(f"Te quedan {cantidad} objetos: {inventario}")

## 📝 Ejercicios de Clase 5
Vamos a poner a prueba tu capacidad para gestionar datos agrupados.

Lista de Tareas (CRUD Básico):

Crea una lista vacía llamada tareas.
Usa un bucle while para mostrar un menú:
Agregar tarea.
Ver todas las tareas.
Completar (eliminar) última tarea.
Salir.
Si elige 1: Pide el nombre de la tarea y usa .append().
Si elige 2: Imprime la lista completa.
Si elige 3: Usa .pop() para sacar la última y avisa cuál se eliminó.

El Analista de Datos:

Crea una lista predefinida con estos números: ventas = [150, 300, 50, 20, 100].
Calcula la suma total de las ventas (puedes usar un bucle for que recorra la lista o la función sum(ventas) si quieres investigar).
Encuentra el valor de la venta más alta (puedes usar lógica o max(ventas)).
Imprime: "Total vendido: $X, Venta récord: $Y".

***Nota Importante sobre el for en listas:***

    for item in lista:
        print(item) # Recorre cada elemento directamente