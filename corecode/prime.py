# Print prime numbers and provide the total count in a given range

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Get the start and end of the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# List to store prime numbers
prime_numbers = []

# Check each number in the range to see if it's prime
for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)

# Print all the prime numbers
print("Prime numbers:", prime_numbers)

# Print the total count of prime numbers
print("Total count of prime numbers:", len(prime_numbers))
