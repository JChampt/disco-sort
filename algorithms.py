import events

# utilities
stop_recursive_sort = False
def swap_bars(graph, i, j):
    bars = graph.bars
    bars[i], bars[j] = bars[j], bars[i]
    bars[i].position = i
    bars[j].position = j


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


def merge_sort(graph, left = 0, right = None, isfirst_call = False):
    global stop_recursive_sort
    if isfirst_call == True:
        stop_recursive_sort = False
    if right == None:
        right = len(graph.bars) -1 

    for j in range(left, right):
        if events.sort_event(graph) == "Stop sort":
            stop_recursive_sort = True
    if stop_recursive_sort == True:
        return None

    if left >= right:
        return None

    middle = left + (right - left) // 2
    merge_sort(graph, left, middle)
    merge_sort(graph, middle + 1, right)

    merge(graph, left, middle, right)

def merge(graph, left, middle, right):
    global stop_recursive_sort
    i, j = left, middle + 1
    m = []
    arr = graph.bars

    while i <= middle and j <= right:
        if events.sort_event(graph) == "Stop sort":
            stop_recursive_sort = True
        if stop_recursive_sort == True:
            return None

        if arr[i] < arr[j]:
            m.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            m.append(arr[j])
            j += 1
        else:
            m.append(arr[i])
            m.append(arr[j])
            i += 1
            j += 1

    m.extend(arr[i:middle+1])
    m.extend(arr[j:right+ 1])
    arr[left:right+1] = m

    graph.update_bar_positions()
    for bar in arr[left:right+1]:
        graph.draw_single_bar(bar.position)
    

class MaxHeap:

    def __init__(self, graph):
        self.graph = graph
        self.heap = graph.bars
        self.make_heap()
        self.sort()


    def extract_max(self, done = 0):
        self.__swap(0, (len(self.heap) - 1) - done)
        self.graph.draw_two_bars(0, (len(self.heap) - 1) - done)
        self.heapify(0, done + 1)

    def sort(self):
        global stop_recursive_sort
        done = 0
        for _ in range(len(self.heap)):
            if events.sort_event(self.graph) == "Stop sort":
                stop_recursive_sort = True
            if stop_recursive_sort == True:
                return None

            self.extract_max(done)
            done += 1

    def make_heap(self):
        start = (len(self.heap) // 2) -1
        for i in range(start, -1, -1):
            self.heapify(i)

    def heapify(self, index, done = 0):
        global stop_recursive_sort
        if events.sort_event(self.graph) == "Stop sort":
            stop_recursive_sort = True
            if stop_recursive_sort == True:
                return None

        left = (index * 2) + 1
        right = (index * 2) + 2
        maximum = index

        if left < (len(self.heap) - done) and self.heap[left] > self.heap[maximum]:
            maximum = left
        if right < (len(self.heap) - done) and self.heap[right] > self.heap[maximum]:
            maximum = right

        if maximum == index:
            return None
        else:
            self.__swap(index, maximum)
            self.graph.draw_two_bars(index, maximum)
            self.heapify(maximum, done)

    def __swap(self, i, j):
        swap_bars(self.graph, i, j)

def heap_sort(graph):
    global stop_recursive_sort
    stop_recursive_sort = False
    MaxHeap(graph)
    return None

