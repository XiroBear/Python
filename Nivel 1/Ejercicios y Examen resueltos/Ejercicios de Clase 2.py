#Entrada del usuario
X = float(input("Ingrese el total de la cuenta: "))

#Ingreso de propina
Y = int(input("Ingrese el porcentaje de la propina: "))

#Total de la propina

A = (X * (Y / 100))

#Calculo entre el monto y la propina
Z = X + A

#resultado final
print(f"Monto: ${X}, Propina: ${A}, Total a Pagar: ${round(Z,2)}")

#Repartidor de Manzanas (Uso de // y %)

#variables
manzanas_totales = 46
niños = 4

#Calculo de manzanas por niños

manzanas_por_niños = manzanas_totales // niños

manzanas_sobrantes = manzanas_totales % niños
print(f"Cada niño recibira {manzanas_por_niños} manzanas")
print(f"Sobrarán {manzanas_sobrantes} manzana(s)")

print(f"La variable 'manzanas_totales' tiene el valor de {manzanas_totales} manzanas, y la variable 'niños' tiene el valor de {niños} niños.")
print(f"Usando el operador // se peude obtener el valor de cuantas manzanas recibira cada niño,\nAl usar el operador % se puede obtener el calculo de las manzanas sobrantes")

"""
# Depuración Mental (Sin código):

Si ejecuto x = input("Ingresa número: ") y el usuario escribe 10.

Luego ejecuto resultado = x * 2.

¿Qué valor tendrá resultado? ¿Será el número 20 o algo diferente? Explica tu razonamiento.

Respuesta: 
Dara como resutado 1010, pues el valor de 'x' se mostrara dos veces

"""