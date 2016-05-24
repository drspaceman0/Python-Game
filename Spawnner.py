import Enemy
import random
import pygame
import Display
import functions
import Potions

class Spawnner():
	
	def __init__(self, playerObj, arr):
		self.name = "GateToHELL!"
		self.container = arr
		self.x = 400
		self.y = 400
		self.collisionx = self.x
		self.collisiony = self.y
		self.color = Display.YELLOW
		self.size = 80
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.health = 50
		self.count = 0
		self.spawnRate = 1 # per second
		self.knocksBack = False
		self.isDead = False
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
		self.playerObj = playerObj
		#self.spriteObj = 
			
			
	def drawSpawnner(self):
		pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x + self.size/2, self.y + self.size/2), self.size/2)
		Display.DISPLAYSURF.blit(self.text, (self.x - self.size/2-10, (self.y - self.size/2-20)))
			
			
	def death(self):
		p = Potions.Potion()
		p.setDrawInfo(self.x, self.y)
		p.setToHealthPotion()
		functions.worldInventory.append(p)
		self.isDead = True
		
	def update(self):
		if self.health > 0:
			if functions.gameTimer == 1:
				self.count += 1
				if self.count == 3:
					self.container.append(functions.spawnEnemy(self.playerObj, self.x, self.y))
					self.count = 0
		if self.health <= 0:
			print "Gate to hell closed!"
	
	def damageOverTime(self, playerObj):
		print "Spawner immune to DOT attacks"
		