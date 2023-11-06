"""
Implement an Insertion sort function
Given the information you have received in the course about the Insertion
sort algorithm, implement a function that uses it. The function needs only 
to accept the array to be sorted as parameter. The function returns nothing.
The array is sorted in-place.

Given an array like: [6, 8, 5, 1, 2], 
the sorted array would be: [1, 2, 5, 6, 8]
"""

def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    # Start from the first index until the end of the array
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]  # Shift the greater elements up to make space for the key
            j -= 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
