from gfs.image import Image

from jam.level.tiles import TILE_SIZE

BACKGROUND_IMAGE_FULL = Image()
BACKGROUND_IMAGE_FULL.load_from_file("assets/images/background.png")

BACKGROUND_IMAGE_300x300 = Image()
BACKGROUND_IMAGE_300x300.load_from_file("assets/images/background.png")
BACKGROUND_IMAGE_300x300.resize(300, 300)

SELECTOR_IMAGE = Image()
SELECTOR_IMAGE.load_from_file("assets/images/SELECT.png")
SELECTOR_IMAGE.resize(TILE_SIZE, TILE_SIZE)

GRASS_IMAGE = Image()
GRASS_IMAGE.load_from_file("assets/images/grass.png")
GRASS_IMAGE.resize(TILE_SIZE, TILE_SIZE)

DIRT_IMAGE = Image()
DIRT_IMAGE.load_from_file("assets/images/dirt.png")
DIRT_IMAGE.resize(TILE_SIZE, TILE_SIZE)

ROAD_IMAGE = Image()
ROAD_IMAGE.load_from_file("assets/images/road.png")
ROAD_IMAGE.resize(TILE_SIZE, TILE_SIZE)

WATER_IMAGE = Image()
WATER_IMAGE.load_from_file("assets/images/water.png")
WATER_IMAGE.resize(TILE_SIZE, TILE_SIZE)