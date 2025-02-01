from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Tuple


# ################################################################
# タイムテーブル用クラス
# ################################################################

@dataclass
class TimeTable:
    vehicle_id: int = None         # 車両(ヘッド・ローリー)ID
    chassis_id: int = None         # シャーシID
    category : str = None          # 作業状況
    start_time : datetime = None   # 開始時刻
    end_time : datetime = None     # 終了時刻
    start_area: str = None         # 開始位置
    end_area : str = None          # 終了位置
    elapsed_time : float = 0.0     # 所要時間
    order_id: int = None           # 割り当てたオーダーID


# ################################################################
# テスト関数
# ################################################################
category = {
    "move": "移動",
    "load_wait": "積待機",
    "load" : "積",
    "unload_wait": "卸待機",
    "unload": "卸",
}

MOVE_TIME = 2
WAIT_TIME = 1
LOAD_TIME = 1
UNLOAD_TIME = 1

test_time_table = [
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 8, 30),
        end_time=datetime(2025, 2, 1, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 1, 10, 30),
        end_time=datetime(2025, 2, 1, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["load"],
        start_time=datetime(2025, 2, 1, 11, 30),
        end_time=datetime(2025, 2, 1, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=LOAD_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 12, 30),
        end_time=datetime(2025, 2, 1, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 1, 13, 30),
        end_time=datetime(2025, 2, 1, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=1,
        category=category["unload"],
        start_time=datetime(2025, 2, 1, 14, 30),
        end_time=datetime(2025, 2, 1, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=UNLOAD_TIME,
        order_id=0,
    ),

    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 8, 30),
        end_time=datetime(2025, 2, 2, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 2, 10, 30),
        end_time=datetime(2025, 2, 2, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["load"],
        start_time=datetime(2025, 2, 2, 11, 30),
        end_time=datetime(2025, 2, 2, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=LOAD_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 12, 30),
        end_time=datetime(2025, 2, 2, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 2, 13, 30),
        end_time=datetime(2025, 2, 2, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle_id=0,
        chassis_id=2,
        category=category["unload"],
        start_time=datetime(2025, 2, 2, 14, 30),
        end_time=datetime(2025, 2, 2, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=UNLOAD_TIME,
        order_id=1,
    ),

    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 8, 30),
        end_time=datetime(2025, 2, 1, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 1, 10, 30),
        end_time=datetime(2025, 2, 1, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["load"],
        start_time=datetime(2025, 2, 1, 11, 30),
        end_time=datetime(2025, 2, 1, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=LOAD_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 12, 30),
        end_time=datetime(2025, 2, 1, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 1, 13, 30),
        end_time=datetime(2025, 2, 1, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle_id=10,
        chassis_id=11,
        category=category["unload"],
        start_time=datetime(2025, 2, 1, 14, 30),
        end_time=datetime(2025, 2, 1, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=UNLOAD_TIME,
        order_id=10,
    ),

    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 8, 30),
        end_time=datetime(2025, 2, 2, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=MOVE_TIME,
        order_id=11,
    ),
    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 2, 10, 30),
        end_time=datetime(2025, 2, 2, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=11,
    ),
    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["load"],
        start_time=datetime(2025, 2, 2, 11, 30),
        end_time=datetime(2025, 2, 2, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=LOAD_TIME,
        order_id=11,
    ),
    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 12, 30),
        end_time=datetime(2025, 2, 2, 12, 30)+timedelta(hours=5.0),
        start_area="area1",
        end_area="area2",
        elapsed_time=5.0,
        order_id=11,
    ),
    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 2, 17, 30),
        end_time=datetime(2025, 2, 2, 17, 30)+timedelta(hours=WAIT_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=WAIT_TIME,
        order_id=11,
    ),
    TimeTable(
        vehicle_id=11,
        chassis_id=12,
        category=category["unload"],
        start_time=datetime(2025, 2, 2, 18, 30),
        end_time=datetime(2025, 2, 2, 18, 30)+timedelta(hours=UNLOAD_TIME),
        start_area="area1",
        end_area="area2",
        elapsed_time=UNLOAD_TIME,
        order_id=11,
    ),
]


# ################################################################
# コンプライアンス表クラス
# ################################################################
from collections import defaultdict
import pandas as pd

# NOTE: 各車両の1日のコンプライアンス時間を集計したものを1レコードとする
@dataclass
class Record:
    vehicle_id : int = None             # 車両（ヘッド・ローリー）ID
    date: datetime = None               # 集計日
    start_time : datetime = None        # 作業開始時刻
    end_time : datetime = None          # 作業終了時刻
    bind_time: float = 0.0              # 拘束時間 (unit:h)
    work_time: float = 0.0              # 労働時間 (unit:h)
    drive_time: float = 0.0             # 運転時間 (unit:h)
    break_time: float = 0.0             # 休憩時間 (unit:h)
    over_time: float = 0.0              # 残業時間 (unit:h)
    rest_time: float = 0.0              # 休息時間 (unit:h)
    drive_interupt_time: float = 0.0    # 連続運転中断時間 (unit:h)

@dataclass
class CompliancePlan:
    record: List[Record] = None         # レコード
    time_table: List[TimeTable] = None  # タイムテーブル
    
    def __init__(self, time_table: List[TimeTable]):
        """コンストラクタ

        Args:
            time_table (List[TimeTable]): _description_
        """
        self.record = []
        self.time_table = time_table
    
    def _group_time_table(self):
        """タイムテーブルをグルーピングする。

        Returns:
            _type_: _description_
        """
        # NOTE: 同じ車両ID and 同じ開始日で分ける
        group_time_tables = defaultdict(list)
        for tt in self.time_table:
            key = (tt.vehicle_id, tt.start_time.date())
            group_time_tables[key].append(tt)
        return group_time_tables

    def _add_record(self, group_time_tables:Dict[Tuple, List[TimeTable]]):
        """コンプライアンス時間を集計する

        Args:
            group_time_tables (List[List[TimeTable]]): _description_

        Raises:
            NotImplementedError: _description_
        """
        
        record = []
        
        # NOTE: 車両IDと日付ごとにレコード生成する方針
        for key in group_time_tables.keys():
            tmp_bind_time = 0.0
            tmp_drive_time = 0.0
            tmp_break_time = 0.0
            tmp_work_time = 0.0
            tmp_over_time = 0.0
            tmp_drive_interrupt_time = 0.0
            
            # 作業開始・終了時刻
            start_time = group_time_tables[key][0].start_time
            end_time = group_time_tables[key][-1].end_time
            for tt in group_time_tables[key]:
                
                # 車両IDと集計日
                vehicle_id = key[0]
                date = key[1]
                
                # 運転時間
                if tt.category == '移動':
                    tmp_drive_time += tt.elapsed_time
                # 休憩時間
                if tt.category == '積待機' or tt.category == '卸待機':
                    tmp_break_time += tt.elapsed_time
                # 労働時間(休憩以外)
                if tt.category != '積待機' and tt.category != '卸待機':
                    tmp_work_time += tt.elapsed_time
                # 連続運転中断時間
                if tt.category == '移動':
                    if tt.elapsed_time > 4.0:
                        tmp_drive_interrupt_time += int(tt.elapsed_time / 4.0)*0.5
            
            # TODO:残業時間(労働時間=8h以下なら残業=0h)
            end_start_diff_time = (end_time - start_time).total_seconds() / 3600
            if end_start_diff_time < 8.0:
                tmp_over_time = 0.0
            else:
                tmp_over_time = end_start_diff_time - tmp_work_time
            
            # TODO:拘束時間
            tmp_bind_time = end_start_diff_time
            
            # レコード生成・登録
            record.append(
                Record(
                    vehicle_id=vehicle_id,
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    bind_time=tmp_bind_time,
                    work_time=tmp_work_time,
                    drive_time=tmp_drive_time,
                    break_time=tmp_break_time,
                    over_time=tmp_over_time,
                    drive_interupt_time=tmp_drive_interrupt_time
                )
            )
        
        return record

        
    def to_dataframe(self, record: List[Record]):
        compliance_df = pd.DataFrame(record)
        compliance_df.columns = [
            "車両ID", 
            "集計日",
            "開始時刻",
            "終了時刻",
            "拘束時間[h]",
            "労働時間[h]",
            "運転時間[h]",
            "休憩時間[h]",
            "残業時間[h]",
            "休息時間[h]",
            "連続運転中断時間[h]"
        ]
        print(compliance_df)
        compliance_df.to_html("compliance.html", index=False)
    
    def exe(self):
        group_time_tables = self._group_time_table()
        record = self._add_record(group_time_tables)
        self.to_dataframe(record=record)
    

compliance_plan = CompliancePlan(time_table=test_time_table)
compliance_plan.exe()