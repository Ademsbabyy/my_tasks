# Simulated USSD Menu Interaction
# 1 Display welcome screen
# 2 Ask for user to dial ussd code
# 3 Print a menu
# 4 Ask users to choose options
# 5 Display confirmation message
#6 Ask for an amount
# 7 Display final message

print("Welcome to 9mobile network service")
ussd = input("Dial the ussd code: ")
print("\n======\tNetwork service menu  =======")
print("1. Airtime-self\n2. Airtime-others\n3. Data\n4. Data-others\n5. Trsf-MFB/eWallet\n6. Cable TV\n7.Next")
print("--------------------------")
option = int(input("Please choose an option: "))
print("--------------------------")
print(f"You have succefully selected option {option}")
amount = int(input("Enter the amount: "))
print("You have successfully completed the transaction.")