# Word Analyzer
# 1. Ask the user to input a word
word = input("Enter a word: ")
# 2. Print the length of the word
print(len(word))
# 3. Check if it is all uppercase,all lowercase, or title case.
print(word.isupper())
print(word.islower())
print(word.istitle())
# 4. Reverse the word using slicing
print(word[::-1])