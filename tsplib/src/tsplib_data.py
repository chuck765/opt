from dataclasses import dataclass
import tsplib95

DATA_DIR = './data'

@dataclass
class TSP:
    file_name : str
    edge_weight_type : str
    dimension : int
    coordinate: dict

def load_data(data_dir=DATA_DIR, file_name='eil51.tsp'):
    
    _tsp_datas = tsplib95.load(f'{data_dir}/{file_name}')
    file_name = _tsp_datas.name
    edge_weight_type = _tsp_datas.edge_weight_type
    dimension = _tsp_datas.dimension
    coordinates = _tsp_datas.node_coords
    tsp_datas = TSP(file_name=file_name, edge_weight_type=edge_weight_type, dimension=dimension, coordinate=coordinates)
    
    return tsp_datas