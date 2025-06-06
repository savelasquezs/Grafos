from models import Graph
from views import GraphVisualizer

class VisualizationService:
    def __init__(self):
        self.visualizer = GraphVisualizer()
    
    def visualize(self, graph: Graph) -> None:
        """Lógica de visualización"""
        self.visualizer.visualize_graph(graph)
    
    def get_screen(self):
        """Obtiene la pantalla de visualización"""
        return self.visualizer.screen