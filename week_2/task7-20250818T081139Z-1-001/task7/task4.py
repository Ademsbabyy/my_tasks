# Unique Members Registration

# 1. Ask the user to enter three names seperated by commas
name = input("Enter three names seperated by commas: ").split(",")

# 2. Convert them to a set to ensure uniqueness
names = set(name)
print(names)

# 3 Create a dictionary where each name is a key and its length is the value

names_length = {name:len(name) for name in names}
print(names_length)