# 📘 Clase 3: Control de Flujo (Tomando Decisiones)
Hasta ahora, tus programas han sido líneas rectas: empiezan en la línea 1 y terminan en la última, ejecutando todo siempre. Pero el software real necesita tomar decisiones.

## 1. La Estructura if, elif, else
En Python, usamos estas palabras clave para bifurcar el camino del código.

    if (si...): Evalúa una condición. Si es True, ejecuta el bloque de código indentado debajo.

    elif (si no, si...): Si el if anterior falló, prueba esta nueva condición. Puedes tener tantos elif como quieras.

    else (si no...): Si ninguna de las condiciones anteriores se cumplió, ejecuta este bloque final. Es opcional.

## 2. La Indentación (Sangría)
***⚠️ Atención: En Python, los espacios importan. A diferencia de otros lenguajes que usan llaves {}, Python usa la sangría (generalmente 4 espacios o 1 tabulador) para saber qué código pertenece a qué bloque. Si no indentas correctamente, el programa fallará (IndentationError).***

## 3. Operadores de Comparación y Lógicos
Para tomar decisiones, necesitas comparar valores:

| Operador | Significado | Ejemplo | Resultado |
| :---: | :---: | :---: | :---: |
| == | Igual a | 5 == 5 | True |
| != | Diferente de | 5 != 3 | True |
| > | Mayor que | 5 > 10 | False |
| < | Menor que | 2 < 4 | True |
| >= | Mayor o igual | 5 >= 5 | True |
| and | Y (ambos ciertos) | True and False | False |
| or | O (al menos uno cierto) | True or False | True |
| not | Negación | not True | False |

## 💻 Ejemplos Prácticos
Observa cómo la indentación define qué se ejecuta y qué no:

    edad = int(input("¿Cuántos años tienes? "))

    if edad >= 18:
        print("Eres mayor de edad.")
        print("Puedes acceder al sistema.") # Pertenece al if
        
    elif edad > 12:
        print("Eres un adolescente.")
        print("Acceso limitado.") # Pertenece al elif

    else:
        print("Eres un niño.")
        print("Acceso denegado.") # Pertenece al else

    print("Fin del programa.") # Esto se ejecuta SIEMPRE, porque no está indentado

## 📝 Ejercicios de Clase 3
Para dominar el flujo, resuelve estos problemas lógicos:

### El Portero de la Discoteca:

Pide la edad del usuario.

Si tiene menos de 18, imprime: "Lo siento, no puedes entrar".

Si tiene entre 18 y 65 (inclusive ambos), imprime: "Bienvenido, diviértete".

Si tiene más de 65, imprime: "Acceso VIP concedido".

Pista: Usa operadores lógicos o el encadenamiento de comparadores (18 <= edad <= 65).

### Calculadora de Descuentos:

Pide el monto de una compra.

Si la compra es mayor a $1000, aplica un 20% de descuento.

Si la compra es mayor a $500 (pero menor o igual a 1000), aplica un 10% de descuento.

Si es menor a $500, no hay descuento.

Imprime el monto original, el descuento aplicado (en dinero) y el total final.

### Identificador de Números:

Pide un número entero al usuario.

Determina si es Par o Impar (Usa el operador módulo %).

Determina si es Positivo, Negativo o Cero.

Imprime un resumen: "El número es Par y Negativo" (ejemplo).

Espero tu código. Presta mucha atención a la indentación.