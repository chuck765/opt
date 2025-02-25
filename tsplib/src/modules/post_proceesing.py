import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List

from modules.dataclass import Node

@dataclass
class OptimizeRouteRecord:
    city: int   = None
    order: int  = None


@dataclass
class OptimizeRoute:
    route: List[List[int]] = None
    record : List[OptimizeRouteRecord]  = None
    
    def __init__(self, route):
        """コンストラクタ

        Args:
            route (List[List[int]]): 最適化で採用したルート情報
        """
        self.route = route
    
    def add_record(self):
        """レコード生成・登録
        """
        records = []
        dimension = len(self.route)
        for i in range(dimension):
            for j in range(dimension):
                if self.route[i][j] == 1:
                    records.append(
                        OptimizeRouteRecord(
                            city=i,
                            order=j,
                        )
                    )
        self.record = records
        

@dataclass
class Visualize:
    """可視化クラス
    """
    nodes: List[Node]      = None
    records : List[OptimizeRouteRecord]  = None
    dist_matrix : dict     = None
    
    def __init__(self, nodes: List[Node], record: List[OptimizeRouteRecord], dist_matrix: dict):
        self.nodes = nodes
        self.records = record
        self.dist_matrix = dist_matrix
    
    def get_sorted_order(self):
        """レコードをオーダーの昇順に並べ替え
        """
        sorted_record = sorted(self.records, key=lambda x: x.order)
        sorted_city = [record.city for record in sorted_record]
        return sorted_city
    
    def get_correct_answer(self):
        """正解データ
        """
        correct_ans = [1,10,9,11,8,13,7,12,6,5,4,3,14,2] # 正解
        update_correct_ans = [ans-1 for ans in correct_ans]
        return update_correct_ans

    def to_objective_value(self, correct_ans_flg=False):
        """目的関数の値を可視化
        """
    
        if correct_ans_flg:
            citys = self.get_correct_answer() # 正解
        else:
            citys = self.get_sorted_order() # 実測値
        
        # ペア生成
        city_pair = list(zip(citys, citys[1:]))
        city_pair.append((citys[-1], citys[0])) # 末尾と先頭の距離も見る
        
        obj_value = 0
        for from_city, to_city in city_pair:
            dist = self.dist_matrix[(from_city, to_city)]
            print(f"{from_city} -> {to_city}: {dist}" )
            obj_value+=dist
        print(f"obj value = {obj_value}")

    def plot_route(self, correct_ans_flg=False):
        """可視化処理
        """

        # 正解か実測値
        if correct_ans_flg:
            orders = self.get_correct_answer() 
        else:
            orders = self.get_sorted_order()
        
        # 地点のプロット
        plt.figure(figsize=(10, 8))
        for i in range(len(orders)):
            x = self.nodes[orders[i]].x_coord
            y = self.nodes[orders[i]].y_coord
            plt.scatter(x, y, color='blue')
            plt.text(x, y, f'{orders[i]}', fontsize=9, ha='right')
        
        # 開始地点
        start_point = orders[0]
        start_x = self.nodes[start_point].x_coord
        start_y = self.nodes[start_point].y_coord
        plt.scatter(start_x, start_y, color='red')
        
        # order順につなげていく
        order_pair = list(zip(orders, orders[1:]))
        order_pair.append((orders[-1], orders[0]))
        for order1, order2 in order_pair:
            x1 = self.nodes[order1].x_coord
            y1 = self.nodes[order1].y_coord
            x2 = self.nodes[order2].x_coord
            y2 = self.nodes[order2].y_coord
            plt.annotate("", xy=(x2, y2), xytext=(x1, y1),
                         arrowprops=dict(arrowstyle="->", color='black', lw=0.5, linestyle='--'))
        
        plt.title("TSPLIB Visualize Result")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)
        plt.show()