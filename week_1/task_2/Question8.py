# Transport fare calculator
distance =float(input("What is the distance travelled in km: "))
fare = float(input("What is the fare per km: "))
total_fare = distance * fare
print(f"Your total fare is {total_fare:.2f}")