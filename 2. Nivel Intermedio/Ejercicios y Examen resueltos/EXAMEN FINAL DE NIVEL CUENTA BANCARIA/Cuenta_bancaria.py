class CuentaBancaria:
    def __init__ (self, titular:str="null",saldo:int=0):
        self.titular=titular
        self.saldo=saldo
    
    def depositar(self,cantidad):
        try:
            if cantidad > 0:
                self.saldo += cantidad
                with open("auditoria.txt", 'a') as archivo:
                    archivo.write(f"-> Se abono el monto de ${cantidad} a su cuenta\n")
                self._guardar_saldo()
                input(f"Se abono el monto de ${cantidad} a su cuenta\nPresione Enter para continuar")
            else:
                input("El monto a depositar debe ser mayor a 0\nPresione Enter para continuar")
        except TypeError:
            input("Error: El valor ingresado debe ser un numero entero\nPresione Enter para continuar")
    
    def retirar(self,cantidad):
        try:
            if cantidad > 0:
                if self.saldo >= cantidad:
                    self.saldo -= cantidad
                    with open("auditoria.txt", 'a') as archivo:
                        archivo.write(f"-> Se retiro el monto de ${cantidad} de su cuenta\n")
                    self._guardar_saldo()
                    input(f"Se retiro el monto ${cantidad} de su cuenta\nPresione Enter para continuar")
                else:
                    input("Saldo insuficiente para el retiro\nPresione Enter para continuar")
            else:
                input("El monto a retirar debe ser mayor a 0\nPresione Enter para continuar")
        except TypeError:
            input("Error: El valor ingresado debe ser un numero entero\nPresione Enter para continuar")
    
    def _guardar_saldo(self): # al poner solo un _ esto indica que solo esta clase puede ocupar este metodo, si fueran dos __ esto indicaria que solo esta clase y sus hijos pueden ocuparla
        nombre_archivo = f"Cliente_saldo_{self.titular}.txt"
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(str(self.saldo))
    def obtener_saldo(self):
        return self.saldo
