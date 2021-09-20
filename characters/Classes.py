import pygame
import settings.GameConfig as GameConfig


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.cool_down_counter = 0

    def draw(self, window):
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
        GameConfig.WIN.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=100)
        self.ship_img = GameConfig.PLAYER_SPACE_SHIP
        self.laser_img = GameConfig.PLAYER_ammo_1
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health = health


class Minions(Ship):
    characters = {'ufo': (GameConfig.UFO_1, GameConfig.UFO_1_LASER),
                  'ufo2': (GameConfig.UFO_2, GameConfig.UFO_2_LASER),
                  'drone1': (GameConfig.DRONE_1, GameConfig.DRONE_1_LASER),
                  'drone2': (GameConfig.DRONE_2, GameConfig.DRONE_2_LASER)
                  }

    def __init__(self, x, y, name, health):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.characters[name]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, speed):
        self.y += speed


def enemy_health_decider(name=''):
    if name == 'ufo':
        return 50
    elif name == 'ufo2':
        return 100
    else:
        pass
