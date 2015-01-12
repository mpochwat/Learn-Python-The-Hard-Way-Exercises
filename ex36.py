from sys import exit

# Start of the game
def start():
	print "You are in a bright room."
	print "You see 2 doors, one is pink and the other blue."
	print "Which one do you go through?"
	
	choice = raw_input("> ")
	
	if "pink" in choice:
		dog_room()
	elif "blue" in choice:
		bull_room()
	else:
		dead("Time runs out you die hahahaha.")

# What happens in the dog room
def dog_room():
	print "You enter a room and there is an evil dog."
	print "You have 3 options: 1) Throw a ball,"
	print "2) give it a treat, 3) Do nothing."
	
	choice = raw_input("> ")
	print choice
	
	if ("ball" or "nothing") in choice:
		dead("The dog went after you and ate you")
	elif "treat" in choice:
		clown_room()
	else:
		dead("Bad choice you died")

# What happens in the bull room		
def bull_room():
	print "You enter a room and find a raging bull."
	print "You can 1) pull out a red flag,"
	print "2) feed it food, or 3) hide in a corner."
	
	choice = raw_input()
	
	if ("flag" or "food") in choice:
		dead("The bull raged into you. Goodbye!")
	elif "corner" in choice:
		print "The bulls runs away."
		cat_room()
	else:
		dead("haha you die.")

# What happens in the cat room		
def cat_room():
	print "You enter a room and find an evil cat."
	print "You can 1) give it a treat, or "
	print "2) throw it a ball."
	mood = False
	
	while True:
		choice = raw_input()
	
		if "treat" in choice:
			dead("The cat attacked you. Goodbye!")
		elif "ball" in choice and mood == False:
			print "The cat turns good."
			print "What do you do now?"
			mood = True
		elif "ball" in choice and mood == True:
			clown_room()
		else:
			dead("haha you die.")

# What happens in the clown room			
def clown_room():
	print "You enter a room and find a scary clown."
	print "You can 1) close your eyes, or "
	print "2) laugh at joke, or 3) give it a snack."
	
	choice = raw_input()
	
	if "close" in choice:
		dead("The clown stabbed you to death. Goodbye!")
	elif "joke" in choice:
		print "The clown become good."
		pearl_room()
	elif "snack" in choice:
		dog_room()
	else:
		dead("haha you die haha.")		

# What happens in the pearl room
def pearl_room():
	print "You enter a room full of pearls."
	print "How many pearls do you take?"
	
	choice = raw_input()
	
	if choice.isdigit():
		amount = int(choice)
	else:
		dead("haha you die haha.")	
	
	# You win if you took enough pearls. Otherwise lose.
	if amount > 200:
		print "Congrats you got the pearls and won!"
		exit()
	else:
		dead("You didn't take enough pearls and die.")
		

# What happens when you die		
def dead(how):
	print how, "Good job!"
	exit()
		
start()