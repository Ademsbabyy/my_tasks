# Ask the user to enter five favourite fruits.



favourite_fruits = ([
   
    input("Enter your first favourite fruit: "),
    input("Enter second favourite fruits: "),
    input("Enter third favourite fruits: "),
    input("Enter fourth favourite fruits: "),
    input("Enter fifth favourite fruits: ")
    ])


# Store them in a set
    
fruits = set(favourite_fruits)

# Display the set

print(fruits)