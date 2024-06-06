import pygame


class Image:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.py_image = pygame.Surface((width, height))

    def load_from_pygame_image(self, py_image):
        self.width = py_image.get_width()
        self.height = py_image.get_height()
        self.py_image = py_image

    def load_from_file(self, file):
        self.py_image = pygame.image.load(file)
        self.width = self.py_image.get_width()
        self.height = self.py_image.get_height()

    def draw_image(self, image, x, y):
        self.py_image.blit(image.py_image, (x, y))

    def draw_rect(self, color, rect):
        self.py_image.fill(color, rect)

    def fill(self, color):
        self.py_image.fill(color)

    def get_rect(self):
        return self.py_image.get_rect()

    def resize(self, width, height):
        self.py_image = pygame.transform.scale(self.py_image, (width, height))
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def subsurface(self, x, y, width, height):
        return self.py_image.subsurface((x, y, width, height))

    def blits(self, blit_list):
        self.py_image.blits(blit_list)
