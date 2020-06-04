# import argument for python
from sys import argv

# naming the script and the variable filename
script, filename = argv

# labeling the variable txt and telling it that it will open a file
txt = open(filename)

# format and print a string with the filename in it
print(f"Here's your file {filename}:")

# print the file
print(txt.read())

# print a string asking for input
print("Type the filename again:")

# ask the user for input
file_again = input("> ")

# open the file
txt_again = open(file_again)

# print the information within the file
print(txt_again.read())
