import pygame

pygame.mixer.init()

HUD = pygame.mixer.Sound('assets/sounds/menu select.wav')
HUD.set_volume(0.1)

PICKUP = pygame.mixer.Sound('assets/sounds/Pickup Coin.wav')
PICKUP.set_volume(0.1)

BUNNY = pygame.mixer.Sound('assets/sounds/animal curious.wav')
BUNNY.set_volume(0.5)

MAIN_MENU_MUSIC = pygame.mixer.Sound('assets/sounds/loopTwo.wav')
MAIN_MENU_MUSIC.set_volume(2.0)

OPTION_MENU_MUSIC = pygame.mixer.Sound('assets/sounds/loop.wav')
OPTION_MENU_MUSIC.set_volume(2.0)

IN_GAME_MUSIC = pygame.mixer.Sound('assets/sounds/loopThree.wav')
IN_GAME_MUSIC.set_volume(1.0)

DEFEAT_SOUND = pygame.mixer.Sound('assets/sounds/loose.wav')
DEFEAT_SOUND.set_volume(2.0)

VICTORY_SOUND = pygame.mixer.Sound('assets/sounds/win.wav')
VICTORY_SOUND.set_volume(2.0)
