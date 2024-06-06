import pygame


class Sprites:
    def __init__(self):
        self.sprites = {}
        self.group = pygame.sprite.Group()

    def add_sprite(self, name, sprite):
        self.sprites[name] = sprite
        self.group.add(sprite)

    def get_sprite(self, name):
        return self.sprites[name]

    def get_sprites(self):
        return self.sprites

    def update(self):
        self.group.update()

    def render(self, surface):
        self.group.draw(surface.py_surface)

    def animate_sprite(self, name, animation):
        self.sprites[name].animate(animation)
