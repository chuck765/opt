# 標準ライブラリ
from IPython.display import display

# サードパーティ
from Bio.PDB import *
from typing import List
import pandas as pd
import numpy as np

# 自作ライブラリ
from modules.dataclass import Monomer, Coordinate

class Entity:
    file_name : str
    monomers : List[Monomer]
    
    def __init__(self, file_name: str):
        self.file_name = file_name
    
    def get_coordinate(self, coord: List[float]):
        return Coordinate(x=coord[0],y=coord[1],z=coord[2])
    
    def generate_monomers(self):
        structure = PDBParser().get_structure('X', self.file_name)
        np.random.seed(0)
        monomers = []
        u_id = 1
        for model in structure.get_list():
            for chain in model.get_list():
                for residue in chain.get_list():
                    for atom in residue.get_list():
                        monomers.append(
                            Monomer(
                                serial_number=u_id,
                                atom=atom.get_name(),
                                base=residue.get_resname(),
                                residue_id=residue.get_id()[1],
                                coordinate=self.get_coordinate(atom.get_coord()),
                                bfactor=np.random.randint(-100, 0)
                            )
                        )
                        u_id+=1
        self.monomers = monomers
    
    def to_dataframe(self):
        display(pd.DataFrame(self.monomers))