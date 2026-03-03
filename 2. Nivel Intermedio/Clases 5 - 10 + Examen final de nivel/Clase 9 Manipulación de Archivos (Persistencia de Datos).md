# 📘 Clase 9: Manipulación de Archivos (Persistencia de Datos)
Hasta este momento, cada vez que cierras tu programa, todos los datos se pierden. Las listas se vacían, los diccionarios se borran y el saldo del cajero vuelve a cero. Es hora de que tus programas tengan memoria permanente.

En Python, manejar archivos de texto (como .txt o .csv) es increíblemente sencillo.

## 1. Los Modos de Apertura
Para trabajar con un archivo, primero debes "abrirlo" y decirle a Python qué quieres hacer con él usando una letra clave:

    'r' (Read / Leer): Abre el archivo solo para leer. (Si el archivo no existe, da error).

    'w' (Write / Escribir): Abre el archivo para escribir. ¡Peligro! Si el archivo ya existe, borra todo su contenido previo y lo sobrescribe. Si no existe, lo crea.

    'a' (Append / Añadir): Abre el archivo para agregar texto al final. No borra lo anterior. Si no existe, lo crea.

## 2. La forma tradicional (No recomendada)

    archivo = open("datos.txt", "w")
    archivo.write("Hola mundo")
    archivo.close() # CRÍTICO: Si olvidas esta línea, el archivo puede corromperse.

## 3. La forma Profesional: El bloque with (Context Manager)
Como los programadores somos humanos y olvidamos poner .close(), Python introdujo la palabra clave with. Esta estructura abre el archivo, ejecuta tu código y lo ***cierra automáticamente*** en cuanto termina la indentación, incluso si ocurre un error entre medias.

    # ESCRITURA (Sobrescribiendo)
    with open("mi_archivo.txt", "w") as archivo:
        archivo.write("Esta es la primera línea.\n") # \n es un salto de línea (Enter)
        archivo.write("Esta es la segunda línea.\n")

    # LECTURA
    with open("mi_archivo.txt", "r") as archivo:
        contenido = archivo.read() # Lee todo el archivo de golpe
        print("El archivo dice:")
        print(contenido)

## 4. Leer línea por línea
Si el archivo es muy grande, leerlo de golpe (.read()) puede agotar la memoria de tu computadora. Es mejor leerlo línea por línea:

    with open("mi_archivo.txt", "r") as archivo:
        for linea in archivo:
            # Usamos .strip() para limpiar saltos de línea extra y espacios vacíos
            print(f"Línea leída: {linea.strip()}")

## 📝 Ejercicios de Clase 9
Vamos a dar memoria a tus programas. Te recomiendo crear una carpeta específica para estos ejercicios, ya que empezarás a generar archivos .txt.

1. El Diario de Vida (Escritura con Append):

Crea un programa que pida al usuario que escriba un pensamiento o frase (input).

Abre (o crea) un archivo llamado diario.txt en modo 'a' (Append).

Escribe la frase del usuario en el archivo, asegurándote de añadir un salto de línea \n al final para que la próxima frase quede abajo.

El programa debe confirmar: "Pensamiento guardado.". (Puedes correr este programa varias veces y ver cómo el archivo crece).

2. El Lector de Registros (Lectura Segura):

Escribe un script diferente que intente leer el archivo diario.txt e imprimir todas sus líneas.

El Reto Ninja: Envuelve tu bloque with open(...) en un try / except. Si el archivo diario.txt aún no existe (porque borraste el archivo por accidente), Python arrojará un FileNotFoundError. Atrápalo e imprime: "Error: El diario aún no ha sido creado."

¡Adelante, dota a tu código de memoria persistente!