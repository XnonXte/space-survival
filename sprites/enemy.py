import pygame
from config import (
    SCREEN,
    ENEMY_VEL,
    SCREEN_HEIGHT,
    LIVES_DECREMENT_EVENT,
    PLAYER_HIT_EVENT,
    ENEMY_BULLET_COOLDOWN_TIME,
    ENEMY_BULLET_VEL,
    TRANSFORM_SCALE,
    ENEMY_HEALTH,
    PLAYER_BULLET_DAMAGE,
    EXPLOSION_1,
    EXPLOSION_2,
)


class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, x_pos, enemy_type, player_rect):
        super().__init__()

        # Load enemy image based on enemy_type
        match enemy_type:
            case "1":
                self.image = pygame.image.load(
                    "./assets/images/enemies/enemy_1.png"
                ).convert_alpha()
            case "2":
                self.image = pygame.image.load(
                    "./assets/images/enemies/enemy_2.png"
                ).convert_alpha()
            case "3":
                self.image = pygame.image.load(
                    "./assets/images/enemies/enemy_3.png"
                ).convert_alpha()
            case "4":
                self.image = pygame.image.load(
                    "./assets/images/enemies/enemy_4.png"
                ).convert_alpha()
            case _:
                raise Exception("Not a valid enemy type!")

        # Set player's rect and transform enemy image
        self.player_rect = player_rect
        self.image = pygame.transform.rotate(
            pygame.transform.scale_by(self.image, TRANSFORM_SCALE), 180
        )
        self.rect = self.image.get_rect(midbottom=(x_pos, 0))
        self.last_bullet_time = 0
        self.enemy_bullet_image = pygame.transform.rotate(
            pygame.transform.scale_by(
                pygame.image.load(
                    "./assets/images/bullets/enemy_bullet.png"
                ).convert_alpha(),
                TRANSFORM_SCALE,
            ),
            180,
        )
        self.bullets = []
        self.health = ENEMY_HEALTH

    def handle_movement(self):
        """Handle enemy's vertical movement and remove it if it goes below screen."""
        self.rect.y += ENEMY_VEL

        if self.rect.top >= SCREEN_HEIGHT:
            pygame.event.post(pygame.event.Event(LIVES_DECREMENT_EVENT))
            self.kill()

    def handle_shot_interval(self):
        """Handle the interval between enemy shots."""
        current_time = pygame.time.get_ticks()
        enemy_bullet_rect = self.enemy_bullet_image.get_rect(
            midtop=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height)
        )

        if current_time - self.last_bullet_time > ENEMY_BULLET_COOLDOWN_TIME:
            self.bullets.append(enemy_bullet_rect)
            self.last_bullet_time = current_time

    def handle_bullets(self):
        """Handle movement and collision of enemy bullets."""
        for bullet in self.bullets:
            bullet.y += ENEMY_BULLET_VEL
            SCREEN.blit(self.enemy_bullet_image, bullet)

            if bullet.colliderect(self.player_rect):
                pygame.event.post(pygame.event.Event(PLAYER_HIT_EVENT))
                self.bullets.remove(bullet)
            elif bullet.y >= SCREEN_HEIGHT:
                self.bullets.remove(bullet)

    def handle_player_damage(self):
        """Handle damage taken by the enemy from player's bullets."""
        self.health -= PLAYER_BULLET_DAMAGE

        if self.health <= 0:
            EXPLOSION_2.play()
            self.kill()

    def handle_collision(self):
        """Handle collision between enemy and player."""
        if self.rect.colliderect(self.player_rect):
            EXPLOSION_1.play()
            pygame.event.post(pygame.event.Event(PLAYER_HIT_EVENT))
            self.kill()

    def update(self):
        """Update enemy's movement, shooting, bullets, and collisions."""
        self.handle_movement()
        self.handle_shot_interval()
        self.handle_bullets()
        self.handle_collision()
