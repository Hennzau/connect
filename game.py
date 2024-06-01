from gfs.image import Image

from jam.main_menu import MainMenu
from jam.in_game import InGame
from jam.states import MAIN_MENU, OPTION_MENU, IN_GAME


class Game:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)

        self.state = [
            MainMenu(width, height),
            None,
            InGame(width, height)
        ]

        self.current_state = 0

    def next_state(self):
        next_state = self.state[self.current_state].next_state
        if next_state is not None:
            self.state[self.current_state].next_state = None
            self.current_state = next_state

    def update(self):
        self.state[self.current_state].update()
        self.next_state()

    def keyboard_input(self, event):
        self.state[self.current_state].keyboard_input(event)
        self.next_state()

    def mouse_input(self, event):
        self.state[self.current_state].mouse_input(event)
        self.next_state()

    def mouse_motion(self, event):
        self.state[self.current_state].mouse_motion(event)
        self.next_state()

    def render(self, surface):
        self.state[self.current_state].render(surface)
