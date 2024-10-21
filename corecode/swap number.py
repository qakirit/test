def swapnumber(a, b):
    a, b = b, a
    return a, b  # Return the swapped values

n1 = input("Enter the value of a: ")
n2 = input("Enter the value of b: ")

a, b = swapnumber(n1, n2)  # Call the function and get swapped values
print(f"After swapping: a = {a}, b = {b}")  # Print the swapped values