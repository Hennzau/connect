import numpy as np

from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = np.zeros((width, height))
        self.tiles.fill(TILE_DIRT)

        # test before being capable of loading grid from file

        self.tiles[0, 0] = TILE_GRASS
        self.tiles[5, 5] = TILE_ROAD
        self.tiles[10, 8] = TILE_WATER

        self.points = np.zeros((width, height))
        self.points[0, 3] = 2

        self.rabbit_start = [0, 0]
        self.robot_start = [5, 5]

        self.victory_points = np.zeros((width, height))
        self.victory_points[0, 3] = TILE_GRASS

    def get_tile(self, x, y):
        return self.tiles[x, y]

    def get_points(self, x, y):
        return self.points[x, y]

    def set_tile(self, x, y, tile):
        self.tiles[x, y] = tile

    def set_points_to_zero(self, x, y):
        self.points[x, y] = 0
