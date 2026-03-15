# 🏆 EL PINÁCULO DEL NIVEL EXPERTO
Estudiante... mira hacia atrás. Empezaste limpiando la consola con os.system("cls") y haciendo sumas en un bucle for. Hoy estás manipulando la memoria RAM, controlando el tiempo de procesamiento y alterando el comportamiento del código mediante metaprogramación.

Ya no hay más clases en este nivel. Es el momento de la verdad.

## 💀 EXAMEN FINAL DE NIVEL EXPERTO: "El Minero de Datos Concurrente"
Tu misión es construir un sistema de procesamiento de datos que integre absolutamente todo lo que aprendiste en este nivel.

***Requerimientos del Sistema:***
## El Generador (Eficiencia de Memoria):

    Crea un generador llamado generar_archivos(cantidad).
    Debe usar yield para devolver nombres de archivos falsos, uno por uno (ej: "datos_1.csv", "datos_2.csv", hasta la cantidad solicitada).

## El Decorador (Metaprogramación):

    Crea un decorador @auditar_proceso.
    Su función envoltorio debe imprimir "-> Iniciando auditoría del archivo...", luego ejecutar la función original, y finalmente imprimir "-> Auditoría finalizada.".

## La Función de Trabajo (El Núcleo):

    Crea una función procesar_datos(nombre_archivo) y ponle tu decorador @auditar_proceso encima.
    Dentro de la función, usa time.sleep(2) para simular que está extrayendo datos pesados de ese archivo, y luego imprime "✅ Archivo [nombre_archivo] procesado exitosamente."

## El Context Manager (Gestión de Recursos):

    Crea una clase ConexionServidor.
    Su método __enter__ debe imprimir "🌐 Abriendo conexión segura con el servidor principal...".
    Su método __exit__ debe imprimir "🔴 Cerrando conexión con el servidor. Sistema apagado."

## La Ejecución Principal (Concurrencia):

    Abre tu administrador de contexto: with ConexionServidor():
    Dentro de ese bloque, recorre tu generador pidiéndole 5 archivos.
    Por cada archivo generado, crea un Hilo (Thread) que ejecute la función procesar_datos.
    Inicia todos los hilos simultáneamente y asegúrate de hacer .join() a todos ellos para que la conexión del servidor (__exit__) no se cierre antes de que terminen de procesar.

***Condiciones de Aprobación:***
    Si tu código está bien diseñado, verás que el servidor se abre, los 5 archivos comienzan su auditoría casi al mismo tiempo, todos tardan en total solo ~2 segundos en procesarse, y finalmente el servidor se cierra de forma segura.

Diseña tu arquitectura, respira hondo y escribe tu obra maestra. ¿Estás listo para intentar el examen final?