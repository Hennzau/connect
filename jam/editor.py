import pygame
import numpy as np

from gfs.gui.interface import Interface
from gfs.gui.button import Button
from gfs.gui.check_box import CheckBox

from gfs.fonts import PLAYGROUND_50, PLAYGROUND_30
from gfs.pallet import DARKBLUE, RED, IVORY
from gfs.images import SELECTOR_IMAGE

from gfs.sprites import Sprites
from gfs.sprite import AnimatedSprite

from jam.states import MAIN_MENU
from jam.states import DEFEAT_MENU

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.point_particle import PointParticle

from jam.level.level import Level
from jam.level.grid import Grid
from jam.level.rabbit import Rabbit
from jam.level.robot import Robot
from jam.level.tiles import TILE_SIZE, TILE_GREEN, TILE_GREY, TILE_WALL


class Editor:
    def __init__(self):
        self.current_type = None
        self.active = False

        self.interface = Interface()

        # check box
        self.green_check_box = CheckBox(PLAYGROUND_30, "Green Tile", (0, 100), self.switch_to_green,
                                        self.switch_to_none)

        self.interface.add_gui(self.green_check_box)

        # check box
        self.grey_check_box = CheckBox(PLAYGROUND_30, "Grey Tile", (0, 200), self.switch_to_grey,
                                       self.switch_to_none)

        self.interface.add_gui(self.grey_check_box)

        # check box
        self.wall_check_box = CheckBox(PLAYGROUND_30, "Wall Tile", (0, 300), self.switch_to_wall,
                                       self.switch_to_none)

        self.interface.add_gui(self.wall_check_box)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def switch_to_none(self):
        self.current_type = None

        self.green_check_box.check = False
        self.grey_check_box.check = False
        self.wall_check_box.check = False

    def switch_to_wall(self):
        self.current_type = TILE_WALL

        self.green_check_box.check = False
        self.grey_check_box.check = False

    def switch_to_green(self):
        self.current_type = TILE_GREEN

        self.grey_check_box.check = False
        self.wall_check_box.check = False

    def switch_to_grey(self):
        self.current_type = TILE_GREY

        self.green_check_box.check = False
        self.wall_check_box.check = False

    def render(self, surface):
        if self.active:
            self.interface.render(surface)

    def keyboard_input(self, event):
        if self.active:
            self.interface.keyboard_input(event)

    def mouse_input(self, event):
        if self.active:
            self.interface.mouse_input(event)

    def mouse_motion(self, event):
        if self.active:
            self.interface.mouse_motion(event)

    def update(self):
        if self.active:
            self.interface.update()
