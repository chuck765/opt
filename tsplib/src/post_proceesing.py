import matplotlib.pyplot as plt

class PostProcessing:
    
    def get_result_city_id(self, data, sample):
        # アニーリングで採用された地点IDを取得
        id_sequence = []
        dimension = data.dimension
        for i in range(dimension):
            for j in range(dimension):
                if sample[i][j] == 1:
                    id_sequence.append(j+1)
                    continue
        
        # 終点と始点を結ぶ
        id_sequence.append(id_sequence[0])
        
        return id_sequence

    def plot_route(self, data, id_sequence):
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