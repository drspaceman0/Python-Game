import Enemy
import random
import pygame
import Display
import functions

class Spawnner():
	
	def __init__(self, arr):
		self.name = "GateToHELL!"
		self.container = arr
		self.counter = 0
		self.x = 400
		self.y = 400
		self.collisionx = self.x
		self.collisiony = self.y
		self.color = Display.YELLOW
		self.size = 40
		self.health = 50
		self.spawnRate = 1 # per second
		self.isDead = False
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.name, 1, (0,0,0))
			
			
	def drawSpawnner(self):
		pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size)
		Display.DISPLAYSURF.blit(self.text, (self.x - self.size-10, (self.y - self.size-20)))
			
			
	def death(self):
		self.isDead = True
		print "Dastroyed"
		
	def update(self):
		if self.health > 0:
			self.counter += 1
			if self.counter == 90:
				self.container.append(functions.spawnEnemy(self.x, self.y))
				self.counter = 0
		if self.health <= 0:
			print "Gate to hell closed!"
		
		