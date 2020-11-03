import pygame

def bubble_sort(g):
    """ bubble sorts a graph object """

    lst = g.bars
    j = 0
    while True:
        count = 0
        for i in range(0, len(lst)-j-1):

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    return None

            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]  
                count += 1
                
                lst[i].position = i
                lst[i+1].position = i+1

                g.draw_two_bars(lst[i], lst[i+1])

        j += 1
        if count == 0:
            g.issorted = True
            return None

