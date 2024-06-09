from gfs.gui.interface import Interface
from gfs.gui.check_box import CheckBox
from gfs.gui.button import Button

from gfs.fonts import PLAYGROUND_30
from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT, POINT_STONE, POINT_TREE


class Editor:
    def __init__(self):
        self.current_type = None
        self.point_type = None
        self.start = None
        self.active = False

        self.interface = Interface()

        self.grass_check_box = CheckBox(PLAYGROUND_30, "Grass Tile", (0, 100), self.switch_to_grass,
                                        self.switch_to_none)

        self.interface.add_gui(self.grass_check_box)

        self.road_check_box = CheckBox(PLAYGROUND_30, "Road Tile", (0, 200), self.switch_to_road,
                                       self.switch_to_none)

        self.interface.add_gui(self.road_check_box)

        self.water_check_box = CheckBox(PLAYGROUND_30, "Water Tile", (0, 300), self.switch_to_water,
                                        self.switch_to_none)

        self.interface.add_gui(self.water_check_box)

        self.dirt_check_box = CheckBox(PLAYGROUND_30, "Dirt Tile", (0, 400), self.switch_to_dirt,
                                       self.switch_to_none)

        self.interface.add_gui(self.dirt_check_box)

        self.stone_check_box = CheckBox(PLAYGROUND_30, "Stone Tile", (0, 500), self.switch_to_stone,
                                        self.switch_to_none)

        self.interface.add_gui(self.stone_check_box)

        self.tree_check_box = CheckBox(PLAYGROUND_30, "Tree Tile", (0, 600), self.switch_to_tree,
                                       self.switch_to_none)

        self.interface.add_gui(self.tree_check_box)

        self.export_button = Button(PLAYGROUND_30, "Export Level to JSON", (900, 200), self.export_level)
        self.has_to_export_level = False

        self.interface.add_gui(self.export_button)

        self.rabbit_start_checkbox = CheckBox(PLAYGROUND_30, "Set Rabbit Start", (900, 300), self.set_rabbit_start,
                                              self.set_none_start)

        self.interface.add_gui(self.rabbit_start_checkbox)

        self.robot_start_checkbox = CheckBox(PLAYGROUND_30, "Set Robot Start", (900, 400), self.set_robot_start,
                                             self.set_none_start)

        self.interface.add_gui(self.robot_start_checkbox)

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
