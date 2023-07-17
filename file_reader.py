"""
Write a program that reads a file and prints its contents to the console.
Instructions

Create a new file called file_reader.py.
In the file, define a function called read_file.
The function should take one argument (the file name)
and print the contents of the file to the console.
In the main part of the program,
prompt the user to enter a file name and call the read_file function.
"""

file_name = input("Please, type the file name: ")
def read_file(file_name):
    with open(file_name) as file:
        print(file.read())
    file.close()
    return file_name
print(read_file(file_name))


