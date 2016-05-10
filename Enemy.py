import EnemyLabelMaker
import random
import math
import Display
import pygame
import Combat
import Weapon
#Hypothetical enemy class

#ADJECTIVE BASE TRAITS
SIZE = 20
SPEED = 2 #playerObj/2
SIZE = Display.TILE_SIZE/2
HEALTH = 10
ATTACK  = "melee"
DAMAGE = 1 #1/20th of player starting health
PLAYEREFFECT = "0"
DROPRATE = 1
RANGE = 5
	

COLOR = Display.BLACK

	
nameGenerator = EnemyLabelMaker.EnemyLabelMaker()
EnemyCombat = Combat.Combat()
class VariableEnemy:
	# sprite library
	outline_sprite = pygame.image.load('images\enemy_outline.png')
	friendly_sprite = pygame.image.load('images\\friendly.png')
	fierce_sprite = pygame.image.load('images\\fierce.png')
	perceptive_sprite = pygame.image.load('images\\perceptive.png')
	
	def __init__(self, locationx, locationy):
		self.adjective = random.randint(0, len(nameGenerator.adjectives)-1)
		self.noun = random.randint(0, len(nameGenerator.nouns)-1)
		self.verb = random.randint(0, len(nameGenerator.verbs)-1)
		self.name = nameGenerator.adjectives[self.adjective] + " " + nameGenerator.verbs[self.verb] + " " + nameGenerator.nouns[self.noun]
		self.x = locationx
		self.y = locationy
		self.size = SIZE
		self.speed = SPEED
		self.health = HEALTH
		self.damage = DAMAGE
		self.attack = ATTACK
		self.color = COLOR
		self.range = RANGE
		self.moveUp = False
		self.moveDown = False
		self.moveRight = False
		self.moveLeft = False
		self.drawDifferent = False
		self.moveThroughDoors = False
		self.canChase = True #Used to see IF an enemey can chase the player
		self.chase = True #Set to true if chasing, false otherwise
		self.canFlee = False #Used to see IF an enemy can flee the player
		self.flee = False #Set to true if fleeing, false otherwise
		self.hasPlayerEffect = False #Used for things like slowing the player, perhaps bleed or poision (status effects)
		self.playerEffect = PLAYEREFFECT #a description of what the effect is
		self.dropRate = DROPRATE #number out of 100 for how often cool stuff drops
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
		self.spriteList = [self.outline_sprite]
		self.getAdjectiveTraits()
		self.getNounTraits()
		self.getVerbTraits()
		self.currentWeapon = Weapon.MeleeWeapon()
		self.updateStatsToCurrentWeapon()
		
		
		
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
			self.spriteList.append(self.fierce_sprite)
			
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
			self.spriteList.append(self.perceptive_sprite)
		
		elif self.adjective == 5: #Deadly
			self.damage = self.damage*2
			self.dropRate += 1 
			
		elif self.adjective == 6: #Bloated
			self.attack = "exploding"
			self.damage = self.damage*2
		
		elif self.adjective == 7: #Friendly
			self.damage = self.damage*0.5
			self.spriteList.append(self.friendly_sprite)
			
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
			#self.color is BLACK by default
			self.drawDifferent = True
		
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
			self.size = self.size*2
			self.damage = self.damage*1.5
			self.health = self.health*2
			self.dropRate = self.dropRate*2
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
		if self.drawDifferent == True:
			if self.noun == 1: #Swarm
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x+5, self.y-5), self.size/5)	#maybe change these
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x+5, self.y+5), self.size/5)	#to be random
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size/5)		#between 1-5
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x-5, self.y+5), self.size/5)	#for swarm movement
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x-5, self.y-5), self.size/5)
		else:
			pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size)
			for sprite in self.spriteList:
				Display.DISPLAYSURF.blit(pygame.transform.scale(sprite, (self.size * 2, self.size * 2)), pygame.Rect(self.x - self.size, self.y - self.size, self.size, self.size))	
			
		Display.DISPLAYSURF.blit(self.text, (self.x - self.size*2, (self.y - self.size*1.5)))
			
	'''distance formula'''
	def collision(self, obj):
		if math.sqrt(pow(self.x - obj.x, 2) + pow(self.y - obj.y, 2)) < self.range:
			return True
		else:
			return False
			
	'''Written so that the Enemy may chase any object, not just the player
		in doing so, we allow them to chase objects, perhaps chests or loot
		they can destroy before the enemy is there? Also, if we want to impliment
		friendlies, this is a start'''
	def chaseObj(self, obj):
		if self.chase == True:
			if self.collision(obj) == False:
				if obj.x > self.x:
					self.moveRight = True
					self.x = self.x + self.speed
				if obj.x < self.x:
					self.moveLeft = True
					self.x = self.x - self.speed
				if obj.y > self.y:
					self.moveDown = True
					self.y += self.speed
				if obj.y < self.y:
					self.moveUp = True
					self.y -= self.speed
			else: #If colliding, attack!
				EnemyCombat.attack(self, obj)
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.moveUp = False
		
	#def patrolX(startx, endx)
			
	def death(self):
		"I died"
		
	def updateStatsToCurrentWeapon(self):
		self.range+=self.currentWeapon.range
		self.damage+=self.currentWeapon.damage
	
				