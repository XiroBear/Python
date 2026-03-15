# 📘 Clase 13: Context Managers (El Control Absoluto de los Recursos)
En el Nivel Intermedio (Clase 9), aprendiste a usar la estructura with open(...) as archivo: para manejar archivos. Te dije que era "profesional" porque cerraba el archivo automáticamente, incluso si ocurría un error.

Pero, ¿qué es exactamente ese ***with***?
No es magia. Es un **Administrador de Contexto (Context Manager).**

En Python, tú puedes crear tus propios bloques ***with*** para gestionar cualquier recurso que necesite ser "abierto" y "cerrado" de forma segura (como conexiones a bases de datos, bloqueos de hilos, o temporizadores).

**1. La Anatomía Subterránea (Métodos Mágicos)**

Para que un objeto funcione con la palabra **with**, su clase debe tener definidos dos métodos mágicos (Dunder methods):

    __enter__(self): Lo que ocurre antes de entrar al bloque indentado.

    __exit__(self, exc_type, exc_val, exc_tb): Lo que ocurre después de salir del bloque indentado, sin importar si hubo un error o no. (Los tres parámetros extra sirven para atrapar errores, pero por ahora no nos preocuparemos por ellos).

**2. Creando un Context Manager desde cero**

Vamos a crear un simulador de conexión a una Base de Datos:

    class ConexionBaseDeDatos:
        def __init__(self, nombre_bd):
            self.nombre_bd = nombre_bd

        def __enter__(self):
            # Esto se ejecuta al iniciar el 'with'
            print(f"-> [ENTER] Conectando a la base de datos '{self.nombre_bd}'...")
            return self # Retornamos el objeto para usarlo con el 'as'

        def __exit__(self, tipo_error, valor_error, traza_error):
            # Esto se ejecuta SIEMPRE al salir del 'with'
            print(f"-> [EXIT] Cerrando conexión de forma segura.")
            
        def hacer_consulta(self):
            print("Obteniendo datos secretos de los clientes...")

    # --- Uso de nuestro Context Manager ---
    print("Iniciando programa.")

    with ConexionBaseDeDatos("Servidor_Financiero") as mi_bd:
        mi_bd.hacer_consulta()
        # Si aquí ocurriera un error fatal, el método __exit__ se ejecutaría igual.

    print("Programa terminado.")

Salida en consola:

    Iniciando programa.
    -> [ENTER] Conectando a la base de datos 'Servidor_Financiero'...
    Obteniendo datos secretos de los clientes...
    -> [EXIT] Cerrando conexión de forma segura.
    Programa terminado.

## 📝 Ejercicios de Clase 13
Tu misión es crear una herramienta vital para cualquier Ingeniero de Software que busca optimizar código: Un Profiler (Medidor de Tiempo de Ejecución).

***El Cronómetro Implacable:***

    Crea una clase llamada Temporizador.

    En el método __enter__(self), debes registrar el tiempo exacto de inicio. 
    
    Puedes usar la librería time y guardar el tiempo en un atributo (ej: self.inicio = time.time()). No olvides importar la librería al inicio del archivo (import time).

    En el método __exit__(self, exc_type, exc_val, exc_tb), debes capturar el tiempo final (fin = time.time()), calcular la diferencia (tiempo_total = fin - self.inicio), e imprimir: "El bloque de código tardó X segundos en ejecutarse".

***La Prueba de Estrés:***

    Fuera de la clase, usa tu nuevo administrador de contexto con la sintaxis with Temporizador():.

    Dentro del bloque with, crea un bucle for gigantesco que haga algo inútil pero pesado, como sumar números del 1 al 10,000,000 (o usa time.sleep(2) para pausar el código 2 segundos simulando un proceso largo).

    Verifica que tu temporizador mida el tiempo con precisión al salir del bloque.

Este ejercicio combina la POO con la gestión avanzada de recursos. Es una herramienta que usarás en el mundo real.