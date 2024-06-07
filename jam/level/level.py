from gfs.image import Image

from jam.level.tiles import TILE_SIZE


class Level:
    def __init__(self, grid, players):
        self.image = Image(grid.width * TILE_SIZE, grid.height * TILE_SIZE)
        self.grid = grid

        self.players = players
        self.current_player = None
        self.current_player = 0

        self.build_image()

    def keyboard_input(self, event):
        if self.current_player is not None:
            self.players[self.current_player].keyboard_input(event)

    def update(self):
        pass

    def build_image(self):
        pass
