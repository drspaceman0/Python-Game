'''The idea here is to only use one enemy class and make them highly extensible/variable based on 
	what they get for adjectives, nouns, and verbs. Color will add even more variety. The best part about this,
	is that a matching label class can be made to modify the single enemy class instead of creating new
	enemies for each type '''


#singleton...?
class LabelMaker:
	adjectives = []
	nouns = []
	verbs = []
	colors = []
	
	def __init__(self):
		#Should also make a matching attribute class, which changes enemies based on traits
		
		#Define Adjectives
		#These change enemy SPEED, SIZE, DAMAGE and DROP_RATE, as well as enemy.misc ATTACK, PATH_LOGIC
		adjectives.append("fierce") #Charge/doesn't do much
		adjectives.append("monstrous") #Size*=2
		adjectives.append("swift") #speed*=2
		adjectives.append("stalking") #changes enemy-to-player pathing logic OR moves through doors?
		adjectives.append("perceptive") #Finds player if they're in the same room
		adjectives.append("deadly") #drains health faster
		adjectives.append("bloated") #explodes harmfully
		adjectives.append("friendly") #deals less damage
		adjectives.append("deranged") #floats aimlessly
		adjectives.append("cowardly") #runs away from player in certain range
		adjectives.append("zombified") #slower, but more health
		adjectives.append("slimy") #slows player  
		adjectives.append("rich") #Double drop rate - for hard
		adjectives.append("poor") #Halves drop rate - for easy 
		adjectives.append("ugly") #nothing/descriptor
		adjectives.append("") #Use this as a template for more additions
		
		
		
		
		#Define Nouns:
		nouns.append("Goo") # Green-
		nouns.append("Swarm") #
		nouns.append("Cow") #
		nouns.append("Golem") #
		nouns.append("Wizard") #
		nouns.append("Bandit") #
		nouns.append("Fighter") #
		nouns.append("Skeleton") #
		nouns.append("Skull") #
		nouns.append("Orc") #
		nouns.append("Demon") #
		nouns.append("Goblin") #
		nouns.append("") #Template
		
		
		