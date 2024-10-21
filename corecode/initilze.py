# Function to get initials

#5)  program to input name, middle name and surname of a
# person and print only the initials.
def get_initials(name, middle_name, surname):
    initials = name[0].upper() + middle_name[0].upper() + surname[0].upper()
    return initials

# Input from the user
name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
surname = input("Enter your surname: ")

# Get and print the initials
initials = get_initials(name, middle_name, surname)
print(f"Your initials are: {initials}")
