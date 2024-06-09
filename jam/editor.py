from gfs.gui.interface import Interface
from gfs.gui.check_box import CheckBox
from gfs.gui.button import Button

from gfs.fonts import PLAYGROUND_30, render_font
from gfs.pallet import DARKGREY, GREEN, LIGHTGREEN
from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT, POINT_STONE, POINT_TREE
import pygame

from gfs.image import Image
from gfs.images import GRASS_IMAGE,ROAD_IMAGE,DIRT_IMAGE,WATER_IMAGE,STONE_IMAGE,TREE_IMAGE, IDLE_SINGLE, TRUCK_SINGLE
from jam.level.tiles import TILE_SIZE


class Editor:
    def __init__(self):
        self.current_type = None
        self.point_type = None
        self.start = None
        self.active = False

        self.interface = Interface()

        self.grass_check_box = CheckBox(PLAYGROUND_30, "Grass Tile", (100, 100), self.switch_to_grass,
                                        self.switch_to_none,GREEN)

        self.interface.add_gui(self.grass_check_box)

        self.road_check_box = CheckBox(PLAYGROUND_30, "Road Tile", (100, 200), self.switch_to_road,
                                       self.switch_to_none,GREEN)

        self.interface.add_gui(self.road_check_box)

        self.water_check_box = CheckBox(PLAYGROUND_30, "Water Tile", (100, 300), self.switch_to_water,
                                        self.switch_to_none, GREEN )

        self.interface.add_gui(self.water_check_box)

        self.dirt_check_box = CheckBox(PLAYGROUND_30, "Dirt Tile", (100, 400), self.switch_to_dirt,
                                       self.switch_to_none,GREEN)

        self.interface.add_gui(self.dirt_check_box)

        self.stone_check_box = CheckBox(PLAYGROUND_30, "Stone Tile", (100, 500), self.switch_to_stone,
                                        self.switch_to_none,GREEN)

        self.interface.add_gui(self.stone_check_box)

        self.tree_check_box = CheckBox(PLAYGROUND_30, "Tree Tile", (100, 600), self.switch_to_tree,
                                       self.switch_to_none,GREEN)

        self.interface.add_gui(self.tree_check_box)

        self.export_button = Button(PLAYGROUND_30, "Save Level to Disk", (900, 200), self.export_level,GREEN)
        self.has_to_export_level = False

        self.interface.add_gui(self.export_button)

        self.rabbit_start_checkbox = CheckBox(PLAYGROUND_30, "Set Rabbit Start", (900, 300), self.set_rabbit_start,
                                              self.set_none_start,GREEN)

        self.interface.add_gui(self.rabbit_start_checkbox)

        self.robot_start_checkbox = CheckBox(PLAYGROUND_30, "Set Robot Start", (900, 400), self.set_robot_start,
                                             self.set_none_start,GREEN)

        self.interface.add_gui(self.robot_start_checkbox)

        # text to indicate that left click if for placing and right click is for removing

        self.place_text = render_font(PLAYGROUND_30, "Left click to place, right click to remove", GREEN)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_rabbit_start(self):
        self.start = "rabbit"
        self.current_type = None
        self.point_type = None

        self.robot_start_checkbox.check = False
        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.grass_check_box.check = False

    def set_robot_start(self):
        self.start = "robot"
        self.current_type = None
        self.point_type = None

        self.rabbit_start_checkbox.check = False
        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.grass_check_box.check = False

    def set_none_start(self):
        self.start = None
        self.current_type = None
        self.point_type = None

    def export_level(self):
        self.has_to_export_level = True

    def switch_to_none(self):
        self.current_type = None
        self.point_type = None
        self.start = None

        self.grass_check_box.check = False
        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_water(self):
        self.current_type = TILE_WATER
        self.point_type = None
        self.start = None

        self.grass_check_box.check = False
        self.road_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_grass(self):
        self.current_type = TILE_GRASS
        self.point_type = None
        self.start = None

        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_road(self):
        self.current_type = TILE_ROAD
        self.point_type = None
        self.start = None

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_dirt(self):
        self.current_type = TILE_DIRT
        self.point_type = None
        self.start = None

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.road_check_box.check = False
        self.stone_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_stone(self):
        self.point_type = POINT_STONE
        self.current_type = None
        self.start = None

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.road_check_box.check = False
        self.dirt_check_box.check = False
        self.tree_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def switch_to_tree(self):
        self.point_type = POINT_TREE
        self.current_type = None
        self.start = None

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.road_check_box.check = False
        self.dirt_check_box.check = False
        self.stone_check_box.check = False
        self.rabbit_start_checkbox.check = False
        self.robot_start_checkbox.check = False

    def render(self, surface):
        if self.active:
            surface.draw_rect(GREEN,pygame.Rect(39,89,282,552))
            surface.draw_rect(LIGHTGREEN,pygame.Rect(40,90,280,550))
            surface.draw_rect(GREEN,pygame.Rect(839,189,382,252))
            surface.draw_rect(LIGHTGREEN,pygame.Rect(840,190,380,250))
            surface.draw_rect(GREEN,pygame.Rect(589,39,self.place_text.get_width()+20+2,self.place_text.get_height()+20+2))
            surface.draw_rect(LIGHTGREEN,pygame.Rect(590,40,self.place_text.get_width()+20,self.place_text.get_height()+20))

            surface.draw_image(GRASS_IMAGE,50, 100)
            surface.draw_image(ROAD_IMAGE,50, 200)
            surface.draw_image(WATER_IMAGE,50, 300)
            surface.draw_image(DIRT_IMAGE,50, 400)
            surface.draw_image(STONE_IMAGE,50, 500)
            surface.draw_image(TREE_IMAGE,50, 600)
            surface.draw_image(IDLE_SINGLE,850-TILE_SIZE/2, 300-TILE_SIZE/2)
            surface.draw_image(TRUCK_SINGLE,850, 400)

            self.interface.render(surface)

            surface.draw_image(self.place_text, 600, 50)

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
