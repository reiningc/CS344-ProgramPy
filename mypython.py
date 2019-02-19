# Class: CS344
# Program name: mypython.py
# Programmer name: Colin Reininger
# Last updated: 2/19/2019

import string
import random
import sys

# Create 3 files, each named differently
filenames = ['test1.txt', 'test2.txt','test3.txt']

# Each file must contain 10 random lowercase characters, 11th char is newline
for x in filenames:
	file = open(x, 'w')
	for i in range(10):
		file.write(random.choice(string.ascii_lowercase))
	file.write('\n')
	file.close()

# Output contents of the 3 files to stdout on lines 1, 2, 3
for x in filenames:
	file = open(x, 'r')
	sys.stdout.write(file.read(11))

# Print out 2 random integers (1-42) on lines 4, 5
num1 = random.randint(1,42)
num2 = random.randint(1,42)
print(num1)
print(num2)

# Print out the product of the 2 random integers on line 6
print(num1 * num2)
