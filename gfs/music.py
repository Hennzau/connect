import pygame


class Music:
    def __init__(self, background_music):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)

        self.background_music = background_music

        self.channel = pygame.mixer.Channel(5)

    def play_short(self, sound):
        self.channel.play(sound)

    def update(self):
        if not self.channel.get_busy():
            sound = pygame.mixer.Sound(self.background_music)
            sound.set_volume(2)

            self.channel.play(sound)

    def stop(self):
        self.channel.stop()
