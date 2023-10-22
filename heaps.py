import heapq

class Heap:
    def __init__(self):
        self._heap = []  # Initial heap data
        self._size = len(self._heap)  # Initialize the size of the heap
    
    def _float(self):
        index = self._size - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index] # Swap
            index = parent_index
    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()
    def _sink(self):
        index = 0
        while index * 2 + 1 < self._size:
            if index * 2 + 2 < self._size:
                child_index = min(index * 2 + 1, index * 2 + 2, key=lambda x: self._heap[x])
            else:
                child_index = index * 2 + 1
            if self._heap[index] > self._heap[child_index]:
                self._heap[index], self._heap[child_index] = self._heap[child_index], self._heap[index]  # Swap
            index = child_index


"""
h = Heap()
# Setting the initial heap data and size for the test
h._heap = [3, 6, 5, 9, 7, 8, 2]  # Initial heap data
h._size = 7  # Initial size of the heap

# Calling the _float method to perform the floating operation
h._float()

# Printing the updated heap after the floating operation

"""
"""
h = Heap()
h._heap = [8, 6, 5, 9, 7]
h._size = 5
h._sink()
print(h._heap)
"""
