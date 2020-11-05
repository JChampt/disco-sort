import pygame
import events
from classes import Graph

pygame.init()

def main():

    screen_width, screen_height = 1440, 810
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sorting algorithm visualization')
    clock = pygame.time.Clock()

    graph = Graph(screen) # pass surface to draw graph on
    graph.gen_array(rand_colors=True)
    
    running = True
    while running: 

        running = events.keypress(graph) # keypress calls some graph object methods
        graph.draw_bars()
        graph.print_text("ESC for menu")
        clock.tick(6)

    pygame.quit()

if __name__== "__main__":
    main()
