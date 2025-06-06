# Visualizador de Grafos Dirigidos

Este proyecto implementa un visualizador interactivo de grafos dirigidos utilizando Python y la biblioteca Turtle para la visualización gráfica. El proyecto sigue una arquitectura MVC (Modelo-Vista-Controlador) y está diseñado para crear y visualizar grafos circulares de manera intuitiva.

## Características

- Implementación de grafos dirigidos usando listas de adyacencia
- Visualización gráfica interactiva de grafos
- Creación automática de grafos circulares
- Interfaz gráfica usando Turtle
- Estructura de proyecto modular y bien organizada
- Componentes de visualización reutilizables y extensibles

## Estructura del Proyecto

```
.
├── controllers/         # Controladores que coordinan la lógica de la aplicación
│   ├── __init__.py
│   └── graphController.py
├── models/             # Modelos de datos
│   ├── __init__.py
│   ├── graph.py       # Implementación del grafo
│   └── node.py        # Implementación de nodos
├── services/          # Servicios que implementan la lógica de negocio
│   ├── __init__.py
│   ├── graphService.py
│   └── visualizationService.py
├── views/             # Componentes de visualización
│   ├── __init__.py
│   ├── visualizer.py  # Visualizador principal del grafo
│   └── components/    # Componentes modulares de visualización
│       ├── __init__.py
│       ├── point.py           # Representación de puntos 2D
│       ├── turtle_manager.py  # Gestión del turtle y pantalla
│       ├── layout_manager.py  # Cálculo de posiciones de nodos
│       ├── node_drawer.py     # Dibujo de nodos
│       └── arrow_drawer.py    # Dibujo de flechas
├── main.py           # Punto de entrada de la aplicación
├── requirements.txt  # Dependencias del proyecto
└── README.md        # Este archivo
```

## Requisitos

El proyecto solo utiliza módulos de la biblioteca estándar de Python, por lo que no se requieren dependencias externas.

## Cómo Ejecutar

1. Asegúrate de tener Python 3.x instalado
2. Clona este repositorio
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## Funcionalidades

### Grafo Dirigido
- Implementación eficiente usando listas de adyacencia
- Soporte para nodos con datos adicionales
- Operaciones básicas: agregar/eliminar nodos y aristas
- Consultas de vecindad y existencia de aristas

### Visualización
- Representación gráfica interactiva
- Layout circular automático
- Nodos numerados y aristas con flechas
- Ventana gráfica redimensionable (800x600 por defecto)
- Componentes modulares y reutilizables:
  - `Point`: Representación de coordenadas 2D
  - `TurtleManager`: Gestión del estado y configuración de Turtle
  - `LayoutManager`: Cálculo de posiciones en layout circular
  - `NodeDrawer`: Dibujo de nodos y etiquetas
  - `ArrowDrawer`: Dibujo de flechas y sus puntas

### Grafo Circular
El proyecto incluye una implementación de grafo circular donde:
- Se crean 10 nodos
- Cada nodo se conecta con los siguientes 3 nodos
- Las conexiones son circulares (el último nodo se conecta con los primeros)

## Arquitectura

### Modelo (models/)
- `Graph`: Implementa la estructura de datos del grafo
- `Node`: Representa los nodos del grafo

### Vista (views/)
- `GraphVisualizer`: Coordina la visualización del grafo
- Componentes modulares en `views/components/`:
  - `Point`: Dataclass para coordenadas 2D
  - `TurtleManager`: Maneja la configuración de Turtle
  - `LayoutManager`: Calcula posiciones de nodos
  - `NodeDrawer`: Dibuja nodos y etiquetas
  - `ArrowDrawer`: Dibuja flechas y sus puntas

### Controlador (controllers/)
- `GraphController`: Coordina la interacción entre el modelo y la vista

### Servicios (services/)
- `GraphService`: Implementa la lógica de creación y manipulación de grafos
- `VisualizationService`: Gestiona la visualización de los grafos

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 