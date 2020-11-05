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
                bars[i], bars[i+1] = bars[i+1], bars[i]  
                count += 1
                
                bars[i].position = i
                bars[i+1].position = i+1

                graph.draw_two_bars(bars[i], bars[i+1])

        j += 1
        if count == 0:
            graph.issorted = True
            return None

