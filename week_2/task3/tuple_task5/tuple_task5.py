# Modify Tuple indirectly

# 1 ask users to enter three items for their shopping_list
List = ([
    input("Enter the first item on your shopping list: "),
 input("Enter the second item on your shopping list: "),
 input("Enter the third item on your shopping list: ") ,
])


# 3 Convert it to a list, then ask for two more items to add
Lists = list(List)
print("Add two more items.")
fr = input("Enter fourth item: ")
fv = input("Enter fifth item: ")
Lists.append(fr)
Lists.append(fv)

# Convert back to tuple
shopping = tuple(Lists)


# Print Updated list

print("|".join(shopping))