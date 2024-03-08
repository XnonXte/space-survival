import pygame

# Inits.
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Screen dimensions.
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 960

# Gameplay.
FPS = 60
TRANSFORM_SCALE = 1 / 4
PLAYER_VEL = 4
PLAYER_BULLET_VEL = 6
PLAYER_BULLET_COOLDOWN_TIME = 300
PLAYER_HEALTH = 20
PLAYER_BULLET_DAMAGE = 1
ENEMY_VEL = 1
ENEMY_BULLET_VEL = 3
ENEMY_BULLET_COOLDOWN_TIME = 2500
ENEMY_HEALTH = 5
ENEMY_BULLET_DAMAGE = 1
ENEMY_COLLISION_DAMAGE = 5
GAME_LIVES = 10
SPAWN_NEW_ENEMY_RATE = 3000
GAME_OVER_DELAY = 2000

# Essentials.
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
ICON = pygame.image.load("./src/assets/icon/space-survival.png").convert_alpha()
BODY = pygame.font.Font("./src/assets/fonts/CosmicAlien-V4Ax.ttf", 24)

# Images.
BACKGROUND_STARFIELD = pygame.transform.scale(
    pygame.image.load(
        "./src/assets/images/backgrounds/Starfields/Starfield 1 - 1024x1024.png"
    ),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)

# Music.
MUSIC_1 = pygame.mixer.Sound("./src/assets/audio/music-1.wav")
MUSIC_2 = pygame.mixer.Sound("./src/assets/audio/music-2.wav")
MUSIC_3 = pygame.mixer.Sound("./src/assets/audio/music-3.wav")

# Sfx.
EXPLOSION_1 = pygame.mixer.Sound("./src/assets/audio/explosion-1.wav")
EXPLOSION_2 = pygame.mixer.Sound("./src/assets/audio/explosion-2.wav")
GUNSHOT = pygame.mixer.Sound("./src/assets/audio/gunshot.wav")

# User-events.
LIVES_DECREMENT = pygame.USEREVENT + 1
GAME_OVER = pygame.USEREVENT + 2
SPAWN_NEW_ENEMY = pygame.USEREVENT + 3
KILLED_ENEMY = pygame.USEREVENT + 4
