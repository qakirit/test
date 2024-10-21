a = input("enter the value of a").split()
b = input("enter the value of b ").split()

#common_number = [item for item in a if item in b]

common_number = []
for item in a:
    if item in b:
        common_number.append(item)

print(common_number)