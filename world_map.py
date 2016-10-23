from cell import Cell
from numpy import add, subtract
from util import tuple_to_str
from pprint import pprint
from sys import exit as die

class WorldMap(object):
    UNMAPPED_CELLS = [(0,0), (5,0), (7,0), (7,1), (0,4), (6,4)]
    EARTH_CELLS = [(1,0), (3,0), (6,0), (8,0), (0,1), (4,1), (2,2), (0,3), (2,4), (4,4)]
    def __init__(self):
        self.col_count = 9
        self.row_count = 5
        self.cells = {}
        self.cell_coords = []
        for col in range(self.col_count):
            for row in range(self.row_count):
                type = Cell.TYPE_WATER
                if (col, row) in self.EARTH_CELLS:
                    type = Cell.TYPE_EARTH
                if (col, row) not in self.UNMAPPED_CELLS:
                    index = tuple_to_str((col, row))
                    self.cells[index] = Cell(col, row, type)
                    self.cell_coords.append((col, row))

    def find_cells_in_range(self, cell, range, origin_cell = None):
        if (origin_cell == None):
            origin_cell = cell
        if (range <= 0):
            return []

        cells_in_range = []
        for deltas in cell.get_directions():
            (delta_col, delta_row) = add((cell.col, cell.row), deltas)
            if (delta_col, delta_row) in self.cell_coords:
                index = tuple_to_str((delta_col, delta_row))
                reachable_cell = self.cells[index]

                if (reachable_cell.is_obstacle()):
                    continue

                if reachable_cell not in cells_in_range and reachable_cell != origin_cell:
                    cells_in_range.append(reachable_cell)

                sub_cells_in_range = self.find_cells_in_range(reachable_cell, range - 1, origin_cell)

                for sub_cell in sub_cells_in_range:
                    if sub_cell not in cells_in_range and sub_cell != origin_cell:
                        cells_in_range.append(sub_cell)
        return cells_in_range
