# Task 4 : Student Record

# 1. Create an empty dictionary

student = dict()

# 2. Ask the user to input their name and age , then store them in the dictionary
name = input("Enter your name : ")
age = int(input("Enter your age : "))

student = dict(name = name,age = age)


# 3. Add a list of scores to the dictionary

score1 = 40
score2 = 70
score3 = 90

scores = [score1,score2,score3]

student = dict(student,scores = scores)


# 4. Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

status = (score1 >= 50)
student = dict(student,scores = scores ,Passed = status)
print(student) 

# 5. Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

Teenager = (age >= 13) and  (age <=19 )

# 6. Print out the complete record in ths format
print(f"Student Record: \nName: {name}\nAge: {age}\nScores: {scores}\nPassed: {status}\nTeenager: {Teenager}")


