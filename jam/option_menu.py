from gfs.gui.interface import Interface
from gfs.gui.button import Button
from gfs.gui.check_box import CheckBox

from gfs.fonts import PLAYGROUND_100, PLAYGROUND_50, PLAYGROUND_30, MOTO_MANGUCODE_50, render_font
from gfs.pallet import IVORY, DARKBLUE, DARKGREY

from jam.states import MAIN_MENU


class OptionMenu:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()

        self.game_name = render_font(PLAYGROUND_100, "Expand", DARKBLUE)

        # Go to main menu button centered at the bottom
        main_menu_button = Button(PLAYGROUND_30, "Go to main menu", (0, 0), self.main_menu)
        main_menu_button.pos = ((width - main_menu_button.normal_image.get_width()) // 2,
                                height - main_menu_button.normal_image.get_height() * 2)

        self.interface.add_gui(main_menu_button)

        # Enable ambient music checkbox
        self.ambient_music = CheckBox(PLAYGROUND_30, "Enable ambient music", (0, 0), self.enable_ambient_music,
                                      self.disable_ambient_music)
        self.ambient_music.pos = ((width - self.ambient_music.normal_image.get_width()) // 2,
                                  height - self.ambient_music.normal_image.get_height() * 4)

        self.ambient_music.check = True

        self.interface.add_gui(self.ambient_music)

        # Enable sound effects checkbox
        self.sound_effects = CheckBox(PLAYGROUND_30, "Enable sound effects", (0, 0), self.enable_sound_effects,
                                      self.disable_sound_effects)
        self.sound_effects.pos = ((width - self.sound_effects.normal_image.get_width()) // 2,
                                  height - self.sound_effects.normal_image.get_height() * 6)

        self.sound_effects.check = True

        self.interface.add_gui(self.sound_effects)

        # Now render the mapping of the keyboard actions

        self.keyboard_up = render_font(MOTO_MANGUCODE_50, "↑", DARKGREY)
        self.keyboard_down = render_font(MOTO_MANGUCODE_50, "↓", DARKGREY)
        self.keyboard_left = render_font(MOTO_MANGUCODE_50, "←", DARKGREY)
        self.keyboard_right = render_font(MOTO_MANGUCODE_50, "→", DARKGREY)

        # keyboard to swap between players

        self.keyboard_swap = render_font(PLAYGROUND_30, "Space to switch players", DARKGREY)

    def main_menu(self):
        self.next_state = MAIN_MENU

    def enable_ambient_music(self):
        pass

    def disable_ambient_music(self):
        pass

    def enable_sound_effects(self):
        pass

    def disable_sound_effects(self):
        pass

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

        # draw the keyboard mapping on the left side of the screen, middle height

        x = surface.get_width() // 2 - 30
        y = surface.get_height() // 2 - self.keyboard_up.get_height() // 2

        surface.draw_image(self.keyboard_up, x, y)

        y += self.keyboard_up.get_height()

        surface.draw_image(self.keyboard_left, x, y)

        x = surface.get_width() // 2 + 30
        y = surface.get_height() // 2 - self.keyboard_up.get_height() // 2

        surface.draw_image(self.keyboard_down, x, y)

        y += self.keyboard_down.get_height()

        surface.draw_image(self.keyboard_right, x, y)

        y += self.keyboard_right.get_height() + 30

        # draw the keyboard swap on the middle bottom of the screen, at the bottom of keyboards

        x = (surface.get_width() - self.keyboard_swap.get_width()) // 2

        surface.draw_image(self.keyboard_swap, x, y)