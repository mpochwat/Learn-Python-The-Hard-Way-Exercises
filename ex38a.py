class MyClass:
	"""A simple emaple class"""
	i = 12345
	def f(self):
		return "hello world"
		
x = MyClass()

print x.i

x.f

recipes = ['hummus', 'chicken', 'beef', 'pork']
courses = ['cs101', 'cs102', 'cs103', 'cs104']

for i in courses:
	print "I passed this course: %s" % i
