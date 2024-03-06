import pygame
from config import PLAYER_BULLET_VEL


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # Load bullet image and set its position
        self.image = pygame.transform.scale_by(
            pygame.image.load("./assets/images/bullets/bullet.png"), 1 / 4
        )
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def handle_movement(self):
        """Handle bullet's vertical movement and remove it if it goes above the screen."""
        self.rect.y -= PLAYER_BULLET_VEL

        if self.rect.bottom <= 0:
            self.kill()

    def update(self):
        """Update bullet's movement."""
        self.handle_movement()
