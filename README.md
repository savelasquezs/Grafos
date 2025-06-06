# Visualizador de Grafos Dirigidos

Este proyecto implementa un visualizador de grafos dirigidos en Python. Permite crear y mostrar grafos de manera interactiva usando la biblioteca Turtle Graphics.

## Estructura del Proyecto

El proyecto está organizado en varios archivos:

- `graph.py`: Contiene la implementación básica del grafo dirigido
  - Clase `Node`: Representa un nodo con un ID y datos opcionales
  - Clase `Graph`: Implementa un grafo dirigido usando lista de adyacencia
    - Métodos para agregar/eliminar nodos y conexiones
    - Métodos para consultar conexiones y datos de nodos

- `circleGraph.py`: Crea un grafo de ejemplo con 10 nodos conectados en círculo
  - Función `create_circle_grapth()`: Genera un grafo circular donde cada nodo apunta al siguiente

- `visualize_graph.py`: Implementa la visualización del grafo
  - Clase `GraphVisualizer`: Dibuja el grafo usando Turtle Graphics
    - Coloca los nodos en círculo
    - Dibuja flechas entre nodos conectados
    - Muestra los IDs de los nodos

- `main.py`: Punto de entrada del programa
  - Crea un grafo circular
  - Lo muestra en pantalla
  - Mantiene la ventana abierta hasta que el usuario la cierre

## Requisitos

Para ejecutar el proyecto necesitas:

- Python 3.6 o superior
- Biblioteca `turtle` (incluida en Python)

## Cómo Usar

1. Asegúrate de tener Python instalado
2. Clona o descarga este repositorio
3. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

## Ejemplo de Uso

El programa mostrará una ventana con:
- 10 nodos numerados del 0 al 9
- Los nodos están colocados en círculo
- Cada nodo tiene una flecha que apunta al siguiente
- El último nodo (9) apunta al primero (0)

## Características

- Visualización interactiva usando Turtle Graphics
- Nodos claramente etiquetados
- Flechas que muestran las conexiones entre nodos
- Diseño circular para mejor visualización
- Código comentado en español para fácil entendimiento

## Estructura del Grafo

El grafo de ejemplo tiene la siguiente estructura:
- 10 nodos (0-9)
- Cada nodo apunta al siguiente en secuencia
- El nodo 9 apunta al nodo 0, cerrando el círculo

## Contribuir

Si quieres contribuir al proyecto:
1. Haz un fork del repositorio
2. Crea una rama para tu característica
3. Haz tus cambios
4. Envía un pull request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles. 