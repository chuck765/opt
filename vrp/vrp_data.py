from dataclasses import dataclass
import pandas as pd
from pre_processing import PreProcessing

DATA_DIR = './data'

@dataclass
class StartOffice:
    id: int = 1
    name: str = "NEC本社ビル"
    address: str = "東京都港区芝５丁目７−１"

@dataclass
class Root:
    id: int
    name: str
    address: str
    load: str
    coordinate : list

@dataclass
class Product:
    id: int
    name: str
    cleaning_flag: bool

@dataclass
class Vehicle:
    id: int
    name: str
    cert_flg: bool

@dataclass
class Driver:
    id: int
    name: str
    cert_flg: bool

def load_data(data_dir=DATA_DIR):
    
    # ルート情報をテーブル形式で格納
    _root_info = pd.read_csv(f'{data_dir}/ルート情報.csv')
    _root_info.columns = ['id', 'root_name', 'address', 'load']
    
    # 前処理で住所から緯度経度変換してデータ保持
    pre_process = PreProcessing()
    root_info = [Root(id=idx, name=row.root_name, address=row.address, load=row.load, 
                          coordinate=pre_process.get_coordinate(row.address)) for idx, row in _root_info.iterrows()]
    
    # ルート情報から2点間の距離マトリクスを取得
    dist_matrix = pre_process.get_dist_matrix(root_info)
    
    # 品物情報をテーブル形式で格納
    _product = pd.read_csv(f'{data_dir}/品物.csv')
    _product.columns = ['id', 'product_name', 'cleaning_flag']
    product = [Product(id=idx, name=row.product_name, cleaning_flag=row.cleaning_flag) for idx, row in _product.iterrows()]
    
    # 車両情報をテーブル形式で格納
    _vehicle = pd.read_csv(f'{data_dir}/車両.csv')
    _vehicle.columns = ['id', 'vehicle_name', 'cert_flg']
    vehicle = [Vehicle(id=idx, name=row.vehicle_name, cert_flg=row.cert_flg) for idx, row in _vehicle.iterrows()]

    # スタート始点情報をテーブル形式で格納
    start_office = [StartOffice()]
    
    # 運転手情報をテーブル形式で格納
    _driver = pd.read_csv(f'{data_dir}/運転手.csv', encoding="Shift-jis")
    _driver.columns = ['id', 'driver_name', 'cert_flg']
    driver = [Driver(id=idx, name=row.driver_name, cert_flg=row.cert_flg) for idx, row in _driver.iterrows()]
    
    return [root_info, product, vehicle, dist_matrix, start_office, driver]