'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

def comp(crewmate1, crewmate2):
    return crewmate1.finish_time < crewmate2.finish_time # 1 has higher priority if this is >= 0

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        crew = []
        for i in range(m):
            mate = CrewMate(i + 1)
            crew.append(mate)
        self.crew = Heap(comp, crew)
        self.busy_crew = []
        self.no_of_treasures = 0
        self.size_of_crew = m
        # for i in self.crew.data:
        #     print(i.id, i.finish_time)
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        mate = self.crew.extract()
        # print(mate.id)
        self.no_of_treasures += 1
        mate.add_treasure(treasure)
        if self.no_of_treasures < self.size_of_crew:
            self.busy_crew.append(mate)
        self.crew.insert(mate)
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        completion_time_list = []
        crewmates = self.busy_crew if self.no_of_treasures < self.size_of_crew else self.crew.data
        for mate in crewmates:
            mate_list = mate.get_completion_time()
            # for treas in mate_list:
            #     completion_time_list.append(treas)
            completion_time_list += mate_list

        completion_time_list.sort(key=lambda treasure: treasure.id)
        return completion_time_list
    
    # You can add more methods if required

