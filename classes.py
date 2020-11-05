import pygame
import random
import menu
import algorithms
from itertools import cycle

class Graph:
    """ a graph of bars of random value to be sorted """

    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.background_color = 0, 0, 0 #black
        self.algorithm = 'bubble'

        self.bars = []
        self.barwidth = 8
        self.issorted = False
        self.issorting = False

        self.gen_array(self.barwidth)
        self.menu = menu.make_menu(self)

        self.font = pygame.font.SysFont('dejavusansmono', 18)
        self.large_font = pygame.font.SysFont('dejavusansmono', 70)


    def print_text(self, txt, fontsize = 'normal', location = (0,0), color = (255, 255, 255)):
        if fontsize == 'normal':
            msg = self.font.render(txt, True, color)
        else:
            msg = self.large_font.render(txt, True, color)
        self.screen.blit(msg, location)
        #self.screen.flip()
        pygame.display.flip()


    def gen_array(self, barwidth = 8, rand_colors = False):
        size = (self.screen_width // barwidth)
        self.clear_array()  # ensure an empty array when generating a new one

        for i, x in enumerate(random.choices(range(1, self.screen_height - 15), k=size)):
            self.bars.append(Bar(position = i, value = x))
        if rand_colors == True:
            for bar in self.bars:
                bar.random_color()

    def clear_array(self):
        self.bars.clear()
        self.issorted = False
    
    def draw_bars(self, rand_colors=False):
        """ draws a bar graph from an input array of values on the screen """
        self.screen.fill(self.background_color)
        barwidth = self.screen_width // len(self.bars)
        x, y = 0, self.screen_height

        for bar in self.bars:
            if rand_colors == True or self.issorted == True:
                if random.randint(1,100) <= 20:
                    bar.random_color() 
            pygame.draw.rect(self.screen, bar.color, [x, y, barwidth, -(bar.height)])
            x += barwidth

        pygame.display.flip()

    def draw_two_bars(self, bar1, bar2):
        barwidth = self.screen_width // len(self.bars)
        x1 = bar1.position * barwidth
        x2 = bar2.position * barwidth
        y =  self.screen_height

        rects = []
        rects.append(pygame.draw.rect(self.screen, (0,0,0), [x1, y, barwidth, -(self.screen_height)]))
        rects.append(pygame.draw.rect(self.screen, bar1.color, [x1, y, barwidth, -(bar1.height)]))

        rects.append(pygame.draw.rect(self.screen, (0,0,0), [x2, y, barwidth, -(self.screen_height)]))
        rects.append(pygame.draw.rect(self.screen, bar2.color, [x2, y, barwidth, -(bar2.height)]))

        pygame.display.update(rects)

    def draw_single_bar(self, bar):
        barwidth = self.screen_width // len(self.bars)
        x, y = bar.position * barwidth, self.screen_height
        rects = []
        rects.append(pygame.draw.rect(self.screen, (0,0,0), [x, y, barwidth, -(self.screen_height)]))
        rects.append(pygame.draw.rect(self.screen, bar.color, [x, y, barwidth, -(bar.height)]))
        pygame.display.update(rects)

    def sort(self):
        self.draw_bars()
        self.issorting = True
        if self.algorithm == 'bubble':
            algorithms.bubble_sort(self)
        self.issorting = False

    def set_screensize(self, size):
        self.screen_width, self.screen_height = size

    def update_screensize(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def display_menu(self):
        self.menu.set_relative_position(50,50)
        self.menu.mainloop(self.screen)

    def close_menu(self):
        self.update_screensize()
        self.gen_array(self.barwidth, rand_colors = True)
        self.menu.disable()
        


class Bar:
    """ a bar in Graph to be sorted """

    def __init__(self, position = 0, value = 1, color = (255,255,255)):
        self.position = position
        self.value = value
        self.color = color
        self.height = value
        self.colors = cycle([
            (239,71,111),
            (255,209,102),
            (6,214,160),
            (17,138,178),
            (7,59,76) 
        ])

    def __str__(self):
        return "Bar object at position: {} with a value of: {} and color of: {}".format(self.position, self.value, self.color)

    def __repr__(self):
        return "position: {}, value: {}, color: {}".format(self.position, self.value, self.color)
    
    def random_color(self):
        self.color = tuple(random.randrange(256) for _ in range(3))
        #self.color = random.choice(colors)
        #self.color = next(colors)

    def clear_color(self):
        self.color = (255, 255, 255) # white

    def __lt__(self, other):
        return self.value < other.value

