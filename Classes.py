import pygame
import GameConfig


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


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=100)
        self.ship_img = GameConfig.PLAYER_SPACE_SHIP
        # self.laser_img = GameConfig.special_ammo_1
        self.mask = pygame.mask.from_surface(self.ship_img)
