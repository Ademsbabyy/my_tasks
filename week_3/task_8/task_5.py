# Task 5 : Store Inventory Update
# 1. Create a dictionary called store with items and their available quantities.
store = {
    "book" : 200,
    "laptop" : 30,
    "smart tv" : 20,
    "designer bags": 120
}


# 2. Ask the user to input the quantity 
item = input("Enter the item you want to buy: ").lower()

# 3. Ask the user to input the quantity they want to purchase
quantity = int(input("Enter the quantity ou want to purchase: "))

# 4. Use the assignment operator -= to update(reduce) the item quantity in the dictionary.
store[item] -= quantity

print(store)


