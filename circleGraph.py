from graph import Graph

def create_circle_grapth() -> Graph:
    """
    Crea un grafo dirigido con 10 nodos conectados en círculo.
    Cada nodo apunta al siguiente, y el último apunta al primero.
    
    Returns:
        Graph: Un grafo con 10 nodos conectados en círculo
    """
    # Creamos un nuevo grafo
    graph = Graph()
    
    # Agregamos 10 nodos con información de ejemplo
    for i in range(10):
        graph.add_node(i, {"valor": f"Nodo {i}"})
    
    # Lista de conexiones entre nodos
    # Cada par (a,b) significa que el nodo 'a' apunta al nodo 'b'
    edges = [
        (0, 1),(0,2) ,(0,3),
        (1, 2),(1,3),(1,4),
          (2, 3),(2,4),(2,5),
            (3, 4),(3,5) ,(3,6),
            (4, 5),(4,6) ,(4,7),
        (5, 6),(5,7),(5,8),
          (6, 7),(6,8),(6,9),
            (7, 8),(7,9),(7,0),
              (8, 9),(8,0),(8,1),
                (9, 0), (9,1) , (9,2)  # Segunda mitad del círculo
    ]
    
    # Agregamos todas las conexiones al grafo
    for from_node, to_node in edges:
        graph.add_edge(from_node, to_node)
    
    return graph
