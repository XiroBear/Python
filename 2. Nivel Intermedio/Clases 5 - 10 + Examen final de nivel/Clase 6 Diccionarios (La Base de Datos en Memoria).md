# 📘 Clase 6: Diccionarios (La Base de Datos en Memoria)
Las listas son geniales para guardar cosas en orden (0, 1, 2...), pero son terribles para buscar información específica si no sabes la posición.

Imagina buscar el número de teléfono de "Xiro" en una lista de 1 millón de nombres. Tendrías que leer uno por uno hasta encontrarlo. Ineficiente.

Aquí entran los Diccionarios (dict).

## 1. ¿Qué es un Diccionario?
Es una colección de pares Clave: Valor (Key: Value). Funciona como una agenda real: buscas por la "Clave" (nombre) y obtienes el "Valor" (teléfono) instantáneamente, sin recorrer todo.

## 2. Sintaxis
Se usan llaves {}.

    # Creando un diccionario de un estudiante
    estudiante = {
        "nombre": "Xiro",
        "edad": 31,
        "curso": "Python Pro",
        "promedio": 9.8
    }

## 3. Operaciones Fundamentales
Acceder a un valor: Usas la clave entre corchetes, no el número de índice.

    print(estudiante["nombre"]) # Imprime: Xiro

Agregar o Modificar:

    estudiante["edad"] = 32      # Modifica el valor existente
    estudiante["ciudad"] = "Santiago" # Crea una nueva clave si no existía

Eliminar:

    del estudiante["curso"]      # Borra la clave y su valor

## 4. Recorrer un Diccionario
A diferencia de las listas, aquí podemos recorrer claves, valores o ambos.

    # Forma profesional: .items() devuelve clave y valor al mismo tiempo
    for clave, valor in estudiante.items():
        print(f"La clave es {clave} y el valor es {valor}")

💻 Ejemplo Práctico: Base de Datos de Precios

    precios = {
        "manzana": 100,
        "pan": 50,
        "leche": 200
    }

    producto = input("¿Qué quieres comprar? ").lower() # lower() convierte a minúsculas

    # Verificamos si la clave existe en el diccionario
    if producto in precios:
        valor = precios[producto]
        print(f"El {producto} cuesta ${valor}")
    else:
        print("No vendemos ese producto.")

## 📝 Ejercicios de Clase 6
Los diccionarios son la estructura más utilizada en Python (incluso para Inteligencia Artificial y Web). Domínalos.

Agenda Telefónica Inteligente:

Crea un diccionario vacío agenda = {}.

Haz un menú (Bucle while):

Guardar: Pide nombre y teléfono. Guárdalo en el diccionario.
Buscar: Pide un nombre. Si existe, muestra el teléfono. Si no, di "No encontrado".
Borrar: Pide un nombre y elimínalo de la agenda.
Ver todos: Imprime toda la lista de contactos (Nombre: Teléfono).
Salir.

Contador de Frecuencias (Algoritmo Clásico):

Tienes este texto (cópialo en tu código):
texto = "manzana banana manzana fresa banana manzana uva"

Primero, convierte ese texto en una lista de palabras usando texto.split(). (Investiga o prueba qué hace .split() si no lo sabes, es muy intuitivo).
Usa un Diccionario para contar cuántas veces aparece cada fruta.
La lógica es: Recorres la lista. Si la fruta ya está en el diccionario, sumas 1 a su valor. Si no está, la creas con valor 1.
Resultado esperado al imprimir el diccionario: {'manzana': 3, 'banana': 2, 'fresa': 1, 'uva': 1}.

***Este segundo ejercicio es una pregunta típica de entrevista técnica en Google o Amazon. ¡A por ello!***