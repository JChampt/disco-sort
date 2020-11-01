import pygame
from random import choices
from random import randrange
from random import randint

pygame.init()

######### initialize global values ##############
screen_size = screen_width, screen_height = 1440, 810
screen_background_color = 0, 0, 0 # black 
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption('Sorting algorithm visualization')
running = True
keys = {pygame.K_1:2, pygame.K_2:4, pygame.K_3:8, pygame.K_4:16, pygame.K_5:32} 

class Screen:
    """ Object to hold all global values and functions for handling screen drawing and key presses """
    keys = {pygame.K_1:2, pygame.K_2:4, pygame.K_3:8, pygame.K_4:16, pygame.K_5:24} 
    pygame.display.set_caption('Sorting algorithm visualization')
    clock = pygame.time.Clock()

    def __init__(self):
        self.width = 1440
        self.height = 810
        screen = pygame.display.set_mode((self.width, self.height))

    def keypress(self):
        pass

    def update(self):
        pass

    def pause(self):
        ispaused = True
        while ispaused == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    ispaused = False
            pygame.time.wait(100)

class Graph:
    """ a graph of bars of random value to be sorted """

    def __init__(self):
        self.gen_array()
        self.beingsorted = False

    def gen_array(self, size = (screen_width // 8), rand_colors = False):
        self.clear_array()  # ensure an empty array when generating a new one
        for i, x in enumerate(choices(range(1, screen_height - 10), k=size)):
            self.bars.append(Bar(position = i, value = x))
        if rand_colors == True:
            for bar in self.bars:
                bar.random_color()

    def clear_array(self):
        self.bars = []
        self.issorted = False
    
    def draw_bars(self, screen_width=screen_width, screen_height=screen_height, rand_colors=False):
        """ draws a bar graph from an input array of values on the screen """

        barwidth = screen_width // len(self.bars)
        x, y = 0, screen_height

        for bar in self.bars:
            if rand_colors == True:
                if randint(1,100) <= 20:
                    bar.random_color() 
            pygame.draw.rect(screen, bar.color, [x, y, barwidth, -(bar.height)])
            x += barwidth

    def draw_single_bar(self, bar, screen_width=screen_width, screen_height=screen_height):
        barwidth = screen_width // len(self.bars)
        x, y = bar.position * barwidth, screen_height
        pygame.draw.rect(screen, (0,0,0), [x, y, barwidth, -(screen_height)])
        pygame.draw.rect(screen, bar.color, [x, y, barwidth, -(bar.height)])

    def sort(self, algorithm):
        self.beingsorted = True
        algorithm(self)


class Bar:
    """ a bar in Graph to be sorted """

    def __init__(self, position = 0, value = 1, color = (255,255,255)):
        self.position = position
        self.value = value
        self.color = color
        self.height = value

    def __str__(self):
        return "Bar object at position: {} with a value of: {} and color of: {}".format(self.position, self.value, self.color)

    def __repr__(self):
        return "position: {}, value: {}, color: {}".format(self.position, self.value, self.color)
    
    def random_color(self):
        self.color = (randrange(256), randrange(256), randrange(256))

    def clear_color(self):
        self.color = (255, 255, 255) # white

    def __lt__(self, other):
        return self.value < other.value


def bubble_sort(g):
    """ bubble sorts a graph object """

    lst = g.bars
    j = 0
    update_freq = 5
    while True:
        framecount = 0
        count = 0
        for i in range(0, len(lst)-j-1):

            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]  
                count += 1
                
                lst[i].position = i
                lst[i+1].position = i+1

                g.draw_single_bar(lst[i])
                g.draw_single_bar(lst[i+1])

            if framecount == update_freq:
                pygame.display.flip()
                framecount = 0
            framecount += 1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    g.beingsorted = False
                    return None
        j += 1
        if count == 0:
            g.beingsorted = False
            g.issorted = True
            return None

def pause():
    ispaused = True
    while ispaused == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ispaused = False
        pygame.time.wait(100)


def keypress():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        # looks for keypresses and changes the amount of bars in the array to change the way it looks
        if event.type == pygame.KEYDOWN and event.key in keys:
            graph.gen_array(size = (screen_width // keys[event.key]), rand_colors=True)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            graph.sort(bubble_sort)

    return True


def update_display():
    screen.fill(screen_background_color)
    graph.draw_bars()
    pygame.display.flip()


# should define a main function and encapsolate everything in that. Init, main loop, cleanup
graph = Graph()
graph.gen_array(rand_colors=True)
while running: 

    running = keypress()
    screen.fill(screen_background_color)
    graph.draw_bars(rand_colors=True)
    pygame.display.flip()
    clock.tick(6)
    
pygame.quit()
