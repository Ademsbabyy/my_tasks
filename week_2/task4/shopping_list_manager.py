# Shopping list manager
# 1. Create an empty list
list = []

# 2. Ask the user to enter 3 shopping items(one by one)
shopping_item1 = input("Enter your first shopping item: ")
shopping_item2= input("Enter your second shopping item: ")
shopping_item3=input("Enter your third shopping item: ")



# 3. Add them to the list.
list.append(shopping_item1)
list.append(shopping_item2)
list.append(shopping_item3)


# 4. Display the list as a single string,seperated by commas
print(list)