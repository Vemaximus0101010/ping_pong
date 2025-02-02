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

w, h = 1200, 1000

window = display.set_mode((w, h))

window.fill((132, 195, 190))

mixer.music.load('ping_pong_music.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
