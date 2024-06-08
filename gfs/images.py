from gfs.image import Image

from jam.level.tiles import TILE_SIZE

BACKGROUND_IMAGE_FULL = Image()
BACKGROUND_IMAGE_FULL.load_from_file("assets/images/background.png")

BACKGROUND_IMAGE_300x300 = Image()
BACKGROUND_IMAGE_300x300.load_from_file("assets/images/background.png")
BACKGROUND_IMAGE_300x300.resize(300, 300)

SELECTOR_IMAGE = Image()
SELECTOR_IMAGE.load_from_file("assets/images/SELECT.png")
#SELECTOR_IMAGE.resize(TILE_SIZE, TILE_SIZE)
