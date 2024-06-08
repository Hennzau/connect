import pygame
import gfs.pallet

from gfs.image import Image
from jam.level.tiles import TILE_SIZE, TILE_GREEN, TILE_GREY, TILE_WALL
from gfs.fonts import PLAYGROUND_50, PLAYGROUND_30, PLAYGROUND_20, render_font

from jam.level.rabbit import Rabbit
from jam.level.robot import Robot


class Level:
    def __init__(self, grid):
        self.image = Image(grid.width * TILE_SIZE, grid.height * TILE_SIZE)
        self.grid = grid

        self.rabbit = Rabbit(self.grid)
        self.robot = Robot(self.grid)
        self.player = self.rabbit

        self.build_image()

        self.last_player_entropy = 0

    def keyboard_input(self, event):
        self.player.keyboard_input(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.player == self.rabbit:
                self.player = self.robot
            else:
                self.player = self.rabbit

    def mouse_motion(self, event):
        pass

    def mouse_input(self, event):
        pass

    def update(self):
        self.player.update()

        if self.player.entropy != self.last_player_entropy:
            self.build_image()
            self.last_player_entropy = self.rabbit.entropy

    def reload(self):
        pass

    def build_image(self):
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                tile_type = self.grid.get_tile(i, j)
                if tile_type == TILE_GREY:
                    self.image.draw_rect(gfs.pallet.DARKGREY,
                                         pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if tile_type == TILE_GREEN:
                    self.image.draw_rect(gfs.pallet.GREEN,
                                         pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if tile_type == TILE_WALL:
                    self.image.draw_rect(gfs.pallet.VOLKSWAGEN_TAUPE,
                                         pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                points = self.grid.get_points(i, j)
                if points > 0:
                    power_image = render_font(PLAYGROUND_20, str(int(points)), gfs.pallet.IVORY)
                    self.image.draw_image(power_image,
                                          i * TILE_SIZE + (TILE_SIZE - power_image.get_width()) / 2,
                                          j * TILE_SIZE + (TILE_SIZE - power_image.get_height()) / 2)

                if [i, j] == self.grid.end:
                    self.image.draw_rect(gfs.pallet.BLACK,
                                         pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))
