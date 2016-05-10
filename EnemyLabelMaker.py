'''The idea here is to only use one enemy class and make them highly extensible/variable based on 
	what they get for adjectives, nouns, and verbs. Color will add even more variety. The best part about this,
	is that a matching label class can be made to modify the single enemy class instead of creating new
	enemies for each type '''


#singleton...?
class EnemyLabelMaker:
	adjectives = []
	nouns = []
	verbs = []
	
	def __init__(self):
		
		#Define Adjectives
		#These change enemy SPEED, SIZE, DAMAGE and DROP_RATE, as well as enemy.misc ATTACK, PATH_LOGIC
		self.adjectives.append("Fierce") #Charge/doesn't do much
		self.adjectives.append("Monstrous") #Size*=2
		self.adjectives.append("Swift") #speed*=2
		self.adjectives.append("Stalking") #changes enemy-to-player pathing logic OR moves through doors?
		self.adjectives.append("Perceptive") #Finds player if they're in the same room
		self.adjectives.append("Deadly") #drains health faster
		self.adjectives.append("Bloated") #explodes harmfully
		self.adjectives.append("Friendly") #deals less damage
		self.adjectives.append("Deranged") #floats aimlessly
		self.adjectives.append("Cowardly") #runs away from player in certain range
		self.adjectives.append("Zombified") #slower, but more health
		self.adjectives.append("Slimy") #slows player  
		self.adjectives.append("Rich") #Double drop rate - for hard
		self.adjectives.append("Poor") #Halves drop rate - for easy 
		self.adjectives.append("Ugly") #nothing/descriptor
		self.adjectives.append("Barbaric") #Descriptor?
		#adjectives.append("") #Use this as a template for more additions
		
		
		
		
		#Define Nouns:
		self.nouns.append("goo") # Green-
		self.nouns.append("swarm") # Black?
		self.nouns.append("golem") # Grey?
		self.nouns.append("wizard") # Blue? Maybe different types
		self.nouns.append("bandit") # Brown
		self.nouns.append("fighter") # Red
		self.nouns.append("skeleton") # White, circle/no fill
		self.nouns.append("skull") # White
		self.nouns.append("orc") #Green
		self.nouns.append("demon") #Orange
		self.nouns.append("goblin") #Green
		#nouns.append("") #Template
		
		#Define Verbs:
		self.verbs.append("fighting") #
		self.verbs.append("slithering") #
		self.verbs.append("polluting") #
		self.verbs.append("disgusting") #
		#verbs.append("") #
		#verbs.append("") #Template
		
		
		