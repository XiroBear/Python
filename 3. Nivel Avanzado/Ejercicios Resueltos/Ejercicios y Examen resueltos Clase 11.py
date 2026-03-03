#1
usuario_logeado = True #Se puede poner False para probar el else

#2, 3 y 4
def verificar_sesion(funcion_original):
    def funda():
        if usuario_logeado: #Se valida si es True, si se quiere validar si es False, se debe poner if not usuario_logeado
            funcion_original()
        else:
            print("ACCESO DENEGADO")
    #5
    return funda

#6
@verificar_sesion
def login():
    print("Bienvenido al sistema")

#7
login()
