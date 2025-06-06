from typing import List, Tuple
from models import Graph
from .components import TurtleManager, LayoutManager, NodeDrawer, ArrowDrawer

class GraphVisualizer:
    """Clase principal que coordina la visualización del grafo."""
    def __init__(self, width: int = 800, height: int = 600):
        self.turtle_manager = TurtleManager(width, height)
        self.layout_manager = LayoutManager()
        self.node_drawer = NodeDrawer(self.turtle_manager)
        self.arrow_drawer = ArrowDrawer(self.turtle_manager)
    
    def visualize_graph(self, graph: Graph) -> None:
        """Visualiza el grafo completo."""
        # Calcular posiciones
        node_positions = self.layout_manager.calculate_circular_layout(graph.num_nodes)
        
        # Dibujar nodos
        print("Drawing nodes...")
        self.turtle_manager.set_style(color="black", fill_color="white")
        
        for node_id, position in node_positions.items():
            self.turtle_manager.turtle.begin_fill()
            self.node_drawer.draw(position, node_id)
            self.turtle_manager.turtle.end_fill()
        
        # Dibujar conexiones
        print("Drawing edges...")
        self.turtle_manager.set_style(color="gray", pen_size=2)
        
        edges = self._get_edges(graph)
        for from_node, to_node in edges:
            start_pos = node_positions[from_node]
            end_pos = node_positions[to_node]
            print(f"Drawing edge {from_node} -> {to_node}")
            self.arrow_drawer.draw(start_pos, end_pos)
        
        print("Graph visualization complete!")
        self.turtle_manager.screen.mainloop()
    
    def _get_edges(self, graph: Graph) -> List[Tuple[int, int]]:
        """Obtiene la lista de aristas del grafo."""
        edges = []
        for node_id in graph.nodes:
            for neighbor in graph.get_neighbors(node_id):
                edges.append((node_id, neighbor))
        return edges

