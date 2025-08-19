# Task 2

#1. Comment the code below appropriately, and using doctring, explain what the code is doing.



# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


"""The code asks user to enter name,age and test score to determine 
eligibility. age must be less than 18 and score must be greater than 70 for
eligibility to be true , otherwise eligibility will be false.  """



# 2. Adapt the code to the case below

# Federal Government Scholarship key eligibility requirements:

# 1. Collecting information to determine eligibilty
name = input("Enter your name: ")
age = input("Enter your age: ")
citizenship = input("Are you a citizen of Nigeria(True or False): ").title()
school = input("Enter your school: ").title()
Enrollment = input("Are you a registered , full-time undergraduate of the said school(True or False):  ").title()
other_scholarships = input("I am not currently receiving scholarships from another entity in the oil and gas industry(True or False)?: ").title()
academic_qualifications = input("Do you have five distinctions (As and Bs) in relevant subjects in WAEC/WASSCE exams including English and Mathematics ?(True or False): ").title()


Mathematics = input("Enter your distinction in Mathematics: ").upper()
English =  input("Enter your distinction in English: ").upper()

    

is_citizen = citizenship
is_enrolled = Enrollment
has_scholarships = other_scholarships
has_qualifications = academic_qualifications
# 2. Display
eligibility = (is_citizen and is_enrolled ) and (has_qualifications and has_scholarships) and (Mathematics == "A" or Mathematics == "B" ) and (English == "A" or English == "B" )

print(f"------- STUDENT Eligibility Status -------\nCandidate: {name}\nAge: {age}\nSchool: {school}\nEligible: {eligibility}")