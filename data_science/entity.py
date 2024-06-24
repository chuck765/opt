import urllib

import numpy as np
import pandas as pd
import requests

from model import AreaModel


DATA_DIR = './data'

def load_data(input_file_name):
    
    area_df = pd.read_csv(f'{DATA_DIR}/{input_file_name}', encoding="CP932")

    # プログラムの便宜上、excelのカラムを英文表記に変更
    area_df.columns = ["address_code", "prefectures_code", "municipalities_code", 
                    "town_area_code", "post_code", "office_flg", "obsolete_flg",
                    "prefectures_name", "prefectures_name_kana", "municipalities_name", "municipalities_name_kana",
                    "town_area_name", "town_area_name_kana", "town_area_supplement", "kyoto_street_name",
                    "character_chome_name", "character_chome_name_kana", "supplement_name", "office_name",
                    "office_name_kana", "office_address_name", "new_address_code"]

    return area_df
    

def get_area_list(area_df):

    area_list = [AreaModel(id=idx, address_code=row.address_code, prefectures_code=row.prefectures_code, municipalities_code=row.municipalities_code,
                        town_area_code=row.town_area_code, post_code=row.post_code, office_flg=row.office_flg, obsolete_flg=row.obsolete_flg,
                        prefectures_name=row.prefectures_name, prefectures_name_kana=row.prefectures_name_kana, municipalities_name=row.municipalities_name,
                        municipalities_name_kana=row.municipalities_name_kana,town_area_name=row.town_area_name, town_area_name_kana=row.town_area_name_kana,
                        town_area_supplement=row.town_area_supplement, kyoto_street_name=row.kyoto_street_name,character_chome_name=row.character_chome_name,
                        character_chome_name_kana=row.character_chome_name_kana, supplement_name=row.supplement_name,office_name=row.office_name,
                        office_name_kana=row.office_name_kana, office_address_name=row.office_address_name, new_address_code=row.new_address_code, 
                        coordinate=None) for idx, row in area_df.iterrows()]
    
    return area_list


def get_coordinates(office_address_name):
    
    # 国土地理院のAPI
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
    
    s_quote = urllib.parse.quote(office_address_name)
    response = requests.get(url + s_quote, verify=False)
    coordinate = response.json()[0]["geometry"]["coordinates"]
    
    return coordinate

def get_dist_matrix(data_list):
    
    dist_matrix = {}
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if i == j:
                continue
            from_area_id = data_list[i].id
            to_area_id = data_list[j].id
            
            from_coordinate = np.array(data_list[i].coordinate)
            to_coordinate = np.array(data_list[j].coordinate)
            
            # ２次元空間のユークリッド距離
            dist_matrix[(from_area_id, to_area_id)] = np.linalg.norm(from_coordinate - to_coordinate)
        
    return dist_matrix