# Simulate a football match ticket system

# 1. Store all seat numbers
seat_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50}

# 2. Ask users to "book" a seat by entering the number
booked_seat = int(input("Welcome to the football match ticket system,please enter a number to book a seat: "))
# 3. Remove booked seats from the set
seat_numbers.remove(booked_seat)

# 4. Show remaining seats 
print(seat_numbers)