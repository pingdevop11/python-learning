"""
Write a program that sorts a list of numbers in ascending order.
Instructions

Create a new file called list_sorter.py.
In the file, define a function called sort_list.
The function should take one argument (the list of numbers to sort)
and return the sorted list.
In the main part of the program,
prompt the user to enter a list of numbers (comma-separated)
and call the sort_list function. Print the sorted list to the console.
"""


def sort_list(list):
    list = list(map(int, input("Enter multiple numbers, comma-separated: \n").split(', ')))
    print(sorted(list))


sort_list(list)
