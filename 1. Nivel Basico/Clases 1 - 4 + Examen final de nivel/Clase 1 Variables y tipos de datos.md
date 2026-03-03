# 📘 Clase 1: Variables y Tipos de Datos Primitivos
En Python, todo gira en torno a los datos. Para empezar a programar, necesitas saber cómo almacenar información y qué "forma" tiene esa información.

## 1. Variables
    Una variable es como una etiqueta que le pones a un valor para poder usarlo después. A diferencia de otros lenguajes, en Python no necesitas declarar el tipo de dato explícitamente; el lenguaje lo infiere (esto se llama tipado dinámico).

    Reglas para nombrar variables:

        Deben empezar con una letra o guion bajo (_).

        No pueden empezar con números.

        Se recomienda usar snake_case (palabras en minúsculas separadas por guiones bajos, ej: mi_variable).

## 2. Tipos de Datos Primitivos:
    Son los bloques de construcción más básicos:

    Integer (int): Números enteros (ej: 5, -10, 2023).

    Float (float): Números con decimales (ej: 3.14, 2.5, -0.01).

    String (str): Cadenas de texto. Deben ir entre comillas simples ' ' o dobles " " (ej: "Hola", 'Python').

    Boolean (bool): Valores lógicos. Solo pueden ser True (Verdadero) o False (Falso). Nota que la primera letra es mayúscula.

## 3. La función print()
    Es tu herramienta principal para ver resultados en la consola. Muestra lo que pongas dentro de los paréntesis.

## 💻 Ejemplos Prácticos: Analiza el siguiente código:

        Asignación de variables
        nombre_curso = "Maestría en Python"  # Esto es un String (str)
        cantidad_alumnos = 1                 # Esto es un Integer (int)
        precio_curso = 0.0                   # Esto es un Float (float)
        esta_activo = True                   # Esto es un Boolean (bool)

        Uso de print para mostrar valores
        print(nombre_curso)
        print(cantidad_alumnos)

        Podemos imprimir varios valores separados por comas
        print("El precio es:", precio_curso)

        Verificar el tipo de dato con type()
        print(type(esta_activo)) # Salida: <class 'bool'>

## 📝 Ejercicios de Clase 1
Para avanzar a la siguiente lección, debes resolver estos ejercicios correctamente. Escribe tu código solución para cada punto.

Identidad: Crea tres variables: nombre (tu nombre), edad (tu edad como número entero) y altura (tu altura aproximada en metros como float). Usa print() para mostrar una frase que diga: "Soy [nombre], tengo [edad] años y mido [altura] metros".

Matemática Simple: Crea dos variables numéricas, numero_a con valor 50 y numero_b con valor 10. Crea una tercera variable resultado que contenga la suma de ambos. Imprime resultado.

Análisis de Tipo: Si escribo la variable codigo = "123", ¿Qué tipo de dato es? ¿Es un número (int) o un texto (str)? Explica por qué e indica cómo verificarlo con código.

Espero tus respuestas. (Para saber la respuesta, revisar el archivo Ejercicios de Clase 1.py, es recomendable practicar por uno mismo antes de ver la respuesta)
