from gfs.gui.interface import Interface
from gfs.gui.check_box import CheckBox

from gfs.fonts import PLAYGROUND_30
from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT


class Editor:
    def __init__(self):
        self.current_type = None
        self.active = False

        self.interface = Interface()

        # check box
        self.grass_check_box = CheckBox(PLAYGROUND_30, "Grass Tile", (0, 100), self.switch_to_green,
                                        self.switch_to_none)

        self.interface.add_gui(self.grass_check_box)

        # check box
        self.road_check_box = CheckBox(PLAYGROUND_30, "Road Tile", (0, 200), self.switch_to_grey,
                                       self.switch_to_none)

        self.interface.add_gui(self.road_check_box)

        # check box
        self.water_check_box = CheckBox(PLAYGROUND_30, "Water Tile", (0, 300), self.switch_to_wall,
                                        self.switch_to_none)

        self.interface.add_gui(self.water_check_box)

        # check box
        self.dirt_check_box = CheckBox(PLAYGROUND_30, "Dirt Tile", (0, 400), self.switch_to_dirt,
                                       self.switch_to_none)

        self.interface.add_gui(self.dirt_check_box)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def switch_to_none(self):
        self.current_type = None

        self.grass_check_box.check = False
        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False

    def switch_to_wall(self):
        self.current_type = TILE_WATER

        self.grass_check_box.check = False
        self.road_check_box.check = False
        self.dirt_check_box.check = False

    def switch_to_green(self):
        self.current_type = TILE_GRASS

        self.road_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False

    def switch_to_grey(self):
        self.current_type = TILE_ROAD

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.dirt_check_box.check = False

    def switch_to_dirt(self):
        self.current_type = TILE_DIRT

        self.grass_check_box.check = False
        self.water_check_box.check = False
        self.road_check_box.check = False

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
