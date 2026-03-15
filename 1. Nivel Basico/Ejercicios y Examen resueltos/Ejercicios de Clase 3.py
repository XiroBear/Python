#El Portero de la Discoteca

edad = int(input("¿Cuantos años tienes?: "))

#Control de flujo

if edad > 65:
    print("Acceso VIP concedido")
elif edad >= 18 and edad <= 65:
    print("Bienvenido, diviertete")
else:
    print("Lo siento, no puedes entrar")

# Calculadora de Descuentos

monto_de_compra = float(input("Ingrese el monto de una compra: "))

#Control de flujo

if monto_de_compra > 1000:
    monto_final= monto_de_compra * 0.80
    print(f"Felicidades, tienes un descuento del 20%, el monto final es de ${round(monto_final, 2)} a pagar")
elif monto_de_compra > 500 and monto_de_compra <= 1000:
    monto_final = monto_de_compra * 0.90
    print(f"Felicidades, tienes un descuento del 10%, el monto final es de ${round(monto_final, 2)} a pagar")
else:
    print(f"La compra no tiene descuento, el monto final es de ${monto_de_compra} a pagar")

#Identificador de Números

numero = float(input("Ingrese un numero: "))

#Control de flujo

if numero % 2 == 0:
    x = "par"
else:
    x ="impar"

if numero > 0:
    y = "positivo"
else:
    y = "negativo"

if numero == 0:
    print(f"El numero es cero")
else:
    print(f"El numero es {x} y es {y}")