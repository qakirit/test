# Find second largest number in an array

# Function to find the second largest number in an array
def find_second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    # Remove duplicates by converting to a set, then back to a list
    unique_arr = list(set(arr))

    if len(unique_arr) < 2:
        return "No second largest number, all elements are the same"

    # Sort the unique elements in descending order
    unique_arr.sort(reverse=True)

    # The second element is the second largest
    return unique_arr[1]


# Example usage
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Find and print the second largest number
second_largest = find_second_largest(arr)
print("Second largest number:", second_largest)
