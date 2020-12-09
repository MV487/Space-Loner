import pygame
import Classes
import GameConfig
from os import unlink

pygame.init()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# the fonts that pygame offers
# print(pygame.font.get_fonts())

player = Classes.Player(300, 650)


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    lives = 5
    level = "Easy"
    player_vel = 5
    main_font = pygame.font.Font(str(GameConfig.ASSETS_DIR / 'Bristone.ttf'), 20)

    def refresh_window():
        GameConfig.WIN.blit(GameConfig.BG_IMG, (0, 0))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level: {level}', 1, (255, 225, 225))
        player.draw(GameConfig.WIN)
        GameConfig.WIN.blit(lives_label, (10, 10))
        GameConfig.WIN.blit(level_label, (GameConfig.WIDTH - level_label.get_width(), 10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        refresh_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # keys to action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + player_vel + 50 < GameConfig.WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y + player_vel + 50 < GameConfig.HEIGHT:  # down
            player.y += player_vel
        # if keys[pygame.K_SPACE]:
        #     player.shoot()


main()