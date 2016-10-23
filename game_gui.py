from cell import Cell
from cell import Status as CellStatus
from configuration import config
from geometry import HexagonGrid
from pygame import font
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
        self.init_screen()

    def init_screen(self):
        screen = display.set_mode((0, 0), FULLSCREEN)

    def toggle_fullscreen(self):

        higher_resolution = display.list_modes()[0]
        screen = display.get_surface()

        if screen.get_flags() & FULLSCREEN:
            screen = display.set_mode(config.windowed_resolution)
        else:
            screen = display.set_mode(higher_resolution, FULLSCREEN)

    def display_world_map(self, world_map):
            grid = HexagonGrid(world_map.cells, display.get_surface())
            x_margin = 0.5 * (display.get_surface().get_width() - grid.width)
            grid.rect = grid.rect.move(x_margin, 0)
            grid_surface = display.get_surface().subsurface(grid.rect)
            for index, cell in world_map.cells.items():
                if cell.row == 1 and cell.col == 1:
                    cell.status = CellStatus.track_start
                    cells = world_map.find_cells_in_range(cell, 3)
                    for reachable_cell in cells:
                        reachable_cell.status = CellStatus.reachable
            for index, cell in world_map.cells.items():
                cell.draw(grid_surface)

    def display_toggle_full_screen_instruction(self):
        display_font = font.Font(config.font['file'], config.font['size'])
        display.get_surface().blit(display_font.render("Press F11 to toggle fullscreen mode.", 1, (255, 255, 255)), (0, 0))
