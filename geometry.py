from math import cos, sin, radians, sqrt
from pygame import Rect


class Hexagon(object):
    def __init__(self, size, center = None):
        self.size = size
        self.center = center
        self.width = self.get_width()
        self.height = self.get_height()
        self.corners = self.get_corners()

    def get_corners(self):
        center_x, center_y = self.center
        for i in range(0, 6):
            angle = radians(60 * i) #pointy topped
            x = center_x + self.size * cos(angle)
            y = center_y + self.size * sin(angle)
            yield x, y

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
    def __init__(self, coords, parent_surface):
        self.parent_surface = parent_surface
        col_count, row_count = self.get_row_count_and_col_count(coords)
        prototype = self.get_prototype(row_count)
        self.width, self.height = self.get_dimensions(col_count, row_count, prototype)
        self.rect = Rect(0, 0, self.width, self.height)
        self.hexagons = {}
        for coord in coords:
            col, row = coord
            index = str(col) + ',' + str(row)
            self.hexagons[index] = self.generate_hexagon(col, row, prototype)

    def get_dimensions(self, col_count, row_count, prototype):
        width = col_count * 0.75 * prototype.width + 0.5 * prototype.width
        height = row_count * prototype.height + 0.5 * prototype.height
        return (width, height)

    def get_prototype(self, row_count):
        height = self.get_prototype_height(row_count)
        size = Hexagon.get_size_from_height(height)
        return Hexagon(size)

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

    def generate_hexagon(self, col, row, prototype):
        x = 0.5 * prototype.width
        y = 0.5 * prototype.height
        delta_x = col * 0.75 * prototype.width
        delta_y = row * prototype.height
        if (col%2 == 0):
            delta_y += 0.5 * prototype.height
        index = str(col) + ',' + str(row)
        x += delta_x
        y += delta_y
        return Hexagon(prototype.size, (x, y))


