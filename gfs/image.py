import pygame


class Image:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.py_image = pygame.Surface((width, height))

    def load(self, py_image):
        self.width = py_image.get_width()
        self.height = py_image.get_height()
        self.py_image = py_image
