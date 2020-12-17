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

        # sets the delay in milliseconds
        self.speed = 0

        self.bars = []
        self.barwidth = 8
        self.issorted = False
        self.issorting = False

        self.gen_array(self.barwidth)
        self.menu = menu.make_menu(self)
        self.help_menu = menu.make_help_menu()

        self.font = pygame.font.SysFont('dejavusansmono', 18)
        self.large_font = pygame.font.SysFont('dejavusansmono', 70)

    def set_screensize(self, size):
        self.screen_width, self.screen_height = size

    def update_screensize(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def adjust_speed(self, adjustment):
        speeds = (135, 45, 15, 5, 0)
        i = speeds.index(self.speed)
        i += adjustment
        if i < 0 or i > len(speeds)-1:
            return None
        else:
            self.speed = speeds[i]

    def get_speed(self):
        speeds = {135:"slowest", 45:"slow", 15:"average", 5:"fast", 0:"fastest"}
        try: return speeds[self.speed]
        except:
            return "unknown"


    # work with the array of bars
    def gen_array(self, barwidth = 8, rand_colors = False):
        size = (self.screen_width // barwidth)
        self.clear_array()  # ensure an empty array when generating a new one

        for i, x in enumerate(random.choices(range(1, self.screen_height - 25), k=size)):
            self.bars.append(Bar(position = i, value = x))
        if rand_colors == True:
            for bar in self.bars:
                bar.random_color()

    def clear_array(self):
        self.bars.clear()
        self.issorted = False

    def update_bar_positions(self):
        for i, bar in enumerate(self.bars):
            bar.position = i
    
    def sort(self):
        self.draw_bars()
        self.display_sorttext()
        if self.algorithm == 'bubble':
            algorithms.bubble_sort(self)

        if self.algorithm == 'insertion':
            algorithms.insertion_sort(self)

        if self.algorithm == 'quick':
            algorithms.quick_sort(self, isfirst_call = True)
            if algorithms.stop_recursive_sort == False:
                self.issorted = True

        if self.algorithm == 'merge':
            algorithms.merge_sort(self, isfirst_call = True)
            if algorithms.stop_recursive_sort == False:
                self.issorted = True

        if self.algorithm == 'heap':
            algorithms.heap_sort(self)
            if algorithms.stop_recursive_sort == False:
                self.issorted = True

    # methods to draw bar objects to the screen
    def draw_bars(self, rand_colors=False):
        """ draws a bar graph from an input array of values on the screen """
        self.screen.fill(self.background_color)
        barwidth = self.screen_width // len(self.bars)
        x = 0
        y = lambda h: self.screen_height - h

        for bar in self.bars:
            if rand_colors == True or self.issorted == True:
                if random.randint(1,100) <= 20:
                    bar.random_color() 
            pygame.draw.rect(self.screen, bar.color, [x, y(bar.height), barwidth, bar.height])
            x += barwidth

        pygame.time.delay(self.speed)
        pygame.display.flip()

    def draw_two_bars(self, i, j):
        """ draws bars and index i & j to the screen """
        bar1 = self.bars[i]
        bar2 = self.bars[j]
        barwidth = self.screen_width // len(self.bars)
        x1 = bar1.position * barwidth
        x2 = bar2.position * barwidth
        y = lambda h: self.screen_height - h

        rects = []
        rects.append(pygame.draw.rect(self.screen, (0,0,0), [x1, y(bar2.height), barwidth, bar2.height]))
        rects.append(pygame.draw.rect(self.screen, bar1.color, [x1, y(bar1.height), barwidth, bar1.height]))

        rects.append(pygame.draw.rect(self.screen, (0,0,0), [x2, y(bar1.height), barwidth, bar1.height]))
        rects.append(pygame.draw.rect(self.screen, bar2.color, [x2, y(bar2.height), barwidth, bar2.height]))

        pygame.time.delay(self.speed)
        pygame.display.update(rects)

    def draw_single_bar(self, i):
        bar = self.bars[i]
        barwidth = self.screen_width // len(self.bars)
        x = i * barwidth
        y = lambda h: self.screen_height - h

        rects = []
        rects.append(
            pygame.draw.rect(self.screen, (0,0,0), 
            [x, 20, barwidth, self.screen_height - 20])
        )
        rects.append(
            pygame.draw.rect(self.screen, bar.color, 
            [x, y(bar.height), barwidth, bar.height])
        )

        pygame.time.delay(self.speed)
        pygame.display.update(rects)

    def draw_key(self, key, i):
        bar = key
        barwidth = self.screen_width // len(self.bars)
        x = i * barwidth
        y = lambda h: self.screen_height - h

        rects = []
        rects.append(
                pygame.draw.rect(self.screen, (0,0,0), 
                    [x, 20, barwidth, self.screen_height - 20])
                )
        rects.append(
                pygame.draw.rect(self.screen, bar.color, 
                    [x, y(bar.height), barwidth, bar.height])
                )

        #pygame.time.delay(self.speed)
        pygame.display.update(rects)

    def display_menu(self):
        self.menu.set_relative_position(50,50)
        self.menu.mainloop(self.screen)

    def display_help(self):
        self.help_menu.set_relative_position(50,50)
        self.help_menu.mainloop(self.screen)

    def close_menu(self):
        self.update_screensize()
        self.gen_array(self.barwidth, rand_colors = True)
        self.menu.disable()

    def print_text(self, txt, fontsize = 'normal', location = (0,0), color = (255, 255, 255)):
        if fontsize == 'normal':
            msg = self.font.render(txt, True, color)
        else:
            msg = self.large_font.render(txt, True, color)
        self.screen.blit(msg, location)
        pygame.display.flip()

    def display_helptext(self):
        self.print_text("ESC for menu or 'h' for help")
        self.print_text(
                "Sort algorithm: " + self.algorithm,
            location = (self.screen_width - 445, 0)
        )
        self.print_text(
                "Speed: " + self.get_speed(),
                location = (self.screen_width - 165, 0)
        )

    def display_sorttext(self):
        self.print_text("SPACE to pause or ENTER stop sort")
        self.print_text(
                "Sort algorithm: " + self.algorithm,
                location = (self.screen_width - 445, 0)
                )
        self.print_text(
                "Speed: " + self.get_speed(),
                location = (self.screen_width - 165, 0)
                )
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

