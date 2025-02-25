from dataclasses import dataclass
from typing import List
import tsplib95

DATA_DIR = '../data'

@dataclass
class Problem:
    file_name : str       = None       # ファイル名
    edge_weight_type: str = None       # エッジタイプ
    dimension: int        = None       # 都市数
    correct_answer: List[int] = None   # 正解
    
    def __init__(self, file_name: str, edge_weight_type: str, dimension: int):
        """コンストラクタ

        Args:
            file_name (str): 入力ファイル
        """
            
        self.file_name = file_name
        self.edge_weight_type = edge_weight_type
        self.dimension = dimension

        if file_name == 'burma14.tsp':
            correct_ans = [1,10,9,11,8,13,7,12,6,5,4,3,14,2]
            self.correct_answer = [ans-1 for ans in correct_ans]
        

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
        try:
            dataset = tsplib95.load(f'{DATA_DIR}/{self.file_name}')
            
            # 問題データ
            problem = Problem(
                file_name=self.file_name,
                edge_weight_type=dataset.edge_weight_type,
                dimension=dataset.dimension,
            )
            
            # ノード情報（各点の座標）
            node = []
            for idx, coordinate in dataset.node_coords.items():
                node.append(Node(id=idx-1, x_coord=coordinate[0], y_coord=coordinate[1]))
                
            self.problem = problem
            self.node = node
        
        except Exception as e:
            print("[Error] tsp file is exists.")
    
    def describe(self):
        print(f"problem: {self.problem}")
        print(f"node: {self.node}")