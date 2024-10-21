# Write a python program to reverse a given string without inbuilt method.

def reverse_string(s):
    # Initialize an empty string for the reversed result
    reversed_string = ""

    # Iterate through the original string in reverse order
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]

    return reversed_string


# Example usage
original_string = input("Enter a string to reverse: ")
reversed= reverse_string(original_string)
print("Reversed string:", reversed)
