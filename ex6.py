#Variables describing types of people in the world
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#Printing the variables
print x
print y

#Repeating printing the variables
print "I said: %r." % x
print "I also said: '%s'." %y

#Variables for next string. Joke_evaluation has a place to insert another variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Printing the string
print joke_evaluation % hilarious

#More variables
w = "This is the left side of..."
e = "a string with a right side."

#2 variables printed together
print w + e
