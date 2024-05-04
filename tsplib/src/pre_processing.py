import math
import numpy as np
import tsplib95

class PreProcessing:
    """前処理クラス
    """
    
    def get_dist(self, edge_weight_type,coord1, coord2):
        """2点間の距離を取得

        Args:
            edge_weight_type (str): 地点間の重みタイプ
            coord1 (list): 移動元の座標情報
            coord2 (list): 移動先の座標情報

        Returns:
            int: 2点間の距離
        """
        
        # ユーグリッド距離を計算
        if edge_weight_type == "EUC_2D":
            dist = tsplib95.distances.euclidean(coord1, coord2)
        
        # GEO距離を計算
        elif edge_weight_type == 'GEO':
            dist = tsplib95.distances.geographical(coord1, coord2)
        return dist

    def get_dist_matrix(self, data):
        """2点間の距離マトリクスを取得

        Args:
            data (tsplib_data.TSP): TSPデータ

        Returns:
            dict: 距離マトリクス
        """
        
        # 距離マトリクスを作成
        matrix = np.zeros((data.dimension, data.dimension))
        for i in range(1, data.dimension + 1):
            for j in range(1, data.dimension + 1):
                matrix[i-1, j-1] = math.ceil(self.get_dist(data.edge_weight_type, data.coordinate[i], data.coordinate[j]))
        return matrix