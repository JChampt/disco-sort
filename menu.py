import pygame_menu

def make_menu(graph):
    _menu = pygame_menu.Menu(
        450, 450, "Main Menu", 
        theme=pygame_menu.themes.THEME_SOLARIZED, 
        onclose=graph.close_menu
    )

    window_options = [
        ('Normal', (1440, 810), graph), 
        ('Large', (1824, 1026), graph), 
        ('Small', (960, 540), graph)
    ]

    bar_options = [
        ('Normal', 8, graph), 
        ('Large', 16, graph), 
        ('Very Large', 32, graph), 
        ('Very Small', 2, graph), 
        ('Small', 4, graph)
    ]

    algorithm_options = [
        ('Bubble Sort', 'bubble', graph)
    ]

    _menu.add_selector('Window size:', window_options, onchange=set_windowsize)
    _menu.add_selector('Bar size:', bar_options, onchange=set_barsize)
    _menu.add_selector('Algorithm:', algorithm_options, onchange=set_algorithm)
    _menu.add_button('Quit', pygame_menu.events.EXIT)
    
    return _menu

def set_windowsize(_, value, graph):
    graph.set_screensize(value)

def set_barsize(_, value, graph):
    graph.barwidth = value

def set_algorithm(_, value, graph):
    graph.algorithm = value

