import pygame
import Display
import functions
import random

class Coin():
		
	def __init__(self):
		self.value = 0
		self.size = 0
		self.collisionx = 0
		self.collisiony = 0
		self.shouldDraw = True

		
	def drawSelf(self):
		if self.shouldDraw == True:
			pygame.draw.circle(Display.DISPLAYSURF, Display.GOLD, (self.collisionx, self.collisiony), self.size)
		else:
			pass
	
	def setDrawInfo(self, value, x, y):
		self.value = value
		self.size = value*2
		self.collisionx = x+random.randint(-20,20)
		self.collisiony = y+random.randint(-20,20) 
		
	def pickup(self):
		if self.shouldDraw == True:
			functions.moveCoinFromWorldToPlayerInv(self)
			self.shouldDraw = False
		else:
			pass