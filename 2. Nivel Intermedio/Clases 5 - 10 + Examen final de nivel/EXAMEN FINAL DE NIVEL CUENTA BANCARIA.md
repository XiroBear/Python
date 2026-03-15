# 🏆 FIN DEL NIVEL INTERMEDIO
Has dominado los pilares estructurales de Python:

    Colecciones: Listas y Diccionarios.
    Modularidad: Funciones y Módulos.
    Robustez: Manejo de Errores (try/except).
    Persistencia: Manejo de Archivos (.txt).
    Arquitectura: Programación Orientada a Objetos (Clases y Objetos).
    Estás a un paso del Nivel Experto, donde te esperan Generadores, Decoradores y Concurrencia. Pero las reglas son absolutas: para certificar este nivel, debes superar la Prueba de Hierro.

# 💀 EXAMEN FINAL DE NIVEL: "El Sistema Bancario Persistente"
Objetivo: Construir una aplicación de consola orientada a objetos que integre POO, manejo de errores y archivos.

Requerimientos del Sistema:

La Clase CuentaBancaria:

Debe tener un constructor que reciba titular (nombre) y saldo_inicial.

Debe tener un método depositar(self, monto) que sume el monto al saldo.

Debe tener un método retirar(self, monto). Si el monto es mayor al saldo, debe imprimir "Fondos insuficientes" y no restar el dinero. Si hay fondos, se resta.

Debe tener un método obtener_saldo(self) que retorne el saldo actual.

El Sistema de Auditoría (Archivos):

Cada vez que se ejecute un depósito o retiro exitoso en los métodos de la clase, el programa debe abrir un archivo llamado historial.txt en modo append ('a') y guardar un registro de la transacción.
Ejemplo de línea a guardar: "Se depositó $50. Nuevo saldo: $150." o "Se retiró $20. Nuevo saldo: $130."

La Interfaz de Usuario (El Menú):

    Al iniciar, el programa crea un objeto fijo: mi_cuenta = CuentaBancaria("TuNombre", 0).

Implementa un menú infinito (while True) con 3 opciones:

    Depositar.
    Retirar.
    Salir.

***bligatorio: Usa try/except cuando pidas los montos al usuario. Si el usuario escribe texto (ej: "cien") en lugar de un número al depositar o retirar, el programa debe atrapar el error, avisar "Monto inválido" y no colapsar.***

Condiciones de Aprobación:

    Superar el 95% de éxito.
    El código debe integrar todo lo aprendido. Un fallo en el manejo del archivo o un colapso del programa por ingresar una letra resultará en suspenso automático.
    Tómate tu tiempo. Planifica tu arquitectura antes de escribir la primera línea de código. ¡Demuestra que estás listo para ser un Experto!