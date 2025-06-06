import math
from typing import Dict
from .point import Point

class LayoutManager:
    """Maneja el cálculo de posiciones de los nodos."""
    def __init__(self, radius: float = 200):
        self.radius = radius
        self.node_positions: Dict[int, Point] = {}
    
    def calculate_circular_layout(self, num_nodes: int) -> Dict[int, Point]:
        """Calcula las posiciones de los nodos en un layout circular."""
        for i in range(num_nodes):
            angle = 2 * math.pi * i / num_nodes
            x = self.radius * math.cos(angle)
            y = self.radius * math.sin(angle)
            self.node_positions[i] = Point(x, y)
        return self.node_positions 