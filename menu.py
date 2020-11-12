import pygame_menu

def make_menu(graph):
    """ Main menu for the program. Alows adjustment of all settings """
    _menu = pygame_menu.Menu(
        350, 450, "Main Menu", 
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
        ('Bubble Sort', 'bubble', graph),
        ('Insertion Sort', 'insertion', graph),
        ('Quick Sort', 'quick', graph),
        ('Merge Sort', 'merge', graph),
        ('Heap Sort', 'heap', graph)
    ]

    speed_options = [
        ('Fastest', 0, graph), 
        ('Slowest', 135, graph), 
        ('Slow', 45, graph), 
        ('Average', 15, graph), 
        ('Fast', 5, graph), 
    ]

    _menu.add_selector('Algorithm:', algorithm_options, onchange=set_algorithm)
    _menu.add_selector('Speed', speed_options, onchange=set_speed)
    _menu.add_selector('Bar size:', bar_options, onchange=set_barsize)
    _menu.add_selector('Window size:', window_options, onchange=set_windowsize)
    _menu.add_button('Quit Program', pygame_menu.events.EXIT)
    
    return _menu

def make_help_menu():
    """ Small text help menu so that users know the keybinds and settings """

    _menu = pygame_menu.Menu(
        425, 495, "Help", 
        theme=pygame_menu.themes.THEME_SOLARIZED, 
        onclose=pygame_menu.events.CLOSE
    )

    _menu.add_label(
        "- Press ESC to Enable/Disable Menu", 
        max_char=-1, font_size=25, 
        font_name = 'ubuntu'
    )

    _menu.add_label(
        "- Press ENTER to Start/Stop Sort", 
        max_char=-1, font_size=25, 
        font_name = 'ubuntu'
    )

    _menu.add_label(
        "- Press SPACE to Pause", 
        max_char=-1, font_size=25, 
        font_name = 'ubuntu'
    )

    _menu.add_label(
        "- Press Number keys 1-5 to Set barsize and Regenerate the array", 
        max_char=-1, font_size=25, 
        font_name = 'ubuntu'
    )

    _menu.add_label(
            "- Press up or down to change speed", 
            max_char=-1, font_size=25, 
            font_name = 'ubuntu'
    )
    
    _menu.add_label(
        "- Press 'q' for Quicksort, 'm' for Mergesort, 'e' for Heapsort, 'i' for Insertion sort or 'b' for Bubblesort", 
        max_char=-1, font_size=25, 
        font_name = 'ubuntu'
    )

    return _menu

def set_windowsize(_, value, graph):
    graph.set_screensize(value)

def set_barsize(_, value, graph):
    graph.barwidth = value

def set_algorithm(_, value, graph):
    graph.algorithm = value

def set_speed(_, value, graph):
    graph.speed = value
