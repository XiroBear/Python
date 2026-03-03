# 📘 Clase 12: Generadores (El Arte de la Eficiencia)
Hasta ahora, cuando querías trabajar con muchos datos (por ejemplo, los números del 1 al 10,000), usabas listas. El problema de las listas es que cargan todos los elementos en la memoria RAM al mismo tiempo. Si pides una lista de un billón de números, tu computadora colapsará.

Aquí entran los **Generadores**.

Un generador no guarda todos los datos en la memoria. En su lugar, "recuerda" en qué punto se quedó y genera el siguiente valor solo cuando se lo pides (uno a la vez, como gotas de agua en lugar de un cubo entero).

***La palabra mágica***: yield (Producir / Ceder)

Para crear un generador, escribes una función normal, pero en lugar de usar return, usas yield.

    return: Devuelve el valor, destruye la función y borra sus variables locales.

    yield: Devuelve el valor, pausa la función, guarda su estado exacto, y espera a que le pidan el siguiente valor.

***Sintaxis y Uso***:

    def contador_simple():
        print("Iniciando generador...")
        yield 1
        print("Pausado. Retomando para el 2...")
        yield 2
        print("Pausado. Retomando para el 3...")
        yield 3

    # Guardamos el generador en una variable
    mi_gen = contador_simple()

    # Para pedirle el siguiente valor, usamos la función integrada next()
    print(next(mi_gen)) # Salida: Iniciando generador... \n 1
    print(next(mi_gen)) # Salida: Pausado. Retomando para el 2... \n 2
    print(next(mi_gen)) # Salida: Pausado. Retomando para el 3... \n 3
    # Si hacemos otro next(mi_gen) aquí, dará un error StopIteration porque ya no hay más yields.

***El verdadero poder: Generadores con Bucles***:

Nadie escribe yield a mano 100 veces. Usamos bucles. Lo hermoso de los generadores es que puedes recorrerlos con un bucle for (el for llama a next() automáticamente por debajo de la mesa y se detiene solo cuando se acaban los datos).

    def generar_pares(limite):
        numero = 0
        while numero <= limite:
            yield numero  # Entrega el número y PAUSA aquí.
            numero += 2   # Cuando le vuelvan a pedir, arranca desde aquí.

    # Uso súper eficiente en memoria:
    for par in generar_pares(10):
        print(par) 
    # Imprime: 0, 2, 4, 6, 8, 10

## 📝 Ejercicios de Clase 12

Demuestra tu dominio sobre la memoria RAM creando estos generadores:

### La Cuenta Regresiva:

Crea una función generadora llamada cuenta_regresiva(inicio).
Debe usar un bucle while para hacer yield del número actual e ir restando 1 en cada iteración hasta llegar a 0 (inclusive).
Fuera de la función, usa un bucle for para consumir el generador desde el número 5 hasta el 0, imprimiendo cada número.
Al final, imprime "¡Despegue!".

### El Generador Infinito (El verdadero terror de las RAMs sin generadores):

Crea un generador llamado multiplos_de_cinco().
Este generador NO debe tener límite. Usa un while True: para generar 5, 10, 15, 20, etc., de forma infinita usando yield.
Peligro: Si lo metes en un for normal, tu pantalla se llenará de números por siempre.
Para probarlo con seguridad: Crea el generador, guárdalo en una variable gen = multiplos_de_cinco(), y usa tres veces la función print(next(gen)) manuales para imprimir solo los primeros tres múltiplos (5, 10 y 15).

Aprender a no saturar la memoria de un servidor es fundamental para un Experto.