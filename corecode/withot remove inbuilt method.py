def remove_duplicates(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)
