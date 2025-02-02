from pygame import *
import pygame_menu

init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_w, p_h, p_x, p_y, p_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (p_w, p_h))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.p_speed = p_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(sprite.Sprite):
    def __init__(self, color, r_x, r_y, r_w, r_h, r_speed):
        super().__init__()
        self.color = color
        self.w = r_w
        self.h = r_h
        self.image = Surface((self.w, self.h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = r_x
        self.rect.y = r_y

    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= r_speed
        elif key_pressed[K_s] and self.rect.y < h - 5:
            self.rect.y += r_speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= r_speed
        elif key_pressed[K_DOWN] and self.rect.y < h - 5:
            self.rect.y += r_speed

    def draw_rocket(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w, h = 1200, 1000

window = display.set_mode((w, h))

window.fill((132, 195, 190))

mixer.music.load('ping_pong_music.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
