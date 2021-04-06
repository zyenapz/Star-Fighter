import pygame
import pygame.math

Vec2 = pygame.math.Vector2

# DIFFICULTY LIST ==============================================================
DIFFICULTIES = ("EASY", "MEDIUM", "HARD")

# SPRITE GROUPS ================================================================
all_sprites_g = pygame.sprite.Group()
hostiles_g = pygame.sprite.Group()
powerups_g = pygame.sprite.Group()
p_bullets_g = pygame.sprite.Group()
e_bullets_g = pygame.sprite.Group()
sentries_g = pygame.sprite.Group()

# ENTITIES' COLLISION RADII =======================================================
PLAYER_RADIUS = 24
PLAYER_BULLET_RADIUS = 16
SMALL_BULLET_RADIUS = 16
FATTY_BULLET_RADIUS = 24
ENEMY_RADIUS = 24
POWERUP_RADIUS = 20
SENTRY_RADIUS = 24
SENTRY_BULLET_RADIUS = 16

# SCORE DEFINES ================================================================
SCORE_MULTIPLIER = {
    "EASY": 0.50,
    "MEDIUM": 1.00,
    "HARD": 1.50
}

SCORE_WORTH = {
    "HELLFIGHTER": 10,
    "RAIDER": 20,
    "FATTY": 30,
    "HELLEYE": 50,
    "SOLTURRET": 100
}

# PLAYER DEFINES ===============================================================
PLAYER_SPEED = 250
PLAYER_BULLET_SPEED = 600
PLAYER_SHOOT_DELAY = 125
PLAYER_INCREASE_BULLET_DELAY = 50
PLAYER_INCREASE_BULLET_TICK = 25
PLAYER_WEAK_BULLET_DELAY = 200
PLAYER_WEAK_BULLET_TICK = 10
PLAYER_DEFAULT_GUN_LEVEL = 1 # Max of 3, Min of 1. Don't change unless debugging.
PLAYER_MAX_GUN_LEVEL = 3 # Don't change.
PLAYER_BULLET_DAMAGE = 1
PLAYER_HEALTH = 20 
PLAYER_MAX_HEALTH = 20

# SENTRY DEFINES ===============================================================
SENTRY_HEALTH = 3

# POWERUP DEFINES ==============================================================
POWERUP_SPEED = {
    "EASY": 100,
    "MEDIUM": 200,
    "HARD": 300
}
POWERUP_TYPES = (
    "GUN",
    "HEALTH",
    "SCORE",
    "SENTRY"
)
POWERUP_TYPES_WEIGHTS = (
    15, # GUN 
    20, # HEALTH
    60, # SCORE
    5 # SENTRY
)
POWERUP_HEALTH_AMOUNT = {
    "EASY": 10,
    "MEDIUM": 5,
    "HARD": 1
}
POWERUP_ROLL_CHANCE = {
    "EASY": 30,
    "MEDIUM": 15,
    "HARD": 5
}
POWERUP_SCORE_BASE_WORTH = 100

# ENEMY DEFINES ================================================================
ENEMY_COLLISION_DAMAGE = PLAYER_HEALTH / 2

# HELLFIGHTER DEFINES ==========================================================
HELLFIGHTER_SPEED = {
    "EASY": 150,
    "MEDIUM": 200,
    "HARD": 300
}
HELLFIGHTER_SHOOT_DELAY = {
    "EASY": 600,
    "MEDIUM": 500,
    "HARD": 300
}
HELLFIGHTER_RANGE = {
    "EASY": 0.2,
    "MEDIUM": 0.4,
    "HARD": 0.6
} 
HELLFIGHTER_BULLET_SPEED = {
    "EASY": 250,
    "MEDIUM": 300,
    "HARD": 350
}
HELLFIGHTER_BULLET_DAMAGE = {
    "EASY": 0.5,
    "MEDIUM": 1,
    "HARD": 1.5
}
HELLFIGHTER_HEALTH = {
    "EASY": 2,
    "MEDIUM": 3,
    "HARD": 5
}

# FATTY DEFINES ================================================================
FATTY_SPEED = {
    "EASY": 100,
    "MEDIUM": 150,
    "HARD": 200
}
FATTY_SHOOT_DELAY = {
    "EASY": 2000,
    "MEDIUM": 1500,
    "HARD": 1200
}
FATTY_LARGE_BULLET_SPEED = {
    "EASY": 200,
    "MEDIUM": 300,
    "HARD": 400
}
FATTY_SMALL_BULLET_SPEED = {
    "EASY": 100,
    "MEDIUM": 200,
    "HARD": 250
}
FATTY_BULLET_DAMAGE = {
    "EASY": 0.5,
    "MEDIUM": 1,
    "HARD": 1.5
}
FATTY_BULLET_DIRECTION = (
    Vec2(1,0), # To Right
    Vec2(1,1), # To Bottom Right
    Vec2(0,1), # To Bottom
    Vec2(-1,1), # To Bottom Left
    Vec2(-1,0), # To Left
)
FATTY_BULLET_SPEED_X = (
    1,
    2,
    3,
    2,
    1
)
FATTY_BULLET_SPEED_Y = (
    2,
    1,
    2,
    1,
    2
)
FATTY_HEALTH = {
    "EASY": 2,
    "MEDIUM": 4,
    "HARD": 5
}

# RAIDER DEFINES ===============================================================
RAIDER_SPEED = {
    "EASY": 200,
    "MEDIUM": 250,
    "HARD": 300
}
RAIDER_DASH_RANGE = {
    "EASY": 0.5,
    "MEDIUM": 0.3,
    "HARD": 0.2
}
RAIDER_MAX_SPEED = {
    "EASY": 500,
    "MEDIUM": 600,
    "HARD": 700
}
RAIDER_HEALTH = {
    "EASY": 2,
    "MEDIUM": 3,
    "HARD": 4
}

# SOLTURRET DEFINES ============================================================
SOLTURRET_SHOOT_DELAY = {
    "EASY": 700,
    "MEDIUM": 500,
    "HARD": 300
}
SOLTURRET_BULLET_SPEED = {
    "EASY": 200,
    "MEDIUM": 300,
    "HARD": 400
}
SOLTURRET_BULLET_DAMAGE = {
    "EASY": 0.5,
    "MEDIUM": 1,
    "HARD": 1.5
}
SOLTURRET_HEALTH = {
    "EASY": 2,
    "MEDIUM": 5,
    "HARD": 6
}

# HELLEYE DEFINES ==============================================================
HELLEYE_BULLET_DIRECTION = (
    Vec2(0,-1),
    Vec2(1,-1),
    Vec2(1,0),
    Vec2(1,1),
    Vec2(0,1),
    Vec2(-1,1),
    Vec2(-1,0),
    Vec2(-1,-1)
)
HELLEYE_SHOOT_DELAY = {
    "EASY": 900,
    "MEDIUM": 700,
    "HARD": 500
}
HELLEYE_SPEED = {
    "EASY": 50,
    "MEDIUM": 100,
    "HARD": 200
}
HELLEYE_BULLET_SPEED = {
    "EASY": 100,
    "MEDIUM": 150,
    "HARD": 250
}
HELLEYE_BULLET_DAMAGE = {
    "EASY": 0.5,
    "MEDIUM": 1,
    "HARD": 1.5
}
HELLEYE_HEALTH = {
    "EASY": 5,
    "MEDIUM": 8,
    "HARD": 12
}