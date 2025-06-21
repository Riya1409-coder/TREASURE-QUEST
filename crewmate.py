'''
    Python file to implement the class CrewMate
'''
from heap import Heap
from treasure import Treasure

def treasure_comp(treasure_1, treasure_2): # t1 has higher priority when this is >= 0
    if (treasure_2.arrival_time + treasure_2.size - treasure_1.arrival_time - treasure_1.size) != 0:
        # print(treasure_2.arrival_time + treasure_2.size - treasure_1.arrival_time - treasure_1.size)
        return treasure_2.arrival_time + treasure_2.size > treasure_1.arrival_time + treasure_1.size
    else:
        return treasure_2.id > treasure_1.id # if same wait time - rem size then least id has greater priority


class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self, id):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.treasures = []
        self.id = id
        self.finish_time = 0 # based on time taken to complete all treasures assigned

    def add_treasure(self, treasure):
        self.treasures.append(treasure)
        self.finish_time = max(self.finish_time, treasure.arrival_time) + treasure.size
    
    def get_completion_time(self):
        ls = []
        self.treasures_heap = Heap(treasure_comp, [])
        t = 0
        for i in range(len(self.treasures)):
            treasure = self.treasures[i]
            new_treasure = Treasure(treasure.id, treasure.size, treasure.arrival_time)
            t = self.treasures[i-1].arrival_time if i > 0 else 0 # to monitor completions after t
            avail_process_time = treasure.arrival_time - t
            while (not self.treasures_heap.is_empty() and avail_process_time >= self.treasures_heap.top().size):
                # print("HI")
                avail_process_time -= self.treasures_heap.top().size
                t += self.treasures_heap.top().size
                completed_treasure = self.treasures_heap.extract()
                completed_treasure.size = 0
                completed_treasure.completion_time = t
                ls.append(completed_treasure)

            if not self.treasures_heap.is_empty():
                heap_top = self.treasures_heap.extract()
                heap_top.size -= avail_process_time
                t += avail_process_time
                # print(heap_top.id, heap_top.size, heap_top.completion_time, heap_top.arrival_time)
                # print()
                self.treasures_heap.insert(heap_top)
            avail_process_time = 0
            self.treasures_heap.insert(new_treasure)
            # print(self.treasures_heap.top().id)

        time_yet = self.treasures[-1].arrival_time
        while (not self.treasures_heap.is_empty()):
            completed_treasure = self.treasures_heap.extract()
            time_yet += completed_treasure.size
            completed_treasure.completion_time = time_yet
            completed_treasure.size = 0
            ls.append(completed_treasure)
        return ls
    # Add more methods if required
