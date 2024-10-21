#13. Given a string, modify a few specified characters to uppercase.

def modify_to_uppercase(s, indices):
    # Convert the string to a list of characters to modify
    chars = list(s)

    # Convert the specified indices to uppercase
    for index in indices:
        if 0 <= index < len(chars):  # Check if the index is within the valid range
            chars[index] = chars[index].upper()

    # Join the list back into a string
    return ''.join(chars)


# Input string and indices
user_input = input("Enter a string: ")
indices_to_modify = list(map(int, input("Enter indices to convert to uppercase, separated by spaces: ").split()))

# Modify the string and print the result
modified_string = modify_to_uppercase(user_input, indices_to_modify)
print("Modified string:", modified_string)
