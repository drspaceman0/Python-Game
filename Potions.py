import PotionLabelMaker
import random

OUTOFBOUNDS = -1 #for default value in init, check for it
WEAKPOTION = 2



NG = PotionLabelMaker.PotionLabelMaker()
class Potion:
	
	
	#This doesn't include the special ones. If we need special potions, they need to be hand "crafted"
	def __init__(self, adjective = random.randint(0, 1), type = random.randint(0, 1), skill = OUTOFBOUNDS):
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
			
		#Functions on the object	
		self.updatePotion()
	
	
	def updatePotion(self):
		if self.type == NG.types[0]:
			self.isHealth = True
			self.name = self.adjective + " potion " + self.type
	
	def setToHealthPotion(self):
		self.type = NG.types[0] #Health
		self.updatePotion()