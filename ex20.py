#import argv from sys module
from sys import argv

#Define the argv variables
script, input_file = argv

#define function that reads a given file
def print_all(f):
	print f.read()

# Define funcn that rewinds the file to the beginning
def rewind(f):
	f.seek(0)

#Function prints the line number and text on that line
def print_a_line(line_count, f):
	print line_count, f.readline()

#Opens input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#prints the details
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Sets back to beginning
rewind(current_file)

print "Let's print three lines:"

#runs function and iterates back
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
