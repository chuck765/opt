from dataclasses import dataclass
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KDTree
from pyqubo import Array, Constraint, Placeholder
from neal import SimulatedAnnealingSampler
import plotly.graph_objects as go
from typing import List, Any

from modules.dataclass import Monomer

class OptimizeClusterPoint:
    monomers : List[Monomer] = None
    cluster_indices : List[Any] = None
    positions: List[Any] = None
    
    def __init__(self, cluster_indices: List[Any], monomers: List[Monomer], positions: List[Any]):
        self.monomers = monomers
        self.cluster_indices = cluster_indices
        self.positions = positions
    
    def optimize_cluster(self):
        cluster_scores = [m.bfactor for m in self.monomers]
        cluster_positions = np.array(self.positions)
        
        # 変数: 点を採用するか否か
        n = len(self.cluster_indices)
        x = Array.create('x', shape=n, vartype='BINARY')
        
        # 制約: 距離を満たさないペアはandzero
        tree = KDTree(cluster_positions)
        pairs = []
        for i in range(n):
            neighbors = tree.query_radius(cluster_positions[i].reshape(1, -1), r=0.1)[0].tolist()
            for j in neighbors:
                j = int(j)
                if i < j:
                    pairs.append((i, j))
        distance_penalty = sum(x[i] * x[j] for i, j in pairs)
        
        # 目的: スコアの最小化
        score_term = sum(cluster_scores[i] * x[i] for i in range(n))

        H = score_term + Placeholder("lambda") * distance_penalty
        model = H.compile()
        feed_dict = {"lambda": 5.0}
        bqm = model.to_bqm(feed_dict=feed_dict)

        sampler = SimulatedAnnealingSampler()
        sampleset = sampler.sample(bqm, num_reads=100)
        decoded = model.decode_sampleset(sampleset, feed_dict=feed_dict)
        best = min(decoded, key=lambda d: d.energy)
        selected = [self.cluster_indices[i] for i in range(n) if best.sample[f"x[{i}]"] == 1]
        return selected
    

class OptimizeOrder:
    positions_selected: List[List[Any]]
    scores_selected:    List[float]
    
    def __init__(self, positions_selected: List[List[Any]], scores_selected: List[float]):
        self.positions_selected = positions_selected
        self.scores_selected = scores_selected
    
    def optimize_order(self):
        n_order = 12
        n_point = len(self.positions_selected)
        positions_selected = np.array(self.positions_selected)
        
        x = Array.create("x", shape=(n_point, n_order), vartype="BINARY")

        # one-hot constraints
        H1 = Constraint(sum((sum(x[i][j] for j in range(n_order)) - 1) ** 2 for i in range(n_point)), label="OneOrderPerNode")
        H2 = Constraint(sum((sum(x[i][j] for i in range(n_point)) - 1) ** 2 for j in range(n_order)), label="OneNodePerOrder")

        # 距離制約
        distance_penalty = 0
        for j in range(n_order - 1):
            for i in range(n_point):
                for k in range(n_point):
                    if i != k:
                        dist = np.linalg.norm(positions_selected[i] - positions_selected[k])
                        if dist < 0.1 :
                            distance_penalty += x[i][j] * x[k][j + 1]

        # スコアの最小化
        score_term = sum(self.scores_selected[i] * x[i][j] for i in range(n_point) for j in range(n_order))

        H = score_term + 5.0 * (H1 + H2) + 5.0 * distance_penalty
        model = H.compile()
        bqm = model.to_bqm()

        sampler = SimulatedAnnealingSampler()
        sampleset = sampler.sample(bqm, num_reads=100)
        decoded = model.decode_sampleset(sampleset)
        best = min(decoded, key=lambda d: d.energy)
        order = [0] * n_order
        for i in range(n_point):
            for j in range(n_order):
                if best.sample[f"x[{i}][{j}]"] == 1:
                    order[j] = i
        return order