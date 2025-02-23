import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List

from modules.dataclass import Node

@dataclass
class Record:
    order: int  = None
    city: int   = None


@dataclass
class OptimizeRoute:
    route: List[List[int]] = None
    record : List[Record]  = None
    
    def __init__(self, route):
        self.route = route
    
    def add_record(self):
        records = []
        dimension = len(self.route)
        for j in range(dimension):
            for i in range(dimension):
                if self.route[i][j] == 1:
                    records.append(
                        Record(
                            order=j,
                            city=i,
                        )
                    )
        self.record = records
        

@dataclass
class Visualize:
    """可視化クラス
    """
    nodes: List[Node]      = None
    records : List[Record]  = None
    dist_matrix : dict     = None
    
    def __init__(self, nodes: List[Node], record: List[Record], dist_matrix: dict):
        self.nodes = nodes
        self.records = record
        self.dist_matrix = dist_matrix

    def to_objective_result(self):
        """目的関数の値を可視化
        """
        
        # NOTE: 実測値
        print("============ 実測値 ============")
        pairs = list(zip(self.records, self.records[1:]))
        pairs.append((self.records[-1], self.records[0]))
        
        obj_value = 0
        for from_node, to_node in pairs:
            dist = self.dist_matrix[(from_node.city, to_node.city)]
            print(f"{from_node.city} -> {to_node.city}: {dist}" )
            obj_value+=dist
        print(f"obj value = {obj_value}")
        print("")
        
        # NOTE: 正解値
        print("============ 正解値 ============")
        correct_ans = [1,10,9,11,8,13,7,12,6,5,4,3,14,2]
        correct_ans = [ans-1 for ans in correct_ans]
        pairs = list(zip(correct_ans, correct_ans[1:]))
        pairs.append((correct_ans[-1], correct_ans[0]))
        
        correct_ans_obj_value = 0
        for from_node, to_node in pairs:
            dist = self.dist_matrix[(from_node, to_node)]
            print(f"{from_node} -> {to_node}: {dist}" )
            correct_ans_obj_value+=dist
        print(f"correct_ans obj value = {correct_ans_obj_value}")

    def plot_route(self, data, id_sequence):
        """可視化処理

        Args:
            data (tsplib_data.TSP): TSPデータ
            id_sequence (list): アニーリングで採用された地点ID
        """
        
        coordinate = data.coordinate
        plt.figure(figsize=(10, 8))
        
        # 散布図に青色の地点、地点IDを表示
        for key in coordinate:
            x, y = coordinate[key][0], coordinate[key][1]
            plt.scatter(x, y, color='blue')
            plt.text(x, y, f'{key}', fontsize=9, ha='right')
        
        # 開始地点を赤色にする
        start_x, start_y = coordinate[id_sequence[0]]
        plt.scatter(start_x, start_y, color='red')
        
        # アニーリング結果をルート順に点線でつなぐ
        for i in range(len(id_sequence) - 1):
            current_id = id_sequence[i]
            next_id = id_sequence[i + 1]
            current_x, current_y = coordinate[current_id]
            next_x, next_y = coordinate[next_id]
            plt.annotate("", xy=(next_x, next_y), xytext=(current_x, current_y),
                         arrowprops=dict(arrowstyle="->", color='black', lw=0.5, linestyle='--'))
        
        plt.title("TSPLIB Visualize Result")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)
        plt.show()