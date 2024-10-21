def reverse_number(num):
    # Convert the number to a string
    num_str = str(num)

    # Reverse the string and convert it back to an integer
    reversed_num = int(num_str[::-1])

    return reversed_num


# Input from the user (multiple numbers separated by spaces)
input_string = input("Enter numbers to reverse, separated by spaces: ")

# Split the input string into a list of numbers (as strings)
numbers_str = input_string.split()

# Convert each number string to an integer, reverse it, and print the result
for number_str in numbers_str:
    number = int(number_str)
    reversed_number = reverse_number(number)
    print(f"Original: {number}, Reversed: {reversed_number}")
