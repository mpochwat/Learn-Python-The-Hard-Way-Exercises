#Calls module from sys
from sys import argv

#argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w+")

#Delete file contents
print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

#raw input lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

text = "%s \n%s \n%s \n" % (line1, line2, line3)

print "I'm going to write these to the file."

#Write each element
target.write(text)
#Including new lines
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()

print "And here are the contents"
txt = open(filename)
print txt.read()