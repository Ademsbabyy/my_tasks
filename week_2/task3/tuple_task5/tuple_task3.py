# 1 Asking users for five nigerian states
Nigerian_state1 = input("Enter a Nigerian state: ")
Nigerian_state2 = input("Enter a Nigerian state: ")
Nigerian_state3 = input("Enter a Nigerian state: ")
Nigerian_state4 = input("Enter a Nigerian state: ")
Nigerian_state5 = input("Enter a Nigerian state: ")

# 2 Storing them in a tuple
Nigerian_states = (Nigerian_state1,Nigerian_state2,Nigerian_state3,Nigerian_state4,Nigerian_state5)
Nigerian_states = tuple(Nigerian_states)

# 3 Printing the first and last states
print(Nigerian_states[0])
print(Nigerian_states[4])

# 4 Checking if lagos is part of the states entered
print("Lagos" in Nigerian_states)
 
 # 5 Print the number of states entered
print(len(Nigerian_states))