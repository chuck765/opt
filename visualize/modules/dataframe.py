from dataclasses import dataclass
from datetime import datetime, timedelta
import pandas as pd

@dataclass
class SampleData:
    id: int = None
    date: datetime = None
    work_time: float = None
    
test_data = [
    SampleData(id=0, date=datetime(2023, 11, 1), work_time=10.0),
    SampleData(id=0, date=datetime(2023, 11, 2), work_time=15.0),
    SampleData(id=0, date=datetime(2023, 11, 3), work_time=20.0),
    SampleData(id=0, date=datetime(2023, 11, 4), work_time=10.0),
    SampleData(id=0, date=datetime(2023, 11, 5), work_time=15.0),
    SampleData(id=0, date=datetime(2023, 11, 6), work_time=20.0),
    SampleData(id=0, date=datetime(2023, 11, 7), work_time=20.0),
    SampleData(id=0, date=datetime(2023, 11, 8), work_time=10.0),
    SampleData(id=0, date=datetime(2023, 11, 9), work_time=15.0),
    SampleData(id=0, date=datetime(2023, 11, 10), work_time=20.0),
    SampleData(id=0, date=datetime(2023, 11, 11), work_time=10.0),
    SampleData(id=0, date=datetime(2023, 11, 12), work_time=15.0),
    SampleData(id=0, date=datetime(2023, 11, 13), work_time=20.0),
    SampleData(id=0, date=datetime(2023, 11, 14), work_time=20.0),
    SampleData(id=1, date=datetime(2023, 11, 1), work_time=5.0),
    SampleData(id=1, date=datetime(2023, 11, 2), work_time=12.0),
    SampleData(id=2, date=datetime(2023, 11, 1), work_time=17.0),
]

df = pd.DataFrame(test_data)
print(df)

# IDごとに2週間分を集計
def aggregate_work_time(df):
    min_date = df['date'].min()
    max_date = min_date + timedelta(days=13)  # 2週間分（14日間）
    
    # 2週間分のデータをフィルタリング
    df_filtered = df[(df['date'] >= min_date) & (df['date'] <= max_date)]
    
    # IDごとに集計
    result = df_filtered.groupby('id').agg(
        total_work_time=('work_time', 'sum'),
        average_work_time=('work_time', 'mean')
    ).reset_index()

    # 集計開始日と終了日を追加
    result['start_date'] = min_date
    result['end_date'] = max_date
    
    return result

# 集計結果を出力
aggregated_result = aggregate_work_time(df)
print(aggregated_result)
