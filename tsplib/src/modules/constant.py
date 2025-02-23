from dataclasses import dataclass
from enum import Enum

@dataclass
class ProblemType(Enum):
    EUC_2D = 0
    GEO = 1