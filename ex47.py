from sys import exit
from random import randint

bag = []
#start = Room("Start", "You can go west and down a hole.", 'gold')
#west = Room("Trees", "There are trees here, you can go east.", 'silver')
#down = Room("Dungeon", "It's dark down here, you can go up.", 'bronze')

class Death(object):

	quips = [
		"You died. YOu kinda suck at this.",
		 "Your mom would be proud...is she were smarter.",
		 "Such a luser.",
		 "I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class Room(object):

	def __init__(self, name, description, item):
		self.name = name
		self.description = description
		self.paths = {}
		self.item = item
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
	def pickup(self):
		bag.append(self.item)
		return bag
		
class GoldRoom(Room):
	
	def enter(self):
		print "You enter a room full of gold. What do you do?"
		print "Thee Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jummps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the Armory"
		print "and about to pull a weapon to blast you. Do you a) shoot!, b) dodge!, or"
		print "c) tell a joke."
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim.  Your laser hits his costume but misses him entirely.  This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead.  Then he eats you."
			#return Death()

		elif action == 'dodge!':
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			#return Death()
		
		elif action == 'tell a joke':
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			self.pickup()		
		
		else:
			print 'DOES NOT COMPUTE!'
			
