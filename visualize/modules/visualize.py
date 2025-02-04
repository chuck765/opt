from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from dataclass import Area, Vehicle, AreaType


# ################################################################
# タイムテーブル用クラス
# ################################################################

@dataclass
class TimeTable:
    vehicle: Optional[Vehicle] = None       # 車両ID
    chassis_id: int = None                  # chassisID
    category : str = None                   # 作業状況
    start_time : datetime = None            # 開始時刻
    end_time : datetime = None              # 終了時刻
    start_area: Optional[Area] = None       # 開始位置
    end_area : Optional[Area] = None        # 終了位置
    elapsed_time : float = 0.0              # 所要時間
    order_id: int = None                    # 割り当てたオーダーID


# ################################################################
# テスト関数
# ################################################################

area = [Area(name='Area1', type=AreaType.OFFICE.value), 
        Area(name='Area2', type=AreaType.LOAD.value),
        Area(name='Area3', type=AreaType.UNLOAD.value),
        Area(name='Area4', type=AreaType.LOAD.value),
        Area(name='Area5', type=AreaType.UNLOAD.value), 
        Area(name='Area6', type=AreaType.LOAD.value),
        Area(name='Area7', type=AreaType.UNLOAD.value),
        Area(name='Area8', type=AreaType.LOAD.value),
        Area(name='Area9', type=AreaType.UNLOAD.value),
        Area(name='Area10', type=AreaType.LOAD.value),
        Area(name='Area11', type=AreaType.UNLOAD.value),
        ]

vehicle = [
    Vehicle(id=0,
            name='車番1',
            type=0),
    Vehicle(id=1,
            name='車番2',
            type=1),
    Vehicle(id=2,
            name='車番3',
            type=0),
    Vehicle(id=3,
            name='車番4',
            type=1),
]


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
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 8, 30),
        end_time=datetime(2025, 2, 1, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[0],
        end_area=area[1],
        elapsed_time=MOVE_TIME,
        order_id=0,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 1, 10, 30),
        end_time=datetime(2025, 2, 1, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[0],
        end_area=area[1],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["load"],
        start_time=datetime(2025, 2, 1, 11, 30),
        end_time=datetime(2025, 2, 1, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area=area[0],
        end_area=area[1],
        elapsed_time=LOAD_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 12, 30),
        end_time=datetime(2025, 2, 1, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[1],
        end_area=area[2],
        elapsed_time=MOVE_TIME,
        order_id=1,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 1, 13, 30),
        end_time=datetime(2025, 2, 1, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[1],
        end_area=area[2],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=1,
        category=category["unload"],
        start_time=datetime(2025, 2, 1, 14, 30),
        end_time=datetime(2025, 2, 1, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area=area[1],
        end_area=area[2],
        elapsed_time=UNLOAD_TIME,
        order_id=None,
    ),

    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 8, 30),
        end_time=datetime(2025, 2, 2, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[2],
        end_area=area[3],
        elapsed_time=MOVE_TIME,
        order_id=2,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 2, 10, 30),
        end_time=datetime(2025, 2, 2, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[2],
        end_area=area[3],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["load"],
        start_time=datetime(2025, 2, 2, 11, 30),
        end_time=datetime(2025, 2, 2, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area=area[2],
        end_area=area[3],
        elapsed_time=LOAD_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 12, 30),
        end_time=datetime(2025, 2, 2, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[3],
        end_area=area[4],
        elapsed_time=MOVE_TIME,
        order_id=3,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 2, 13, 30),
        end_time=datetime(2025, 2, 2, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[3],
        end_area=area[4],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[0],
        chassis_id=2,
        category=category["unload"],
        start_time=datetime(2025, 2, 2, 14, 30),
        end_time=datetime(2025, 2, 2, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area=area[3],
        end_area=area[4],
        elapsed_time=UNLOAD_TIME,
        order_id=None,
    ),

    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 8, 30),
        end_time=datetime(2025, 2, 1, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[4],
        end_area=area[5],
        elapsed_time=MOVE_TIME,
        order_id=10,
    ),
    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 1, 10, 30),
        end_time=datetime(2025, 2, 1, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[4],
        end_area=area[5],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["load"],
        start_time=datetime(2025, 2, 1, 11, 30),
        end_time=datetime(2025, 2, 1, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area=area[4],
        end_area=area[5],
        elapsed_time=LOAD_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 12, 30),
        end_time=datetime(2025, 2, 1, 12, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[5],
        end_area=area[6],
        elapsed_time=MOVE_TIME,
        order_id=20,
    ),
    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 1, 13, 30),
        end_time=datetime(2025, 2, 1, 13, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[5],
        end_area=area[6],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[1],
        chassis_id=11,
        category=category["unload"],
        start_time=datetime(2025, 2, 1, 14, 30),
        end_time=datetime(2025, 2, 1, 14, 30)+timedelta(hours=UNLOAD_TIME),
        start_area=area[5],
        end_area=area[6],
        elapsed_time=UNLOAD_TIME,
        order_id=None,
    ),

    TimeTable(
        vehicle=vehicle[1],
        chassis_id=12,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 8, 30),
        end_time=datetime(2025, 2, 2, 8, 30)+timedelta(hours=MOVE_TIME),
        start_area=area[6],
        end_area=area[7],
        elapsed_time=MOVE_TIME,
        order_id=30,
    ),
    TimeTable(
        vehicle=vehicle[2],
        chassis_id=12,
        category=category["load_wait"],
        start_time=datetime(2025, 2, 2, 10, 30),
        end_time=datetime(2025, 2, 2, 10, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[6],
        end_area=area[7],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[2],
        chassis_id=12,
        category=category["load"],
        start_time=datetime(2025, 2, 2, 11, 30),
        end_time=datetime(2025, 2, 2, 11, 30)+timedelta(hours=LOAD_TIME),
        start_area=area[6],
        end_area=area[7],
        elapsed_time=LOAD_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[2],
        chassis_id=12,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 12, 30),
        end_time=datetime(2025, 2, 2, 12, 30)+timedelta(hours=5.0),
        start_area=area[7],
        end_area=area[8],
        elapsed_time=5.0,
        order_id=40,
    ),
    TimeTable(
        vehicle=vehicle[2],
        chassis_id=12,
        category=category["unload_wait"],
        start_time=datetime(2025, 2, 2, 17, 30),
        end_time=datetime(2025, 2, 2, 17, 30)+timedelta(hours=WAIT_TIME),
        start_area=area[7],
        end_area=area[8],
        elapsed_time=WAIT_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[2],
        chassis_id=12,
        category=category["unload"],
        start_time=datetime(2025, 2, 2, 18, 30),
        end_time=datetime(2025, 2, 2, 18, 30)+timedelta(hours=UNLOAD_TIME),
        start_area=area[7],
        end_area=area[8],
        elapsed_time=UNLOAD_TIME,
        order_id=None,
    ),
    TimeTable(
        vehicle=vehicle[3],
        chassis_id=101,
        category=category["move"],
        start_time=datetime(2025, 2, 1, 8, 30),
        end_time=datetime(2025, 2, 1, 8, 30)+timedelta(hours=10.0),
        start_area=area[8],
        end_area=area[9],
        elapsed_time=10.0,
        order_id=100,
    ),
    TimeTable(
        vehicle=vehicle[3],
        chassis_id=101,
        category=category["move"],
        start_time=datetime(2025, 2, 2, 6, 30),
        end_time=datetime(2025, 2, 2, 6, 30)+timedelta(hours=14.0),
        start_area=area[9],
        end_area=area[10],
        elapsed_time=14.0,
        order_id=200,
    ),
]


# ################################################################
# コンプライアンス表クラス
# ################################################################
from collections import defaultdict
import pandas as pd

DRIVE_INTERRUPT_TIME = 0.5          # 連続運転後の中断時間
CONTINUTE_DRIVE_TIME_LIMIT = 4.0    # 最大連続運転時間
FIXED_WORK_TIME = 8.0               # 所定労働時間


# NOTE: 各車両の1日のコンプライアンス時間を集計したものを1レコードとする
@dataclass
class ComplianceRecord:
    vehicle_id : int = None             # 車両ID
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


# NOTE: https://www.mhlw.go.jp/content/001035021.pdf
@dataclass
class CompliancePlan:
    _record: List[ComplianceRecord] = None         # レコード
    time_table: List[TimeTable] = None  # タイムテーブル
    
    def __init__(self, time_table: List[TimeTable]):
        """コンストラクタ

        Args:
            time_table (List[TimeTable]): 生成したタイムテーブル
        """
        self._record = []
        self.time_table = time_table
    
    def _group_time_table(self) -> Dict[Tuple, List[TimeTable]]:
        """集計用にタイムテーブルをグルーピングする。

        Returns:
            Dict[Tuple, List[TimeTable]]: グルーピングしたタイムテーブル
        """
        # NOTE: 日別で集計するため、同じ車両ID and 同じ開始日で分ける
        group_time_tables = defaultdict(list)
        for tt in self.time_table:
            key = (tt.vehicle.id, tt.start_time.date())
            group_time_tables[key].append(tt)
        return group_time_tables
    
    def _is_next_time(self, group_time_tables: Dict[Tuple, List[TimeTable]], next_key: Tuple) -> bool:
        """翌日の作業計画が無いかチェック。あればTrueを返す
        Args:
            key (Tuple): _description_

        Returns:
            bool: _description_
        """
        
        if next_key in group_time_tables:
            return True
        return False

    def _calc_current_start_time(self, group_time_tables:Dict[Tuple, List[TimeTable]], 
                                 vehicle_id:int, totaling_date: datetime) -> datetime:
        """当日の作業開始時刻を計算

        Args:
            group_time_tables (Dict[Tuple, List[TimeTable]]): タイムテーブル
            vehicle_id (int): 車両ID
            totaling_date (datetime): 集計日

        Returns:
            datetime: 当日の作業開始時刻
        """
        return group_time_tables[(vehicle_id, totaling_date)][0].start_time

    def _calc_current_end_time(self, group_time_tables:Dict[Tuple, List[TimeTable]], 
                                 vehicle_id:int, totaling_date: datetime) -> datetime:
        """当日の作業終了時刻を計算

        Args:
            group_time_tables (Dict[Tuple, List[TimeTable]]): タイムテーブル
            vehicle_id (int): 車両ID
            totaling_date (datetime): 集計日

        Returns:
            datetime: 当日の作業終了時刻
        """
        return group_time_tables[(vehicle_id, totaling_date)][-1].end_time

    def _calc_next_start_time(self, group_time_tables:Dict[Tuple, List[TimeTable]], 
                                 vehicle_id:int, totaling_date: datetime) -> datetime:
        """翌日の作業開始時刻を計算(ある場合)

        Args:
            group_time_tables (Dict[Tuple, List[TimeTable]]): タイムテーブル
            vehicle_id (int): 車両ID
            totaling_date (datetime): 集計日

        Returns:
            datetime: 翌日の作業開始時刻
        """

        next_key = (vehicle_id, totaling_date+timedelta(days=1)) # 翌日のキー
        if self._is_next_time(group_time_tables=group_time_tables, next_key=next_key):
            return group_time_tables[next_key][0].start_time
        return None

    def _calc_current_extra_bind_time(self, group_time_tables:Dict[Tuple, List[TimeTable]], 
                                 vehicle_id:int, totaling_date: datetime, 
                                 current_start_time:datetime,next_start_time:datetime) -> float:
        """当日の拘束時間を計算する際に、翌日の作業開始時刻との差分を考慮した時間

        Args:
            group_time_tables (Dict[Tuple, List[TimeTable]]): タイムテーブル
            vehicle_id (int): 車両ID
            totaling_date (datetime): 集計日
            current_start_time (datetime): 作業開始時刻
            next_start_time (datetime) : 翌日の作業開始時刻

        Returns:
            float: 翌日分も考慮した拘束時間
        """
        next_key = (vehicle_id, totaling_date+timedelta(days=1)) # 翌日のキー
        if self._is_next_time(group_time_tables=group_time_tables, next_key=next_key):
            # NOTE: 例として当日8時開始、翌日8時より前ならその差分を当日の拘束時間に含める。
            if current_start_time.hour > next_start_time.hour:
                return current_start_time.hour - next_start_time.hour
        return 0.0
    
    def _calc_rest_time(self, group_time_tables:Dict[Tuple, List[TimeTable]], 
                                 vehicle_id:int, totaling_date: datetime, 
                                 current_end_time:datetime,next_start_time:datetime) -> float:
        """休息時間を計算

        Args:
            group_time_tables (Dict[Tuple, List[TimeTable]]): タイムテーブル
            vehicle_id (int): 車両ID
            totaling_date (datetime): 集計日
            current_end_time (datetime): 作業終了時刻
            next_start_time (datetime) : 翌日の作業開始時刻

        Returns:
            float: 休息時間
        """
        next_key = (vehicle_id, totaling_date+timedelta(days=1)) # 翌日のキー
        if self._is_next_time(group_time_tables=group_time_tables, next_key=next_key):
            return (next_start_time - current_end_time).seconds / 3600
        return 0.0
    
    def _calc_over_time(self, current_bind_time: datetime, work_time: float) -> float:
        """残業時間を計算

        Args:
            current_bind_time (datetime): 当日の拘束時間
            work_time (float): 労働時間

        Returns:
            float: 残業時間
        """
        if current_bind_time > FIXED_WORK_TIME:
            return current_bind_time - work_time
        return 0.0

    def _add_record(self, group_time_tables:Dict[Tuple, List[TimeTable]]) -> List[ComplianceRecord]:
        """コンプライアンス時間を集計したレコードを取得

        Args:
            group_time_tables Dict[Tuple, List[TimeTable]]: _description_

        Returns:
            List[Record]: コンプライアンス時間を集計したレコード
        """
        
        for vehicle_id, totaling_date in group_time_tables.keys():
                      
            # 当日の作業開始・終了時刻
            current_start_time = self._calc_current_start_time(group_time_tables,vehicle_id,totaling_date)
            current_end_time = self._calc_current_end_time(group_time_tables,vehicle_id,totaling_date)

            # 翌日の作業開始時刻
            next_start_time = self._calc_next_start_time(group_time_tables,vehicle_id,totaling_date)
            
            # 休息時間
            current_rest_time = self._calc_rest_time(group_time_tables,vehicle_id,totaling_date,
                                                 current_end_time, next_start_time)

            # コンプライアンス時間を集計
            current_bind_time = 0.0
            current_drive_time = 0.0
            current_break_time = 0.0
            current_work_time = 0.0
            current_drive_interrupt_time = 0.0                  
            for tt in group_time_tables[(vehicle_id, totaling_date)]:
        
                # 運転時間
                if tt.category == '移動':
                    current_drive_time += tt.elapsed_time
                # 休憩時間
                if tt.category == '積待機' or tt.category == '卸待機':
                    current_break_time += tt.elapsed_time
                # 労働時間(休憩以外)
                if tt.category != '積待機' and tt.category != '卸待機':
                    current_work_time += tt.elapsed_time
                # 連続運転中断時間
                if tt.category == '移動' and tt.elapsed_time > CONTINUTE_DRIVE_TIME_LIMIT:
                    # 中断回数 = int(所要時間 / 最大連続運転時間) [回]
                    interrupt_count = int(tt.elapsed_time / CONTINUTE_DRIVE_TIME_LIMIT)
                    current_drive_interrupt_time += interrupt_count*DRIVE_INTERRUPT_TIME
            
            # 拘束時間
            # NOTE: 始業から起算した24時間内の拘束時間
            current_bind_time = (current_end_time - current_start_time).total_seconds() / 3600
            current_extra_bind_time = self._calc_current_extra_bind_time(group_time_tables,vehicle_id,totaling_date,
                                                                         current_start_time, next_start_time)
            current_total_bind_time = current_bind_time + current_extra_bind_time

            # 残業時間
            # NOTE: 拘束時間から法定労働時間を差し引いた時間
            current_over_time = self._calc_over_time(current_bind_time, current_work_time)
                
            # レコード生成・登録
            self._record.append(
                ComplianceRecord(
                    vehicle_id=vehicle_id,
                    date=totaling_date,
                    start_time=current_start_time,
                    end_time=current_end_time,
                    bind_time=current_total_bind_time,
                    work_time=current_work_time,
                    drive_time=current_drive_time,
                    break_time=current_break_time,
                    over_time=current_over_time,
                    rest_time=current_rest_time,
                    drive_interupt_time=current_drive_interrupt_time,
                )
            )

        
    def to_dataframe(self):
        """コンプライアンス表の可視化

        Args:
            record (List[Record]): コンプライアンス時間を集計したレコード
        """
        
        # 表作成
        compliance_df = pd.DataFrame(self._record)
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
        
        # html出力
        compliance_df.to_html("compliance.html", index=True)
    
    def exe(self):
        """実行
        """
        group_time_tables = self._group_time_table()
        self._add_record(group_time_tables=group_time_tables)
        self.to_dataframe()
    
compliance_plan = CompliancePlan(time_table=test_time_table)
compliance_plan.exe()


# ################################################################
# 実車率クラス
# ################################################################
VEHICLE_SPEED = 26

@dataclass
class ActualVehicleRateRecord:
    vehicle_id : int = None                       # 車両ID
    vehicle_type : int = None                     # 車両タイプ
    load_dist : float = None                      # 実車距離
    unload_dist : float = None                    # 空車距離


@dataclass
class ActualVehicleRate:
    records: List[ActualVehicleRateRecord] = None  # レコード
    timetable : List[TimeTable] = None            # タイムテーブル
    
    def __init__(self, timetable: List[TimeTable]):
        """コンストラクタ

        Args:
            timetable (List[TimeTable]): 生成したタイムテーブル
        """
        self.records = []
        self.timetable = timetable

    def _group_time_table(self) -> Dict[int, List[TimeTable]]:
        """タイムテーブルをグルーピングする。

        Returns:
            Dict[Tuple, List[TimeTable]]: グルーピングしたタイムテーブル
        """
        # NOTE: 車両IDごとに集計する
        group_time_tables = defaultdict(list)
        for tt in self.timetable:
            group_time_tables[tt.vehicle.id].append(tt)
        return group_time_tables
    
    def _convert_move_dist(self, elapsed_time: float) -> float:
        """所要時間から距離に戻す

        Args:
            elapsed_time (float): 所要時間

        Returns:
            float: 移動距離
        """
        return elapsed_time*VEHICLE_SPEED
    
    def _add_record(self, group_time_tables: List[TimeTable]):
        """レコード生成・登録

        Args:
            group_time_tables (List[TimeTable]): グルーピングしたタイムテーブル
        """
        for vehicle_id in group_time_tables.keys():
            load_dist = 0.0
            unload_dist = 0.0
            vehicle_type = None
            for tt in group_time_tables[vehicle_id]:
                vehicle_type = tt.vehicle.type
                if tt.category == '移動':
                    if tt.start_area.type == 0 and tt.end_area.type == 1: # 実車
                        load_dist += self._convert_move_dist(tt.elapsed_time)
                    else:
                        unload_dist += self._convert_move_dist(tt.elapsed_time)
            
            # レコードを生成・登録
            self.records.append(ActualVehicleRateRecord(
                vehicle_id=vehicle_id,
                vehicle_type=vehicle_type,
                load_dist=load_dist,
                unload_dist=unload_dist
            ))
    
    def calc_rate(self):
        """実車率を計算
        """
        for r in self.records:
            rate = (r.load_dist / (r.load_dist + r.unload_dist))*100 
            rate = round(rate, 2) # unit[%]
            print(f"Vehicle_id: {r.vehicle_id},  Vehicle_type: {r.vehicle_type}, Rate: {rate} [%]")
    
    def exe(self):
        """実行
        """
        group_time_table = self._group_time_table()
        self._add_record(group_time_tables=group_time_table)
        self.calc_rate()

acutual_vehicle_rate = ActualVehicleRate(timetable=test_time_table)
acutual_vehicle_rate.exe()
