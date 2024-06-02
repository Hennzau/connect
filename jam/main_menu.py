from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.fonts import MOTO_MANGUCODE_50, render_font
from gfs.pallet import IVORY

from jam.states import IN_GAME


class MainMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()
        self.interface.add_gui(Button("Go to game", (0, 0), self.in_game))

    def in_game(self):
        self.next_state = IN_GAME

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

    def update(self):
        self.interface.update()

    def render(self, surface):
        surface.fill(IVORY)
        self.interface.render(surface)
