# Write a program that collects the names of people attending a seminar

attendee1 = input("Enter your name: ")
print(f"Welcome, {attendee1}")
attendee2 = input("Enter your name: ")
print(f"Welcome, {attendee2}")
attendee3 = input("Enter your name: ")
print(f"Welcome, {attendee3}")
attendee4 = input("Enter your name: ")
print(f"Welcome, {attendee4}")
attendee5 = input("Enter your name: ")
print(f"Welcome, {attendee5}")

attendees = {attendee1,attendee2,attendee3,attendee4,attendee5}

# Display them in alphabetical order
attendees_sorted = sorted(attendees)
print(attendees_sorted)