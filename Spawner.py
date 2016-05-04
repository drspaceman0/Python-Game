import random
import math
import Enemy
import Player
import Display
MAXENEMY = 6 #for testing - not set in stone, despite being a constant. maybe by difficulty?
ENEMYSIZE = 30
EDGING = 30 #Used to account for the edge of the displaysurf so they don't delete as spawned
MULTIPLIER = 1.7 # Same as edging

class Spawner:
	maxEnemy = MAXENEMY
	def __init__(self):
		self.maxEnemy = MAXENEMY
		#self.display = Display.DISPLAYSURF
		#stuff
	
	
	def spawnQuadrant1(self): #Do I need self here?
		Enemy.Enemy(random.randint(EDGING, Display.QUADRANTX), random.randint(EDGING, Display.QUADRANTY), ENEMYSIZE)
		
	def spawnQuadrant2(self):
		Enemy.Enemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(EDGING, Display.QUADRANTY), ENEMYSIZE) #Quadrant 2
		
	def spawnQuadrant3(self):
		Enemy.Enemy(random.randint(EDGING, Display.QUADRANTX), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYSIZE) #Quadrant 3
		
	def spawnQuadrant4(self):
		Enemy.Enemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYSIZE) #Quadrant 4
	
	def overIChance(self, i):
		i+= 1
		return random.randint(1, i)
	
	def update(self, quadrant):
		if Enemy.Enemy.num_enemies < (self.maxEnemy/2):
			#If the player is in the first Quadrant
			if quadrant == 1:
				#Spawn an enemy in the other three
				if self.overIChance(3) == 3: # 1/3rd chance - randint excludes high value
					self.spawnQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnQuadrant4()
				return
			if quadrant == 2:
				if self.overIChance(3) == 3:
					self.spawnQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnQuadrant4
			if quadrant == 3:
				if self.overIChance(3) == 3:
					self.spawnQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnQuadrant4()
			if quadrant == 4:
				if self.overIChance(3) == 3:
					self.spawnQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnQuadrant3()