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
    electricity_and_heat_co2_emissions: float|None
    electricity_and_heat_co2_emissions_per_capita: float|None
    energy_co2_emissions: float|None
    energy_co2_emissions_per_capita: float|None
    total_co2_emissions_excluding_lucf: float|None
    total_co2_emissions_excluding_lucf_per_capita: float|None

@dataclass(frozen = True)
class Node:
    value: Row
    next: Node|None
# ...

# Then your functions.
#Turns the rows from the file into Row objects and builds a linked list of Nodes using that data
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        parse_row(next(reader))
    return read_csv_lines(filename)

#converts the data given in the csv file from string into float or int
def parse_row(fields: list[str]) -> Row:
    convert = Row(fields[0], int(fields[1]), float(fields[2]), float(fields[3]), float(fields[4]), float(fields[5]), float(fields[6]), float(fields[7]))
    return convert

#returns the number of Rows there are in a list
def listlen(data: Optional[Node], count: int = 0) -> int:
    if data == None:
        return count
    if data.next != None:
        return listlen(data.next, count + 1)

#filters the data given certain bounds
def filter_rows(data: Optional[Node],field_name: str,comparison: str,value: Union[str, float, int]) -> Optional[Node]:
    if data.value.country == value:
        return data
    pass

#for reference for now
#def total_item_count(filename: str) -> int:
 #   with open(filename, newline="") as csvfile:
  #      iter = csv.reader(csvfile)
   #     topline = next(iter)
    #    if not (topline == expected_labels):
     #       raise ValueError("unexpected first line: got: {}".format(topline))
      #  item_count = 0
       # for line in iter:
        #    item_count = item_count + float(line[2])
        #return item_count
