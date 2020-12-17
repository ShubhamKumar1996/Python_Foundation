from sys import argv

script, filename = argv

print(f"Script: {script} \nFilename: {filename}")

target = open(filename, 'w')

print("Truncating file...")
target.truncate()

print("Enter new content")
target.write(input("line1: ") + "\n")
target.write(input("line2: ") + "\n")
target.write(input("line3: ") + "\n")

print("Closing File...")
target.close()
