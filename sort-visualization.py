import pygame
pygame.init()

screen_size = screen_width, screen_height = 1440, 810
screen_background_color = 0, 0, 0 # default color 
screen = pygame.display.set_mode(screen_size)


def gen_array(size = 100):
    """ Return an array of random elements to be sorted by various sorting algorithms """
    from random import sample
    # check for inputs outside of bounds
    if size < 0 or size > 1000000:
        size = 100
    return tuple(sample(range(1, size + 1), k=size))

def draw_bars(screen_width, screen_height, arr):
    arrlen = len(arr)
    barwidth = round(screen_width / arrlen)
    bar_color = (255, 255, 255)
    x, y = 0, screen_height

    for val in arr:
        barheight = ((val / arrlen) * screen_height) * .95
        pygame.draw.rect(screen, bar_color, [x, y, barwidth, -(barheight)])
        x += barwidth


bars = gen_array(700)
#draw_bars(screen_width, screen_height, bars)

while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(screen_background_color)
    #x, y, width, height = 10, 750, 100, -200
    #pygame.draw.rect(screen, (255, 255, 255), [x, y, width, height]) 
    draw_bars(screen_width, screen_height, bars)
    pygame.display.flip()
    
    
