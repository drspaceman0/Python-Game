'''projectile class for arrows and the like (throwing knives?
 which spawns at an x and y coordinate, and quickly moves to an end
 x and y coordinate'''
import pygame
import Display
import math
 
SPEED = 10
 
class Projectile:
	
	def __init__(self, x, y, targetX, targetY, damage):
		self.x = x
		self.y = y
		self.endX = targetX
		self.endY = targetY
		self.speed = SPEED
		self.damage = damage
		self.exists = True
		
	def move(self):
		if self.x < self.endX:
			self.x += self.speed
		if self.x > self.endX:
			self.x -= self.speed
		if self.y < self.endY:
			self.y += self.speed
		if self.y > self.endY:
			self.y -= self.speed
			
		if math.sqrt(pow(self.x - self.endX, 2) + pow(self.y - self.endY, 2)) < 20:
			self.exists = False
			
	def collide(self):
		pass #for now
		
	def draw(self):
		pygame.draw.line(Display.DISPLAYSURF, Display.BLACK, (self.x, self.y), (self.x+10, self.y), 1)
		
		
	def update(self):
		if self.exists:
			self.draw()
			self.move()
			self.collide()