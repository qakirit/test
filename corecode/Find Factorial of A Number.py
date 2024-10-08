# Recursive function to calculate factorial  5!=5×4×3×2×1=120
factorial = 1
num = 5
print("-------mehtod1--------")
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("The factorial of", num, "is", factorial)


def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! = 1 and 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print("-------method2---------")
# Input from the user
number = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"The factorial of {number} is {factorial(number)}")
