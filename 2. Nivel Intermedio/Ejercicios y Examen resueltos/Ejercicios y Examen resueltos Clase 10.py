class Personaje:
    def __init__ (self, nombre:str="null", vida:int = 0, ataque:int = 0):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def recibir_daño(self, daño:int):
        self.vida -= daño
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} fue derrotado")
        else:
            print(f"{self.nombre} recibio un daño de {daño} y le quedan {self.vida} puntos de vida\n{self.nombre} esta vivo")
    
    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con {self.ataque} puntos de daño")
        objetivo.recibir_daño(self.ataque)

Heroe = Personaje("Arturo", 100, 20)
orco = Personaje("Orco feo", 80, 10)


orco.recibir_daño(Heroe.ataque)
print(orco.esta_vivo())