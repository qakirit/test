#11. Given a string, remove the white spaces, reverse it, and print only the characters at odd positions.

def process_string(s):
    # Remove white spaces from the string
    no_spaces = s.replace(" ", "")

    # Reverse the string
    reversed_str = no_spaces[::-1]

    # Collect characters at odd positions (1-based index, which is even index in 0-based)
    result = [reversed_str[i] for i in range(1, len(reversed_str), 2)]

    return ''.join(result)


# Input from the user
user_input = input("Enter a string: ")

# Process the string and print the result
output = process_string(user_input)
print("Characters at odd positions after removing spaces and reversing:", output)
