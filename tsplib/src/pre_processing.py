import math
import numpy as np
import tsplib95

class PreProcessing:
    
    def get_dist(self, edge_weight_type,coord1, coord2):
        
        # ユーグリッド距離を計算
        if edge_weight_type == "EUC_2D":
            dist = tsplib95.distances.euclidean(coord1, coord2)
        
        # GEO距離を計算
        elif edge_weight_type == 'GEO':
            dist = tsplib95.distances.geographical(coord1, coord2)
        return dist

    def get_dist_matrix(self, data):
        # 距離マトリクスを作成
        matrix = np.zeros((data.dimension, data.dimension))
        for i in range(1, data.dimension + 1):
            for j in range(1, data.dimension + 1):
                matrix[i-1, j-1] = math.ceil(self.get_dist(data.edge_weight_type, data.coordinate[i], data.coordinate[j]))
        return matrix