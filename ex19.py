#Def function that produces text w/ number of cheese and cracker boxes
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# 20 cheese and 30 crackers	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#Using variables
print "OR we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#math as variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def cats_and_dogs(cats, dogs):
	print "There are %d cats & dogs" % (cats+dogs)
	
cats_and_dogs(2,3)

cats = 3
dogs = 4
cats_and_dogs(cats, dogs)
cats_and_dogs(cats+dogs,cats+dogs)

print "How many cats & dogs do you own?"
numb = int(raw_input("?"))

cats_and_dogs(numb, 0)

