import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KDTree
from pyqubo import Array, Constraint, Placeholder
from neal import SimulatedAnnealingSampler
import plotly.graph_objects as go

from typing import List, Dict, Any

class Visualize:
    positions: List[float]
    n_points : int
    selected_points: int
    positions_ordered: List[float]
    
    def __init__(self, data: Dict[str, Any]):
        self.positions = data["positions"]
        self.n_points = data["n_points"]
        self.selected_points = data["selected_points"]
        self.positions_ordered = data["positions_ordered"]
        
    
    def to_visualize(self):
        fig = go.Figure()
        non_selected = list(set(range(self.n_points)) - set(self.selected_points))
        positions = np.array(self.positions)
        fig.add_trace(go.Scatter3d(
            x=positions[non_selected, 0],
            y=positions[non_selected, 1],
            z=positions[non_selected, 2],
            mode='markers',
            marker=dict(size=1, color='gray', opacity=0.5),
            name='Non-selected'
        ))

        fig.add_trace(go.Scatter3d(
            x=self.positions_ordered[:, 0],
            y=self.positions_ordered[:, 1],
            z=self.positions_ordered[:, 2],
            mode='markers',
            marker=dict(size=2, color='red', opacity=1.0),
            line=dict(color='red', width=2),
            name='Selected (Ordered)'
        ))

        fig.update_layout(title='3D Visualization of Selected Points (Ordered)',
                        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
        fig.show()