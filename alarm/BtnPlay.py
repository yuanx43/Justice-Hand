import pygame.mixer
import time
from gpiozero import Button

pygame.mixer.init()

'''
sound1 = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/ambi_glass_rub.wav')

btn_sound1 = Button(23)


btn_sound1.when_pressed = sound1.play

'''
button_sounds = {Button(25):pygame.mixer.music.load('/home/pi/mp3/gunshot.mp3')}

for button, music in button_sounds.items():
    button.when_pressed = pygame.mixer.music.play()
