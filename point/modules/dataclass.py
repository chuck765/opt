from dataclasses import dataclass

@dataclass
class Coordinate:
    x: float
    y: float
    z: float

@dataclass
class Monomer:
    serial_number : int
    atom : str
    base : str
    residue_id: int
    coordinate: Coordinate
    bfactor : float