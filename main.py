from pygame import *
import pygame_menu

init()
mixer.init()

w, h = 1200, 1000

window = display.set_mode((w, h))

window.fill((132, 195, 190))

mixer.music.load('ping_pong_music.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
