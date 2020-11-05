import pygame

#dictionary of 5 possible bar widths in pixels 
barwidths = {
        pygame.K_1:2, 
        pygame.K_2:4, 
        pygame.K_3:8, 
        pygame.K_4:16, 
        pygame.K_5:32
} 

def keypress(graph):
    """ process keypresses during main loop returns running bool """
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        # looks for keypresses and changes the amount of bars in the array to change the way it looks
        if event.type == pygame.KEYDOWN and event.key in barwidths:
            graph.gen_array(barwidth =  barwidths[event.key], rand_colors=True)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause(graph)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            graph.sort()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            graph.display_menu()
            graph.menu.toggle()

    return True


def sort_event(graph):
    """ process events inside of a sort loop """
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "Stop sort"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause(graph)

def pause(graph):
    ispaused = True
    graph.draw_bars()
    graph.print_text("PAUSED", fontsize = 'large', location = (graph.screen_width//2 -100, graph.screen_height//2 -100))
    while ispaused == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ispaused = False
        pygame.time.wait(100)
    graph.draw_bars()
