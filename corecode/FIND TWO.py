# Function to find the two largest numbers in an array
def find_largest_two(numbers):
    if len(numbers) < 2:
        return "Array must have at least two elements"

    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # The first two elements will be the largest
    return sorted_numbers[0], sorted_numbers[1]

# Input from the user
numbers = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Find and print the two largest numbers
largest_two = find_largest_two(numbers)
print("The two largest numbers are:", largest_two)
