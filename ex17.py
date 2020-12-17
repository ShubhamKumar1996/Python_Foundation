from sys import argv

# Why we imported os.path.exists
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print("Copying Content...")
outdata = open(to_file, 'w').write(indata)

print("Copied!!!")
