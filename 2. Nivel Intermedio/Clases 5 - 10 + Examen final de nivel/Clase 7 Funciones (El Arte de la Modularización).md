# Clase 7 Funciones (El Arte de la Modularización)

Hasta ahora, tu código es un bloque largo de instrucciones (programación secuencial). Si quieres repetir la lógica de la "Agenda" en otro programa, tendrías que copiar y pegar todo el código. 

***Eso es ineficiente y propenso a errores.***

Las Funciones te permiten encapsular código en bloques reutilizables. Es como crear tus propios comandos personalizados. 

## 1.Definición (def)
Usamos la palabra clave def seguida del nombre de la función y paréntesis.

    def saludar():
        print("¡Hola! Bienvenido al sistema.")

    # Para usarla, debemos "llamarla" o "invocarla":
    saludar() 

## 2. Parámetros y Argumentos
Las funciones son más útiles si pueden recibir datos para trabajar.
Parámetros: Son las variables que definimos en la función.
Argumentos: Son los valores reales que enviamos al llamar la función.

    def saludar_persona(nombre, edad):  # 'nombre' y 'edad' son parámetros
        print(f"Hola {nombre}, tienes {edad} años.")

    saludar_persona("Fabrizio", 31)     # "Fabrizio" y 31 son argumentos

## 3. El Retorno (return) - Concepto Crítico
Hasta ahora solo hemos usado print dentro de funciones. Pero en la vida real, una función suele procesar un dato y devolver un resultado para que el programa principal lo use.

print solo muestra texto en pantalla (para el humano).
return devuelve el dato al programa (para la computadora).

    def sumar(a, b):
        resultado = a + b
        return resultado  # Devuelve el valor, no lo imprime

    # Guardamos el resultado en una variable
    total = sumar(10, 5) 
    print(f"La suma es: {total}")

## 4. Scope (Alcance de las Variables)
Variables Locales: Las que creas dentro de una función solo existen allí. Si intentas usarlas fuera, dará error.
Variables Globales: Las que creas fuera, pueden ser leídas dentro (pero modificarlas requiere cuidado).

## 💻 Ejemplo Práctico: Refactorizando con Funciones
Mira cómo convertimos un cálculo de área en una función reutilizable.
    # Definición de la función
    def calcular_area_rectangulo(base, altura):
        area = base * altura
        return area

    # Programa principal
    print("--- Calculadora Geométrica ---")
    b = float(input("Base: "))
    h = float(input("Altura: "))

    # Llamamos a la función y guardamos lo que devuelve
    superficie = calcular_area_rectangulo(b, h)

    print(f"El área es: {superficie} metros cuadrados.")

## 📝 Ejercicios de Clase 7
Vamos a modularizar tu pensamiento.

1. Calculadora Modular:
Crea 4 funciones simples: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b). Cada una debe retornar el resultado.
***Ojo con la división: si b es 0, debe retornar None o imprimir un error (tú decides la lógica).***
Crea un menú principal que pida dos números y la operación deseada, y llame a la función correspondiente.
2. Verificador de Palíndromos:
Un palíndromo es una palabra que se lee igual al revés (ej: "radar", "neuquen", "reconocer").
Crea una función es_palindromo(palabra) que reciba un texto.
Debe retornar True si es palíndromo y False si no lo es.
***Pista: En Python, puedes invertir un string con texto[::-1].***
En el bloque principal, pide una palabra al usuario y usa tu función para decirle si es o no palíndromo.
3. Conversor de Temperatura:
Crea una función celsius_a_fahrenheit(grados) que retorne la conversión ($F = C \times 1.8 + 32$).
Pide al usuario los grados Celsius e imprime el resultado usando la función.

***Nota: A partir de ahora, intenta que tu código principal (el menú, los inputs) esté separado de las definiciones de tus funciones.***
¡A codear!