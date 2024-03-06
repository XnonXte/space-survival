import pygame
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_VEL,
    GUN_SHOT_EVENT,
    PLAYER_BULLET_COOLDOWN_TIME,
    GUNSHOT,
    TRANSFORM_SCALE,
)


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player image and set its position
        self.image = pygame.transform.scale_by(
            pygame.image.load("./assets/images/players/player.png").convert_alpha(),
            TRANSFORM_SCALE,
        )
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4)
        )
        self.last_bullet_time = 0

    def handle_movement(self):
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

    def handle_shooting(self):
        """Handle player shooting."""
        keys_pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if (
            keys_pressed[pygame.K_SPACE]
            and current_time - self.last_bullet_time > PLAYER_BULLET_COOLDOWN_TIME
        ):
            # If SPACE key is pressed and bullet is not on cooldown, shoot
            GUNSHOT.play()
            pygame.event.post(pygame.event.Event(GUN_SHOT_EVENT))
            self.last_bullet_time = current_time

    def update(self):
        """Update player's movement and shooting."""
        self.handle_movement()
        self.handle_shooting()
