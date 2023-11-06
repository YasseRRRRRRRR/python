"""
Implement a heapsort function
Given the information you have received in the course about the heapsort 
algorithm, implement a sort function that uses it. The function needs only 
to accept the array to be sorted as parameter. Use the sift_down helper 
function to complete the task (it is available even if it is not visible)

Given an array like: [6, 8, 5, 1, 2], 
the sorted array would be: [1, 2, 5, 6, 8]
"""

from SiftDown import sift_down
"this is from the previous exercise ^^"

def heapify(array, count):
    # Build the max heap
    start = (count - 2) // 2  # The last parent node
    while start >= 0:
        sift_down(array, start, count - 1)
        start -= 1

def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    count = len(array)
    heapify(array, count)
    
    end = count - 1
    while end > 0:
        # Swap the max element with the last item of the heap followed by decreasing the size of heap by one
        array[end], array[0] = array[0], array[end]
        # Sift down the new top element to its proper place
        sift_down(array, 0, end - 1)
        end -= 1
