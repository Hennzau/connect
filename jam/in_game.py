import pygame
import numpy as np

from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.fonts import MOTO_MANGUCODE_50
from gfs.pallet import DARKBLUE, RED, IVORY
from gfs.images import SELECTOR_IMAGE

from gfs.sprites import Sprites
from gfs.sprite import AnimatedSprite

from jam.states import MAIN_MENU

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.point_particle import PointParticle

from jam.level.level import Level
from jam.level.grid import Grid
from jam.level.player import Player
from jam.level.tiles import TILE_SIZE


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()

        main_menu_button = Button(MOTO_MANGUCODE_50, "Go to main menu", (0, 0), self.main_menu)

        x = (width - main_menu_button.normal_image.get_width()) // 2
        y = height - main_menu_button.normal_image.get_height() * 2

        main_menu_button.pos = (x, y)

        self.interface.add_gui(main_menu_button)

        # tests

        self.sprites = Sprites()
        self.particle_system = ParticleSystem()

        # end tests

        # levels list

        self.levels = []
        self.current_level = None

        # tests

        self.levels.append(Level(Grid(10, 10), [Player()]))
        self.current_level = 0

    def main_menu(self):
        self.next_state = MAIN_MENU

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_motion(event)

    def update(self):
        self.interface.update()
        self.sprites.update()
        self.particle_system.update()

    def render(self, surface):
        surface.fill(IVORY)

        if self.current_level is not None:
            current_level = self.levels[self.current_level]

            # center the level image on the surface, and draw a frame around it

            x = (surface.get_width() - current_level.image.get_width()) / 2
            y = (surface.get_height() - current_level.image.get_height()) / 2

            surface.draw_rect(DARKBLUE, pygame.Rect(
                x - 5, y - 5, current_level.image.get_width() + 10, current_level.image.get_height() + 10))

            surface.draw_image(current_level.image, x, y)

            for player in current_level.players:
                surface.draw_image(player.image, x + player.grid_pos[0] * TILE_SIZE, y + player.grid_pos[1] * TILE_SIZE)

            # draw selector

            gap_x = x % TILE_SIZE
            gap_y = y % TILE_SIZE

            x = current_level.selector_pos[0] * TILE_SIZE + gap_x
            y = current_level.selector_pos[1] * TILE_SIZE + gap_y

            surface.draw_image(SELECTOR_IMAGE, x, y)

        self.interface.render(surface)
        self.sprites.render(surface)
        self.particle_system.render(surface)
