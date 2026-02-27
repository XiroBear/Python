# La sumatoria

N = int(input("Ingrese un numero entero: "))
X = 0

for i in range (1, N + 1):
    X = X + i
print(X)

# El Validador Insistente (While):

intento = 1
while intento != 0:
    numero = float(input("Ingrese un numero positivo: "))
    if numero <= 0:
        print("Error, debe ser positivo")
    else:
        print(f"Gracias, numero aceptado: {numero}")
        intento = 0

# Tabla de Multiplicar

numero = int(input("Ingrese un numero entero para mostrar su tabla de multiplicar: "))

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")