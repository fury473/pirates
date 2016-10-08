from graphic_component import GraphicComponentMixin
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

class Status(Enum):
    default = 0
    reachable = 1
    track_start = 2
    track_end = 3
