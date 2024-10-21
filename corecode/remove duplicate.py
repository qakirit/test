# Get input from the user
user_input = input("Enter the elements of the list separated by spaces: ")

# Convert the input string to a list of integers
user_list = list(map(int, user_input.split()))

# Remove duplicates by converting to a set, then back to a list
unique_list = list(set(user_list))

# Print the list without duplicates
print("List without duplicates:", unique_list)
