from gfs.image import Image
import gfs.pallet
from jam.level.tiles import TILE_SIZE,TILE_GREEN, TILE_GREY, TILE_WALL
import pygame


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

            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                self.current_player=(self.current_player+1)%len(self.players)

    def mouse_motion(self, event):
        pass

    def mouse_input(self, event):
        pass

    def update(self):
        for player in self.players:
            player.update()

    def build_image(self):
        for i in range (self.grid.width):
            for j in range (self.grid.height):
                type = self.grid.get_tile(i,j)
                if type == TILE_GREY:
                    self.image.draw_rect(gfs.pallet.DARKGREY,pygame.Rect(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE,TILE_SIZE))
                if type == TILE_GREEN:
                    self.image.draw_rect(gfs.pallet.GREEN,pygame.Rect(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE,TILE_SIZE))
                if type == TILE_WALL:
                    self.image.draw_rect(gfs.pallet.VOLKSWAGEN_TAUPE,pygame.Rect(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE,TILE_SIZE))


