def bubble_sort(g):
    """ bubble sorts a graph object """

    lst = g.bars
    j = 0
    r = 0
    while True:
        count = 0
        for i in range(0, len(lst)-j-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]  
                count += 1

            if r == 4:
                screen.fill(screen_background_color)
                g.draw_bars()
                pygame.display.flip()
                r = 0
            r += 1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    return None
        j += 1
        if count == 0:
            g.issorted = True
            return None

