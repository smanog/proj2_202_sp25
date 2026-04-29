import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)


# Put your data definitions first!
@dataclass
class Row:
    emissions: float

@dataclass
class Node:
    value: Row
    next: Node|None
# ...

# Then your functions.
def read_csv_lines(filename: str) -> Optional[Node]:
    pass

def listlen(data: Optional[Node]) -> int:
    pass
