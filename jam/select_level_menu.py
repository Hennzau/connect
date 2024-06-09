from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.fonts import PLAYGROUND_100, PLAYGROUND_50, PLAYGROUND_30, PLAYGROUND_20, render_font
from gfs.pallet import IVORY, DARKBLUE, GREEN, LIGHTGREEN

from jam.states import IN_GAME, MAIN_MENU

from gfs.music import Music
from gfs.sounds import MAIN_MENU_MUSIC

from gfs.images import BACKGROUND_IMAGE_FULL

import pygame

from jam.level.grid import Grid

from jam.level.level import Level
from jam.level.grid import Grid
from jam.level.rabbit import Rabbit
from jam.level.robot import Robot
from jam.level.tiles import TILE_SIZE, TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT

import numpy as np


class SelectLevelMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None
        self.music = Music(MAIN_MENU_MUSIC)

        self.interface = Interface()

        self.game_name = render_font(PLAYGROUND_100, "Expand", GREEN)

        # explanations
        self.go_to = render_font(PLAYGROUND_20, "Move the rabbit to a level", GREEN)
        self.select = render_font(PLAYGROUND_20, "Press enter to play", GREEN)

        main_menu_button = Button(PLAYGROUND_50, "Go to main menu", (0, 0), self.main_menu, GREEN, LIGHTGREEN)

        x = (width - main_menu_button.normal_image.get_width()) // 2
        y = height - main_menu_button.normal_image.get_height() * 2

        main_menu_button.pos = (x, y)

        self.interface.add_gui(main_menu_button)

        self.levels = []

        grid = Grid(15, 15, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/levels/level_0.json")

        self.levels.append(Level(grid))
        self.levels[0].rabbit.level0 = True
        self.levels[0].robot.level0 = True

        self.current_level = 0

    def in_game(self):
        self.next_state = IN_GAME
        self.music.stop()

    def main_menu(self):
        self.next_state = MAIN_MENU

    def keyboard_input(self, event, game):
        self.interface.keyboard_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].keyboard_input(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pos = self.levels[0].rabbit.grid_pos
                points = self.levels[0].grid.get_points(pos[0], pos[1])
                if points > 0:
                    game.current_level = points
                    self.next_state = IN_GAME
                    self.music.stop()
                    game.editor_check_box.activate = False
                    game.editor.active = False
                    game.select_level_button.activate = True
                    game.select_custom_button.activate = False

    def mouse_input(self, event):
        self.interface.mouse_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)
        if self.current_level is not None:
            self.levels[self.current_level].mouse_motion(event)

    def update(self, option_menu):
        self.interface.update()

        if self.current_level is not None:
            level = self.levels[self.current_level]
            level.update()

        if option_menu.play_music:
            self.music.update()

    def render(self, surface):
        surface.draw_image(BACKGROUND_IMAGE_FULL, 0, 0)
        surface.draw_rect(GREEN, pygame.Rect(60 - 1, 60 - 1, 40 + self.go_to.get_width() + 2,
                                             40 + self.go_to.get_height() + 2))
        surface.draw_rect(LIGHTGREEN, pygame.Rect(60, 60, 40 + self.go_to.get_width(), 40 + self.go_to.get_height()))
        surface.draw_image(self.go_to, 80, 80)

        self.interface.render(surface)

        pos = self.levels[0].rabbit.grid_pos
        points = self.levels[0].grid.get_points(pos[0], pos[1])
        if points > 0:
            surface.draw_rect(GREEN,
                              pygame.Rect(60 + (self.go_to.get_width() - self.select.get_width()) / 2 - 1, 140 - 1,
                                          40 + self.select.get_width() + 2, 40 + self.select.get_height() + 2))
            surface.draw_rect(LIGHTGREEN, pygame.Rect(60 + (self.go_to.get_width() - self.select.get_width()) / 2, 140,
                                                      40 + self.select.get_width(), 40 + self.select.get_height()))
            surface.draw_image(self.select, 80 + (self.go_to.get_width() - self.select.get_width()) / 2, 160)

        if self.current_level is not None:
            current_level = self.levels[self.current_level]

            # center the level image on the surface, and draw a frame around it

            x = (surface.get_width() - current_level.image.get_width()) / 2
            y = (surface.get_height() - current_level.image.get_height()) / 2

            surface.draw_rect(DARKBLUE, pygame.Rect(
                x - 5, y - 5, current_level.image.get_width() + 10, current_level.image.get_height() + 10))

            surface.draw_image(current_level.image, x, y)

            current_level.rabbit.sprite.rect.x = x + current_level.rabbit.render_pos[0] * TILE_SIZE - TILE_SIZE // 2
            current_level.rabbit.sprite.rect.y = y + current_level.rabbit.render_pos[1] * TILE_SIZE - TILE_SIZE // 2

            current_level.robot.sprite.rect.x = -200

            current_level.sprites.render(surface)
