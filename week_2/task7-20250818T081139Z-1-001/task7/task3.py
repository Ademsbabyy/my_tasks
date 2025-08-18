## 


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x = zip(a, b)

# #use the tuple() function to display a readable version of the result:

# print(tuple(x))



# usernames = ("Adems","Rid")
# password = ("YRRIR","DJDNDNJD")
# users = dict(zip(usernames,password))
# for key,value in users.items():
#     print(key,value)





 # Days and Activities pairing


# # Store the days of the week in a tuple and ask the user to input an actvity for three specific days.


days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

activity1 = input("Enter activities for Monday: ").title()
activity2 = input("Enter activities for Friday: ").title()
activity3 = input("Enter activities for Sunday: ").title()

activities = (activity1,activity2,activity3)

# Use dictionary comprehension to pair days and activities


day_activities = dict(zip(days , activities))
print(type(day_activities))
# Print the dictionary

for key,value in day_activities.items():
    print(key + " : " + value)

