from models import Graph

class GraphService:
    def __init__(self):
        self.graph = Graph()

    def create_circle_graph(self):
        """Lógica de creación del grafo circular"""
       
        for i in range(10):
            self.graph.add_node(i)
        for i in range(10):
            for j in range(1, 4):
                target = (i + j) % 10
                self.graph.add_edge(i, target)
        
        return self.graph
       
      
    
    def get_graph(self) -> Graph:
        """Obtiene el grafo actual"""
        return self.graph
    
    