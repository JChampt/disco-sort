import pygame
import events
from classes import Graph

pygame.init()

def main():

    screen_width, screen_height = 1440, 810
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sorting algorithm visualization')
    clock = pygame.time.Clock()

    graph = Graph(screen)
    graph.gen_array(rand_colors=True)
    
    running = True
    while running: 

        running = events.keypress(graph)
        graph.draw_bars(rand_colors=True)
        clock.tick(6)

    pygame.quit()

if __name__== "__main__":
    main()
