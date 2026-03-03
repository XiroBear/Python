# 📘 Clase 14: Concurrencia Básica (Threading)
Hasta ahora, tu código es de un solo carril. Si pones un time.sleep(5), todo tu programa se congela 5 segundos. No puede hacer nada más.

En el mundo real, un servidor web no puede congelarse para todos los usuarios solo porque uno está descargando un archivo pesado. Necesitamos abrir "múltiples carriles". A esto lo llamamos Hilos (Threads).

## Importar la librería
Python trae una librería nativa para esto:

    import threading
    import time

## La Ejecución Secuencial (El problema)
Imagina esta función que simula descargar un archivo:

    def descargar(nombre_archivo):
        print(f"Empezando a descargar {nombre_archivo}...")
        time.sleep(3) # Simula que tarda 3 segundos
        print(f"¡{nombre_archivo} completado!")

    # Si hacemos esto de forma normal:
    descargar("Juego.exe")
    descargar("Pelicula.mp4")
    # Tardará 6 segundos en total, uno detrás del otro.

## La Ejecución Concurrente (La solución)
Podemos delegar cada descarga a un "trabajador" (un Hilo) independiente para que ocurran al mismo tiempo.

    # 1. Creamos los hilos (les pasamos la función SIN paréntesis y los argumentos en una tupla)
    hilo1 = threading.Thread(target=descargar, args=("Juego.exe",))
    hilo2 = threading.Thread(target=descargar, args=("Pelicula.mp4",))

    # 2. Iniciamos los hilos (aquí arranca la magia simultánea)
    hilo1.start()
    hilo2.start()

    # 3. Le decimos al programa principal que ESPERE a que terminen antes de seguir
    hilo1.join()
    hilo2.join()

    print("Todas las descargas han finalizado.")
    # ¡Tardará solo 3 segundos en total, porque se descargaron a la vez!

## 📝 Ejercicio de Clase 14
Vamos a crear un simulador de procesamiento en segundo plano.

## El Simulador de Correos:

    Crea una función enviar_correo(destinatario) que reciba un nombre (ej: "Juan").
    La función debe imprimir "Enviando correo a [destinatario]...".
    Usa time.sleep(2) para simular la latencia de red.
    Luego imprime "Correo enviado a [destinatario] con éxito".

## La Carrera Simultánea:

    Crea una lista de clientes: clientes = ["Ana", "Pedro", "Marta", "Luis"].
    El Reto: Usa un bucle for para crear y hacer .start() de un hilo (Thread) por cada cliente en la lista.
    (Opcional pero recomendado): Guarda los hilos creados en una lista vacía lista_hilos = [] (con .append()) y luego usa otro bucle for para hacer .join() a cada uno de ellos.
    Al final de tu código principal, imprime "Campaña de correos finalizada."

Si lo haces bien, verás que enviar 4 correos de 2 segundos cada uno no tardará 8 segundos, sino solo 2 segundos en total, porque todos se enviarán a la vez.

¿Te atreves a abrir la caja de Pandora del Multithreading?