import pandas as pd
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    id: int
    order_no: int


def get_order(order_file: str) -> List[Order]:
    order_df = pd.read_csv(order_file)
    order_df.columns = ['order_no1', 'order_no2']
    order_df['order_no2'] = order_df['order_no1'] # 値の差し替え（列単位）
    print(order_df)


if __name__ == "__main__":
    get_order('../input/order.csv')