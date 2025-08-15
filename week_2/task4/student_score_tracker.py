# Student Score Tracker

# 1. Ask the user for 3 student names
empty_list1 = []
empty_list2 = []
names = ([
input("Enter the first student's name: "),
input("Enter the second student's name: "),
input("Enter the third student's name: ")
])

# 2. For each student,ask for their score
scores =([ 
int(input("Enter the first student's score: ")),
int(input("Enter the second student's score: ")),
int(input("Enter the third student's score: ")),    
])


# 3. Store the results in two lists (one for names, one for scores).
empty_list1.extend(names)
empty_list2.extend(scores)

# 4. Print a formatted output showing  Name-score aligned neatly.
print(f"----------------------------\nStudents names\tScores\n---------------------------\n{names[0]}\t\t{scores[0]}\n{names[1]}\t\t{scores[1]}\n{names[2]}\t\t{scores[2]}")