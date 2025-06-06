from services import GraphService, VisualizationService
class GraphController:
    def __init__(self):
        self.graph_service = GraphService()
        self.visualization_service = VisualizationService()
    
    def run(self):
        """Coordina los servicios"""
        graph = self.graph_service.create_circle_graph()
        self.visualization_service.visualize(graph)
        self.visualization_service.get_screen().mainloop()