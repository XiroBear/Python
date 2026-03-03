# 📘 Clase 2: Operadores y Entrada de Datos (Input)
Ahora que sabes guardar datos "estáticos", es hora de hacer que el programa interactúe con el usuario y procese información.

## 1. Operadores Aritméticos
Python funciona como una calculadora potente. Además de lo básico, tiene operadores especiales que debes dominar.

| Operador | Nombre | Descripción | Ejemplo | Resultado |
| :---: | :---: | :---: | :---: | :---: |
| + | Suma | Suma dos valores | 5 + 2 | 7 |
| - | Resta | Resta dos valores | 5 - 2 | 3 |
| * | Multiplicación | Multiplica dos valores | 5 * 2 | 10 |
| / | División | Divide (siempre devuelve float) | 5 / 2 | 2.5 |
| // | División Entera | Divide y descarta los decimales | 5 // 2 | 2 |
| % | Módulo | Devuelve el resto de la división | 5 % 2 | 1 |
| ** | Potencia | Eleva un número a otro | 5 ** 2 | 25 |

***Nota: El operador Módulo (%) es vital para determinar si un número es par (resto 0 al dividir por 2) o impar.***

## 2. Entrada de Datos: input()
Para que el usuario escriba información, usamos la función input("Mensaje: ").

⚠️ Regla de Oro:
La función input() siempre devuelve un texto (str), incluso si el usuario escribe números.
Si quieres hacer matemáticas con lo que escribe el usuario, debes convertirlo (castearlo) a int o float.

    int("5") -> Convierte el texto "5" al número 5.

    float("5.5") -> Convierte el texto "5.5" al número 5.5.

    str(5) -> Convierte el número 5 al texto "5".

## 💻 Ejemplos Prácticos: Analiza cómo pedimos datos y los transformamos para operar:
    Pedir el nombre (es texto, no necesita conversión)
    nombre = input("Ingresa tu nombre: ")

    Pedir la edad (input devuelve texto, debemos convertirlo a int)
    edad_texto = input("Ingresa tu edad: ")
    edad_numero = int(edad_texto) 

    Forma abreviada (la más común)
    altura = float(input("Ingresa tu altura en m (ej 1.70): "))

    Cálculo matemático
    edad_en_dias = edad_numero * 365

    print(f"Hola {nombre}, has vivido aproximadamente {edad_en_dias} días.")
    print(f"El tipo de dato de tu altura es: {type(altura)}")

## 📝 Ejercicios de Clase 2
Aplica lo aprendido. Crea un nuevo archivo o script para resolver lo siguiente:

Calculadora de Propina:

Pide al usuario el monto total de la cuenta en un restaurante (puede tener decimales).

Pregunta qué porcentaje de propina quiere dejar (ej: 10, 15, 20). Introduce solo el número entero.

Calcula el monto de la propina y el total final a pagar.

Imprime: "Monto: $[X], Propina: $[Y], Total a Pagar: $[Z]".

Repartidor de Manzanas (Uso de // y %):

Tienes 45 manzanas (guárdalo en una variable) y quieres repartirlas equitativamente entre 4 niños (guárdalo en otra variable).

Calcula cuántas manzanas completas le tocan a cada niño.

Calcula cuántas manzanas sobran.

Imprime los resultados explicando qué es cada número.

Depuración Mental (Sin código):

Si ejecuto x = input("Ingresa número: ") y el usuario escribe 10.

Luego ejecuto resultado = x * 2.

¿Qué valor tendrá resultado? ¿Será el número 20 o algo diferente? Explica tu razonamiento.

Adelante. Espero tu solución.