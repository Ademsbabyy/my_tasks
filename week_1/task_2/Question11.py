# User input
amount_naira = float(input("Enter amount in Naira: "))
usd_rate = float(input("Enter exchange rate to US Dollars: "))
gbp_rate = float(input("Enter exchange rate to British Pounds: "))

# Converting amounts
amount_usd = amount_naira / usd_rate
amount_gbp = amount_naira / gbp_rate

# Printing the results in a table-like format using escape sequences
print("\n\t=== Currency Conversion Table ===")
print("Currency\tAmount")
print("--------\t-------")
print(f"Naira (₦)\t₦{amount_naira:,.2f}")
print(f"US Dollar ($)\t${amount_usd:,.2f}")
print(f"Pound (£)\t£{amount_gbp:,.2f}")
