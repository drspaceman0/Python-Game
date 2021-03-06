import PotionLabelMaker
import random
import functions
import pygame
import Display

OUTOFBOUNDS = -1 #for default value in init, check for it
WEAKPOTION = 2



NG = PotionLabelMaker.PotionLabelMaker()
class Potion:
	
	
	#This doesn't include the special ones. If we need special potions, they need to be hand "crafted"
	def __init__(self, adjective = random.randint(0, 1), type = random.randint(0, 1), skill = OUTOFBOUNDS):
		self.collisionx = 0
		self.collisiony = 0
		self.shouldDraw = True
		self.potionStrength = WEAKPOTION
		self.isHealth = False
		self.isStamina = False
		#add more
		self.adjective = NG.adjectives[adjective]
		self.type = NG.types[type]
		self.skill = skill
		self.name = self.adjective + " potion " + self.type
		if(self.skill != OUTOFBOUNDS):
			self.skill = skill
		self.size = 10
			
		#Functions on the object	
		self.updatePotion()
	
	
	def updatePotion(self):
		if self.type == NG.types[0]:
			self.isHealth = True
			self.name = self.adjective + " potion " + self.type
	
	def setToHealthPotion(self):
		self.type = NG.types[0] #Health
		self.updatePotion()
		
	def drawAsLoot(self):
		pygame.draw.circle(Display.DISPLAYSURF, Display.RED, (self.collisionx, self.collisiony), self.size)
	
	def setDrawInfo(self, x, y):
		self.collisionx = x+random.randint(-20,20)
		self.collisiony = y+random.randint(-20,20)
		
	def pickup(self):
		if self.shouldDraw == True:
			print "acquired potion!"
			functions.movePotionFromWorldToPlayerInv(self)
			self.shouldDraw = False
		else:
			pass
		
		