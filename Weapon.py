import WeaponLabelMaker
import random
import math
import Display
import pygame

#Weapon Defaults
RANGE = 20 #swing across this many pixels collide with objects in range, hurt them
DAMAGE = 1 #Base Damage dealt by weapon
EFFECT = "none"
WM = WeaponLabelMaker.WeaponLabelMaker()

class MeleeWeapon:
	def __init__(self):
		self.range = RANGE
		self.damage = DAMAGE
		self.hasEffect = False
		self.effect = EFFECT
		self.speed = 0
		self.dot = 0
		self.damageUser = False
		self.damateToUser = 0
		self.originx = 0
		self.originy = 0
		self.direction = "none"
		self.adjective = random.randint(0, len(WM.lladjectives)-1)
		self.material = random.randint(0, len(WM.llmaterial)-1)
		self.noun = random.randint(0, len(WM.llnouns)-1)
		self.hasSpecial = False
		if self.isSpecial():
			self.hasSpecial = True
			self.verb = random.randint(0, len(WM.llverbs)-1)
			self.name = WM.lladjectives[self.adjective] + " " + WM.llmaterial[self.material] + " " + WM.llnouns[self.noun] + " " + WM.llverbs[self.verb]
		else:
			self.name = WM.lladjectives[self.adjective] + " " + WM.llmaterial[self.material] + " " + WM.llnouns[self.noun]
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
	
	
	#This adds special "effects" - magic, bleed, etc. if the drop rate is above 3
	def isSpecial(self, dropRate = 0):
		if (random.randint(0, 18) + dropRate) > 20:
		#add some stuff about picking new adjectives and nouns and material to ensure it's good L00t!
			return True
			
	def getAdjectiveTraits(self):
		'''Used to retrieve the trait changes of the adjective applied'''
		if self.adjective == 0: #Tainted
			self.damageUser = True
			self.damageToUser = 1
		
		elif self.adjective == 1: #Chaotic
			self.damageUser = True
			self.damageToSelf = random.randint(0,4) #Between zero and three
			self.damage = self.damage + random.randint(2, 5)
		
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
			
		else:
			pass #Default values are fine
	
	def getNounTraits(self):
		if self.noun == 0: #Straightsword
			pass #default
		elif self.noun == 1: #Axe
			self.speed -= 1
			self.damage += 1
		
		elif self.noun == 2:#dagger
			self.range /= 2
			self.damage /= 2
			self.speed += 3
			self.hasEffect = True
			self.effect = "bleed"
			self.dot = .5
		
		elif self.noun == 3: #mace
			self.damage += 2 
			self.speed -= 1 
			
		elif self.noun == 4: #Katana
			self.damage += 1
			self.speed += 1
			self.hasEffect = True
			self.effect = "bleed"
			self.dot = 1 
		
		elif self.noun == 5: #Broadsword
			self.damage += 1 
			self.speed -= 1 
			
		elif self.noun == 6: #Longsword
			self.range += 2 
			self.speed -= 1 
		
		elif self.noun == 7: #Cudgel
			self.damage += 2
			
		else: #defaults
			pass
	
	def getMaterialTraits(self):
		if self.material == 0: # Wood
			self.damage -= 1
			self.speed += 1 
		
		elif self.material == 2: # Iron
			self.damage += 1 
			self.speed -= 1

		elif self.material == 3: #Copper
			pass #Defaults good 
		
		elif self.material == 4: #Glass 
			self.damage += 1 
			self.hasEffect = True 
			self.effect = "bleed"
			self.dot = 0.5
		else:
			pass #Defaults 
			
	def getSpecialTraits(self):
		if self.hasSpecial:
			if self.verb == 0: #of smoldering
				self.hasEffect = True
				self.effect = "fire"
				self.dot = 1 
			
			elif self.verb == 1: #of numbing
				self.hasEffect = True 
				self.effect = "frost"
				self.dot = 1 
			
			elif self.verb == 2: #of sparking
				self.hasEffect = True
				self.effect = "electric"
				self.dot = 1
				
			elif self.verb == 3: #of mild stink (lol)
				self.hasEffect = True
				self.effect = "poison"
				self.dot = 1 
			
			else: # TODO: log when these happen to debugging
				pass #Shouldn't happen

	def printName(self):
		print "%s" % (self.name)	
	
	def dropWeapon(self, x, y):
		originx = x 
		originy = y
		
	def drawAsLoot(self):
		pygame.draw.line(Display.DISPLAYSURF, Display.BLACK, (self.originx, self.originy), (self.originx + 50, self.originy), 1)
		Display.DISPLAYSURF.blit(self.text, (self.originx -5, (self.originy)))
		
