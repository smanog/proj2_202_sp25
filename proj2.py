import csv
import math
from dataclasses import dataclass
from typing import *


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

# ...
