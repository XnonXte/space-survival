import pygame
from config import TRANSFORM_SCALE, ENEMY_BULLET_VEL, SCREEN_HEIGHT


class EnemyBulletSprite(pygame.sprite.Sprite):
    def __init__(self, midtop_x: int, midtop_y: int) -> None:
        super().__init__()

        self.image = pygame.transform.rotate(
            pygame.transform.scale_by(
                pygame.image.load(
                    "./src/assets/images/bullets/enemy_bullet.png"
                ).convert_alpha(),
                TRANSFORM_SCALE,
            ),
            180,
        )
        self.rect = self.image.get_rect(
            midtop=(
                midtop_x,
                midtop_y,
            )
        )

    def handle_movement(self) -> None:
        """Handling bullet movement from top to bottom, kill self if it's higher or equal to the height of the screen."""
        self.rect.y += ENEMY_BULLET_VEL

        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()

    def update(self) -> None:
        self.handle_movement()
