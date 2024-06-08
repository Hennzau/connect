from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.fonts import PLAYGROUND_100, PLAYGROUND_50, render_font
from gfs.pallet import IVORY, DARKBLUE

from jam.states import IN_GAME, OPTION_MENU


class DefeatMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()

        self.game_name = render_font(PLAYGROUND_100, "You lost", DARKBLUE)

        game_button = Button(PLAYGROUND_50, "Go to game", (0, 0), self.in_game)

        x = (width - game_button.normal_image.get_width()) // 2
        y = height // 3 - game_button.normal_image.get_height() // 2

        game_button.pos = (x, y + self.game_name.get_height() * 2)

        self.interface.add_gui(game_button)

        option_button = Button(PLAYGROUND_50, "Go to options", (0, 0), self.option_menu)

        x = (width - option_button.normal_image.get_width()) // 2
        y = height // 3 - option_button.normal_image.get_height() // 2

        option_button.pos = (x, y + self.game_name.get_height() * 2.7)

        self.interface.add_gui(option_button)

    def in_game(self):
        self.next_state = IN_GAME

    def option_menu(self):
        self.next_state = OPTION_MENU

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

        # center the game name : middle, but first third height

        x = (surface.get_width() - self.game_name.get_width()) // 2
        y = surface.get_height() // 3 - self.game_name.get_height() // 2

        surface.draw_image(self.game_name, x, y)