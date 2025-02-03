from dataclasses import dataclass
from enum import Enum

# ################################################################
# 車両クラス
# ################################################################
@dataclass
class VehicleType(Enum):
    TANK = 0
    HEAD = 1

@dataclass
class Vehicle:
    id: int = None                 # 車両ID
    name: str = None               # 車番
    type: VehicleType = None       # 車のタイプ


# ################################################################
# 場所クラス
# ################################################################
@dataclass
class Area:
    name : str = None              # 地点名