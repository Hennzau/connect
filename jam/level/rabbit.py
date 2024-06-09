import pygame
import numpy as np

from gfs.fonts import PLAYGROUND_20, render_font
from gfs.pallet import IVORY

from jam.level.tiles import TILE_SIZE, TILE_GRASS, POINT_TREE, TILE_WATER

from gfs.images import JUMPING_RIGHT, JUMPING_LEFT, JUMPING_UP, JUMPING_DOWN, IDLE_RIGHT, IDLE_LEFT, IDLE_UP, IDLE_DOWN

from gfs.sprite import AnimatedSprite

from gfs.sounds import PICKUP, BUNNY


class Rabbit:
    def __init__(self, grid):
        self.grid = grid

        self.power = grid.rabbit_power
        self.power_image = render_font(PLAYGROUND_20, str(int(self.power)), IVORY)

        self.grid_pos = grid.rabbit_start

        self.render_pos = np.array([self.grid_pos[0], self.grid_pos[1]], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)

        self.entropy = 0

        self.type = TILE_GRASS
        self.level0 = False

        self.sprite = AnimatedSprite(0, 0, TILE_SIZE, TILE_SIZE, {
            "jump_right": (4, JUMPING_RIGHT),
            "jump_left": (4, JUMPING_LEFT),
            "jump_up": (4, JUMPING_UP),
            "jump_down": (4, JUMPING_DOWN),
            "idle_right": (4, IDLE_RIGHT),
            "idle_left": (4, IDLE_LEFT),
            "idle_up": (4, IDLE_UP),
            "idle_down": (4, IDLE_DOWN)
        }, 4)

        self.sprite.animate("idle_right")

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.timer = 0.0
        # dans rabbit créer un bool Level0 ou pas : si Level0, on consomme pas les points, on a 0 power

    def move_up(self):
        if self.grid_pos[1] - 1 >= 0 and TILE_GRASS == self.grid.get_tile(self.grid_pos[0], self.grid_pos[
                                                                                                1] - 1) and not self.grid.get_tile(
            self.grid_pos[0], self.grid_pos[1] - 1) == TILE_WATER:
            self.grid_pos[1] -= 1
        elif self.grid_pos[1] - 1 >= 0 and TILE_GRASS != self.grid.get_tile(self.grid_pos[0],
                                                                            self.grid_pos[
                                                                                1] - 1) and self.power > 0 and not self.grid.get_tile(
            self.grid_pos[0], self.grid_pos[1] - 1) == TILE_WATER:
            self.grid_pos[1] -= 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], TILE_GRASS)
            self.entropy += 1

    def move_down(self):
        if self.grid_pos[1] + 1 < self.grid.height and TILE_GRASS == self.grid.get_tile(self.grid_pos[0],
                                                                                        self.grid_pos[
                                                                                            1] + 1) and not self.grid.get_tile(
            self.grid_pos[0], self.grid_pos[1] + 1) == TILE_WATER:
            self.grid_pos[1] += 1
        elif self.grid_pos[1] + 1 < self.grid.height and TILE_GRASS != self.grid.get_tile(self.grid_pos[0],
                                                                                          self.grid_pos[
                                                                                              1] + 1) and self.power > 0 and not self.grid.get_tile(
            self.grid_pos[0], self.grid_pos[1] + 1) == TILE_WATER:
            self.grid_pos[1] += 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], TILE_GRASS)
            self.entropy += 1

    def move_left(self):
        if self.grid_pos[0] - 1 >= 0 and TILE_GRASS == self.grid.get_tile(self.grid_pos[0] - 1,
                                                                          self.grid_pos[1]) and not self.grid.get_tile(
            self.grid_pos[0] - 1, self.grid_pos[1]) == TILE_WATER:
            self.grid_pos[0] -= 1
        elif self.grid_pos[0] - 1 >= 0 and TILE_GRASS != self.grid.get_tile(self.grid_pos[0] - 1,
                                                                            self.grid_pos[
                                                                                1]) and self.power > 0 and not self.grid.get_tile(
            self.grid_pos[0] - 1, self.grid_pos[1]) == TILE_WATER:
            self.grid_pos[0] -= 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], TILE_GRASS)
            self.entropy += 1

    def move_right(self):
        if self.grid_pos[0] + 1 < self.grid.width and TILE_GRASS == self.grid.get_tile(
                self.grid_pos[0] + 1, self.grid_pos[1]) and not self.grid.get_tile(self.grid_pos[0] + 1,
                                                                                   self.grid_pos[1]) == TILE_WATER:
            self.grid_pos[0] += 1
        elif self.grid_pos[0] + 1 < self.grid.width and TILE_GRASS != self.grid.get_tile(self.grid_pos[0] + 1,
                                                                                         self.grid_pos[
                                                                                             1]) and self.power > 0 and not self.grid.get_tile(
            self.grid_pos[0] + 1, self.grid_pos[1]) == TILE_WATER:
            self.grid_pos[0] += 1
            self.power -= 1
            self.build_image()
            self.grid.set_tile(self.grid_pos[0], self.grid_pos[1], TILE_GRASS)
            self.entropy += 1

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.up = True
                BUNNY.play()
            elif event.key == pygame.K_DOWN:
                self.down = True
                BUNNY.play()
            elif event.key == pygame.K_LEFT:
                self.left = True
                BUNNY.play()
            elif event.key == pygame.K_RIGHT:
                self.right = True
                BUNNY.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up = False
            elif event.key == pygame.K_DOWN:
                self.down = False
            elif event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False

    def build_image(self):
        self.power_image = render_font(PLAYGROUND_20, str(int(self.power)), IVORY)

    def update(self):
        if self.up and self.timer < 0.016:
            self.move_up()
            self.sprite.animate("jump_up", "idle_up")
        if self.down and self.timer < 0.016:
            self.move_down()
            self.sprite.animate("jump_down", "idle_down")
        if self.left and self.timer < 0.016:
            self.move_left()
            self.sprite.animate("jump_left", "idle_left")
        if self.right and self.timer < 0.016:
            self.move_right()
            self.sprite.animate("jump_right", "idle_right")

        if self.up or self.down or self.left or self.right:
            self.timer += 1 / 60
        else:
            self.timer = 0.0

        if self.timer >= 0.5:
            self.timer = 0.0

        self.render_pos += self.velocity * (1 / 60)

        if np.linalg.norm(self.grid_pos - self.render_pos) < 0.05:
            self.render_pos = np.array([self.grid_pos[0], self.grid_pos[1]], dtype=float)
            self.velocity = np.array([0, 0], dtype=float)
        else:
            self.velocity = (self.grid_pos - self.render_pos) * 15

        if self.level0 == False:
            if self.grid.get_points(self.grid_pos[0], self.grid_pos[1]) > 0 and self.grid.get_victory_points(
                    self.grid_pos[0], self.grid_pos[1]) == POINT_TREE:
                self.power += self.grid.get_points(self.grid_pos[0], self.grid_pos[1])
                self.build_image()
                self.grid.set_points_to_zero(self.grid_pos[0], self.grid_pos[1])
                self.entropy += 1
                PICKUP.play()

        if self.level0 == True:
            self.power = 0
