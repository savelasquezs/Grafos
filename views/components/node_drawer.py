from typing import Tuple
from .turtle_manager import TurtleManager
from .point import Point

class NodeDrawer:
    """Se encarga de dibujar los nodos."""
    def __init__(self, turtle_manager: TurtleManager):
        self.turtle = turtle_manager.turtle
        self.turtle_manager = turtle_manager
    
    def draw(self, position: Point, node_id: int, radius: int = 20) -> None:
        """Dibuja un nodo como un círculo con su ID."""
        state = self.turtle_manager.save_state()
        
        # Dibujar el círculo
        self.turtle.penup()
        self.turtle.goto(position.x, position.y - radius)
        self.turtle.pendown()
        self.turtle.circle(radius)
        
        # Escribir el ID del nodo
        self.turtle.penup()
        self.turtle.goto(position.x, position.y - 10)
        self.turtle.write(str(node_id), align="center", font=("Arial", 12, "bold"))
        
        self.turtle_manager.restore_state(state) 