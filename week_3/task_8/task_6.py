# Task 6
# 1 . First process : To collect applicant's information
# 2. Second process : To determine if applicant's UTME and O'Level meets requirement
# 3. Third process : To determine if applicant's first choice is UNILAG
# 4. Fourth process : To determine if the applicant participated in the post-utme and what the applicant's score is
# 5. Fifth process : Determine eligibility
# 6 . Display outputs

# 1. First process
name = input("Enter your full name : ").title()
secondary_school = input("Enter your secondary school's name: ")
age = int(input("Enter your age: "))

#2. Second process
academic_qualification = input("Do you have five distinctions (As and Bs) in relevant subjects in WAEC/WASSCE exams including English and Mathematics ?(True or False): ").title()
Mathematics = input("Enter your distinction in Mathematics: ").upper()
English =  input("Enter your distinction in English: ").upper()
other_qualifications = input("Do you have at least three distinctions in other relevant subjects in WAEC/WASSCE exams(Yes/No):  ").title()
utme = int(input("Enter your UTME result: "))

# 3. Third process
choice = input("Is UNILAG your first choice university(True or False): ").title()

post_utme = input("Did you participate in the online post-utme screening(True or False)?: ").title()

utme_score = int(input("Enter your post utme score: "))

#4. Fourth process
has_academic_qualification = academic_qualification
is_choice = choice
has_post_utme = post_utme




eligibility = (age >= 16 and has_academic_qualification) and (utme >= 200 and is_choice ) and (has_post_utme) and (utme_score >= 200 ) and (Mathematics == "A" or Mathematics == "B" ) and (English == "A" or English == "B" ) and (other_qualifications == "Yes")

# 5. Fifth process
print(print(f"------- Student Eligibility Status -------\nCandidate: {name}\nAge: {age}\nSchool: {secondary_school}\nMathematics distinction: {Mathematics}\nEnglish Language distinction: {English}\nDo you have at least three distinctions in other relevant subjects in WAEC/WASSCE exams: {other_qualifications}\nPost-Utme: {utme} \nPost-Utme participation : {post_utme} \nEligible: {eligibility}"))