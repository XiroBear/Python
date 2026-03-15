# 🚀 BIENVENIDO AL NIVEL EXPERTO
Aquí es donde se separa a los desarrolladores promedio de los verdaderos ingenieros de Python. En esta etapa, el código deja de ser solo "funcional" y pasa a ser "meta-funcional" (código que modifica otro código).

## Ruta de Aprendizaje (Experto):

***Metaprogramación I: Decoradores.***

***Eficiencia de Memoria: Generadores e Iteradores.***

***Gestión de Recursos: Context Managers (Crear tus propios with).***

***Concurrencia Básica: Tareas en segundo plano (Threading).***

## Nivel actual: Experto

## 📘 Clase 11: Decoradores desde Cero
Imagina que tienes un teléfono móvil (tu función principal). Su trabajo es hacer llamadas.
Un día decides que quieres que tu teléfono sea resistente al agua y a las caídas. Tienes dos opciones:

    Abrir el teléfono con un destornillador, soldar piezas nuevas y alterar su circuito interno (Modificar la función original, lo cual es peligroso y propenso a errores).

    Comprarle una funda protectora. La funda envuelve al teléfono. Le añade nuevas capacidades (resistencia) sin alterar ni un solo cable interno del teléfono.

Un **Decorador** es exactamente eso: una "funda" de código que envuelve a una función para darle nuevas habilidades, sin tocar el código de la función original.

Para entender cómo fabricamos esa "funda" en Python, debes aceptar tres reglas fundamentales del lenguaje:

**Regla 1: Las funciones son simples variables**
En Python, una función no es un ente mágico; es un tipo de dato, igual que un int o un str. Puedes guardarla en otra variable.

    def ladrar():
        print("Guau!")

    # Guardo la función en una variable (SIN paréntesis)
    mi_variable = ladrar 

    # Ahora mi variable hace lo mismo que la función
    mi_variable()

**Regla 2: Puedes pasar una función como parámetro a otra función**
Igual que pasas un número, puedes pasar una función para que otra la ejecute.

    def ejecutar_dos_veces(funcion_recibida):
        funcion_recibida()
        funcion_recibida()

    # Le paso la función 'ladrar' (sin paréntesis)
    ejecutar_dos_veces(ladrar) 
    # Salida: Guau! Guau!

**Regla 3: Puedes crear funciones DENTRO de funciones**
Esto es vital. Puedes anidar código.

    def fabrica_de_funciones():
        def funcion_interna():
            print("Soy una función creada aquí adentro.")
        
        return funcion_interna # Retorna la función, lista para usarse

## ⚙️ Construyendo el Decorador (La Funda)

Sabiendo esas tres reglas, vamos a construir un decorador que avise cada vez que una función se ejecuta.

**Paso 1: El molde del decorador**
Un decorador es una función que recibe otra función como parámetro.

    def avisador(funcion_original):
        # Paso 2: Creamos la "funda" (el envoltorio)
        def funda():
            print("ATENCIÓN: La función está a punto de ejecutarse.") # Acción extra ANTES
            
            funcion_original() # Aquí ejecutamos la función real que recibimos
            
            print("ATENCIÓN: La función ha terminado.") # Acción extra DESPUÉS
            
        # Paso 3: Retornamos la funda terminada (SIN paréntesis, solo la entregamos)
        return funda

¡Ya fabricaste la funda! Ahora, ¿cómo se la ponemos a nuestro teléfono?

**🎩 La Magia del @**
En el pasado, para ponerle la funda a una función hacíamos esto: mi_funcion = avisador(mi_funcion). Era feo y difícil de leer.

Python creó un "atajo visual" elegante: el símbolo @. Si pones @nombre_del_decorador justo encima de la función que quieres proteger, Python le pone la funda automáticamente.

    @avisador
    def saludar():
        print("¡Hola, mundo!")

    @avisador
    def despedir():
        print("¡Adiós, mundo!")

Si ahora en tu código principal llamas a saludar(), mira lo que ocurre:

**Salida en consola:**

    ATENCIÓN: La función está a punto de ejecutarse.
    ¡Hola, mundo!
    ATENCIÓN: La función ha terminado.

¡La función saludar() no tiene idea de que imprimió esos avisos! Ella solo hizo su trabajo, pero la "funda" (el decorador) interceptó la llamada, hizo su lógica extra, la dejó pasar, y luego hizo más lógica al final.

## 📝 Ejercicio: El Guardia de Seguridad

Ahora que entiendes que el decorador es una "funda interceptora", tu tarea cobra todo el sentido. Te la vuelvo a plantear:

Objetivo: Crear una funda que solo deje ejecutar la función si el usuario ha iniciado sesión. Si no, bloquea el paso.

    1. Crea una variable global arriba del todo: usuario_logueado = False.
    2. Crea tu decorador: def verificar_login(funcion_original):
    3. Dentro, crea tu envoltorio: def funda():
    4. La lógica de la funda debe ser:
        Si usuario_logueado es igual a True: ejecuta funcion_original().
        Si es False: no ejecutes nada y haz un print("ACCESO DENEGADO").
    5. Recuerda hacer return funda al final de tu decorador.
    6. Crea un par de funciones (ej: ver_panel()) y ponles el @verificar_login arriba.
    7. Intenta ejecutarlas.

Lee este texto las veces que necesites. Cierra los ojos y visualiza la función entrando en la "fábrica" del decorador y saliendo envuelta en la funda.