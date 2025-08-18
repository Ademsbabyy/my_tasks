

# Contact Quick Lookup
# 1. Store three names and their phone numbers in two seperate tuples
names = ("Richard", "Rihannat", "Rihanna")
phone_numbers = (804994884, 9048848449, 99038383949)

# 2. Create a dictionary from them using dict(zip())

names_numbers = dict(zip(names, phone_numbers))
print(names_numbers)

# 3. Ask the user for a name and display the corresponding number (or an error message).
name = input("Choose a name you want to display the number:  ").title()

print(names_numbers.get(name))
