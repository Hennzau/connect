import pygame
import numpy as np

from gfs.image import Image

from gfs.fonts import PLAYGROUND_50, PLAYGROUND_30, PLAYGROUND_20, render_font
from gfs.pallet import DARKBLUE, RED, IVORY

from jam.level.tiles import TILE_SIZE
from jam.level.grid import Grid

RABBIT_TYPE = 0
ROBOT_TYPE = 1


class Player:
    def __init__(self, grid, player_type, grid_pos):
        self.image = Image(TILE_SIZE, TILE_SIZE)
        self.type = player_type
        self.grid = grid
        if self.type == RABBIT_TYPE:
            self.image.fill((255, 0, 0))
        elif self.type == ROBOT_TYPE:
            self.image.fill((0, 0, 255))

        self.power = 5
        self.power_image = render_font(PLAYGROUND_20, str(int(self.power)), IVORY)

        self.grid_pos = grid_pos

        self.render_pos = np.array([grid_pos[0], grid_pos[1]], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)

        self.entropy = 0

    def move_up(self):
        if [self.grid_pos[0], self.grid_pos[1] - 1] == self.grid.end:
            self.grid_pos[1] -= 1
        elif self.grid_pos[1] - 1 >= 0 and self.type == self.grid.get_tile(self.grid_pos[0], self.grid_pos[1] - 1):
            self.grid_pos[1] -= 1
        elif self.grid_pos[1] - 1 >= 0 and self.type != self.grid.get_tile(self.grid_pos[0],
                                                                           self.grid_pos[1] - 1) and self.power > 0:
            self.grid_pos[1] -= 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], self.type)
            self.entropy += 1

    def move_down(self):
        if [self.grid_pos[0], self.grid_pos[1] + 1] == self.grid.end:
            self.grid_pos[1] += 1
        elif self.grid_pos[1] + 1 < self.grid.height and self.type == self.grid.get_tile(self.grid_pos[0],
                                                                                         self.grid_pos[1] + 1):
            self.grid_pos[1] += 1
        elif self.grid_pos[1] + 1 < self.grid.height and self.type != self.grid.get_tile(self.grid_pos[0],
                                                                                         self.grid_pos[
                                                                                             1] + 1) and self.power > 0:
            self.grid_pos[1] += 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], self.type)
            self.entropy += 1

    def move_left(self):
        if [self.grid_pos[0] - 1, self.grid_pos[1]] == self.grid.end:
            self.grid_pos[0] -= 1
        elif self.grid_pos[0] - 1 >= 0 and self.type == self.grid.get_tile(self.grid_pos[0] - 1, self.grid_pos[1]):
            self.grid_pos[0] -= 1
        elif self.grid_pos[0] - 1 >= 0 and self.type != self.grid.get_tile(self.grid_pos[0] - 1,
                                                                           self.grid_pos[1]) and self.power > 0:
            self.grid_pos[0] -= 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], self.type)
            self.entropy += 1

    def move_right(self):
        if [self.grid_pos[0] + 1, self.grid_pos[1]] == self.grid.end:
            self.grid_pos[0] += 1
        elif self.grid_pos[0] + 1 < self.grid.width and self.type == self.grid.get_tile(
                self.grid_pos[0] + 1, self.grid_pos[1]):
            self.grid_pos[0] += 1
        elif self.grid_pos[0] + 1 < self.grid.width and self.type != self.grid.get_tile(self.grid_pos[0] + 1,
                                                                                        self.grid_pos[
                                                                                            1]) and self.power > 0:
            self.grid_pos[0] += 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], self.type)
            self.entropy += 1

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

    def build_image(self):
        self.power_image = render_font(PLAYGROUND_20, str(int(self.power)), IVORY)

    def update(self):

        self.render_pos += self.velocity * (1 / 60)

        self.velocity = (self.grid_pos - self.render_pos) * 10

        if self.grid.get_points(self.grid_pos[0], self.grid_pos[1]) > 0:
            self.power += self.grid.get_points(self.grid_pos[0], self.grid_pos[1])
            self.build_image()
            self.grid.set_points_to_zero(self.grid_pos[0], self.grid_pos[1])
            self.entropy += 1
