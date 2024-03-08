import pygame
import random
from sys import exit
from sprites import player, enemy
from utils import Utils
from config import (
    MUSIC_3,
    ICON,
    SPAWN_NEW_ENEMY,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LIVES_DECREMENT,
    SCREEN,
    BACKGROUND_STARFIELD,
    CLOCK,
    FPS,
    GAME_OVER,
    GAME_LIVES,
    SPAWN_NEW_ENEMY_RATE,
    GAME_OVER_DELAY,
    KILLED_ENEMY,
)


class SpaceSurvival:
    def main(self) -> None:
        MUSIC_3.play(-1)

        pygame.display.set_caption("Space Survival", "Space Survival 2D")
        pygame.display.set_icon(ICON)
        pygame.time.set_timer(SPAWN_NEW_ENEMY, SPAWN_NEW_ENEMY_RATE)

        # Bullet sprite group.
        bullet_group = pygame.sprite.Group()
        enemy_bullet_group = pygame.sprite.Group()

        # Enemy sprite group.
        enemy_group = pygame.sprite.Group()

        # Player sprite group single.
        player_group = pygame.sprite.GroupSingle()
        player_group.add(
            player.PlayerSprite(bullet_group, enemy_bullet_group, enemy_group)
        )

        # Game variables.
        score = 0
        killed_count = 0
        game_lives = GAME_LIVES
        game_status = Utils.GameStatus.MENU

        while True:
            match game_status:
                case Utils.GameStatus.MENU:
                    SCREEN.fill("Black")
                    SCREEN.blit(BACKGROUND_STARFIELD, (0, 0))

                    Utils().render_font(
                        "Press space to play...",
                        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                    )
                    player_group.draw(SCREEN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit(0)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            game_status = Utils.GameStatus.PLAYING

                case Utils.GameStatus.PLAYING:
                    SCREEN.fill("Black")
                    SCREEN.blit(BACKGROUND_STARFIELD, (0, 0))

                    score += CLOCK.get_time()

                    player_group.draw(SCREEN)
                    player_group.update()
                    bullet_group.draw(SCREEN)
                    bullet_group.update()
                    enemy_group.draw(SCREEN)
                    enemy_group.update()
                    enemy_bullet_group.draw(SCREEN)
                    enemy_bullet_group.update()

                    Utils().render_font(f"Killed: {killed_count}", topleft=(0, 0))
                    Utils().render_font(
                        str(int(score / 1000)),
                        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8),
                    )
                    Utils().render_font(
                        f"Lives: {game_lives}",
                        bottomright=(SCREEN_WIDTH, SCREEN_HEIGHT),
                    )
                    Utils().render_font(
                        f"Health: {player_group.sprite.health if len(player_group) != 0 else 0}",
                        bottomleft=(0, SCREEN_HEIGHT),
                    )

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit(0)
                        if event.type == SPAWN_NEW_ENEMY:
                            enemy_sprite = enemy.EnemySprite(
                                random.randint(0, SCREEN_WIDTH),
                                random.choice(["1", "2", "3", "4"]),
                                bullet_group,
                                enemy_bullet_group,
                            )
                            enemy_group.add(enemy_sprite)
                        if event.type == LIVES_DECREMENT:
                            game_lives -= 1

                            if game_lives <= 0:
                                pygame.event.post(pygame.event.Event(GAME_OVER))
                        if event.type == KILLED_ENEMY:
                            killed_count += 1
                        if event.type == GAME_OVER:
                            # Displaying end screen with a delay of 3 seconds.
                            Utils().render_font(
                                "Game Over!",
                                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                            )
                            Utils().render_font(
                                f"Score: {int(score / 1000)}",
                                center=(
                                    SCREEN_WIDTH // 2,
                                    SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 8,
                                ),
                            )

                            # Restart procedure.
                            game_lives = GAME_LIVES
                            bullet_group.remove()
                            enemy_group.remove()
                            enemy_bullet_group.remove()
                            player_group.add(
                                player.PlayerSprite(
                                    bullet_group, enemy_bullet_group, enemy_group
                                )
                            )
                            game_status = Utils.GameStatus.MENU
                            score = 0
                            killed_count = 0

                            pygame.display.update()
                            pygame.time.delay(GAME_OVER_DELAY)

            pygame.display.update()
            pygame.display.flip()

            CLOCK.tick(FPS)


if __name__ == "__main__":
    SpaceSurvival().main()
