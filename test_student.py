import unittest
from typing import Optional, Union
from proj2 import (
    Row,
    Node,
    read_csv_lines,
    listlen,
    filter_rows,
    parse_row
)

class Test(unittest.TestCase):
    def test_csv_lines(self):
        pass

    def test_parse_row(self):
        row = parse_row([
            "Afghanistan", "1990", "0.32", "0.029921072", "", "0.1870067", "2.05", "0.19168186"
        ])
        self.assertIsInstance(row, Row)
        self.assertEqual(row.energy_co2_emissions, None)

    def test_listlen(self):
        r1 = Row("Afghanistan", 1990, 0.32, 0.029921072, 0.1870067, 2.05, 0.19168186, None)
        r2 = Row("Africa", 2002, 0.5, None, None, None, None, None)
        r3 = Row("Albania", 2024, None, None, None, None, None, None)
        lst = Node(r1, Node(r2, Node(r3, None)))
        self.assertEqual(listlen(lst), 3)

    def test_filter_rows(self):
        pass

if __name__ == "__main__":
    unittest.main()
