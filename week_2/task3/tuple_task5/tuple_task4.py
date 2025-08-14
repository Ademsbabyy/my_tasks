# Ask the users for their first name,age,favorite color ,hometown

first_name = input("Enter your first name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
home_town = input("Where's your hometown: ")


# Store them in a tuple profile and Unpack them into variables

information = (first_name,age,favorite_color,home_town)
information = tuple(information)


# Print and use escape sequence to align each piece of information nicely.

print("\n",first_name,"\n",age,"\n", favorite_color, "\n",home_town)