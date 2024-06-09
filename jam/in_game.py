import pygame
import numpy as np

from gfs.gui.interface import Interface
from gfs.gui.button import Button
from gfs.gui.check_box import CheckBox

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.point_particle import PointParticle

from gfs.fonts import PLAYGROUND_50, PLAYGROUND_30, PLAYGROUND_20, render_font
from gfs.pallet import DARKBLUE, RED, IVORY, GREEN, LIGHTGREEN
from gfs.images import SELECTOR_IMAGE, JUMPING_RIGHT, BACKGROUND_IMAGE_FULL

from gfs.sprites import Sprites
from gfs.sprite import AnimatedSprite

from jam.states import MAIN_MENU
from jam.states import DEFEAT_MENU, VICTORY_MENU, LEVEL_SELECTION, CUSTOM_LEVEL_SELECTION

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.particles import RED_POINT_5, YELLOW_POINT_3

from jam.level.level import Level
from jam.level.grid import Grid
from jam.level.rabbit import Rabbit
from jam.level.robot import Robot
from jam.level.tiles import TILE_SIZE, TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT

from jam.editor import Editor

from gfs.music import Music
from gfs.sounds import IN_GAME_MUSIC, DEFEAT_SOUND, VICTORY_SOUND


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.music = Music(IN_GAME_MUSIC)

        self.interface = Interface()
        self.editor = Editor()

        self.select_level_button = Button(PLAYGROUND_50, "Select a Level", (0, 0), self.select_level, GREEN, LIGHTGREEN)

        x = (width - self.select_level_button.normal_image.get_width()) // 2
        y = height - self.select_level_button.normal_image.get_height() * 2

        self.select_level_button.pos = (x, y)

        self.interface.add_gui(self.select_level_button)

        self.select_custom_button = Button(PLAYGROUND_50, "Select a Level", (0, 0), self.select_custom, GREEN,
                                           LIGHTGREEN)

        x = (width - self.select_custom_button.normal_image.get_width()) // 2
        y = height - self.select_custom_button.normal_image.get_height() * 2

        self.select_custom_button.pos = (x, y)

        self.interface.add_gui(self.select_custom_button)

        # reload level # at the right of the screen

        reload_button = Button(PLAYGROUND_50, "Reload Level", (0, 0), self.reload_level, GREEN, LIGHTGREEN)

        x = width - reload_button.normal_image.get_width() - 10
        y = height - self.select_level_button.normal_image.get_height() * 2

        reload_button.pos = (x, y)

        self.interface.add_gui(reload_button)

        # check box
        self.editor_check_box = CheckBox(PLAYGROUND_30, "Editor Enabled/Disabled", (0, 20), self.editor.activate,
                                         self.editor.deactivate, GREEN, LIGHTGREEN)

        self.interface.add_gui(self.editor_check_box)

        self.levels = []
        self.current_level = None

        self.selector_pos = (0, 0)

        self.left_click = False
        self.right_click = False

        self.particle_system = ParticleSystem()

        # tests

        grid = Grid(15, 15, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/levels/level_0.json")

        self.levels.append(Level(grid))

        grid = Grid(6, 6, np.array([0, 0]), np.array([5, 5]), 3, 2)
        grid.load_from_json("assets/levels/level_1.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]), 5, 7)
        grid.load_from_json("assets/levels/level_2.json")

        self.levels.append(Level(grid))

        grid = Grid(5, 5, np.array([0, 0]), np.array([3, 1]), 3, 1)
        grid.load_from_json("assets/levels/level_3.json")

        self.levels.append(Level(grid))

        grid = Grid(7, 10, np.array([0, 0]), np.array([3, 5]), 5, 5)
        grid.load_from_json("assets/levels/level_4.json")

        self.levels.append(Level(grid))

        grid = Grid(7, 10, np.array([0, 0]), np.array([5, 5]), 2, 3)
        grid.load_from_json("assets/levels/level_5.json")

        self.levels.append(Level(grid))

        grid = Grid(15, 15, np.array([0, 0]), np.array([5, 5]))
        # grid.load_from_json("assets/levels/level_6.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_1.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_2.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_2.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_3.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_4.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_5.json")

        self.levels.append(Level(grid))

        grid = Grid(10, 10, np.array([0, 0]), np.array([5, 5]))
        grid.load_from_json("assets/custom/custom_6.json")

        self.levels.append(Level(grid))

        self.victory_timer = 0.0
        self.defeat_timer = 0.0

    def select_level(self):
        self.next_state = LEVEL_SELECTION
        if self.current_level is not None:
            self.levels[self.current_level].reload()
        self.music.stop()

    def select_custom(self):
        self.next_state = CUSTOM_LEVEL_SELECTION
        if self.current_level is not None:
            self.levels[self.current_level].reload()
        self.music.stop()

    def reload_level(self):
        if self.current_level is not None:
            self.levels[self.current_level].reload()

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].keyboard_input(event)

        self.editor.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

        if self.current_level is not None:
            self.levels[self.current_level].mouse_input(event)

            if self.editor.active:
                level = self.levels[self.current_level]

                if self.selector_pos is not None:
                    x = int(self.selector_pos[0])
                    y = int(self.selector_pos[1])
                    if self.left_click:
                        if self.editor.point_type is not None:
                            current_points = level.grid.get_points(x, y)
                            level.grid.set_points(x, y, current_points + 1, self.editor.point_type)
                            level.build_image()
                        if self.editor.start is not None:
                            if self.editor.start == "rabbit":
                                level.grid.rabbit_start = np.array([x, y])
                                level.grid.set_tile(x, y, TILE_GRASS)
                                level.rabbit.grid_pos = np.array([x, y])
                            if self.editor.start == "robot":
                                level.grid.robot_start = np.array([x, y])
                                level.grid.set_tile(x, y, TILE_ROAD)
                                level.robot.grid_pos = np.array([x, y])

                            level.build_image()
                    if self.right_click:
                        current_points = int(level.grid.get_points(x, y))
                        point_type = level.grid.get_victory_points(x, y)
                        if current_points <= 1:
                            level.grid.set_points(x, y, 0, 0)
                            level.build_image()
                        else:
                            level.grid.set_points(x, y, current_points - 1, point_type)
                            level.build_image()

        self.left_click = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        self.right_click = event.type == pygame.MOUSEBUTTONDOWN and event.button == 3

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

    def update(self, option_menu):
        self.interface.update()
        self.particle_system.update()
        if self.levels[self.current_level].change_character :
            particles = []
            x = (self.surface_configuration[0] - self.levels[self.current_level].image.get_width()) / 2
            y = (self.surface_configuration[1] - self.levels[self.current_level].image.get_height()) / 2

            for i in range(100):
                particles.append(PointParticle(
                    (x + self.levels[self.current_level].player.grid_pos[0] * TILE_SIZE + TILE_SIZE // 2 + 20 * np.sin((2 * 3.14 * i) / 100),
                        y + self.levels[self.current_level].player.grid_pos[1] * TILE_SIZE + TILE_SIZE // 2 + 20 * np.cos((2 * 3.14 * i) / 100) ),
                    (np.random.randint(10)-5,
                       np.random.randint(10)-5),
                    np.random.randint(80) / 100))
                
            self.particle_system.add("WHITE_POINT_1", particles)
            self.levels[self.current_level].change_character=False

        if option_menu.play_music:
            self.music.update()

        if self.editor.has_to_export_level:
            self.editor.has_to_export_level = False
            json = self.levels[self.current_level].grid.save_to_json()

            if self.current_level <= 6:
                file_name = "assets/levels/level_" + str(self.current_level) + ".json"
            else:
                file_name = "assets/custom/custom_" + str(self.current_level - 6) + ".json"

            with open(file_name, "w") as file:
                file.write(json)

            self.levels[self.current_level].grid.load_from_json(file_name)
            self.levels[self.current_level].reload()

        if self.current_level is not None:
            level = self.levels[self.current_level]
            level.update()

            if not self.editor.active:
                if level.grid.get_tile(level.rabbit.grid_pos[0],
                                       level.rabbit.grid_pos[1]) != level.rabbit.type or level.grid.get_tile(
                    level.robot.grid_pos[0], level.robot.grid_pos[1]) != level.robot.type or self.defeat_timer > 0.0:
                    if self.defeat_timer == 0.0:
                        self.music.play_short(DEFEAT_SOUND)
                        particles = []
                        x = (self.surface_configuration[0] - level.image.get_width()) / 2
                        y = (self.surface_configuration[1] - level.image.get_height()) / 2

                        for i in range(100):
                            particles.append(PointParticle(
                                (x + level.player.grid_pos[0] * TILE_SIZE + TILE_SIZE // 2,
                                 y + level.player.grid_pos[1] * TILE_SIZE + TILE_SIZE // 2),
                                (np.random.randint(100) * np.sin((2 * 3.14 * i) / 100),
                                 np.random.randint(100) * np.cos((2 * 3.14 * i) / 100)),
                                np.random.randint(50) / 100))

                        self.particle_system.add("RED_POINT_5", particles)

                    self.defeat_timer += 1.0 / 60.0

                    if self.defeat_timer > 0.5:
                        self.defeat_timer = 0.0
                        level.reload()
                        self.next_state = DEFEAT_MENU

                if level.victory or self.victory_timer > 0.0:
                    if self.victory_timer == 0.0:
                        self.music.play_short(VICTORY_SOUND)

                    self.victory_timer += 1.0 / 60.0
                    if self.victory_timer > 0.5:
                        self.victory_timer = 0.0

                        level.victory = False
                        level.reload()
                        if self.current_level < 6 or (6 < self.current_level < 12):
                            self.current_level += 1
                        self.next_state = VICTORY_MENU

            if self.editor.active:
                level = self.levels[self.current_level]

                if self.selector_pos is not None:
                    x = int(self.selector_pos[0])
                    y = int(self.selector_pos[1])
                    if self.left_click:
                        if self.editor.current_type is not None:
                            level.grid.set_tile(x, y, self.editor.current_type)
                            level.build_image()
                    if self.right_click:
                        level.grid.set_tile(x, y, TILE_DIRT)
                        level.build_image()

        self.editor.update()

    def render(self, surface):
        surface.draw_image(BACKGROUND_IMAGE_FULL, 0, 0)

        if self.current_level == 1:
            text_1 = render_font(PLAYGROUND_20, "Press directional keys move.", GREEN)
            text_2 = render_font(PLAYGROUND_20, "Press space key to change character.", GREEN)
            text_3 = render_font(PLAYGROUND_20, "How do we connect the machines.", GREEN)
            text_4 = render_font(PLAYGROUND_20, "without disconnecting the living?", GREEN)
            text_5 = render_font(PLAYGROUND_20, "We must find a way for them to", GREEN)
            text_6 = render_font(PLAYGROUND_20, "cohabit.", GREEN)
            text_7 = render_font(PLAYGROUND_20, "Connect the forests together", GREEN)
            text_8 = render_font(PLAYGROUND_20, "and the houses together!", GREEN)
            text_9 = render_font(PLAYGROUND_20, "The truck can build on water.", GREEN)
            surface.draw_rect(GREEN, pygame.Rect(10 - 1, 70 - 1, text_4.get_width() + 20 + 2, 190 + 2))
            surface.draw_rect(GREEN, pygame.Rect(790 - 1, 70 - 1, text_2.get_width() + 20 + 2, 100 + 2))
            surface.draw_rect(LIGHTGREEN, pygame.Rect(10, 70, text_4.get_width() + 20, 190))
            surface.draw_rect(LIGHTGREEN, pygame.Rect(790, 70, text_2.get_width() + 20, 100))
            surface.draw_image(text_1, 800, 80)
            surface.draw_image(text_2, 800, 110)
            surface.draw_image(text_9, 800, 140)
            surface.draw_image(text_3, 20, 80)
            surface.draw_image(text_4, 20, 110)
            surface.draw_image(text_5, 20, 140)
            surface.draw_image(text_6, 20, 170)
            surface.draw_image(text_7, 20, 200)
            surface.draw_image(text_8, 20, 230)

        if self.current_level is not None:
            current_level = self.levels[self.current_level]

            # center the level image on the surface, and draw a frame around it

            x = (surface.get_width() - current_level.image.get_width()) / 2
            y = (surface.get_height() - current_level.image.get_height()) / 2

            surface.draw_rect(DARKBLUE, pygame.Rect(
                x - 5, y - 5, current_level.image.get_width() + 10, current_level.image.get_height() + 10))

            surface.draw_image(current_level.image, x, y)

            surface.draw_image(current_level.robot.power_image,
                               x + (current_level.robot.render_pos[0] + 1) * TILE_SIZE,
                               y + current_level.robot.render_pos[
                                   1] * TILE_SIZE - current_level.robot.power_image.height)

            surface.draw_image(current_level.rabbit.power_image,
                               x + (current_level.rabbit.render_pos[0] + 1) * TILE_SIZE,
                               y + current_level.rabbit.render_pos[
                                   1] * TILE_SIZE - current_level.rabbit.power_image.height)

            # draw the sprites but move them to the right position

            current_level.rabbit.sprite.rect.x = x + current_level.rabbit.render_pos[0] * TILE_SIZE - TILE_SIZE // 2
            current_level.rabbit.sprite.rect.y = y + current_level.rabbit.render_pos[1] * TILE_SIZE - TILE_SIZE // 2

            current_level.robot.sprite.rect.x = x + current_level.robot.render_pos[0] * TILE_SIZE
            current_level.robot.sprite.rect.y = y + current_level.robot.render_pos[1] * TILE_SIZE

            current_level.sprites.render(surface)

            # draw selector
            if self.editor.active:
                if self.selector_pos is not None:
                    x = self.selector_pos[0] * TILE_SIZE + x
                    y = self.selector_pos[1] * TILE_SIZE + y

                    surface.draw_image(SELECTOR_IMAGE, x, y)

        self.interface.render(surface)

        self.editor.render(surface)
        self.particle_system.render(surface)
