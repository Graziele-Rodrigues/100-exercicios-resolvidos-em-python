# reproduza um audio mp3 #
import pygame
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()