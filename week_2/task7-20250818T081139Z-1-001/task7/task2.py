# Super Market Price List
# Create a program that stores items and their prices in a dictionary




# Items should come from a list

Items = ["Rice","Toiletries","Hiscense 45 inches tv","Ring","Bowls"]

# prices are entered by the user.
price1 = int(input("Enter the price for rice: "))
price2 = int(input("Enter the price for toiletries: "))
price3 = int(input("Enter the price for the smart tv: "))
price4 = int(input("Enter the price for ring: "))
price5 = int(input("Enter the price for bowls: "))

# storing the items and their prices in a dictionary
items_prices = dict(rice = price1,toiletries = price2,smarttv = price3,ring=price4,bowls=price5)
print(items_prices.keys())

# Display all items and prices
print(items_prices)

# Then allow user to update the price of an item.
price_update1 = int(input("Enter updated price for rice: "))
price_update2 = int(input("Enter updated price for toiletries: "))
price_update3 = int(input("Enter updated price for the smart tv: "))
price_update4 = int(input("Enter updated price for ring: "))
price_update5 = int(input("Enter updated price for bowls: "))

items_prices.update(dict(rice = price_update1,toiletries = price_update2,smarttv = price_update3,ring = price_update4,bowls = price_update5))
print(items_prices)