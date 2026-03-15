import time

class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.fin = time.time()
        tiempo_total = self.fin - self.inicio
        print(f"-> [EXIT] El bloque de codigo tardo {tiempo_total} sengundos en ejecutarse")

with Temporizador() as tiempo:
    print("Iniciando proceso")
    numero = 0
    for i in range(1,10000000):
        numero = numero + i
        print(numero)
        time.sleep(2)
print("Proceso terminado")

'''
Este ejercicio es una trampa, dado que el bucle se ejecuta 10000000 veces,
se tardaria 20000000 segundos en ejecutarse, es decir, mas de 231 dias.

Si se desea ejecutar de todas maneras sin cambiar el bucle y ver si
[EXIT] funciona, dentro del terminal se debe precionar  CTRL + C para detener
la ejecucion del programa.

Esto mostrara dos cosas:
1. El tiempo que tardo en ejecutarse el bucle.
2. El mensaje de error que se genero al detener la ejecucion del programa.

Si el programa se ejecuta normalmente, es decir, sin detener la ejecucion
del programa, se mostrara el mensaje de error que se genero al detener la
ejecucion del programa, sin mostrar el tiempo que tardo en ejecutarse el bucle.

Si te salio [EXIT] antes de "KeyboardInterrupt", felicidades, tu codigo
esta correcto, si no, compara tu codigo con este ejercicio
'''