import pygame
from sprites import enemy_bullet
from config import (
    ENEMY_VEL,
    SCREEN_HEIGHT,
    LIVES_DECREMENT,
    ENEMY_BULLET_COOLDOWN_TIME,
    TRANSFORM_SCALE,
    ENEMY_HEALTH,
    PLAYER_BULLET_DAMAGE,
    EXPLOSION_2,
    GUNSHOT,
    KILLED_ENEMY,
)


class EnemySprite(pygame.sprite.Sprite):

    def __init__(
        self,
        x_pos: int,
        enemy_type: str,
        bullet_group: pygame.sprite.Group,
        enemy_bullet_group: pygame.sprite.Group,
    ) -> None:
        super().__init__()

        # Load enemy image based on enemy_type
        match enemy_type:
            case "1":
                image_path = "./src/assets/images/enemies/enemy_1.png"

            case "2":
                image_path = "./src/assets/images/enemies/enemy_2.png"

            case "3":
                image_path = "./src/assets/images/enemies/enemy_3.png"

            case "4":
                image_path = "./src/assets/images/enemies/enemy_4.png"

            case _:
                raise Exception("Not a valid enemy type!")

        # Set player's rect and transform enemy image
        self.image = pygame.transform.rotate(
            pygame.transform.scale_by(
                pygame.image.load(image_path).convert_alpha(), TRANSFORM_SCALE
            ),
            180,
        )
        self.rect = self.image.get_rect(midbottom=(x_pos, 0))
        self.bullet_group = bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.last_bullet_time = 0
        self.health = ENEMY_HEALTH

    def handle_movement(self) -> None:
        """Handle enemy's vertical movement and remove it if it goes below screen."""
        self.rect.y += ENEMY_VEL

        if self.rect.top >= SCREEN_HEIGHT:
            pygame.event.post(pygame.event.Event(LIVES_DECREMENT))
            self.kill()

    def handle_shooting(self) -> None:
        """Handle the interval between enemy shots."""
        current_time = pygame.time.get_ticks()
        enemy_bullet_sprite = enemy_bullet.EnemyBulletSprite(
            self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height
        )

        if current_time - self.last_bullet_time > ENEMY_BULLET_COOLDOWN_TIME:
            self.enemy_bullet_group.add(enemy_bullet_sprite)
            self.last_bullet_time = current_time
            GUNSHOT.play()

    def handle_player_damage(self) -> None:
        """Handle damage taken by the enemy from player's bullets."""

        if pygame.sprite.spritecollide(self, self.bullet_group, True):
            self.health -= PLAYER_BULLET_DAMAGE
        if self.health <= 0:
            pygame.event.post(pygame.event.Event(KILLED_ENEMY))
            EXPLOSION_2.play()
            self.kill()

    def update(self) -> None:
        """Update enemy's movement and collisions."""
        self.handle_movement()
        self.handle_shooting()
        self.handle_player_damage()
