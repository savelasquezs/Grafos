from typing import  Optional

class Node:
    """Representa un nodo en el grafo con un ID y datos opcionales."""
    
    

    def __init__(self,id: int, data: Optional[dict] = None ):
        """Crea un grafo dirigido vacío."""
        self.id: id
        self.data:data
        