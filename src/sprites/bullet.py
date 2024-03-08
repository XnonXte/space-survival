import pygame
from config import PLAYER_BULLET_VEL


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, midbottom_x: int, midbottom_y: int) -> None:
        super().__init__()
        # Load bullet image and set its position
        self.image = pygame.transform.scale_by(
            pygame.image.load("./src/assets/images/bullets/bullet.png").convert_alpha(),
            1 / 4,
        )
        self.rect = self.image.get_rect(midbottom=(midbottom_x, midbottom_y))

    def handle_movement(self) -> None:
        """Handle bullet's vertical movement and remove it if it goes above the screen."""
        self.rect.y -= PLAYER_BULLET_VEL

        if self.rect.bottom <= 0:
            self.kill()

    def update(self) -> None:
        """Update bullet's movement."""
        self.handle_movement()
