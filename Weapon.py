import WeaponMaker
import random
import math


#Weapon Defaults
RANGE = 20 #swing across this many pixels collide with objects in range, hurt them
DAMAGE = 1 #Base Damage dealt by weapon
EFFECT = "none"

class MeleeWeapon:
	WM = WeaponMaker.WeaponMaker()
	def __init__(self):
		self.range = RANGE
		self.damage = DAMAGE
		self.effect = EFFECT
		self.dot = 0
		self.damageUser = False
		self.damateToUser = 0
		self.originx = 0
		self.originy = 0
		self.direction = "none"
		self.adjective = random.randint(0, len(WM.lladjectives)-1)
		self.material = random.randint(0, len(WM.llmaterial)-1)
		self.noun = random.randint(0, len(WM.llnouns)-1)
		if isSpecial(dropRate) == True:
			self.verb = random.randint(0, len(WM.llverbs)-1)
	
	
	#This adds special "effects" - magic, bleed, etc. if the drop rate is above 3
	def isSpecial(dropRate = 0):
		if (random.randint(0, 18) + dropRate) > 20:
		#add some stuff about picking new adjectives and nouns and material to ensure it's good L00t!
			return True
			
	def getAdjectiveTraits():
		'''Used to retrieve the trait changes of the adjective applied'''
		if self.adjective == 0: #Tainted
			self.damageUser = True
			self.damageToUser = 1
		
		elif self.adjective == 1: #Chaotic
			self.damageUser = True
			self.damageToSelf = random.randint(0,4) #Between zero and three
			self.damage = random.randint(2, 5)
		
		#Between 2 and 11 are default values - handled in ELSE
		elif self.adjective == 12: #Rotten 
			self.effect = "poison"
			self.dot = 1
		elif self.adjective == 13: #Moldy
			self.effect = "poison"
			self.dot = 1
		elif self.adjective == 14: #Sharp
			self.effect = "bleed"
			self.dot = 1
		elif self.adjective == 15: #Ancient
			self.effect = "magic"
			self.dot = 1