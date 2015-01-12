# Access module 
from sys import argv

#list argument variables we will use
script, filename = argv

#Open the filename
txt = open(filename)

#Prints the filename
print "Here's your file %r:" % filename
#prints the text in the filename
print txt.read()

#Lets user choose the file again
print "Type the filename again:"
file_again = raw_input("> ")

#Opens the selected file
txt_again = open(file_again)

#Reads the selected file
print txt_again.read()