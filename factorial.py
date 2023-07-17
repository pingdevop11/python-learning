"""
Write a program that calculates the factorial of a given number.
Instructions
Create a new file called factorial.py.
In the file, define a function called factorial.
The function should take one argument (the number to calculate the factorial of)
and return the factorial of that number.
In the main part of the program, prompt the user to enter a number and call the factorial function.
Print the factorial to the console.
"""


def factorial(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)


num = int(input("Enter a number for factorial check: "))
result = factorial(num)
print("The factorial of", num, "is", result)
