Estudiante, has llegado a un momento crucial. Estás a punto de enfrentarte al concepto más importante de la programación moderna. Si dominas esto, dejarás de ser un simple escritor de scripts y te convertirás en un Arquitecto de Sistemas.

Nivel actual: Intermedio

# 📘 Clase 10: Programación Orientada a Objetos (POO)
Hasta ahora, has programado usando el paradigma "Estructurado" (variables por un lado, funciones por otro). La POO (o OOP en inglés) cambia las reglas del juego: agrupa los datos (variables) y el comportamiento (funciones) en una sola entidad llamada Objeto.

## 1. Clases y Objetos (El Molde y el Producto)
Clase (Class): Es el plano o molde. Define qué características y acciones tendrá algo, pero no es el objeto en sí. (Ej: El plano de una casa).

Objeto (Object): Es la materialización de ese plano. (Ej: La casa real ya construida). Puedes crear múltiples objetos a partir de una sola clase.

## 2. Sintaxis: La Clase y el Constructor (__init__)
En Python, las clases se escriben con PascalCase (cada palabra con mayúscula, sin guiones bajos).

El método __init__ (con dobles guiones bajos) es el Constructor. Es la primera función que se ejecuta automáticamente cuando creas un objeto. Su trabajo es inicializar los atributos (variables) del objeto.

## 3. El misterioso self
En la POO, self es la forma que tiene el objeto de referirse a sí mismo. Cuando dices self.nombre, le estás diciendo a Python: "Guarda esto en el atributo 'nombre' de este objeto en particular".

    # 1. Definimos el Molde (La Clase)
    class Perro:
        # El Constructor: Define los atributos iniciales
        def __init__(self, nombre, raza, edad):
            self.nombre = nombre  # Atributo del objeto
            self.raza = raza
            self.edad = edad

        # Un Método (una función que pertenece a la clase)
        def ladrar(self):
            # Usamos self para acceder a los datos de ESTE perro
            print(f"{self.nombre} dice: ¡Guau, guau!")

        def cumplir_anios(self):
            self.edad += 1
            print(f"{self.nombre} ahora tiene {self.edad} años.")

    # 2. Creamos los Objetos (Instanciación)
    perro1 = Perro("Firulais", "Mestizo", 3)
    perro2 = Perro("Rex", "Pastor Alemán", 5)

    # 3. Usamos los objetos
    print(f"Mi perro se llama {perro1.nombre}")
    perro1.ladrar()         # Salida: Firulais dice: ¡Guau, guau!
    perro2.cumplir_anios()  # Rex pasa a tener 6 años

Como ves, perro1 y perro2 son independientes. Ambos son de la clase Perro, pero tienen sus propios datos y su propia "vida".

## 📝 Ejercicios de Clase 10
Este es tu último desafío antes del Examen Final del Nivel Intermedio. Vamos a crear un videojuego RPG de texto muy básico.

1. El Héroe y el Monstruo:

Crea una clase llamada Personaje.

Su método __init__ debe recibir y guardar tres atributos: nombre (string), vida (int, ej: 100) y ataque (int, ej: 15).

Crea un método llamado recibir_danio(self, cantidad) que reste la cantidad recibida a la vida del personaje. Si la vida baja de 0, que se quede en 0.

Crea un método llamado esta_vivo(self) que retorne True si la vida es mayor a 0, y False si es 0.

2. La Arena de Combate (Fuera de la clase):

Instancia (crea) dos objetos de tu clase Personaje:

heroe = Personaje("Arturo", 100, 20)

orco = Personaje("Orco Feo", 80, 10)

Haz que el orco reciba daño usando el poder de ataque del héroe: orco.recibir_danio(heroe.ataque).

Imprime la vida restante del orco.

Verifica si el orco está vivo imprimiendo el resultado del método orco.esta_vivo().

Diseña tus moldes con cuidado. ¿Estás listo para dominar la Programación Orientada a Objetos? Espero tu código.