from typing import Dict, Set, Optional
from models import Node

from collections import defaultdict



class Graph:
    """Implementación de un grafo dirigido usando una lista de adyacencia."""
    
    def __init__(self):
        """Crea un grafo dirigido vacío."""
        self.nodes: Dict[int, Node] = {}  # Guarda todos los nodos
        self.adjacency_list: Dict[int, Set[int]] = defaultdict(set)  # Guarda las conexiones
        self.num_nodes = 0  # Cuenta de nodos
        self.num_edges = 0  # Cuenta de conexiones

    def add_node(self, node_id: int, data: Optional[dict] = None) -> None:
        """
        Agrega un nuevo nodo al grafo.
        
        Args:
            node_id (int): El número que identifica al nodo
            data (dict, opcional): Información adicional para guardar en el nodo
        """
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(id=node_id, data=data)
            self.num_nodes += 1

    def add_edge(self, from_node: int, to_node: int) -> None:
        """
        Agrega una flecha desde un nodo hacia otro.
        
        Args:
            from_node (int): El número del nodo de donde sale la flecha
            to_node (int): El número del nodo hacia donde va la flecha
        """
        if from_node not in self.nodes or to_node not in self.nodes:
            raise ValueError("Ambos nodos deben existir en el grafo")
        
        self.adjacency_list[from_node].add(to_node)
        self.num_edges += 1

    def remove_edge(self, from_node: int, to_node: int) -> None:
        """
        Elimina una flecha entre dos nodos.
        
        Args:
            from_node (int): El número del nodo de donde sale la flecha
            to_node (int): El número del nodo hacia donde va la flecha
        """
        if from_node in self.adjacency_list and to_node in self.adjacency_list[from_node]:
            self.adjacency_list[from_node].remove(to_node)
            self.num_edges -= 1

    def get_neighbors(self, node_id: int) -> Set[int]:
        """
        Obtiene todos los nodos a los que apunta este nodo.
        
        Args:
            node_id (int): El número del nodo del que queremos ver sus conexiones
            
        Returns:
            Set[int]: Conjunto de IDs de nodos a los que apunta
        """
        return self.adjacency_list.get(node_id, set())

    def has_edge(self, from_node: int, to_node: int) -> bool:
        """
        Verifica si existe una flecha entre dos nodos.
        
        Args:
            from_node (int): El número del nodo de donde sale la flecha
            to_node (int): El número del nodo hacia donde va la flecha
            
        Returns:
            bool: True si existe la flecha, False si no existe
        """
        return to_node in self.adjacency_list.get(from_node, set())

    def get_node_data(self, node_id: int) -> Optional[dict]:
        """
        Obtiene la información guardada en un nodo.
        
        Args:
            node_id (int): El número del nodo del que queremos obtener la información
            
        Returns:
            Optional[dict]: La información del nodo o None si no existe
        """
        node = self.nodes.get(node_id)
        return node.data if node else None

    def __str__(self) -> str:
        """Muestra el grafo como texto, con cada nodo y sus conexiones."""
        result = []
        for node_id in sorted(self.nodes.keys()):
            neighbors = sorted(self.adjacency_list[node_id])
            result.append(f"Nodo {node_id} -> {neighbors}")
        return "\n".join(result) 