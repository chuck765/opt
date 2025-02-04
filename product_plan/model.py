from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass()
class Order:
    id : int
    order_no : str
    start_time : datetime
    load_area_id : int
    unload_area_id : int
    work_time : float

@dataclass()
class Area:
    id: int
    area_name : str
    coordinate : List[float]

@dataclass()
class Vehicle:
    id : int
    vehicle_name : str

@dataclass()
class Util:
    break_time : 1 # 休憩時間: 1h
    load_time : 1 # 積み時間: 1h
    unload_time : 1 # 卸し時間 : 1h
    vehicle_speed : 26 # 26km/h
    