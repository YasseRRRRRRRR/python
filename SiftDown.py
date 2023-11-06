"""
Implement a sift_down function
Given the information you have received about the sift_down function,
implement it.

Given an array like: [6, 2, 5, 8, 1], and calling the sift_down function 
with the parameters "array, start=1, end=4" 
(sink the node with the value of 1), the array should be modified to look 
like this: [6, 8, 5, 2, 1]

Remember that the left child on a zero based array is 
at position: 2*current_node_index+1 and 
the right child is at: 2*current_node_index+2
"""
def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node
    
    Returns: None
    """
    root = start
    while True:
        # Calculate the index of the left and right children
        left_child = 2 * root + 1
        right_child = 2 * root + 2
        largest = root

        # If the left child exists and is greater than the current largest, update the largest
        if left_child <= end and array[left_child] > array[largest]:
            largest = left_child

        # If the right child exists and is greater than the current largest, update the largest
        if right_child <= end and array[right_child] > array[largest]:
            largest = right_child

        # If the largest is not the root, swap their values and continue sifting down
        if largest != root:
            array[root], array[largest] = array[largest], array[root]
            root = largest
        else:
            # The root is the largest, no need to sift down further
            break

	
array = [2, 5, 6, 1, 8]
sift_down(array, 0, 3)
print(array)