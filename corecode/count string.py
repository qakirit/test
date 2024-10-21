# 8) Count the occurrence of each character/integer in an array.

from collections import Counter

# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")

user_list = user_input.split()
counts = Counter(user_list)
print("Occurrences of each element:", dict(counts))
