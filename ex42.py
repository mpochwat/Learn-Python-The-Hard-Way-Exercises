## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):
	
	def __init__(self, name):
		self.name = name
		
	def run(speed):
		print "The animal has run %d km/h" % speed
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name, speed, height):
		## Dog has-a name
		super(Dog, self).__init__(name)
		print "The dog ran %d km/h" % speed
		self.speed = speed
		self.height = height
		print "The dog jumped %d metres high" % height
		
# Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a name
		self.name = name
		self.tricks = []
		
	def add_trick(self, trick):
		self.tricks.append(trick)
		
# Person is-a object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a person
class Employee(Person):
	
	def __init__(self, name, salary):
		## 
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
# Salmon is-a fish
class Salmon(Fish):
	pass
	
## Halibut is-a fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover", 20, 10)
#rover.run()

# statan is a cat
satan = Cat("Satan")
satan.add_trick("Jump")
print satan.tricks

## mary is a person
mary = Person("Mary")

# Mary has-a pet named satan
mary.pet = satan

## drank is-a employee and has-a 120000 salary
frank = Employee("Frank", 120000)

## flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

