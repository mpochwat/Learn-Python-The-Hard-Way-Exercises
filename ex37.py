with open("hello.txt", "wb") as f:
	f.write("Hello Python!\n")

while True: break
print "hello"
	
# x = 23
# assert x > 0, "x is not zero or negative"
# assert x%2 == 0, "x is not an even number"

#y = True
#while True:
#	try:
#		x = int(raw_input("Please enter a number: "))
#		break
#	except ValueError:
#		print "Oops! Not a number try again"
#		
#def this_fails():
#	x = 1/0
	
#try:
#	this_fails()
#except ZeroDivisionError as detail:
#	print 'Handling run-time error:', detail
	
#def divide(x,y):
#	try:
#		result = x / y
#	except ZeroDivisionError:
#		print "division by zero!"
#	else:
#		print "result is", result
#	finally:
#		print "executing finally clause"

#def bob():
#	global me
#	me = "locally defined"
#	print me
	
#bob()
#print me

#g = lambda x: x**2
#print g(3)

#def empty():
#	pass

#empty()

#raise ValueError("No")	

#x = None

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tek['jack']
del tel['sape']
tel.keys()
'guido' in tel

dict([('sape',4139),('guido',4127),('jack',4098)])
