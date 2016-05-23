import EnemyLabelMaker
import random
import math
import Display
import pygame
import SpriteAnimation
import Combat
import Weapon
import Inventory
import Coin
import functions

#ADJECTIVE BASE TRAITS
SPEED = 2 #playerObj/2
SIZE = Display.TILE_SIZE
HEALTH = 10
ATTACK  = "melee"
DAMAGE = 1 #1/20th of player starting health
DROPRATE = 1
RANGE = 30
COLOR = Display.BLACK
nameGenerator = EnemyLabelMaker.EnemyLabelMaker()

class VariableEnemy:
	enemyList = []
	numberOfEnemies = 0

	# sprite library
	outline_sprite = pygame.image.load('images\enemy_outline.png')
	friendly_sprite = pygame.image.load('images\\friendly.png')
	fierce_sprite = pygame.image.load('images\\fierce.png')
	perceptive_sprite = pygame.image.load('images\\perceptive.png')
	rich_sprite = pygame.image.load('images\\rich.png')
	disgusting_sprite = [pygame.image.load('images\\flys1.png'), pygame.image.load('images\\flys2.png')]
	polluting_sprite = [pygame.image.load('images\\polluting1.png'), pygame.image.load('images\\polluting2.png')]

	#Note that this has default values if we don't pass it stuff. The "stuff" comes from the spawner calling it, allowing for types of spawners
	def __init__(self, playerObj, locationx, locationy, adjective = random.randint(0, len(nameGenerator.adjectives)-1), noun = random.randint(0, len(nameGenerator.nouns)-1), verb = random.randint(0, len(nameGenerator.verbs)-1)):
		VariableEnemy.enemyList.append(self)
		VariableEnemy.numberOfEnemies += 1
		self.adjective = adjective
		self.noun = noun
		self.verb = verb
		self.name = nameGenerator.adjectives[self.adjective] + " " + nameGenerator.verbs[self.verb] + " " + nameGenerator.nouns[self.noun]
		self.x = locationx
		self.y = locationy
		self.collisionx = self.x
		self.collisiony = self.y
		self.size = SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.range = RANGE
		self.speed = SPEED
		self.health = HEALTH
		self.damage = DAMAGE
		self.attack = ATTACK
		self.color = COLOR
		self.drawDifferent = False
		self.isDead = False
		self.chase = True
		self.shouldFlank = False
		self.weaponx = 0
		self.weapony = 0
		self.dropRate = DROPRATE #number out of 100 for how often cool stuff drops
		self.coin = Coin.Coin()
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
		self.spriteList = [self.outline_sprite]
		self.spriteObj = SpriteAnimation.SpriteAnimation([self.outline_sprite, self.outline_sprite], 10)
		self.verbAnimSpriteObj = None
		self.playerObj = playerObj
		self.items = []
		self.inventory = 0
		#Functions To update self before spawning
		self.getAdjectiveTraits()
		self.getNounTraits()
		self.getVerbTraits()
		self.currentWeapon = Weapon.MeleeWeapon()
		self.updateStatsToCurrentWeapon()
		self.updateInventory()
		
		
		
	def updateInventory(self):
		self.items.append(self.currentWeapon)
		self.inventory = Inventory.Inventory(self.dropRate, self.items)
		
		
	def printName(self):
		print "%s" % (self.name)
		
	def update(self):
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.drawSelf()
		self.updateColliders()
		#self.drawCollider()
		self.chaseObj(self.playerObj)
		if self.isDead == True:
			self.playerObj.score += 1
			self.playerObj.dungeonObj.returnCurrentRoom().enemylist.remove(self)	
	

	def collision(self, obj):
		"""distance formula"""
		if math.sqrt(pow(self.x - obj.x, 2) + pow(self.y - obj.y, 2)) <= self.range:
			return True

			
	def death(self):
		functions.worldEnemiesKilled += 1
		self.isDead = True
		self.dropLoot()
		"I died"
	

			
	def updateStatsToCurrentWeapon(self):
		self.range += self.currentWeapon.range
		self.damage += self.currentWeapon.damage

	def drawCollider(self):
		""" This circle will be our collision box where we draw our attack from """
		pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.collisionx, self.collisiony), self.size+2, 1)
				
	def updateColliders(self):
		self.collisionx = self.x
		self.collisiony = self.y
		
	def isPlayer(self):
		return False
		
		
	def dropLoot(self):
		self.currentWeapon.dropWeapon(self.x, self.y)
		print "Dropped"
		self.inventory.dropItems()
		functions.worldCoins.append(self.coin)
		self.coin.setDrawInfo(self.inventory.coins, self.x, self.y)
		
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
			self.size *= 2
			self.health *= 2
			self.dropRate += 1
		elif self.adjective == 2: #Swift
			self.speed *= 2
		
		elif self.adjective == 3: #Stalking
			self.moveThroughDoors = True
			self.dropRate += 1
		
		elif self.adjective == 4: #Perceptive
			self.chase = True
			self.spriteList.append(self.perceptive_sprite)
		
		elif self.adjective == 5: #Deadly
			self.damage *= 2
			self.dropRate += 1 
			
		elif self.adjective == 6: #Bloated
			self.attack = "exploding"
			self.damage *= 2
		
		elif self.adjective == 7: #Friendly
			self.damage *= 0.5
			self.spriteList.append(self.friendly_sprite)
			
		elif self.adjective == 8: #Deranged
			self.canChase = False
		
		elif self.adjective == 9: #Cowardly
			self.canChase = False
			self.flee = True
		
		elif self.adjective == 10: #Zombified
			self.speed /= 2
			self.health *= 2
		
		elif self.adjective == 11: #Slimy
			self.hasPlayerEffect = True
			self.playerEffect = "slimy"
		
		elif self.adjective == 12: #Rich
			self.dropRate += 3
			self.spriteList.append(self.rich_sprite)
			
		elif self.adjective == 13: #Poor
			self.dropRate -= .5
			
		elif self.adjective == 14: #Ugly
			pass #just a descriptor
			
		elif self.adjective == 15: #Barbaric
			pass #just a descriptor
			
		else:
			pass # TODO: log
			
		
	def getNounTraits(self):
		"""These need to be balance tested to achieve better
		drop rates, health and damage modifiers so that 
		they can easily change the pace of the game and it isn't
		just retexturing the enemies"""
		
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
			self.size *= 2
			self.damage *= 1.5
			self.health *= 2
			self.dropRate *= 2
		elif self.noun == 10: #Goblin
			self.color = Display.GOBLINGREEN
		else:
			pass # TODO: log
		
	def getVerbTraits(self):
		#COME up with better and more verbs...
		#balance required
		if self.verb == 0: #Fighting
			self.chase = True
			self.damage += 1
		
		elif self.verb == 1: #Slithering
			self.speed -= 1
			
		elif self.verb == 2: #Polluting
			self.verbAnimSpriteObj = SpriteAnimation.SpriteAnimation(self.polluting_sprite, 10)
			self.attack = "poision"
		
		elif self.verb == 3: #Disgusting
			self.verbAnimSpriteObj = SpriteAnimation.SpriteAnimation(self.disgusting_sprite, 10)
			pass #Player fear level?	

		else:
			pass # TODO: log
			
			
	def updateName(self):
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))	
	
	def drawSelf(self):
		if self.drawDifferent:
			if self.noun == 1: #Swarm
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x+5, self.y-5), self.size/5)	#maybe change these
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x+5, self.y+5), self.size/5)	#to be random
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size/5)		#between 1-5
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x-5, self.y+5), self.size/5)	#for swarm movement
				pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x-5, self.y-5), self.size/5)
		else:
			pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x + self.size/2, self.y + self.size/2), self.size/2)
			pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (self.x, self.y), (self.weaponx, self.weapony), 1)
			for sprite in self.spriteList:
				Display.DISPLAYSURF.blit(pygame.transform.scale(sprite, (self.size, self.size)), pygame.Rect(self.x, self.y, self.size, self.size))	
			# draw verb animation
			if self.verbAnimSpriteObj:
				self.verbAnimSpriteObj.update(self.x - self.size/2, self.y - self.size/2, False, 0)
				self.verbAnimSpriteObj.update(self.x + self.size/2, self.y - self.size/2, True, 0)

		Display.DISPLAYSURF.blit(self.text, (self.x - self.size*2, (self.y - self.size*1.5)))

	def collision(self, obj):
		"""distance formula"""
		if math.sqrt(pow(self.x - obj.x, 2) + pow(self.y - obj.y, 2)) <= self.range:
			return True

	"""Written so that the Enemy may chase any object, not just the player
		in doing so, we allow them to chase objects, perhaps chests or loot
		they can destroy before the enemy is there? Also, if we want to implement
		friendlies, this is a start"""
	def chaseObj(self, obj):
		self.shouldFlankPlayer()
		if self.chase and self.shouldFlank == False:
			#if not self.collision(obj):
			if obj.x > self.x: #Move right
				self.x += self.speed
				self.weaponx = self.x + self.range
			if obj.x < self.x: #Move left
				self.x -= self.speed
				self.weaponx = self.x - self.range
			if obj.y > self.y: #Move down
				self.y += self.speed
				self.weapony = self.y
			if obj.y < self.y: #Move up
				self.y -= self.speed
				self.weapony = self.y
		if self.chase and self.shouldFlank == True:
			if not self.collision(obj):
				self.flank(obj)
				
		else: #If colliding, attack!
				#EnemyCombat.attack(self, obj)
				Combat.attack(self, self.playerObj, False)

		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.moveUp = False
		#INVENTORY STUFF
		#self.inventory.printInventory()
		
	#def patrolX(startx, endx)
			
	def flank(self, obj):
		if obj.x+20 > self.x:
			self.x += self.speed
		if obj.x-20 < self.x:
			self.x -= self.speed
		if obj.y+20 > self.y:
			self.y += self.speed
		if obj.y-20 < self.y:
			self.y -= self.speed
			
	def death(self):
		functions.worldEnemiesKilled += 1
		self.isDead = True
		self.dropLoot()
		"I died"
		
	def updateStatsToCurrentWeapon(self):
		self.range += self.currentWeapon.range
		self.damage += self.currentWeapon.damage

	def drawCollider(self):
		""" This circle will be our collision box where we draw our attack from """
		pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.collisionx, self.collisiony), self.size+2, 1)
				
	def updateColliders(self):
		self.collisionx = self.x
		self.collisiony = self.y
		
	def isPlayer(self):
		return False
		
		
	def dropLoot(self):
		self.currentWeapon.dropWeapon(self.x, self.y)
		print "Dropped"
		self.inventory.dropItems()
		functions.worldCoins.append(self.coin)
		self.coin.setDrawInfo(self.inventory.coins, self.x, self.y)
		
	def shouldFlankPlayer(self):
		'''if VariableEnemy.numberOfEnemies > 2:
			chance = random.randint(1, 10)
			if chance % 9 == 0:
				self.shouldFlank = True
			else:
				self.shouldFlank = False'''
		pass
