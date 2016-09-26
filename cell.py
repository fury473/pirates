class Cell(object):
    TYPE_EARTH = 'earth'
    TYPE_WATER = 'water'
    TYPES = [TYPE_EARTH, TYPE_WATER]

    def __init__(self, col, row, type = TYPE_WATER):
        self.col = col
        self.row = row
        self.type = type
