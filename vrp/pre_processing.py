import requests
import urllib
import mojimoji
import numpy as np

API = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

class PreProcessing:
    
    def get_coordinate(self, address):
        
        address = mojimoji.zen_to_han(address)
        query_param = urllib.parse.quote(address)
        response = requests.get(API + query_param)
        print(response.json())
        
        return response.json()[0]["geometry"]["coordinates"]
    
    def get_dist(self, coord1, coord2):
        
        return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    def get_dist_matrix(self, data):
        
        # 距離マトリクスを作成
        dimension = len(data)
        matrix = np.zeros((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                matrix[i, j] = self.get_dist(data[i].coordinate, data[j].coordinate)
        return matrix