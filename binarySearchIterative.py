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


array = [1, 2, 3]
print(binary_search_iterative(array, 2))