def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


number = int(input("Enter value the value"))
print("------------Method1-------------")
if is_prime(number):
    print(f"{number} this is not prime number")

else:
    print(f"{number} this is  prime number")




