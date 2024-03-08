import pygame
from sprites import bullet
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_VEL,
    PLAYER_BULLET_COOLDOWN_TIME,
    GUNSHOT,
    TRANSFORM_SCALE,
    PLAYER_HEALTH,
    ENEMY_COLLISION_DAMAGE,
    ENEMY_BULLET_DAMAGE,
    GAME_OVER,
    EXPLOSION_1,
)


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        bullet_group: pygame.sprite.Group,
        enemy_bullet_group: pygame.sprite.Group,
        enemy_group: pygame.sprite.Group,
    ) -> None:
        super().__init__()
        # Load player image and set its position
        self.image = pygame.transform.scale_by(
            pygame.image.load("./src/assets/images/players/player.png").convert_alpha(),
            TRANSFORM_SCALE,
        )
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4)
        )
        self.enemy_group = enemy_group
        self.bullet_group = bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.last_bullet_time = 0
        self.health = PLAYER_HEALTH

    def handle_movement(self) -> None:
        """Handle player movement based on key presses."""
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w] and self.rect.top - PLAYER_VEL >= 0:
            self.rect.y -= PLAYER_VEL
        if keys_pressed[pygame.K_s] and self.rect.bottom + PLAYER_VEL <= SCREEN_HEIGHT:
            self.rect.y += PLAYER_VEL
        if keys_pressed[pygame.K_a] and self.rect.left - PLAYER_VEL >= 0:
            self.rect.x -= PLAYER_VEL
        if keys_pressed[pygame.K_d] and self.rect.right + PLAYER_VEL <= SCREEN_WIDTH:
            self.rect.x += PLAYER_VEL

    def handle_shooting(self) -> None:
        """Handle player shooting."""
        keys_pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if (
            keys_pressed[pygame.K_SPACE]
            and current_time - self.last_bullet_time > PLAYER_BULLET_COOLDOWN_TIME
        ):
            # If SPACE key is pressed and bullet is not on cooldown, shoot
            GUNSHOT.play()
            player_bullet = bullet.BulletSprite(
                self.rect.x + self.rect.width // 2, self.rect.y
            )
            self.bullet_group.add(player_bullet)
            self.last_bullet_time = current_time

    def handle_enemy_damage(self) -> None:
        """Handling damage caused by enemy's bullet."""
        if pygame.sprite.spritecollide(self, self.enemy_bullet_group, True):
            self.health -= ENEMY_BULLET_DAMAGE

    def handle_enemy_collision(self) -> None:
        """Handling collision damage with the enemy."""
        if pygame.sprite.spritecollide(self, self.enemy_group, True):
            self.health -= ENEMY_COLLISION_DAMAGE
            EXPLOSION_1.play()

    def handle_game_over(self) -> None:
        """Does what it say."""
        if self.health <= 0:
            EXPLOSION_1.play()
            self.kill()
            pygame.event.post(pygame.event.Event(GAME_OVER))

    def update(self) -> None:
        """Update player's movement and shooting."""
        self.handle_movement()
        self.handle_shooting()
        self.handle_enemy_collision()
        self.handle_enemy_damage()
        self.handle_game_over()
