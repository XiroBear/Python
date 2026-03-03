# Objetivo: Crear un simulador de cajero automático (ATM) funcional.

## Requerimientos del Sistema:

    Seguridad (Inicio):
    El programa debe tener una variable con una clave secreta (ej: "1234").
    Al iniciar, debe pedir la clave al usuario.
    El usuario tiene 3 intentos. Si falla los 3, el programa imprime "Tarjeta bloqueada" y termina.
    Si acierta, da la bienvenida y pasa al menú.

## El Menú Principal (Bucle Infinito):

    Una vez dentro, el usuario tiene un saldo inicial de $1000.
    El programa debe mostrar un menú con 4 opciones y pedir al usuario que elija una:
    Consultar saldo.
    Retirar dinero.
    Depositar dinero.
    Salir.

## Lógica de las Opciones:

    Opción 1: Muestra el saldo actual.
    Opción 2 (Retiro): Pide el monto.
    Si el monto es mayor al saldo, dice "Saldo insuficiente".
    Si el monto es negativo, dice "Error".
    Si es correcto, resta el monto y muestra el nuevo saldo.
    Opción 3 (Depósito): Pide el monto.
    Si es negativo, dice "Error".
    Si es correcto, suma el monto y muestra el nuevo saldo.
    Opción 4: Imprime "Gracias por usar nuestro banco" y termina el programa (rompe el bucle).
    Opción inválida: Si el usuario pone "5" u otra cosa, debe decir "Opción no válida" y volver a mostrar el menú.

## Condiciones de Aprobación:

    El código debe correr sin errores de sintaxis.
    Debe manejar lógica de if/else, bucles while, y operadores matemáticos.
    No puedes usar librerías externas.

Tómate tu tiempo. Este código define si estás listo para el siguiente nivel. ¡Éxito!