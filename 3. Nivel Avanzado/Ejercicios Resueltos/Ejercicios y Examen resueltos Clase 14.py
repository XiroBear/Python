#importar librerias
import threading
import time

#Simulado de correos:
def enviar_correo(nombre_usuario):
    print(f"Enviando correo a {nombre_usuario}")
    time.sleep(2)
    print(f"Correo enviado a {nombre_usuario}")

#La carrera simultanea:
clientes = ["Ana", "Pedro", "Marta", "Luis"]
lista_hilos = []
for i in clientes:
    hilo = threading.Thread(target=enviar_correo, args=(i,))
    lista_hilos.append(hilo)
    hilo.start() #Inicia los hilos en este bucle, o sino, deberas hacer otro bucle for solo para hilos.start(), se ahorra codigo
for i in lista_hilos:
    i.join()

print("Campaña de correos finalizada")