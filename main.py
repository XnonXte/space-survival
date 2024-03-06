import pygame
import random
from sys import exit
from config import *
from sprites import player, bullet, enemy


class SpaceSurvival:
    def main(self):
        MUSIC_3.play(-1)

        pygame.display.set_caption("Space Survival", "Space Survival 2D")
        pygame.display.set_icon(ICON)

        pygame.time.set_timer(SPAWN_NEW_ENEMY, 5000)

        # Player sprite group single.
        player_sprite = player.PlayerSprite()
        player_group = pygame.sprite.GroupSingle()
        player_group.add(player_sprite)

        # Bullet sprite group.
        bullet_group = pygame.sprite.Group()

        # Enemy sprite group.
        enemy_group = pygame.sprite.Group()

        while True:

            SCREEN.fill("Black")
            SCREEN.blit(BACKGROUND_STARFIELD, (0, 0))

            player_rect = player_sprite.rect

            # Drawing groups.
            player_group.draw(SCREEN)
            player_group.update()
            bullet_group.draw(SCREEN)
            bullet_group.update()
            enemy_group.draw(SCREEN)
            enemy_group.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == GUN_SHOT_EVENT:
                    # The bullet's x and y pos that depend on the player's x and y pos.
                    bullet_x = player_rect.x + player_rect.width // 2
                    bullet_y = player_rect.y

                    player_bullet_sprite = bullet.BulletSprite(bullet_x, bullet_y)
                    bullet_group.add(player_bullet_sprite)

                if event.type == SPAWN_NEW_ENEMY:
                    enemy_sprite = enemy.EnemySprite(
                        random.randint(0, SCREEN_WIDTH),
                        random.choice(["1", "2", "3", "4"]),
                        player_rect,
                    )
                    enemy_group.add(enemy_sprite)

                if event.type == LIVES_DECREMENT_EVENT:
                    print("TODO: Add handler for lives decrement event.")

                if event.type == PLAYER_HIT_EVENT:
                    print("TODO: Add handler for player hit event.")

            for enemy_sprite in enemy_group:
                # Find damaged enemies
                damaged_enemies = pygame.sprite.groupcollide(
                    bullet_group, enemy_group, True, False
                ).values()

                if damaged_enemies:
                    # If it ain't broke don't fix it!
                    damaged_enemy = next(iter(next(iter(damaged_enemies))))
                    damaged_enemy.handle_player_damage()

            CLOCK.tick(FPS)
            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    SpaceSurvival().main()
