from gfs.image import Image

BACKGROUND_IMAGE_FULL = Image()
BACKGROUND_IMAGE_FULL.load_from_file("assets/images/background.png")

BACKGROUND_IMAGE_300x300 = Image()
BACKGROUND_IMAGE_300x300.load_from_file("assets/images/background.png")
BACKGROUND_IMAGE_300x300.resize(300, 300)