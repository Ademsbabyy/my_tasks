# Task 3 Online Store Cart Calculation
# 1. Create a list of items 
items = ["Book","Pen","Eraser","Drawing board","Laptop"]
# 2. Create another list of prices
prices = [1000,300,120,16000,450000]

items_prices = zip(items,prices)
print(tuple(items_prices))
# 3. Start with an empty cart total (cart_total = 0)

cart_total = 0

# 4. Use assignment operators (+=) to add price of some items into cart_total
cart_total += 1000
cart_total += 300
cart_total += 120
cart_total += 16000
cart_total += 450000

# 5. Print the list of items and the total price using an f-string

print(f"Items: {items}\nTotal Price: {cart_total}")
