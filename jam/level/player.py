import pygame
import numpy as np

from gfs.image import Image

from jam.level.tiles import TILE_SIZE
from jam.level.grid import Grid

RABBIT_TYPE = 0
ROBOT_TYPE = 1


class Player:
    def __init__(self, grid, player_type,grid_pos):
        self.image = Image(TILE_SIZE, TILE_SIZE)
        self.type = player_type
        self.grid = grid
        if self.type == RABBIT_TYPE:
            self.image.fill((255, 0, 0))
        elif self.type == ROBOT_TYPE:
            self.image.fill((0,0,255))
        

        self.power = 5

        self.grid_pos = grid_pos

        self.render_pos = np.array([grid_pos[0], grid_pos[1]], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)

    def move_up(self):
        if self.grid_pos[1] - 1 >= 0 and self.type == self.grid.get_tile(self.grid_pos[0], self.grid_pos[1] - 1):
            self.grid_pos[1] -= 1

    def move_down(self):
        if self.grid_pos[1] + 1 < self.grid.height and self.type == self.grid.get_tile(self.grid_pos[0],
                                                                                       self.grid_pos[1] + 1):
            self.grid_pos[1] += 1

    def move_left(self):
        if self.grid_pos[0] - 1 >= 0 and self.type == self.grid.get_tile(self.grid_pos[0] - 1, self.grid_pos[1]):
            self.grid_pos[0] -= 1

    def move_right(self):
        if self.grid_pos[0] + 1 < self.grid.width and self.type == self.grid.get_tile(
                self.grid_pos[0] + 1, self.grid_pos[1]):
            self.grid_pos[0] += 1

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_up()
            elif event.key == pygame.K_DOWN:
                self.move_down()
            elif event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
            

    def update(self):
        self.render_pos += self.velocity * (1 / 60)
        self.velocity = (self.grid_pos - self.render_pos) * 10

        if self.grid.get_points(self.grid_pos[0],self.grid_pos[1])>0:
            self.power+=self.grid.get_points(self.grid_pos[0],self.grid_pos[1])
            self.grid.set_points_to_zero(self.grid_pos[0],self.grid_pos[1])
