import pygame

from gfs.surface import Surface, flip, events
from gfs.music import Music

from game import Game


def main():
    music = Music("assets/sounds/soundtrack.mp3")
    surface = Surface(1280, 720, "Game jam!")
    clock = pygame.time.Clock()

    game = Game(surface.width, surface.height)

    is_running = True
    timer = 0

    while is_running:
        for event in events():
            if event.type == pygame.QUIT:
                is_running = False

        music.update()
        game.update()

        if timer == 0:
            print("Game running at ", int(clock.get_fps()), " fps")

        surface.clear((0, 0, 0))

        game.render(surface)

        flip()

        clock.tick(60)
        timer = (timer + 1) % 60

    pygame.quit()


if __name__ == "__main__":
    main()
