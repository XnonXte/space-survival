import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Dimension constants.
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 960

# Gameplay constants.
FPS = 60
TRANSFORM_SCALE = 1 / 4
PLAYER_VEL = 4
PLAYER_BULLET_VEL = 4
PLAYER_BULLET_COOLDOWN_TIME = 300
PLAYER_HEALTH = 20
PLAYER_BULLET_DAMAGE = 1
ENEMY_VEL = 1
ENEMY_BULLET_VEL = 5
ENEMY_BULLET_COOLDOWN_TIME = 1800
ENEMY_HEALTH = 5
ENEMY_BULLET_DAMAGE = 1
GAME_LIVES = 10


# Screen surface.
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Pygame essentials.
CLOCK = pygame.time.Clock()

# Background images.
BACKGROUND_STARFIELD = pygame.transform.scale(
    pygame.image.load(
        "./assets/images/backgrounds/Starfields/Starfield 1 - 1024x1024.png"
    ),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

# Screen icon.
ICON = pygame.image.load("./assets/icon/space-survival.png")

# Font.
FONT = pygame.font.Font("./assets/fonts/CosmicAlien-V4Ax.ttf", 40)

# Music.
MUSIC_1 = pygame.mixer.Sound("./assets/audio/music-1.wav")
MUSIC_2 = pygame.mixer.Sound("./assets/audio/music-2.wav")
MUSIC_3 = pygame.mixer.Sound("./assets/audio/music-3.wav")

# Sfx.
EXPLOSION_1 = pygame.mixer.Sound("./assets/audio/explosion-1.wav")
EXPLOSION_2 = pygame.mixer.Sound("./assets/audio/explosion-2.wav")
GUNSHOT = pygame.mixer.Sound("./assets/audio/gunshot.wav")

# Events.
GUN_SHOT_EVENT = pygame.USEREVENT + 1
PLAYER_HIT_EVENT = pygame.USEREVENT + 2
LIVES_DECREMENT_EVENT = pygame.USEREVENT + 3
SPAWN_NEW_ENEMY = pygame.USEREVENT + 4
