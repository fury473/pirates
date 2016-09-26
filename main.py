#!/usr/bin/env python

from game_gui import Gui
import pygame
from world_map import WorldMap
def main():

    pygame.init()
    gui = Gui()
    world_map = WorldMap()
    gui.display_world_map(world_map)
    gui.display_toggle_full_screen_instruction()
    pygame.display.flip()

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_F11:
                gui.toggle_fullscreen()
                gui.display_world_map(world_map)
                gui.display_toggle_full_screen_instruction()
            elif e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                return
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
