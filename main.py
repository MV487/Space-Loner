import pygame
import random
import Classes
import GameConfig
from os import unlink

pygame.init()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# the fonts that pygame offers
# print(pygame.font.get_fonts())




def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    lives = 5
    level = 0
    player_vel = 7
    main_font = pygame.font.Font(str(GameConfig.ASSETS_DIR / 'Bristone.ttf'), 20)

    player = Classes.Player(300, 650)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    def refresh_window():
        GameConfig.WIN.blit(GameConfig.BG_IMG, (0, 0))

        # lives and level label
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level: {level}', 1, (255, 225, 225))
        GameConfig.WIN.blit(lives_label, (10, 10))
        GameConfig.WIN.blit(level_label, (GameConfig.WIDTH - level_label.get_width(), 10))

        # enemy rendering
        for enemy in enemies:
            enemy.draw(GameConfig.WIN)

        player.draw(GameConfig.WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if level <= 3:
            if len(enemies) == 0:
                level += 1
                wave_length += 5
                for i in range(wave_length*5):
                    x = random.randrange(100, GameConfig.WIDTH-100)
                    y = random.randrange(-800, -100)
                    enemy_name = random.choice(['ufo', 'ufo2'])
                    health = Classes.enemy_health_decider(enemy_name)
                    enemy = Classes.Minions(x, y, enemy_name, health)
                    enemies.append(enemy)


        # keys to action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + player_vel + player.get_height() < GameConfig.WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y + player.get_width() < GameConfig.HEIGHT:  # down
            player.y += player_vel
        # if keys[pygame.K_SPACE]:
        #     player.shoot()

        refresh_window()
        for enemy in enemies:
            enemy.move(enemy_vel)

main()