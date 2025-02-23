import math
import numpy as np
import tsplib95
from typing import List
from itertools import product

from modules.dataclass import Problem, Node

class Area:
    """地点クラス
    """
    problem: Problem      = None
    nodes: List[Node]     = None
    
    def __init__(self, problem: Problem, nodes:List[Node]):
        self.problem = problem
        self.nodes = nodes
    
    def is_euc_2d(self):
        return self.problem.edge_weight_type == "EUC_2D"
    
    def is_geo(self):
        return self.problem.edge_weight_type == "GEO"

    def get_dist_matrix(self) -> dict:
        """2点間の距離マトリクスを取得

        Args:
            data (tsplib_data.TSP): TSPデータ

        Returns:
            dict: 距離マトリクス
        """
        
        # 距離マトリクスを辞書型で生成
        dist_matrix = {}
        for from_node, to_node in product(self.nodes, repeat=2):
            
            # 同じ地点同士は無視
            if from_node.id == to_node.id:
                continue
            
            # エッジタイプによって計算方法が異なる
            if self.is_euc_2d():
                dist = tsplib95.distances.euclidean([from_node.x_coord, from_node.y_coord],
                                                    [to_node.x_coord, to_node.y_coord])
            if self.is_geo():
                dist = tsplib95.distances.geographical([from_node.x_coord, from_node.y_coord],
                                                    [to_node.x_coord, to_node.y_coord])
            
            dist_matrix[(from_node.id, to_node.id)] = dist
            
        return dist_matrix
            