from graphic_component import GraphicComponentMixin
from util import tuple_to_str
from enum import Enum

class Cell(GraphicComponentMixin):
    TYPE_EARTH = 'earth'
    TYPE_WATER = 'water'
    TYPES = [TYPE_EARTH, TYPE_WATER]

    def __init__(self, col, row, type = TYPE_WATER):
        super().__init__()
        self.status = Status.default
        self.col = col
        self.row = row
        self.type = type

    def get_index(self):
        return tuple_to_str((self.col, self.row))

    def get_directions(self):
        if self.col % 2 == 0: #even
            return [
            (1, 1), (1,  0), (0, -1),
            (-1,  0), (-1, 1), ( 0, 1)]
        else: #odd
            return [
            (1, 0), (1,  -1), (0, -1),
            (-1, -1), (-1, 0), ( 0, 1)]

    def is_obstacle(self):
        return self.type == self.TYPE_EARTH

class Status(Enum):
    default = 0
    reachable = 1
    track_start = 2
    track_end = 3
