import turtle
import math


class GraphVisualizer:
    def __init__(self, width=800, height=600):
        """Initialize the visualizer with a turtle screen."""
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title("Directed Graph Visualization")
        self.screen.bgcolor("white")
        
    #    Creacion de el objeto turtle para dibujar
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10) 
        # Posiciones de los nodos dentro del canvas
        self.node_positions = {}
        # Tamaño de la flecha
        self.arrow_size = 10
        
      

    def calculate_node_positions(self, num_nodes):
        """Calcular las posiciones de los nodos en un layout circular."""
        radius = 200  # Radio del circulo que formaran los nodos
        
        for i in range(num_nodes):
            # calculo del angulo de cada nodo
            # para 10 nodos seria un nodo cada  2*pi/10= 36 grados
            angle = 2 * math.pi * i / num_nodes
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            self.node_positions[i] = (x, y)

    def draw_node(self, x, y, node_id, radius=20):
        """Dibuja un nodo como un circulo con su ID."""
        # Guardar el estado actual del lapiz
        current_pen = self.turtle.pen()
        current_fill = self.turtle.fillcolor()
        
        # Dibujar el circulo
        self.turtle.penup()
        self.turtle.goto(x, y - radius)
        self.turtle.pendown()
        self.turtle.circle(radius)
        
        # Escribir el ID del nodo
        self.turtle.penup()
        self.turtle.goto(x, y - 10)  # Centrar el texto del nodo
        self.turtle.write(str(node_id), align="center", font=("Arial", 12, "bold"))
        
       
        
       

    def draw_arrow(self, start_pos, end_pos):
        """Dibuja una flecha desde una posicion inicial hasta la final"""
      
        
        # calcula el angulo entre los 2 nodos ayudar a dibujar la linea
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        angle = math.atan2(dy, dx)
        
        # Calcula la distancia entre los 2 nodos
        distance = math.sqrt(dx*dx + dy*dy)
        
        # Calcula las nuevas coordenadas de inicio y fin de la linea para que no 
        # atraviese los nodos
        node_radius = 20
        # longitud de la linea
        line_length = distance - node_radius
        arrow_start_x = start_pos[0]+ node_radius * math.cos(angle)
        arrow_start_y = start_pos[1] + node_radius * math.sin(angle)
        arrow_end_x = start_pos[0]+ line_length * math.cos(angle)
        arrow_end_y = start_pos[1] + line_length * math.sin(angle)

       
        
        # Dibujamos la linea
        self.turtle.penup()
        self.turtle.goto([arrow_start_x, arrow_start_y])
        self.turtle.pendown()
        self.turtle.goto(arrow_end_x, arrow_end_y)
        
        ## Calculamos las coordenadas para la punta de la flecha
        # primelo los angulos
        arrow_angle = math.pi/6  # 30 degrees
        arrow_length = self.arrow_size
        # Hacia un lado y hacia el otro
        arrow_angle1 = angle + math.pi - arrow_angle
        arrow_angle2 = angle + math.pi + arrow_angle
        
        #ahora si las coordentadas de los extremos de la punta de flecha
        arrow_x1 = arrow_end_x + arrow_length * math.cos(arrow_angle1)
        arrow_y1 = arrow_end_y + arrow_length * math.sin(arrow_angle1)
        arrow_x2 = arrow_end_x + arrow_length * math.cos(arrow_angle2)
        arrow_y2 = arrow_end_y + arrow_length * math.sin(arrow_angle2)
        
        # Dibujamos la punta de flecha
        self.turtle.penup()
        self.turtle.goto(arrow_end_x, arrow_end_y)
        self.turtle.pendown()
        self.turtle.goto(arrow_x1, arrow_y1)
        self.turtle.goto(arrow_x2, arrow_y2)
        self.turtle.goto(arrow_end_x, arrow_end_y)
        
      
       
      

    def visualize_graph(self, graph):
        """Visualizamos el grafico completo del grafo"""
        # Calculamos las posiciones de los nodos
        self.calculate_node_positions(graph.num_nodes)
        
        # Primero dibujamos los nodos
        print("Drawing nodes...")
        self.turtle.color("black")
        self.turtle.fillcolor("white")
        
        for node_id, (x, y) in self.node_positions.items():
            self.turtle.begin_fill()
            self.draw_node(x, y, node_id)
            self.turtle.end_fill()
        
        # Luego dibujamos las conexiones
        print("Drawing edges...")
        self.turtle.pensize(2)
        self.turtle.color("gray")
        
        # traemos las aristas directamente de cada nodo
        edges = []
        for node_id in graph.nodes:
            for neighbor in graph.get_neighbors(node_id):
                edges.append((node_id, neighbor))
        
        # Dibujamos las flechas una por una
        for from_node, to_node in edges:
            start_pos = self.node_positions[from_node]
            end_pos = self.node_positions[to_node]
            print(f"Drawing edge {from_node} -> {to_node}")
            self.draw_arrow(start_pos, end_pos)
        
        print("Graph visualization complete!")
       
        self.screen.mainloop()

