# Example list
my_list = [1, 2, 3, 4, 5]

# Reverse the list in place
my_list.reverse()

print(my_list)  # Output: [5, 4, 3, 2, 1]


# Example list
my_list = [1, 2, 3, 4, 5]

# Reverse the list using slicing
reversed_list = my_list[::-1]

print(reversed_list)  # Output: [5, 4, 3, 2, 1]
print(my_list)        # Output: [1, 2, 3, 4, 5] (original list remains unchanged)


# Example list
my_list = [1, 2, 3, 4, 5]

# Reverse the list using a loop
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)

print(reversed_list)  # Output: [5, 4, 3, 2, 1]
