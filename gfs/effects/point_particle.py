import pygame
import numpy as np


class PointParticle:

    def __init__(self, position, velocity, lifetime):

        self.position = position
        self.velocity = velocity
        self.lifetime = lifetime

    def update(self):
        """
        The update function manages movements of the particle
        """

        if self.lifetime > 0:
            self.position = (
                self.position[0] + self.velocity[0] * float(1 / 60.0),
                self.position[1] + self.velocity[1] * float(1 / 60.0))

            self.lifetime = self.lifetime - float(1 / 60.0)
