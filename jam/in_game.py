from gfs.fonts import MOTO_MANGUCODE_50, render_font
from gfs.pallet import IVORY, DARKBLUE

from jam.states import MAIN_MENU


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.title = render_font(MOTO_MANGUCODE_50, "Welcome to the Game", IVORY)

    def keyboard_input(self, event):
        self.next_state = MAIN_MENU

    def mouse_input(self, event):
        pass

    def mouse_motion(self, event):
        pass

    def update(self):
        pass

    def render(self, surface):
        surface.fill(DARKBLUE)
        surface.draw_image(self.title, 100, 100)
