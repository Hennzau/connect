import numpy as np

from jam.level.tiles import TILE_GREEN, TILE_GREY, TILE_WALL


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = np.zeros((width, height))
        self.tiles.fill(TILE_GREY)
        self.tiles[0, 0] = TILE_GREEN
        self.points = np.zeros((width, height))
        self.points[0, 3] = 2
        self.end = [width - 1, height - 1]

    def get_tile(self, x, y):
        return self.tiles[x, y]

    def get_points(self, x, y):
        return self.points[x, y]

    def set_tile(self, x, y, tile):
        self.tiles[x, y] = tile

    def set_points_to_zero(self, x, y):
        self.points[x, y] = 0
