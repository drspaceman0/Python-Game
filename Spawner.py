import random
import math
import Enemy
import Player
import Display
import GooEnemy
import BrickEnemy
MAXENEMY = 10 #for testing - not set in stone, despite being a constant. maybe by difficulty?
ENEMYGOOSIZE = 30
ENEMYBRICKSIZE = 20
EDGING = 30 #Used to account for the edge of the displaysurf so they don't delete as spawned
MULTIPLIER = 1.7 # Same as edging

class Spawner:
	def __init__(self):
		self.maxGooEnemy = MAXENEMY
		self.maxBrickEnemy = MAXENEMY/2
		#self.display = Display.DISPLAYSURF
		#stuff
	
	
	def spawnGooQuadrant1(self): #Do I need self here?
		GooEnemy.GooEnemy(random.randint(EDGING, Display.QUADRANTX), random.randint(EDGING, Display.QUADRANTY), ENEMYGOOSIZE)
		
	def spawnGooQuadrant2(self):
		GooEnemy.GooEnemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(EDGING, Display.QUADRANTY), ENEMYGOOSIZE) #Quadrant 2
		
	def spawnGooQuadrant3(self):
		GooEnemy.GooEnemy(random.randint(EDGING, Display.QUADRANTX), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYGOOSIZE) #Quadrant 3
		
	def spawnGooQuadrant4(self):
		GooEnemy.GooEnemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYGOOSIZE) #Quadrant 4



	def spawnBrickQuadrant1(self): #Do I need self here?
		BrickEnemy.BrickEnemy(random.randint(EDGING, Display.QUADRANTX), random.randint(EDGING, Display.QUADRANTY), ENEMYBRICKSIZE)
		
	def spawnBrickQuadrant2(self):
		BrickEnemy.BrickEnemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(EDGING, Display.QUADRANTY), ENEMYBRICKSIZE) #Quadrant 2
		
	def spawnBrickQuadrant3(self):
		BrickEnemy.BrickEnemy(random.randint(EDGING, Display.QUADRANTX), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYBRICKSIZE) #Quadrant 3
		
	def spawnBrickQuadrant4(self):
		BrickEnemy.BrickEnemy(random.randint(Display.QUADRANTX, Display.QUADRANTX*MULTIPLIER), random.randint(Display.QUADRANTY, Display.QUADRANTY*MULTIPLIER), ENEMYBRICKSIZE) #Quadrant 4
	



		
	def overIChance(self, i):
		i+= 1
		return random.randint(1, i)
	
	def updateGoo(self, quadrant):
		if GooEnemy.GooEnemy.numGooEnemies < (self.maxGooEnemy/2):
			#If the player is in the first Quadrant
			if quadrant == 1:
				#Spawn an enemy in the other three
				if self.overIChance(3) == 3: # 1/3rd chance - randint excludes high value
					self.spawnGooQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant4()
				return
			if quadrant == 2:
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant4
			if quadrant == 3:
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant4()
			if quadrant == 4:
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnGooQuadrant3()
					
					
					
	def updateBrick(self, quadrant):
		if BrickEnemy.BrickEnemy.numBrickEnemies < (self.maxBrickEnemy/2):
			#If the player is in the first Quadrant
			if quadrant == 1:
				#Spawn an enemy in the other three
				if self.overIChance(3) == 3: # 1/3rd chance - randint excludes high value
					self.spawnBrickQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant4()
				return
			if quadrant == 2:
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant3()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant4
			if quadrant == 3:
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant4()
			if quadrant == 4:
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant1()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant2()
				if self.overIChance(3) == 3:
					self.spawnBrickQuadrant3()
					