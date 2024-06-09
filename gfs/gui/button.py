import pygame

from gfs.image import Image
from gfs.fonts import render_font
from gfs.surface import Surface

from gfs.pallet import IVORY, DARKBLUE, DARKGREY, VOLKSWAGEN_TAUPE

from gfs.sounds import HUD

class Button:
    def __init__(self, font, text, pos, function, normal_color=DARKGREY, over_color=DARKBLUE):
        self.text = text
        self.function = function
        self.pos = pos
        self.normal_color = normal_color
        self.over_color = over_color

        self.over = False

        self.over_text = render_font(font, text, self.over_color)
        self.normal_text = render_font(font, text, self.normal_color)

        self.rect = self.normal_text.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])

        self.over_image = Image(self.rect.width, self.rect.height)
        self.over_image.draw_image(self.over_text, 0, 0)

        self.normal_image = Image(self.rect.width, self.rect.height)
        self.normal_image.draw_image(self.normal_text, 0, 0)

    def keyboard_input(self, event):
        pass

    def mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.function()
                HUD.play()

    def mouse_motion(self, event):
        if self.over != self.rect.collidepoint(event.pos):
            HUD.play()
            self.over = self.rect.collidepoint(event.pos)

    def update(self):
        self.rect = self.normal_text.get_rect()
        self.rect = self.rect.move(self.pos[0], self.pos[1])

    def render(self, surface):
        if self.over:
            surface.draw_image(self.over_image, self.pos[0], self.pos[1])
        else:
            surface.draw_image(self.normal_image, self.pos[0], self.pos[1])
