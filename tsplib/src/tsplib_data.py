from dataclasses import dataclass
import tsplib95

DATA_DIR = './data'

@dataclass
class TSP:
    """TSPデータクラス
    """
    file_name : str
    edge_weight_type : str
    dimension : int
    coordinate: dict

def load_data(data_dir=DATA_DIR, file_name='eil51.tsp'):
    """入力データ読み込み関数

    Args:
        data_dir (str): 入力データ格納フォルダ名. Defaults to DATA_DIR.
        file_name (str): 入力データ名. Defaults to 'eil51.tsp'.

    Returns:
        TSP: 入力データ格納済のTSPデータ
    
    Examples:
        >>> print(load_data())
        TSP(file_name='eil51', edge_weight_type='EUC_2D', dimension=51, coordinate={1: [37, 52], 2: [49, 49], 3: [52, 64], 4: [20, 26], 
        5: [40, 30], 6: [21, 47], 7: [17, 63], 8: [31, 62], 9: [52, 33], 10: [51, 21], 11: [42, 41], 12: [31, 32], 13: [5, 25], 14: [12, 42], 15: [36, 16], 
        16: [52, 41], 17: [27, 23], 18: [17, 33], 19: [13, 13], 20: [57, 58], 21: [62, 42], 22: [42, 57], 23: [16, 57], 24: [8, 52], 25: [7, 38], 26: [27, 68], 
        27: [30, 48], 28: [43, 67], 29: [58, 48], 30: [58, 27], 31: [37, 69], 32: [38, 46], 33: [46, 10], 34: [61, 33], 35: [62, 63], 36: [63, 69], 37: [32, 22], 
        38: [45, 35], 39: [59, 15], 40: [5, 6], 41: [10, 17], 42: [21, 10], 43: [5, 64], 44: [30, 15], 45: [39, 10], 46: [32, 39], 47: [25, 32], 48: [25, 55], 
        49: [48, 28], 50: [56, 37], 51: [30, 40]})
    """
    
    _tsp_datas = tsplib95.load(f'{data_dir}/{file_name}')
    file_name = _tsp_datas.name
    edge_weight_type = _tsp_datas.edge_weight_type
    dimension = _tsp_datas.dimension
    coordinates = _tsp_datas.node_coords
    tsp_datas = TSP(file_name=file_name, edge_weight_type=edge_weight_type, dimension=dimension, coordinate=coordinates)
    
    return tsp_datas