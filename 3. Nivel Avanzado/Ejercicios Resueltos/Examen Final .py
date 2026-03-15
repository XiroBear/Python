import threading
import time

#El generador
def generar_archivos(cantidad):
    for i in range(1, cantidad + 1):
        yield f"datos_{i}.csv"

#El decorador
def auditar_proceso(funcion_original):
    def funda(nombre_archivo):
        print(f"-> Iniciando auditoria del archivo {nombre_archivo}...")
        funcion_original(nombre_archivo)
        print(f"-> Auditoria finalizada del archivo {nombre_archivo}")
    return funda

#La funcion principal
@auditar_proceso
def procesar_datos(nombre_archivo):
    time.sleep(2)
    print(f"-> Archivo {nombre_archivo} procesado.")

#Context Manager
class conexionServidor:
    def __enter__(self):
        print("Conectando al servidor...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Desconectando del servidor.")

#La concurrencia
with conexionServidor():
    hilos = []
    for archivo in generar_archivos(5):
        hilo = threading.Thread(target=procesar_datos, args=(archivo,))
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()