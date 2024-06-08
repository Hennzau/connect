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

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.point_particle import PointParticle

from jam.level.level import Level
from jam.level.grid import Grid
from jam.level.player import Player, RABBIT_TYPE, ROBOT_TYPE
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
        self.levels.append(
            Level(grid, [Player(grid, RABBIT_TYPE, np.array([0, 0])), Player(grid, ROBOT_TYPE, np.array([0, 4]))]))
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
            self.levels[self.current_level].update()

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

                if level.current_player is not None:
                    player = level.players[level.current_player]
                    player_type = player.type
                    power = player.power
                    if self.selector_pos is not None:
                        x = int(self.selector_pos[0])
                        y = int(self.selector_pos[1])
                        if self.left_click:
                            if power > 0 and level.grid.get_tile(x, y) != player_type:
                                level.grid.set_tile(x, y, player_type)
                                level.build_image()
                                player.power = power - 1
                                player.build_image()

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

            for player in current_level.players:
                surface.draw_image(player.image, x + player.render_pos[0] * TILE_SIZE,
                                   y + player.render_pos[1] * TILE_SIZE)
                surface.draw_image(player.power_image, x + (player.render_pos[0] + 1) * TILE_SIZE,
                                   y + player.render_pos[1] * TILE_SIZE - player.power_image.height)

            # draw selector

            if self.selector_pos is not None:
                x = self.selector_pos[0] * TILE_SIZE + x
                y = self.selector_pos[1] * TILE_SIZE + y

                surface.draw_image(SELECTOR_IMAGE, x, y)

        self.interface.render(surface)
        self.sprites.render(surface)
        self.particle_system.render(surface)

        self.editor.render(surface)
