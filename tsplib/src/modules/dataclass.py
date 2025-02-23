from dataclasses import dataclass
from typing import List
import tsplib95

DATA_DIR = '../data'

@dataclass
class Problem:
    file_name : str       = None     # ファイル名
    edge_weight_type: str = None     # エッジタイプ
    dimension: int        = None     # 都市数

@dataclass
class Node:
    id: int        = None            # ID
    x_coord: float = None            # x座標
    y_coord: float = None            # y座標

@ dataclass
class TSP:
    problem : Problem = None
    node: Node = None
    
    def __init__(self, file_name: str):
        """コンストラクタ

        Args:
            file_name (str): 入力ファイル
        """
        self.file_name = file_name

    def generate(self):
        
        # データセット
        dataset = tsplib95.load(f'{DATA_DIR}/{self.file_name}')
        
        # 問題データ
        problem = Problem(
            file_name=dataset.name,
            edge_weight_type=dataset.edge_weight_type,
            dimension=dataset.dimension,
        )
        
        # ノード情報（各点の座標）
        node = []
        for idx, coordinate in dataset.node_coords.items():
            node.append(Node(id=idx-1, x_coord=coordinate[0], y_coord=coordinate[1]))
            
        self.problem = problem
        self.node = node