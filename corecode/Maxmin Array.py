# Function to find the maximum and minimum in an array
def find_max_min(arr):
    max_element = arr[0]
    min_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num

    return max_element, min_element


# Example array
array = [12, 34, 5, 67, 23, 89, 1]

# Find and print the maximum and minimum elements
max_value, min_value = find_max_min(array)
print(f"Maximum element: {max_value}")
print(f"Minimum element: {min_value}")
