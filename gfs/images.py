from gfs.image import Image

from jam.level.tiles import TILE_SIZE

BACKGROUND_IMAGE_FULL = Image()
BACKGROUND_IMAGE_FULL.load_from_file("assets/images/fond_petit.png")
BACKGROUND_IMAGE_FULL.resize(1280, 1280)

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

JUMPING_RIGHT = Image()
JUMPING_RIGHT.load_from_file("assets/images/jumping_right.png")
JUMPING_RIGHT.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

JUMPING_LEFT = Image()
JUMPING_LEFT.load_from_file("assets/images/jumping_left.png")
JUMPING_LEFT.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

JUMPING_UP = Image()
JUMPING_UP.load_from_file("assets/images/jumping_up.png")
JUMPING_UP.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

JUMPING_DOWN = Image()
JUMPING_DOWN.load_from_file("assets/images/jumping_down.png")
JUMPING_DOWN.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

IDLE_RIGHT = Image()
IDLE_RIGHT.load_from_file("assets/images/idle_right.png")
IDLE_RIGHT.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

IDLE_LEFT = Image()
IDLE_LEFT.load_from_file("assets/images/idle_left.png")
IDLE_LEFT.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

IDLE_UP = Image()
IDLE_UP.load_from_file("assets/images/idle_up.png")
IDLE_UP.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

IDLE_DOWN = Image()
IDLE_DOWN.load_from_file("assets/images/idle_down.png")
IDLE_DOWN.resize(8 * TILE_SIZE, 2 * TILE_SIZE)

TREE_IMAGE = Image()
TREE_IMAGE.load_from_file("assets/images/tree.png")
TREE_IMAGE.resize(TILE_SIZE, TILE_SIZE)

STONE_IMAGE = Image()
STONE_IMAGE.load_from_file("assets/images/house.png")
STONE_IMAGE.resize(TILE_SIZE, TILE_SIZE)

TRUCK_RIGHT = Image()
TRUCK_RIGHT.load_from_file("assets/images/camion_droite.png")
TRUCK_RIGHT.resize(4 * TILE_SIZE, TILE_SIZE)

TRUCK_LEFT = Image()
TRUCK_LEFT.load_from_file("assets/images/camion_gauche.png")
TRUCK_LEFT.resize(4 * TILE_SIZE, TILE_SIZE)

TRUCK_UP = Image()
TRUCK_UP.load_from_file("assets/images/camion_haut.png")
TRUCK_UP.resize(4 * TILE_SIZE, TILE_SIZE)

TRUCK_DOWN = Image()
TRUCK_DOWN.load_from_file("assets/images/camion_bas.png")
TRUCK_DOWN.resize(4 * TILE_SIZE, TILE_SIZE)

IDLE_SINGLE= Image()
IDLE_SINGLE.load_from_file("assets/images/rabbit_single.png")
IDLE_SINGLE.resize(2*TILE_SIZE,2*TILE_SIZE)

TRUCK_SINGLE= Image()
TRUCK_SINGLE.load_from_file("assets/images/camion_single.png")
TRUCK_SINGLE.resize(TILE_SIZE,TILE_SIZE)
