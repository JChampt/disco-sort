import pygame
from algorithms import *


keys = {pygame.K_1:2, pygame.K_2:4, pygame.K_3:8, pygame.K_4:16, pygame.K_5:32} 

def pause():
    ispaused = True
    while ispaused == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ispaused = False
        pygame.time.wait(100)

def keypress(graph):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        # looks for keypresses and changes the amount of bars in the array to change the way it looks
        if event.type == pygame.KEYDOWN and event.key in keys:
            graph.gen_array(barwidth =  keys[event.key], rand_colors=True)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            graph.sort(bubble_sort)

    return True

