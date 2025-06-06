from circleGraph import create_circle_grapth
from visualize_graph import GraphVisualizer

def main():
    """
    Función principal que crea y muestra un grafo circular.
    Crea un grafo con 10 nodos conectados en círculo y lo dibuja en pantalla.
    """
    # Creamos el grafo circular
    graph = create_circle_grapth()
    
    # Creamos el visualizador y mostramos el grafo
    visualizer = GraphVisualizer()
    visualizer.visualize_graph(graph)
    
    # Mantenemos la ventana abierta hasta que el usuario la cierre
    visualizer.screen.mainloop()

if __name__ == "__main__":
    main() 