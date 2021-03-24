import pygame
import pygame.math
Vec2 = pygame.math.Vector2
import math
import random
from data.scripts.settings import *
from data.scripts.MUDA import (
    load_img, 
    load_sound, 
    sort,
    read_savedata,
    write_savedata,
    Scene,
    SceneManager,
    draw_background, 
    draw_text,
    shake,
    slice_list
)

# Player =====================================

class Player(pygame.sprite.Sprite):
    def __init__(self, images, bullet_image):
        super().__init__()
        self.images = images
        self.image = self.images["N"]
        self.rect = self.image.get_rect()
        self.rect.x = WIN_RES["w"]*0.3
        self.rect.y = WIN_RES["h"]*0.9
        self.position = Vec2(self.rect.x,self.rect.y)
        self.velocity = Vec2(0,0)
        self.speed = 225
        self.gun_level = 1
        
        # For shooting
        self.bullet_image = bullet_image
        self.shoot_delay = 125
        self.shoot_timer = pygame.time.get_ticks()
        self.bullet_increase_delay = 50
        self.bullet_increase_timer = 0
        self.bullet_increase_tick = 25
        self.weak_bullet_delay = 200
        self.weak_bullet_timer = pygame.time.get_ticks()
        self.weak_bullet_tick = 10

    def update(self, dt):
        self.image = self.images["N"]
        self.velocity *= 0

        keyspressed = pygame.key.get_pressed()
        self.move(keyspressed)
        self.shoot(keyspressed)

        self.position += self.velocity * dt 
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.check_bounds()

    def move(self, keyspressed):
        if keyspressed[pygame.K_UP]:
            self.velocity.y = -self.speed
        if keyspressed[pygame.K_DOWN]:
            self.velocity.y = self.speed
        if keyspressed[pygame.K_LEFT]:
            self.image = self.images["L"]
            self.velocity.x = -self.speed
        if keyspressed[pygame.K_RIGHT]:
            self.image = self.images["R"]
            self.velocity.x = self.speed

    def check_bounds(self):
        if self.rect.right > WIN_RES["w"]:
            self.rect.right = WIN_RES["w"]
            self.position.x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0 
            self.position.x = self.rect.x
        if self.rect.bottom > WIN_RES["h"]:
            self.rect.bottom = WIN_RES["h"]
            self.position.y = self.rect.y 
        if self.rect.top < 0:
            self.rect.top = 0
            self.position.y = self.rect.y
    
    def shoot(self,  keyspressed):
        now = pygame.time.get_ticks()
        if now - self.shoot_timer > self.shoot_delay:
            self.shoot_timer = now
            if keyspressed[pygame.K_z]:
                if self.bullet_increase_timer >= self.bullet_increase_delay * 2 and self.gun_level == 3:
                    self.attack3()
                elif self.bullet_increase_timer >= self.bullet_increase_delay and self.gun_level >= 2:
                    self.attack2()
                else:
                    self.attack1()
                self.bullet_increase_timer += self.bullet_increase_tick
            else:
                self.bullet_increase_timer = 0

    def attack1(self):
        b = PlayerBullet(self.bullet_image, Vec2(self.rect.centerx, self.rect.top), Vec2(0, -self.speed))
        all_sprites_g.add(b)
        p_bullets_g.add(b)

    def attack2(self):
        b1 = PlayerBullet(self.bullet_image, Vec2(self.rect.centerx-10, self.rect.top+12), Vec2(0, -self.speed))
        b2 = PlayerBullet(self.bullet_image, Vec2(self.rect.centerx+10, self.rect.top+12), Vec2(0, -self.speed))
        all_sprites_g.add(b1)
        all_sprites_g.add(b2)
        p_bullets_g.add(b1)
        p_bullets_g.add(b2)

    def attack3(self):
        self.attack1()
        self.attack2()
    
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, image, position, velocity):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = position.x
        self.rect.bottom = position.y
        self.position = Vec2(self.rect.centerx, self.rect.bottom)
        self.velocity = Vec2(velocity.x, velocity.y*3)
        self.damage = PLAYER_DAMAGE

    def update(self, dt):
        self.position += self.velocity * dt 
        self.rect.centerx = self.position.x
        self.rect.bottom = self.position.y

        if self.rect.bottom < 0:
            self.kill()

# Netherdrone =====================================

class Netherdrone(pygame.sprite.Sprite):
    def __init__(self, position, velocity, player):
        super().__init__() 
        self.image = pygame.Surface((32,32))
        self.image.fill("CYAN")
        self.rect = self.image.get_rect()
        self.rect.x = position.x 
        self.rect.y = position.y 
        self.position = position
        self.velocity = velocity
        self.player = player

    def update(self, dt):
        pass

# Helleye =====================================

class Helleye(pygame.sprite.Sprite):
    def __init__(self, position, velocity, player):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill("RED")
        self.rect = self.image.get_rect()
        self.rect.x = position.x
        self.rect.y = position.y
        self.position = position
        self.velocity = velocity
        self.player = player
    
        # For shooting
        self.shoot_delay = 600
        self.shoot_timer = pygame.time.get_ticks()

        # For the 'following' state
        self.distance = 0
    
    def update(self, dt):
        self.follow_player()
        self.shoot()
        self.position += self.velocity * dt 
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        if self.rect.left < -64 or self.rect.right > WIN_RES["h"] + 64:
            self.kill()

    def follow_player(self):
        # Calculate delta-x
        radians = math.atan2(self.rect.y - self.player.rect.y, self.rect.x - self.player.rect.x)
        dx = math.cos(radians)

        # Add delta-x to velocity
        self.velocity.x = -(dx * 100)

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_timer > self.shoot_delay:
            self.shoot_timer = now

            patterns = [
                (0,-1),
                (1,-1),
                (1,0),
                (1,1),
                (0,1),
                (-1,1),
                (-1,0),
                (-1,-1)
            ]

            for i in range(len(patterns)):
                b = HEBullet(
                    Vec2(self.rect.center),
                    Vec2(patterns[i])
                )
                e_bullets_g.add(b)
                all_sprites_g.add(b)

class HEBullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = pygame.Surface((8,8))
        self.image.fill("ORANGE")
        self.rect = self.image.get_rect()
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.position = Vec2(self.rect.centerx, self.rect.bottom)
        self.velocity = Vec2(velocity*100)
        self.damage = 1

    def update(self, dt):
        self.position += self.velocity * dt 
        self.rect.centerx = self.position.x
        self.rect.bottom = self.position.y

        if self.rect.top > WIN_RES["h"] or self.rect.bottom < 0:
            self.kill()