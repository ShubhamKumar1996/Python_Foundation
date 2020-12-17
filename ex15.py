# importing argv from sys module
from sys import argv

# unpacking arguments
script, filename = argv

# Opening file and returning a stream
txt = open(filename)

# Printing formatted string.
print(f"Here's your file {filename}: ")

# Reading the content fo file.
print(txt.read())

# Taking input from user.
print("Type the filename again: ")
file_again = input("> ")

# Opening file and returning a stream of user given file.
txt_again = open(file_again)

# Printing content of file.
print(txt_again.read())
