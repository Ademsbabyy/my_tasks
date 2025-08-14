# Task 2
first_friend = input("Enter your first best friends' names: ")
second_friend = input("Enter your second best friends' names: ")
third_friend = input("Enter your third best friends' names: ")
fourth_friend = input("Enter your fourth best friends' names: ")
fifth_friend = input("Enter your fifth best friends' names: ")
friends = (first_friend , second_friend , third_friend , fourth_friend ,fifth_friend)
friends = tuple(friends)
print(friends[::-1])