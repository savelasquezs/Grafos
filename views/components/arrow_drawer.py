import math
from .turtle_manager import TurtleManager
from .point import Point

class ArrowDrawer:
    """Se encarga de dibujar las flechas."""
    def __init__(self, turtle_manager: TurtleManager, arrow_size: int = 10, node_radius: int = 20):
        self.turtle = turtle_manager.turtle
        self.turtle_manager = turtle_manager
        self.arrow_size = arrow_size
        self.node_radius = node_radius
    
    def draw(self, start: Point, end: Point) -> None:
        """Dibuja una flecha desde una posición inicial hasta la final."""
        # Calcular ángulo y distancia
        dx = end.x - start.x
        dy = end.y - start.y
        angle = math.atan2(dy, dx)
        distance = math.sqrt(dx*dx + dy*dy)
        
        # Calcular puntos de inicio y fin de la línea
        line_length = distance - self.node_radius
        arrow_start = Point(
            start.x + self.node_radius * math.cos(angle),
            start.y + self.node_radius * math.sin(angle)
        )
        arrow_end = Point(
            start.x + line_length * math.cos(angle),
            start.y + line_length * math.sin(angle)
        )
        
        # Dibujar la línea
        self.turtle.penup()
        self.turtle.goto(arrow_start.x, arrow_start.y)
        self.turtle.pendown()
        self.turtle.goto(arrow_end.x, arrow_end.y)
        
        # Dibujar la punta de la flecha
        self._draw_arrow_head(arrow_end, angle)
    
    def _draw_arrow_head(self, end: Point, angle: float) -> None:
        """Dibuja la punta de la flecha."""
        arrow_angle = math.pi/6  # 30 degrees
        
        # Calcular puntos de la punta
        arrow_angle1 = angle + math.pi - arrow_angle
        arrow_angle2 = angle + math.pi + arrow_angle
        
        arrow_x1 = end.x + self.arrow_size * math.cos(arrow_angle1)
        arrow_y1 = end.y + self.arrow_size * math.sin(arrow_angle1)
        arrow_x2 = end.x + self.arrow_size * math.cos(arrow_angle2)
        arrow_y2 = end.y + self.arrow_size * math.sin(arrow_angle2)
        
        # Dibujar la punta
        self.turtle.penup()
        self.turtle.goto(end.x, end.y)
        self.turtle.pendown()
        self.turtle.goto(arrow_x1, arrow_y1)
        self.turtle.goto(arrow_x2, arrow_y2)
        self.turtle.goto(end.x, end.y) 