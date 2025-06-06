import turtle
from typing import Tuple

class TurtleManager:
    """Maneja la configuración y estado del turtle."""
    def __init__(self, width: int = 800, height: int = 600):
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title("Directed Graph Visualization")
        self.screen.bgcolor("white")
        
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10)
    
    def save_state(self) -> Tuple:
        """Guarda el estado actual del turtle."""
        return (self.turtle.pen(), self.turtle.fillcolor())
    
    def restore_state(self, state: Tuple) -> None:
        """Restaura el estado del turtle."""
        self.turtle.pen(state[0])
        self.turtle.fillcolor(state[1])
    
    def set_style(self, color: str = "black", fill_color: str = "white", pen_size: int = 1) -> None:
        """Configura el estilo del turtle."""
        self.turtle.color(color)
        self.turtle.fillcolor(fill_color)
        self.turtle.pensize(pen_size) 