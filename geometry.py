from graphic_component import GraphicComponent
from cell import Cell
from configuration import config
from math import cos, sin, radians, sqrt
from pygame import Rect
from pygame import draw
from cell import Status as CellStatus

class Hexagon(GraphicComponent):
    def __init__(self, cell, size, center = (0, 0)):
        super().__init__(cell)
        self.size = size
        self.center = center
        self.width = self.get_width()
        self.height = self.get_height()
        self.corners = self.get_corners()

    def draw(self, surface):
        color = config.types_border[self.model.type]
        if (self.model.status == CellStatus.reachable):
            color = (0, 0, 255)
        if (self.model.status == CellStatus.track_start):
            color = (255, 0, 0)
        draw.polygon(surface, color, self.corners)

    def get_corners(self):
        center_x, center_y = self.center
        corners = []
        for i in range(0, 6):
            angle = radians(60 * i) #pointy topped
            x = center_x + self.size * cos(angle)
            y = center_y + self.size * sin(angle)
            corners.append((x, y))
        return corners

    def get_width(self):
        return 2 * self.size

    def get_height(self):
        return sqrt(3) * self.size

    @staticmethod
    def get_size_from_height(h):
        #pointy topped
        #h = sqrt(3)/2 * w  <=>  w = size * 2  <=>  h = sqrt(3) * size
        size = h/sqrt(3);
        return size

class HexagonGrid(object):
    def __init__(self, cells, parent_surface):
        self.parent_surface = parent_surface
        coords = self.get_coords(cells)
        col_count, row_count = self.get_row_count_and_col_count(coords)
        prototype = self.get_prototype(row_count)
        self.width, self.height = self.get_dimensions(col_count, row_count, prototype)
        self.rect = Rect(0, 0, self.width, self.height)
        self.hexagons = {}
        for i, cell in cells.items():
            hex = self.generate_hexagon(cell, prototype)
            self.hexagons[i] = hex

    def get_coords(self, cells):
        coords = []
        for i,cell in cells.items():
            coords.append((cell.col, cell.row))
        return coords


    def get_dimensions(self, col_count, row_count, prototype):
        width = col_count * 0.75 * prototype.width + 0.5 * prototype.width
        height = row_count * prototype.height + 0.5 * prototype.height
        return (width, height)

    def get_prototype(self, row_count):
        height = self.get_prototype_height(row_count)
        size = Hexagon.get_size_from_height(height)
        return Hexagon(Cell(0, 0), size)

    def get_prototype_height(self, row_count):
        r = row_count
        H = self.parent_surface.get_height()
        # H = rh + h/2
        h = H/(r+0.5)
        return h

    def get_row_count_and_col_count(self, coords):
        max_coord = list(map(max, zip(*coords)))
        col_count = max_coord[0] + 1
        row_count = max_coord[1] + 1
        return (col_count, row_count)

    def generate_hexagon(self, cell, prototype):
        col = cell.col
        row = cell.row
        x = 0.5 * prototype.width
        y = 0.5 * prototype.height
        delta_x = col * 0.75 * prototype.width
        delta_y = row * prototype.height
        if (col%2 == 0):
            delta_y += 0.5 * prototype.height
        index = str(col) + ',' + str(row)
        x += delta_x
        y += delta_y
        return Hexagon(cell, prototype.size, (x, y))


