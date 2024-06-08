import pygame

from gfs.image import Image
from gfs.fonts import render_font
from gfs.surface import Surface

from gfs.pallet import IVORY, DARKBLUE, DARKGREY


class CheckBox:
    def __init__(self, font, text, pos, check_function, uncheck_function, normal_color=DARKGREY, over_color=DARKBLUE):
        self.text = text

        self.check_function = check_function
        self.uncheck_function = uncheck_function

        self.pos = pos

        self.over = False
        self.check = False

        self.over_color = over_color
        self.normal_color = normal_color

        self.text = render_font(font, text, self.normal_color)

        # create a rect at the right of the text, of the same height

        self.rect = pygame.Rect(self.text.get_width() + self.text.get_height() // 2, 0,
                                self.text.get_height(), self.text.get_height())

        self.over_image = Image(
            self.text.get_width() + self.rect.height // 2 + self.rect.height,
            self.rect.height)
        self.over_image.draw_image(self.text, 0, 0)
        self.over_image.draw_rect(self.over_color, self.rect)

        self.normal_image = Image(
            self.text.get_width() + self.rect.height // 2 + self.rect.height,
            self.rect.height)
        self.normal_image.draw_image(self.text, 0, 0)
        self.normal_image.draw_rect(self.normal_color, self.rect)

        self.rect.move(self.pos[0], self.pos[1])

    def keyboard_input(self, event):
        pass

    def mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.check = not self.check

                if self.check:
                    self.check_function()
                else:
                    self.uncheck_function()

    def mouse_motion(self, event):
        self.over = self.rect.collidepoint(event.pos)

    def update(self):
        self.rect = pygame.Rect(self.pos[0] + self.text.get_width() + self.text.get_height() // 2, self.pos[1],
                                self.text.get_height(), self.text.get_height())

    def render(self, surface):
        if self.over or self.check:
            surface.draw_image(self.over_image, self.pos[0], self.pos[1])
        else:
            surface.draw_image(self.normal_image, self.pos[0], self.pos[1])
