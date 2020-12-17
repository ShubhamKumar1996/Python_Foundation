from sys import argv

script, file = argv

def print_all(input_file):
    print(input_file.read())

def rewind(input_file):
    input_file.seek(0)

def print_a_line(current_line, input_file):
    content = input_file.readline()
    print(f"{current_line} {content}")

input_file = open(file)

print("First let's print the whole file:\n")
print_all(input_file)

print("Let's print it line by line:\n")
rewind(input_file)

current_line = 0;

current_line = current_line + 1
print_a_line(current_line, input_file)

current_line = current_line + 1
print_a_line(current_line, input_file)

current_line = current_line + 1
print_a_line(current_line, input_file)
