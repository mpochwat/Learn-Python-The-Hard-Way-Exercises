mystuff = {'apple': "I am apples!"}
print mystuff['apple']

import mystuff
mystuff.apple()
print mystuff.tangerine

class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print "O AM CLASSY APPLES"
		
thing = MyStuff()
thing.apple()
print thing.tangerine

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy bday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parage = Song(["They rally around tha family",
						"With pockets full of shells"])

spanish_song = ["Hola", 2, "Senior"]

spanish = Song(spanish_song, spanish_song)

spanish.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parage.sing_me_a_song()

