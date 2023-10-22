#Linear Search
def linear_search(array, value):
    for index, element in enumerate(array):
        if element == value:
            return index
    return None

#Binary Search
def binary_search_iterative(array, value):
        start = 0  # Initialize the start pointer to the beginning of the array
        end = len(array) - 1  # Initialize the end pointer to the end of the array

        while start <= end:  # Continue the loop as long as the start pointer is less than or equal to the end pointer
            midpoint = start + (end - start + 1) // 2  # Calculate the midpoint of the current search space

            if array[midpoint] == value:
                return midpoint  # If the value is found at the midpoint, return its index
            elif value < array[midpoint]:
                end = midpoint - 1  # If the value is smaller than the midpoint, adjust the end pointer to search in the left half
            else:
                start = midpoint + 1  # If the value is larger than the midpoint, adjust the start pointer to search in the right half

        return None  # If the value is not found in the array, return None

#Interpolation search
def interpolation_search(array, value, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    while start <= end and array[start] <= value <= array[end]:
        if start == end:
            if array[start] == value:
                return start
            return None

        # Estimate the midpoint using interpolation formula
        midpoint = start + int((end - start) * ((value - array[start]) / (array[end] - array[start])))

        if array[midpoint] == value:
            return midpoint
        elif array[midpoint] < value:
            start = midpoint + 1
        else:
            end = midpoint - 1

    return None

# Example usage
#array =  [10, 17, 25, 50, 90, 140, 200]
#print(interpolation_search(array, 140))
#print(binary_search_iterative(array, 140)) 
#print(linear_search(array, 140))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

