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
# BLUE_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_ship_blue_small.png'))
# YELLOW_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_ship_yellow.png'))

# Lasers & ammo
# RED_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_laser_red.png'))
# GREEN_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_laser_green.png'))
# BLUE_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_laser_blue.png'))
# YELLOW_LASER = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'pixel_laser_yellow.png'))
# special_ammo_1 = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'bullet.png'))

# PLAYER'S SHIP
PLAYER_SPACE_SHIP = pygame.image.load(str(ASSETS_DIR / 'pictures' / 'spaceship.png'))
