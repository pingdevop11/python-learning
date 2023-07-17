"""
Write a program that checks if a given word is a palindrome.
Instructions
Create a new file called palindrome.py.
In the file, define a function called is_palindrome.
The function should take one argument (the word to check)
and return True if the word is a palindrome and False otherwise.
In the main part of the program, prompt the user to enter a word
and call the is_palindrome function.
Print whether the word is a palindrome or not to the console.
"""


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


word = input("Please enter a word for a palindrome check: ")
result = is_palindrome(word)
print(result)
