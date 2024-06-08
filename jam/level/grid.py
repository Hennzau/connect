import numpy as np
import json

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
            self.rabbit_start = np.fromstring(self.initial_json_file["rabbit_start"])
            self.robot_start = np.fromstring(self.initial_json_file["robot_start"])
            self.tiles = np.fromstring(self.initial_json_file["tiles"])
            self.points = np.fromstring(self.initial_json_file["points"])
            self.victory_points = np.fromstring(self.initial_json_file["victory_points"])

    def load_from_json(self, json_file_name):
        json_file = open(json_file_name)
        data = json.load(json_file)

        self.width = data["width"]
        self.height = data["height"]
        self.rabbit_start = np.fromstring(data["rabbit_start"])
        self.robot_start = np.fromstring(data["robot_start"])
        self.tiles = np.fromstring(data["tiles"])
        self.points = np.fromstring(data["points"])
        self.victory_points = np.fromstring(data["victory_points"])

        self.initial_json_file = data

    def save_to_json(self):
        dic_json_file = {"width": self.width, "height": self.height, "rabbit_start": np.array2string(self.rabbit_start),
                         "robot_start": np.array2string(self.robot_start), "tiles": np.array2string(self.tiles),
                         "points": np.array2string(self.points), "victory_points": np.array2string(self.victory_points)}

        json_file = json.dumps(dic_json_file)

        return json_file
