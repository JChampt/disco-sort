import events

def bubble_sort(graph):
    """ bubble sorts a graph object """

    bars = graph.bars
    j = 0
    while True:
        count = 0
        for i in range(0, len(bars)-j-1):

            if events.sort_event(graph) == "Stop sort": # stop on sort keypress
                return None

            if bars[i] > bars[i+1]:
                swap_bars(graph, i, i+1)
                graph.draw_two_bars(i, i+1)
                count += 1
        j += 1
        if count == 0:
            graph.issorted = True
            return None

stop_recursive_sort = False
def quick_sort(graph, left = 0, right = None, isfirst_call = False):
    global stop_recursive_sort
    if isfirst_call == True:
        stop_recursive_sort = False
    if stop_recursive_sort == True:
        return None

    if right == None:
        right = len(graph.bars) - 1 
    if left >= right:
        return None

    pivot = partition(graph, left, right)
    quick_sort(graph, left, pivot - 1)
    quick_sort(graph, pivot + 1, right)

def partition(graph, left, right):
    global stop_recursive_sort
    if stop_recursive_sort == True:
        return None

    bars = graph.bars
    set_pivot(graph, left, right)
    pivot = bars[right]

    i = left - 1
    for j in range(left, right):
        if events.sort_event(graph) == "Stop sort":
            stop_recursive_sort = True

        if bars[j] < pivot:
            i += 1
            swap_bars(graph, i, j)
            graph.draw_two_bars(i, j)

    swap_bars(graph, i+1, right)
    graph.draw_two_bars(i+1, right)

    return i+1

def set_pivot(graph, left, right):
    if right - left == 1:
        return None
    bars = graph.bars

    # indices of 3 points to compare.
    a = left
    b = ((right - left) // 2) + left # middle of section
    c = right

    # set pivot index to the median of a,b,c. first <= median <= last
    if bars[b] < bars[a]:
        a, b = b, a
    if bars[c] < bars[a]:
        pivot = a
    elif bars[c] < bars[b]:
        pivot = c
    else:
        pivot = b

    if pivot == right:
        return None
    else:
        swap_bars(graph, pivot, right)
        graph.draw_two_bars(pivot, right)
    return None


def swap_bars(graph, i, j):
    bars = graph.bars
    bars[i], bars[j] = bars[j], bars[i]
    bars[i].position = i
    bars[j].position = j
