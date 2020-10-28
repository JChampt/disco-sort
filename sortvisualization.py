import pygame
from random import choices
from random import randrange
pygame.init()

###### initialize global values ##############
screen_size = screen_width, screen_height = 1440, 810
screen_background_color = 0, 0, 0 # black 
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

class Graph:
    """ a graph of bars of random value to be sorted """

    def __init__(self):
        self.bars = []
        pass

    def gen_array(self, size = (screen_width // 8)):
        position = 0
        for x in choices(range(1, screen_height - 10), k=size):
            self.bars.append(Bar(x, position))
            position += 1

    def clear_array(self):
        bars = []
    
    def draw_bars(self):
        pass

    def sort(self, algorithm):
        pass

class Bar:
    """ a bar in Graph to be sorted """

    def __init__(self, value=1, position=0, color=(255,255,255)):
        self.value = value
        self.position = position
        self.color = color
        self.height = value

    def __str__(self):
        return "Bar object at position: {} with a value of: {} and color of: {}".format(self.position, self.value, self.color)

    def __repr__(self):
        return "position: {}, value: {}, color: {}".format(self.position, self.value, self.color)

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

def bubble_sort(arr):
    """ bubble sorts a list object """

    lst = list(arr[:])
    j = 0
    while True:
        count = 0
        for i in range(0, len(lst)-j-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]  
                count += 1
        j += 1
        if count == 0:
            return lst

# should define a main function and encapsolate everything in that. Init, main loop, cleanup
array = gen_array()
keys = {pygame.K_1:1, pygame.K_2:2, pygame.K_3:4, pygame.K_4:8, pygame.K_5:16} 

while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # looks for keypresses and changes the amount of bars in the array to change the way it looks
        if event.type == pygame.KEYDOWN and event.key in keys:
            array = gen_array(size = (screen_width // keys[event.key]))

    screen.fill(screen_background_color)
    draw_bars(array)
    pygame.display.flip()

    clock.tick(6)
    
pygame.quit()
