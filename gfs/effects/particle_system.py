import pygame
import numpy as np

from gfs.effects.particles import RED_POINT_5, WHITE_POINT_3, YELLOW_POINT_3, WHITE_POINT_1


class ParticleSystem:
    """
    The ParticleSystem class manages every particle in the game. Particles belong to the visual aspect of the game
    """

    def __init__(self):
        """
        The ParticleSystem __init__ function initializes an empty list of particles PointParticle
        """

        self.particles = {}

    def update(self):
        """
        The update function manages the update of each particle (motion) and clears the list when all particles are dead
        """

        for motif in self.particles:
            for particle in self.particles[motif]:
                if particle.lifetime > 0:
                    particle.update()

            if len(self.particles[motif]) > 0 and len(
                    [1 for particle in self.particles[motif] if particle.lifetime <= 0]) == len(self.particles[motif]):

                self.particles[motif] = []

    def add(self, particle_scheme, particles):
        if particle_scheme not in self.particles:
            self.particles[particle_scheme] = particles
        else:
            self.particles[particle_scheme].extend(particles)

    def clear(self):
        """
        clear the list
        """

        self.particles = []

    def render(self, surface):
        """
        Render all particles on the given surface
        """

        for motif in self.particles:
            if motif == "RED_POINT_5":
                surface.blits(
                    [(RED_POINT_5.py_image, particle.position) for particle in self.particles[motif] if
                     particle.lifetime > 0])
                
            if motif == "WHITE_POINT_3":
                surface.blits(
                    [(WHITE_POINT_3.py_image, particle.position) for particle in self.particles[motif] if
                     particle.lifetime > 0])
                
            if motif == "YELLOW_POINT_3":
                surface.blits(
                    [(YELLOW_POINT_3.py_image, particle.position) for particle in self.particles[motif] if
                     particle.lifetime > 0])

            if motif == "WHITE_POINT_1":
                surface.blits(
                    [(WHITE_POINT_1.py_image, particle.position) for particle in self.particles[motif] if
                     particle.lifetime > 0])
                

