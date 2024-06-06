import numpy as np

from gfs.gui.interface import Interface
from gfs.gui.button import Button

from gfs.fonts import MOTO_MANGUCODE_50
from gfs.pallet import DARKBLUE, RED
from gfs.image import Image

from gfs.images import BACKGROUND_IMAGE_300x300

from gfs.sprites import Sprites
from gfs.sprite import AnimatedSprite

from jam.states import MAIN_MENU

from gfs.effects.particle_system import ParticleSystem
from gfs.effects.point_particle import PointParticle


class InGame:
    def __init__(self, width, height):
        self.surface_configuration = (width, height)
        self.next_state = None

        self.interface = Interface()
        self.interface.add_gui(Button(MOTO_MANGUCODE_50, "Back to main menu", (200, 300), self.main_menu))

        self.sprites = Sprites()
        running = Image()
        running.load_from_file("assets/images/Run.png")
        animation = (8, running)

        self.sprites.add_sprite("main", AnimatedSprite(0, 0, 300, 300, {"running": animation}, 5))
        self.sprites.animate_sprite("main", "running")

        self.particle_system = ParticleSystem()

    def main_menu(self):
        self.next_state = MAIN_MENU

    def keyboard_input(self, event):
        self.interface.keyboard_input(event)

    def mouse_input(self, event):
        self.interface.mouse_input(event)

        particles = []
        for i in range(100):
            particles.append(PointParticle((event.pos[0], event.pos[1]),
                                           (np.random.randint(100) * np.sin((2 * 3.14 * i) / 100),
                                            np.random.randint(100) * np.cos((2 * 3.14 * i) / 100)),
                                           np.random.randint(150) / 100))

        self.particle_system.add("RED_POINT_5", particles)

    def mouse_motion(self, event):
        self.interface.mouse_motion(event)

    def update(self):
        self.interface.update()
        self.sprites.update()
        self.particle_system.update()

    def render(self, surface):
        surface.fill(DARKBLUE)

        self.interface.render(surface)
        self.sprites.render(surface)
        self.particle_system.render(surface)
