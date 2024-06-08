import numpy as np

from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT, POINT_TREE


class Grid:
    def __init__(self, width, height, rabbit_start, robot_start):
        self.width = width
        self.height = height

        self.rabbit_start = rabbit_start
        self.robot_start = robot_start

        self.tiles = np.zeros((width, height))
        self.tiles.fill(TILE_DIRT)

        self.tiles[rabbit_start[0], rabbit_start[1]] = TILE_GRASS
        self.tiles[robot_start[0], robot_start[1]] = TILE_ROAD

        self.points = np.zeros((width, height))
        self.victory_points = np.zeros((width, height))

        # sauvegarder self.tiles, rabbit_start, robot_start, self.points, self.victory_points

    def get_tile(self, x, y):
        return self.tiles[x, y]

    def get_points(self, x, y):
        return self.points[x, y]

    def get_victory_points(self, x, y):
        return self.victory_points[x, y]

    def set_tile(self, x, y, tile):
        self.tiles[x, y] = tile

    def set_points_to_zero(self, x, y):
        self.points[x, y] = 0

    def set_points(self, x, y, points, point_type):
        self.points[x, y] = points
        self.victory_points[x, y] = point_type
