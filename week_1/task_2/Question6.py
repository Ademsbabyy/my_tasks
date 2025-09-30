# Electricity Bill Formatter
full_name = input("Enter your full name: ")
units = int(input("Enter the units consumed (kWh): "))
cost = float(input("Enter the cost per unit: "))
total_bill = units * cost
print(f"{full_name}, your total units for the month is {units}\n Cost per unit is {cost}\nYour total bill for the month is {total_bill} naira")