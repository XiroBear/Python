# 📘 Clase 8: Manejo de Errores y Excepciones (try / except)
En tu menú usaste .if numero1.isdigit(): para prevenir errores. En programación, a eso se le llama el enfoque LBYL (Look Before You Leap - Mira antes de saltar).

Sin embargo, Python fue diseñado bajo la filosofía EAFP (Easier to Ask for Forgiveness than Permission - Es más fácil pedir perdón que permiso). En lugar de comprobar todo antes de ejecutar, intentamos ejecutar el código y, si falla, "capturamos" el error para que el programa no explote.

Para eso usamos el bloque try / except.

## 1. Sintaxis Básica
***try:*** "Intenta" ejecutar este bloque de código.
***except:*** Si ocurre un error en el try, no detengas el programa, ejecuta esto en su lugar.

    try:
        numero = int(input("Ingresa un número: "))
        print(f"Ingresaste el {numero}")
    except ValueError:  # Atrapa el error específico de conversión de tipos
        print("Error: No ingresaste un número válido. Intenta de nuevo.")

Con esto, ya no necesitas .isdigit() y puedes aceptar números negativos tranquilamente, porque si int("-5") funciona, pasará, y si es int("hola"), fallará y saltará al except.

## 2. Capturando Diferentes Errores
Puedes tener múltiples except para manejar distintas crisis:

    try:
        a = int(input("Numerador: "))
        b = int(input("Denominador: "))
        resultado = a / b
        print(resultado)
    except ValueError:
        print("Debes ingresar números, no texto.")
    except ZeroDivisionError:
        print("Matemáticamente imposible: No se puede dividir por cero.")
    except Exception as e:
        # Este atrapa CUALQUIER otro error inesperado
        print(f"Ha ocurrido un error catastrófico: {e}")

## 3. Los bloques else y finally (Opcionales)
***else:*** Se ejecuta SOLO si el try fue un éxito (no hubo errores).

***finally:*** Se ejecuta SIEMPRE, haya habido error o no (útil para cerrar archivos o conexiones a bases de datos).

## 📝 Ejercicios de Clase 8
Vamos a robustecer tu código usando la filosofía de Python. Crea un archivo para resolver lo siguiente:

### El Formulario Indestructible:

Escribe un programa que, usando un bucle while True, pida la edad del usuario.

Usa try/except para convertir el input a int.

Si el usuario ingresa texto (ej: "veinte") o decimales, debe atrapar el ValueError y decirle "Entrada inválida. Ingrese un número entero." y volver a preguntarle.

Si el usuario ingresa un número correcto, el bucle se rompe (break) y el programa imprime "Edad registrada: [X]".

### El Buscador A Ciegas:

Tienes esta lista: catalogo = ["TV", "Radio", "Laptop", "Mouse"].

Pide al usuario que ingrese un número de índice para ver el producto.

Usa try/except para atrapar dos errores posibles:

    ValueError: Por si no ingresa un número.

    IndexError: Por si ingresa un número mayor a los elementos que hay (ej: índice 10).

    Muestra el producto si tiene éxito.

¿Estás listo para escribir código a prueba de fallos? Adelante con la tarea.