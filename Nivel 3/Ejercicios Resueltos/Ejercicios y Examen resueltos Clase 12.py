#La cuenta regresiva
def cuenta_regresiva(inicio):
    while inicio >= 0:
        yield inicio
        inicio -= 1
    yield "Despegue!"

for conteo in cuenta_regresiva(5):
    print(conteo)

#El Generador Infinito
def generador_infinito():
    numero = 5
    while True:
        yield numero
        numero +=5
mi_gen = generador_infinito() #Guardamos la funcion en una variable e la impimimos de manera segura
print(next(mi_gen))
print(next(mi_gen))
print(next(mi_gen))