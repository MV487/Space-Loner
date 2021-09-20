import pygame
import pathlib

ASSETS_DIR = pathlib.Path.cwd() / 'assets'
# print(os.listdir(str(assets_dir/'pictures')))

# WINDOW SIZE
WIDTH, HEIGHT = 1080, 750
TITLE = 'Space-invaders-test'
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Background
BG_IMG = pygame.transform.scale(pygame.image.load(str(ASSETS_DIR / 'pictures' / 'background-black.png')), (WIDTH, HEIGHT))
# Load the character
# RED_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_ship_red_small.png'))
# GREEN_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_ship_green_small.png'))
UFO_1 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'ufo.png'))
UFO_2 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'enemy.png'))
DRONE_1 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'drone.png'))
DRONE_2 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'space-ship.png'))


# Lasers & ammo
# RED_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_laser_red.png'))
DRONE_1_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'torpedo.png'))
DRONE_2_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'torpedo.png'))
UFO_1_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'torpedo.png'))
UFO_2_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'torpedo.png'))

# PLAYER'S SHIP
PLAYER_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'spaceship.png'))
PLAYER_ammo_1 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'torpedo.png'))