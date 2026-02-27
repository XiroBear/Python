# Clase 4: Bucles (Ciclos)
Hasta ahora, tu código se ejecuta una vez y termina. Pero el poder de la computación radica en realizar tareas repetitivas millones de veces sin cansarse. Para eso existen los Bucles.

## 1. El Bucle for (Para...)  
Se usa cuando sabemos cuántas veces queremos repetir algo o queremos recorrer una colección de cosas (como una lista de nombres o un rango de números).

La función range(inicio, fin) es su mejor amiga:

range(5): Genera 0, 1, 2, 3, 4 (El límite superior nunca se incluye).

range(1, 6): Genera 1, 2, 3, 4, 5

    # Ejemplo: Imprimir números del 1 al 5
    for i in range(1, 6):
        print(f"Contando: {i}")

## 2. El Bucle while (Mientras...)
Se usa cuando no sabemos cuántas veces se repetirá la acción, pero sí sabemos qué condición debe cumplirse para seguir. Es peligroso: si la condición nunca cambia a False, crearás un Bucle Infinito y tu programa se congelará (Ctrl+C para detenerlo manualmente).

    ## Ejemplo: Preguntar hasta que el usuario diga "si"
    respuesta = ""
    while respuesta != "si":
        respuesta = input("¿Quieres terminar? (escribe 'si'): ")
    print("¡Terminado!")

## 3. Control de Bucles: break y continue
break: Rompe el bucle inmediatamente y sale de él, sin importar si la condición se cumplió o no.

continue: Salta la iteración actual y vuelve al principio del bucle para la siguiente vuelta.

## 💻 Ejemplos Prácticos
Analiza este sistema de seguridad simulado:

    # INTENTOS DE CONTRASEÑA
    clave_secreta = "python123"
    intentos = 0

    print("--- SISTEMA DE SEGURIDAD ---")

    while intentos < 3:
        ingreso = input("Ingresa la contraseña: ")
        
        if ingreso == clave_secreta:
            print("Acceso Concedido.")
            break # Rompe el while, salimos del bucle
        else:
            print("Contraseña incorrecta.")
            intentos = intentos + 1 # Incrementamos el contador

    if intentos == 3:
        print("Has agotado tus intentos. Sistema bloqueado.")

## 📝 Ejercicios de Clase 4
Estos ejercicios son vitales. Los bucles son el corazón de los algoritmos.

La Sumatoria (Acumulador):

Escribe un programa que pida un número entero positivo N al usuario.

Usa un bucle for para sumar todos los números desde el 1 hasta N.

Ejemplo: Si ingreso 5, el programa calcula 1+2+3+4+5 y devuelve 15.

Imprime el resultado final.

El Validador Insistente (While):

Pide al usuario que ingrese un número positivo.

Si el usuario ingresa un número negativo o cero, el programa debe decirle "Error, debe ser positivo" y volver a pedirle el número.

El programa no debe avanzar hasta que el usuario obedezca.

Cuando finalmente ingrese un positivo, imprime: "Gracias, número aceptado: [X]".

Tabla de Multiplicar:

Pide un número entero al usuario (ej: 7).

Usa un bucle for para imprimir su tabla de multiplicar del 1 al 10.

Formato de salida:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

¡A trabajar!