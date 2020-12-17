# Importing argv functionality from sys module.
from sys import argv

# Unpacking command line arguments
script, filename = argv

# Communicating with user.
print("Script: ", script)
print("filename: ", filename)
print(f"We will erase content of {filename}")

# Opening file ex16_sample.txt with only write & truncate permission
target = open(filename, 'w')
# print(target.read())      Not allowed operation.

# Erasing file content
print("Truncating file....")
target.truncate()

# Taking input from user.
print("Now I am going to take three lines")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# Writing files in file ex16_sample.txt
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write('\n')

# Closing file.
print("Closing file")
target.close()
