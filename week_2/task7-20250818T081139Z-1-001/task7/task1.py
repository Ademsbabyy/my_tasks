# Student Bio Data Storage

# Create a program that collects student bio data from users input

name = input("Please enter your name: ")
age = int(input("Enter your age : "))
gender = input("Enter your gender: ")
courses = input("Enter your courses: ")

# store it in a dictionary
# Courses stored as a list

student_info = dict(name = name,age = age,gender = gender,courses =[courses])
# Display the bio-data neatly using escape sequences

print(f"------Student info ------\nName:\t\t{student_info["name"]}\nAge:\t\t{age}\nGender:\t\t{student_info["gender"]}\nCourses:\t{student_info["courses"]}")

