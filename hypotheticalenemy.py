import LabelMaker
import random
import Display
import pygame

#Hypothetical enemy class

#ADJECTIVE BASE TRAITS
SIZE = 20
SPEED = 5 #playerObj/2
HEALTH = 10
ATTACK  = "melee"
DAMAGE = 1 #1/20th of player starting health
PLAYEREFFECT = "0"
DROPRATE = 1
	
#NOUN TRAITS
COLOR = Display.BLACK
#	SPRITE #if we use this, could be lots of code/images, but cool af
	
#VERB TRAITS
nameGenerator = LabelMaker.LabelMaker()
class VariableEnemy:
	def __init__(self, locationx, locationy):
		self.adjective = random.randint(0, len(nameGenerator.adjectives)-1)
		self.noun = random.randint(0, len(nameGenerator.nouns)-1)
		self.verb = random.randint(0, len(nameGenerator.verbs)-1)
		self.name = nameGenerator.adjectives[self.adjective] + " " + nameGenerator.verbs[self.verb] + " " + nameGenerator.nouns[self.noun]
		self.x = locationx
		self.y = locationy
		self.speed = SPEED
		self.size = SIZE
		self.health = HEALTH
		self.damage = DAMAGE
		self.attack = ATTACK
		self.color = COLOR
		self.moveThroughDoors = False
		self.canChase = True #Used to see IF an enemey can chase the player
		self.chase = False #Set to true if chasing, false otherwise
		self.canFlee = False #Used to see IF an enemy can flee the player
		self.flee = False #Set to true if fleeing, false otherwise
		self.hasPlayerEffect = False #Used for things like slowing the player, perhaps bleed or poision (status effects)
		self.playerEffect = PLAYEREFFECT #a description of what the effect is
		self.dropRate = DROPRATE #number out of 100 for how often cool stuff drops
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
		self.getAdjectiveTraits()
		self.getNounTraits()
		self.getVerbTraits()
		
		
	def printName(self):
		print "%s" % (self.name)
		
	def getAdjectiveTraits(self):
		'''Balance teseting required, 
		need to do this along with nouns and verbs,
		perhaps upper tier enemies get a second adjective modifier, 
		or even have different lists for 'badasses', 'bosses', 'mini-bosses', etc. (differnt enemy class?)
		'''
	
		if self.adjective == 0: #Fierce
			self.speed += 1
			self.dropRate += 1
			
		elif self.adjective == 1: #Monstrous
			self.size = self.size*2
			self.health = self.health*2
			self.dropRate += 1
		elif self.adjective == 2: #Swift
			self.speed = self.speed*2
		
		elif self.adjective == 3: #Stalking
			self.moveThroughDoors = True
			self.dropRate += 1
		
		elif self.adjective == 4: #Perceptive
			self.chase = True
		
		elif self.adjective == 5: #Deadly
			self.damage = self.damage*2
			self.dropRate += 1 
			
		elif self.adjective == 6: #Bloated
			self.attack = "exploding"
			self.damage = self.damage*2
		
		elif self.adjective == 7: #Friendly
			self.damage = self.damage*0.5
			
		elif self.adjective == 8: #Deranged
			self.canChase = False
		
		elif self.adjective == 9: #Cowardly
			self.canChase = False
			self.flee = True
		
		elif self.adjective == 10: #Zombified
			self.speed = self.speed/2
			self.health = self.health*2
		
		elif self.adjective == 11: #Slimy
			self.hasPlayerEffect = True
			self.playerEffect = "slimy"
		
		elif self.adjective == 12: #Rich
			self.dropRate += 3
			
		elif self.adjective == 13: #Poor
			self.dropRate -= .5
			
		elif self.adjective == 14: #Ugly
			pass #just a descriptor
			
		elif self.adjective == 15: #Barbaric
			pass #just a descriptor
			
		else:
			pass #Shouldn't happen
			
		
	def getNounTraits(self):
		'''These need to be balance tested to achieve better 
		drop rates, health and damage modifiers so that 
		they can easily change the pace of the game and it isn't
		just retexturing the enemies'''
		
		if self.noun == 0: #Goo
			self.color = Display.GOOGREEN
			
		elif self.noun == 1: #Swarm
			pass #self.color is BLACK by default
			#Try to find a way to make a bunch of tiny circles on top of the normally drawn enemy to look like a swarm?
		
		elif self.noun == 2: #Golem
			self.color = Display.GREY
			
		elif self.noun == 3: #Wizard
			self.color = Display.BLUE
		
		elif self.noun == 4: #Bandit
			self.color = Display.BROWN
			
		elif self.noun == 5: #Fighter
			self.color = Display.FIGHTERRED
			
		elif self.noun == 6: #Skeleton
			self.color = Display.WHITE #figure a way to make the circled not filled
			
		elif self.noun == 7: #Skull
			self.color = Display.WHITE
			
		elif self.noun == 8: #Orc
			self.color = Display.ORCGREEN #might clash with goo and goblins
			
		elif self.noun == 9: #Demon
			self.color = Display.DEMONORANGE
			
		elif self.noun == 10: #Goblin
			self.color = Display.GOBLINGREEN
		
		
	def getVerbTraits(self):
		#COME up with better and more verbs...
		#balance required
		if self.verb == 0: #Fighting
			self.chase = True
			self.damage += 1
		
		elif self.verb == 1: #Slithering
			self.speed -= 1
		
		elif self.verb == 2: #Polluting
			self.attack = "poision"
		
		elif self.verb == 3: #Disgusting
			pass #Player fear level?	
			
			
			
	def updateName(self):
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))	
	
	def drawSelf(self):
		pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size)
		Display.DISPLAYSURF.blit(self.text, (self.x - self.size*1.5, (self.y - self.size*1.5)))
		
		