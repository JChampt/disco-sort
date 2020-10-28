import pygame
from random import choices
from random import randrange
pygame.init()

###### initialize global values ######
screen_size = screen_width, screen_height = 1440, 810
screen_background_color = 0, 0, 0 # black 
screen = pygame.display.set_mode(screen_size)

"""
I am thinking I should use classes to organize these functions.  Maybe the graph is 
an object, and each bar is an object?  That way I can associate the original set of values
and the set that is being sorted with methods to generate and draw the values? I think 
each sorting algorithm should be its own module? 
"""
class graph:
    pass


def gen_array(size = (screen_width // 4)):
    """ Return an array of random elements to be sorted by various sorting algorithms """
    return tuple(choices(range(1, screen_height - 10), k=size))

def draw_bars(arr, width = screen_width, height = screen_height):
    """ draws a bar graph from an input array of values on the screen """
    barwidth = width // len(arr)
    bar_color = (255, 255, 255)
    x, y = 0, height

    for val in arr:
        barheight = val
        random_color = (randrange(255), randrange(255), randrange(255))
        pygame.draw.rect(screen, random_color, [x, y, barwidth, -(barheight)])
        #pygame.draw.rect(screen, bar_color, [x, y, barwidth, -(barheight)])
        x += barwidth

# should define a main function and encapsolate everything in that. Init, main loop, cleanup
array = gen_array()
clock = pygame.time.Clock()
running = True

while running: 

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        # looks for keypresses and changes the amount of bars in the array
        # this does overwrite the array.  I will need to change this to just tweak
        # the way the array is displayed? 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                array = gen_array(size = (screen_width // 1))
            if event.key == pygame.K_2:
                array = gen_array(size = (screen_width // 2))
            if event.key == pygame.K_3:
                array = gen_array(size = (screen_width // 4))
            if event.key == pygame.K_4:
                array = gen_array(size = (screen_width // 8))
            if event.key == pygame.K_5:
                array = gen_array(size = (screen_width // 16))

    screen.fill(screen_background_color)
    draw_bars(array)
    pygame.display.flip()

    clock.tick(6)
    
pygame.quit()
