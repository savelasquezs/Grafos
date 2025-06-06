"""
Módulo de servicios que implementa la lógica de negocio de la aplicación.
Contiene los servicios que actúan como intermediarios entre los controladores y los modelos.

Este módulo es responsable de:
- Implementar la lógica de negocio compleja
- Coordinar operaciones entre modelos
- Proporcionar una capa de abstracción para los controladores
- Manejar la creación y manipulación de grafos
- Gestionar la visualización de los grafos
"""

from .graphService import GraphService
from .visualizationService import VisualizationService

# Exportar los servicios principales para facilitar su importación
__all__ = ['GraphService', 'VisualizationService']
