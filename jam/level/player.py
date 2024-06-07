import pygame
import numpy as np

from gfs.image import Image

from jam.level.tiles import TILE_SIZE


class Player:
    def __init__(self):
        self.image = Image(TILE_SIZE, TILE_SIZE)
        self.image.fill((255, 0, 0))

        self.grid_pos = np.array([0, 0])

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.grid_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                self.grid_pos[1] += 1
            elif event.key == pygame.K_LEFT:
                self.grid_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                self.grid_pos[0] += 1

    def update(self):
        pass
