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

from jam.editor import Editor


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()
        self.editor = Editor()

        main_menu_button = Button(PLAYGROUND_50, "Go to main menu", (0, 0), self.main_menu)

        x = (width - main_menu_button.normal_image.get_width()) // 2
        y = height - main_menu_button.normal_image.get_height() * 2

        main_menu_button.pos = (x, y)

        self.interface.add_gui(main_menu_button)

        # check box
        editor_check_box = CheckBox(PLAYGROUND_30, "Editor Enabled/Disabled", (0, 20), self.editor.activate,
                                    self.editor.deactivate)

        self.interface.add_gui(editor_check_box)

        # tests

        self.sprites = Sprites()
        self.particle_system = ParticleSystem()

        # end tests

        # levels list

        self.levels = []
        self.current_level = None

        # tests
        grid = Grid(20, 10)
        self.levels.append(Level(grid))
        self.current_level = 0
        self.selector_pos = (0, 0)

        self.left_click = False

    def main_menu(self):
        self.next_state = MAIN_MENU

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].keyboard_input(event)

        self.editor.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_input(event)

        self.left_click = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

        self.editor.mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_motion(event)

            # get the position of the top left corner of the level image
            x = (self.surface_configuration[0] - self.levels[self.current_level].image.get_width()) / 2
            y = (self.surface_configuration[1] - self.levels[self.current_level].image.get_height()) / 2

            # get the position of the selector
            x = (event.pos[0] - x) // TILE_SIZE
            y = (event.pos[1] - y) // TILE_SIZE

            # set the selector position if it is inside the level grid

            if 0 <= x < self.levels[self.current_level].grid.width and 0 <= y < self.levels[
                self.current_level].grid.height:
                self.selector_pos = (x, y)
            else:
                self.selector_pos = None

        self.editor.mouse_motion(event)

    def update(self):
        self.interface.update()
        self.sprites.update()
        self.particle_system.update()

        if self.current_level is not None:
            level = self.levels[self.current_level]
            level.update()

            if level.grid.get_tile(level.rabbit.grid_pos[0], level.rabbit.grid_pos[1]) != level.rabbit.type:
                level.reload()
                self.next_state = DEFEAT_MENU

            if level.grid.get_tile(level.robot.grid_pos[0], level.robot.grid_pos[1]) != level.robot.type:
                level.reload()
                self.next_state = DEFEAT_MENU

            if self.editor.active:
                level = self.levels[self.current_level]

                if self.selector_pos is not None:
                    x = int(self.selector_pos[0])
                    y = int(self.selector_pos[1])
                    if self.left_click:
                        if self.editor.current_type is not None:
                            level.grid.set_tile(x, y, self.editor.current_type)
                            level.build_image()
            else:
                level = self.levels[self.current_level]

                player_type = level.player.type
                power = level.player.power
                if self.selector_pos is not None:
                    x = int(self.selector_pos[0])
                    y = int(self.selector_pos[1])
                    if self.left_click:
                        if power > 0 and level.grid.get_tile(x, y) != player_type and level.grid.end != [x, y]:
                            level.grid.set_tile(x, y, player_type)
                            level.build_image()
                            level.player.power = power - 1
                            level.player.build_image()

        self.editor.update()

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

            surface.draw_image(current_level.rabbit.image, x + current_level.rabbit.render_pos[0] * TILE_SIZE,
                               y + current_level.rabbit.render_pos[1] * TILE_SIZE)
            surface.draw_image(current_level.rabbit.power_image,
                               x + (current_level.rabbit.render_pos[0] + 1) * TILE_SIZE,
                               y + current_level.rabbit.render_pos[
                                   1] * TILE_SIZE - current_level.rabbit.power_image.height)

            surface.draw_image(current_level.robot.image, x + current_level.robot.render_pos[0] * TILE_SIZE,
                               y + current_level.robot.render_pos[1] * TILE_SIZE)
            surface.draw_image(current_level.robot.power_image,
                               x + (current_level.robot.render_pos[0] + 1) * TILE_SIZE,
                               y + current_level.robot.render_pos[
                                   1] * TILE_SIZE - current_level.robot.power_image.height)

            # draw selector

            if self.selector_pos is not None:
                x = self.selector_pos[0] * TILE_SIZE + x
                y = self.selector_pos[1] * TILE_SIZE + y

                surface.draw_image(SELECTOR_IMAGE, x, y)

        self.interface.render(surface)
        self.sprites.render(surface)
        self.particle_system.render(surface)

        self.editor.render(surface)
