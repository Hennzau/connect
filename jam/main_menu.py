from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.images import BACKGROUND_IMAGE_FULL

from gfs.fonts import PLAYGROUND_100, PLAYGROUND_50, render_font
from gfs.pallet import IVORY, DARKBLUE, GREEN, DARKGREY, LIGHTGREEN

from jam.states import IN_GAME, OPTION_MENU, LEVEL_SELECTION, CUSTOM_LEVEL_SELECTION

from gfs.music import Music
from gfs.sounds import MAIN_MENU_MUSIC


class MainMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.music = Music(MAIN_MENU_MUSIC)

        self.interface = Interface()

        self.game_name = render_font(PLAYGROUND_100, "Expand", GREEN)

        game_button = Button(PLAYGROUND_50, "Select a level", (0, 0), self.select_level, GREEN, LIGHTGREEN)

        x = (width - game_button.normal_image.get_width()) // 2
        y = height // 3 - game_button.normal_image.get_height() // 2

        game_button.pos = (x, y + self.game_name.get_height() * 2)

        self.interface.add_gui(game_button)

        custom_button = Button(PLAYGROUND_50, "Create a level", (0, 0), self.custom_level, GREEN, LIGHTGREEN)
        
        x = (width - custom_button.normal_image.get_width()) // 2
        y = height // 3 - custom_button.normal_image.get_height() // 2
        
        custom_button.pos = (x, y + self.game_name.get_height() * 2.7)
        
        self.interface.add_gui(custom_button)

        option_button = Button(PLAYGROUND_50, "Go to options", (0, 0), self.option_menu, GREEN, LIGHTGREEN)

        x = (width - option_button.normal_image.get_width()) // 2
        y = height // 3 - option_button.normal_image.get_height() // 2

        option_button.pos = (x, y + self.game_name.get_height() * 3.4)

        self.interface.add_gui(option_button)

    def select_level(self):
        self.next_state = LEVEL_SELECTION

    def custom_level(self):
        self.next_state = CUSTOM_LEVEL_SELECTION

    def option_menu(self):
        self.next_state = OPTION_MENU

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

    def update(self, option_menu):
        self.interface.update()

        if option_menu.play_music:
            self.music.update()

    def render(self, surface):
        surface.draw_image(BACKGROUND_IMAGE_FULL, 0, 0)
        self.interface.render(surface)

        # center the game name : middle, but first third height

        x = (surface.get_width() - self.game_name.get_width()) // 2
        y = surface.get_height() // 3 - self.game_name.get_height() // 2

        surface.draw_image(self.game_name, x, y)
