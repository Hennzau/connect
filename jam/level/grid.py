import numpy as np

from jam.level.tiles import TILE_GREEN


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = np.zeros((width, height))
        self.tiles.fill(TILE_GREEN)

    def get_tile(self, x, y):
        pass
