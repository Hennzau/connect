import numpy as np
import json

from jam.level.tiles import TILE_GRASS, TILE_ROAD, TILE_WATER, TILE_DIRT, POINT_TREE


class Grid:
    def __init__(self, width, height, rabbit_start, robot_start):
        self.width = width
        self.height = height

        self.rabbit_start = rabbit_start
        self.robot_start = robot_start

        self.tiles = np.zeros((width, height), dtype=int)
        self.tiles.fill(TILE_DIRT)

        self.tiles[rabbit_start[0], rabbit_start[1]] = TILE_GRASS
        self.tiles[robot_start[0], robot_start[1]] = TILE_ROAD

        self.points = np.zeros((width, height), dtype=int)
        self.victory_points = np.zeros((width, height), dtype=int)

        self.initial_json_file = None

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

    def reload(self):
        if self.initial_json_file is not None:
            self.width = self.initial_json_file["width"]
            self.height = self.initial_json_file["height"]
            self.rabbit_start = np.array(self.initial_json_file["rabbit_start"], dtype=int).reshape(2)
            self.robot_start = np.array(self.initial_json_file["robot_start"], dtype=int).reshape(2)

            self.tiles = np.array(self.initial_json_file["tiles"], dtype=int).reshape((self.width, self.height))
            self.points = np.array(self.initial_json_file["points"], dtype=int).reshape((self.width, self.height))
            self.victory_points = np.array(self.initial_json_file["victory_points"], dtype=int).reshape((self.width, self.height))

    def load_from_json(self, json_file_name):
        json_file = open(json_file_name)
        data = json.load(json_file)

        self.width = data["width"]
        self.height = data["height"]
        self.rabbit_start = np.array(data["rabbit_start"], dtype=int).reshape(2)
        self.robot_start = np.array(data["robot_start"], dtype=int).reshape(2)

        self.tiles = np.array(data["tiles"], dtype=int).reshape((self.width, self.height))
        self.points = np.array(data["points"], dtype=int).reshape((self.width, self.height))
        self.victory_points = np.array(data["victory_points"], dtype=int).reshape((self.width, self.height))

        self.initial_json_file = data

    def save_to_json(self):
        dic_json_file = {"width": self.width, "height": self.height, "rabbit_start": self.rabbit_start.tolist(),
                         "robot_start": self.robot_start.tolist(), "tiles": self.tiles.tolist(),
                         "points": self.points.tolist(), "victory_points": self.victory_points.tolist()}

        json_file = json.dumps(dic_json_file)

        return json_file
