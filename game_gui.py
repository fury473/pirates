from cell import Cell
from configuration import Configuration
from geometry import HexagonGrid
from pygame import display
from pygame import draw
from pygame import FULLSCREEN
from debug import debug
from util import tuple_to_str

class Gui(object):
    def __init__(self):
        self.base_hex = None
        self.x_margin_grid = None
        display.set_caption('Pirates!')
        self.config = Configuration('gui_conf.json')
        self.init_screen()

    def init_screen(self):
        screen = display.set_mode((0, 0), FULLSCREEN)

    def toggle_fullscreen(self):

        higher_resolution = display.list_modes()[0]
        screen = display.get_surface()

        if screen.get_flags() & FULLSCREEN:
            screen = display.set_mode(self.config.windowed_resolution)
        else:
            screen = display.set_mode(higher_resolution, FULLSCREEN)

    def display_world_map(self, world_map):
            grid = HexagonGrid(world_map.cell_coords, display.get_surface())
            x_margin = 0.5 * (display.get_surface().get_width() - grid.width)
            grid.rect = grid.rect.move(x_margin, 0)
            grid_surface = display.get_surface().subsurface(grid.rect)
            for index, cell in world_map.cells.items():
                cells = world_map.find_cells_in_range(cell, 2)
                debug(cell)
                debug(cells)
                index = tuple_to_str((cell.col, cell.row))
                hexagon = grid.hexagons[index]
                draw.polygon(grid_surface, self.config.types_border[cell.type], list(hexagon.get_corners()), 1)

    def display_toggle_full_screen_instruction(self):
        display.get_surface().blit(self.config.font.render("Press F11 to toggle fullscreen mode.", 1, (255, 255, 255)), (0, 0))
