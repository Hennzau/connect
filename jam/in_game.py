from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.pallet import DARKBLUE

from jam.states import MAIN_MENU


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()
        self.interface.add_gui(Button("Back to main menu", (200, 300), self.main_menu))

    def main_menu(self):
        self.next_state = MAIN_MENU

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

    def update(self):
        self.interface.update()

    def render(self, surface):
        surface.fill(DARKBLUE)
        self.interface.render(surface)
