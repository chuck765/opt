from dataclasses import dataclass

@dataclass
class AreaModel:
    id: int
    address_code : str # 住所CD
    prefectures_code : str # 都道府県CD
    municipalities_code: str #市町村区CD
    town_area_code: str # 町域CD
    post_code: str # 郵便番号
    office_flg: bool # 事業所フラグ
    obsolete_flg : bool #廃止フラグ
    prefectures_name: str #都道府県名
    prefectures_name_kana: str #都道府県カナ
    municipalities_name: str
    municipalities_name_kana: str
    town_area_name : str
    town_area_name_kana: str
    town_area_supplement: str
    kyoto_street_name: str
    character_chome_name: str
    character_chome_name_kana: str
    supplement_name: str
    office_name: str
    office_name_kana: str
    office_address_name: str
    new_address_code: str
    coordinate : tuple # 緯度経度の座標
    
    
    
    
    
    
    