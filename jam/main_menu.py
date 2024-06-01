from gfs.fonts import MOTO_MANGUCODE_50, render_font
from gfs.pallet import IVORY

from jam.states import IN_GAME


class MainMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.title = render_font(MOTO_MANGUCODE_50, "CS Game Jam 2024!", IVORY)

    def keyboard_input(self, event):
        self.next_state = IN_GAME

    def mouse_input(self, event):
        pass

    def mouse_motion(self, event):
        pass

    def update(self):
        pass

    def render(self, surface):
        surface.draw_image(self.title, 100, 100)
