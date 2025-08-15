# Name organizers

#1. Ask the user to enter 5 names (seperated by spaces) and convert to lower case

names = input("Enter 5 names seperated by spaces : ")
name_to_lower = names.lower()
# 2. Sort the list alphabetically
names_list = name_to_lower.split(" ")

names_list.sort()
print(names_list)
# 3. Display them one name per line
for name in range(len(names_list)):
    print(names_list[name])
