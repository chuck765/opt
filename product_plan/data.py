from datetime import datetime
import random

import numpy as np
import pandas as pd

from model import Order, Vehicle, Area

class PoCData:
    
    def get_data(self):
        
        # Order
        order_num = 100
        order_no = ['order_' + str(i) for i in range(order_num)]
        start_time = ['2023/11/1' for i in range(order_num)]
        load_area_id = [i for i in range(order_num)]
        unload_area_id = [i+order_num for i in range(order_num)]
        work_time = [None for i in range(order_num)]
        
        _orders_df = pd.DataFrame({
            'order_no': order_no,
            'start_time' : start_time,
            'load_area_id': load_area_id,
            'unload_area_id' : unload_area_id,
            'work_time' : work_time,
        })
        orders = self.get_order(_orders_df)
        
        # Area
        area_num = 100
        area_name = ['area_' + str(i) for i in range(area_num)]
        coordinate = [random.random(), random.random()]
        _areas_df = pd.DataFrame({
            'area_name' : area_name,
            'coordinate': coordinate
        })
        areas = self.get_area(_areas_df)
        
        
        # Vehicle
        vehicle_num = 100
        vehicle = ['vehicle_' + str(i) for i in range(vehicle_num)]
        _vehicles_df = pd.DataFrame({
            'vehicle_name' : vehicle
        })
        vehicles = self.get_vehicle(_vehicles_df)

        return orders, areas, vehicles
    

    
    def get_order(self, _orders_df):
        orders = [Order(id=idx, 
                        order_no=row.order_no,
                        start_time=row.start_time,
                        load_area_id=row.load_read_id,
                        unload_area_id=row.unload_read_id,
                        work_time=None) for idx, row in _orders_df.iterrows()]
        
        return orders
    
    def get_area(self, _areas_df):
        random.seed(0)
        areas = [Area(id=idx,
                      area_name=row.area_name,
                      coordinate=row.coordinate) for idx, row in _areas_df.iterrows()]
        return areas
    
    def get_vehicle(self, _vehicles_df):
        vehicles = [Vehicle(id=idx,
                            vehicle_name=row.vehicle_name
                            ) for idx, row in _vehicles_df.iterrows()]
        return vehicles