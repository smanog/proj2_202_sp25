import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)


# Put your data definitions first!
@dataclass(frozen = True)
class Row:
    country: str|None
    year: int|None
    heat_emissions: float|None
    heat_per_capita: float|None
    energy_emissions: float|None
    energy_per_capita: float|None
    total_emissions: float|None
    total_per_capita: float|None
    emissions: float

@dataclass(frozen = True)
class Node:
    value: Row
    next: Node|None
# ...

# Then your functions.
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
    return Node(read_csv_lines(filename))

def listlen(data: Optional[Node]) -> int:
    pass
#for reference for now
def total_item_count(filename: str) -> int:
    with open(filename, newline="") as csvfile:
        iter = csv.reader(csvfile)
        topline = next(iter)
        if not (topline == expected_labels):
            raise ValueError("unexpected first line: got: {}".format(topline))
        item_count = 0
        for line in iter:
            item_count = item_count + float(line[2])
        return item_count
