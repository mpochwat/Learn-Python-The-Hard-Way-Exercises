numbers = []

#num = raw_input("Input a number: ")

def list_create(num,increment):
	i = 0
	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num 
		
def list_creator(num,increment):
	i = 0
	for i in range(0,num):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num 