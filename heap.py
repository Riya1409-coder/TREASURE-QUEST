'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comp = comparison_function
        self.data = init_array[:]
        last = len(self.data) - 1
        start_ = self.parent(last)  # Start from the last non-leaf node
        for j in range(start_, -1, -1):
            self.downheap(j)  # Ensure the heap property is maintained

        
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.data.append(value)
        self.upheap(len(self.data) - 1)  # upheap newly added position
        # print("BYE")
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        if self.is_empty():
            raise Exception("Heap is empty")
        self.swap(0, len(self.data) - 1)  # put minimum item at the end
        item = self.data.pop()  # and remove it from the list
        self.downheap(0)  # then fix new root
        return item
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.data[0]
    
    def parent(self, j):
        return (j - 1) // 2

    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self.data)  # index beyond end of list?

    def has_right(self, j):
        return self.right(j) < len(self.data)  # index beyond end of list?

    def swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        par = self.parent(j)
        if par >= 0 and self.comp(self.data[j], self.data[par]) > 0:
            # print(par, "hi")
            self.swap(par, j)
            self.upheap(par)

    def downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            high_child = left  # although right may be smaller
            if self.has_right(j):
                right = self.right(j)
                if self.comp(self.data[right], self.data[left]) > 0:
                    high_child = right
            if self.comp(self.data[high_child], self.data[j]) > 0:
                self.swap(j, high_child)
                self.downheap(high_child)  # recur at position of small child


    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    
