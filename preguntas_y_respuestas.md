# Preguntas y respuestas del Data Lab

# 01. Preparar el entorno
Pregunta: ¿Qué versión de Python aparece?
Respuesta: Se muestra una versión de Python 3, por ejemplo: Python 3.11.x o Python 3.12.x.

# 02. Crear el proyecto
Pregunta: ¿Para qué sirve separar app.py de templates/index.html?
Respuesta: Para mantener el código organizado: la lógica del servidor va en app.py y la interfaz va en index.html. Así se separa la parte de lógica y proceso de la parte visual.

# 03. Crear el entorno virtual
Pregunta: ¿Qué ventaja ofrece un entorno virtual?
Respuesta: Evita conflictos entre dependencias del sistema y del proyecto. Cada proyecto puede tener sus propias versiones de Python y Flask sin interferir con otros.

# 04. Instalar Flask
Pregunta: ¿Qué ocurre si Flask no está instalado en el entorno que ejecuta app.py?
Respuesta: La aplicación no puede arrancar. Python lanzará un error de importación y el servidor no responde.

# 05. Parte del código que envía datos al servidor
Pregunta: ¿Qué parte del código envía los datos del navegador al servidor?
Respuesta: La parte del cliente en JavaScript, dentro de index.html, usa fetch('/api/operacion') para enviar JSON al backend.

# 06. Ejecutar el proyecto
Pregunta: ¿Qué mensaje aparece en la terminal cuando Flask inicia correctamente?
Respuesta: Normalmente aparece algo como:
* Running on http://127.0.0.1:5000
* Debugger is active!
Eso indica que la app se está sirviendo correctamente.

# 07. Comprobar las cinco estructuras
Pregunta: ¿En qué se diferencian las operaciones de una pila, una cola y una lista?
Respuesta:
- Pila: inserta y extrae por el extremo final (append y pop).
- Cola: inserta por el final y extrae por el inicio (append y pop(0)).
- Lista: permite acceder y modificar elementos en cualquier posición, sin la restricción de pila ni cola.

# 08. Probar casos de error
Pregunta: ¿Por qué conviene validar los datos antes de modificar una estructura?
Respuesta: Porque así se evitan errores, se entienden mejor los mensajes y la interfaz puede mostrar información útil al usuario. También mejora el mantenimiento del código y facilita detectar fallos antes de que se produzcan.

# 09. Preparar la entrega
Pregunta: ¿Qué mejorarías en la interfaz y en el código?
Respuesta: Añadiría más pruebas de casos límite, mejoraría el diseño visual, haría la API más clara y dejaría la validación más robusta para futuras extensiones.

# 10. Producto final y entrega
Pregunta: ¿Qué se debe entregar al final del proyecto?
Respuesta: La carpeta del proyecto con app.py, requirements.txt y templates/index.html, sin incluir la carpeta .venv. Además, se deben adjuntar capturas de la interfaz, resultados y respuestas a las preguntas con una conclusión final.

# Retos

# Reto 1: Pila · Historial de edición
Descripción: Agrega, inserta y guarda. Extrae dos elementos, predice el orden de salida y compruébalo.
Respuesta:
- Se usa una pila porque el último elemento añadido es el primero en salir.
- Al guardar un historial, cada nueva acción se apila y al deshacer se extrae la última.
- Ejemplo: escribir, borrar y luego deshacer vuelve al estado anterior.
- Si se añade "escribir", luego "borrar" y después "deshacer", la última acción es la que se revierte primero.

# Reto 2: Cola · Atención de estudiantes
Descripción: Agrega Ana, Luis y Marta. Atiende dos turnos. Explica quién queda esperando.
Respuesta:
- Se usa una cola porque el primer estudiante que llega es el primero en ser atendido.
- La persona que entra primero queda al principio y sale primero.
- Cada nuevo estudiante entra al final de la fila y se atiende el de la cabeza.

# Reto 3: Lista · Registro académico
Descripción: Agrega E01, E02 y E03; elimina E02. Explica qué elementos permanecen y qué falta para implementar una lista enlazada real.
Respuesta:
- Se usa una lista porque puede albergar varios elementos y permitir añadidos, eliminaciones y búsquedas.
- En una lista se pueden insertar, borrar o buscar registros sin seguir la lógica de pila ni cola.
- En este caso, E01, E02 y E03 son elementos de la lista; si falta E02, se puede eliminar o detectar su ausencia.

# Reto 4: Árbol · Organización universitaria
Descripción: Crea Facultad como raíz; agrega Sistemas e Industrial con padre Facultad. Describe la relación padre-hijo.
Respuesta:
- Un árbol representa jerarquías: un nodo principal tiene hijos y cada hijo puede tener más descendientes.
- La Facultad es el nodo raíz.
- Sistemas e Industrial son nodos hijos de Facultad.
- La relación padre-hijo describe la estructura organizativa.
- El árbol es útil para representar niveles y dependencia.

# Reto 5: Grafo · Red del campus
Descripción: Crea vértices A, B y C. Conecta A-B y B-C. Explica por qué A y C no tienen conexión directa.
Respuesta:
- Un grafo representa conexiones entre puntos.
- Los vértices son A, B, C, etc.
- Las aristas son las conexiones entre ellos.
- Si A está conectado con B y B con C, pero A y C no tienen conexión directa, eso demuestra que la relación no tiene que ser directa entre todos los nodos.
- El grafo permite modelar redes, caminos y relaciones.

# Reto 6: Reto avanzado · Extensión de código
Descripción: Implementa una operación buscar para listas o una visualización con tarjetas y flechas. Describe qué archivos modificaste y cómo podrías mejorarlo.
Respuesta:
- Se puede añadir una operación para buscar elementos dentro de una lista o mostrar datos filtrados.
- También podría mejorarse la vista para mostrar el estado de las estructuras con más detalle.
- Se podría crear una operación de búsqueda por valor o un panel que muestre el contenido de cada estructura.
- La mejora es útil porque facilita ver qué hay dentro de cada estructura sin modificar la lógica principal.

# Conclusión
En esta práctica aprendí a crear una aplicación web con Flask para trabajar con estructuras de datos como pila, cola, lista, árbol y grafo. Comprendí cómo se comportan cada una y cómo se pueden manipular desde la interfaz. También resolví errores de configuración y ejecución del proyecto, lo que me permitió mejorar mi comprensión de Python y del uso del servidor local. Como mejora futura, podría ampliar la interfaz y añadir más validaciones para que la app sea más completa y fácil de usar.
