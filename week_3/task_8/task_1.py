# Task 1
# 1. Explain each output of the program

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")

# This means if the first number entered is equal to the second number entered the output will be true and the output will be false if otherwise is the case. 

print(f"{num1} != {num2} : {num1 != num2}")


# This means if the first number entered is equal to the second number entered the output will be false and the output will be true if otherwise is the case. 

print(f"{num1} > {num2} : {num1 > num2}")

# This means if the first number entered is greater than the second number entered the output will be true and the output will be false if otherwise is the case. 

print(f"{num1} < {num2} : {num1 < num2}")

# This means if the first number entered is less than the second number entered the output will be true and the output will be false if otherwise is the case. 




# Give 3 usercases or scenarios where you can apply the program below

# 1. In determing students that passed above a particular number in a test/exam.
# 2. Admission eligibility
# 3. to determine grade 

# 1. In determining grade 

# 1. Grade checker to allow students to know their grade
# 2. An input to allow students to enter their score to check if they passed or failed
exam_result = int(input("Enter your score in the exam to check if you passed or failed: "))

# 3. Displaying the output(scores above 40 passed while those below failed.)
print("Passed: " , exam_result >= 40)


