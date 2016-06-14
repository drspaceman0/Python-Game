'''projectile class for arrows and the like (throwing knives?
 which spawns at an x and y coordinate, and quickly moves to an end
 x and y coordinate'''
import pygame
import Display
import math
 
SPEED = 10
 
class Projectile:
	
	def __init__(self, x, y, targetX, targetY, damage):
		self.collisionx = x
		self.collisiony = y
		self.endX = targetX
		self.endY = targetY
		self.speed = SPEED
		self.damage = damage
		self.exists = True
		self.range = 30 # Distance in collision checking.. Is 30, as the arrow dissapears at 20 from end point 
		
	def move(self):
		if self.collisionx < self.endX:
			self.collisionx += self.speed
		if self.collisionx > self.endX:
			self.collisionx -= self.speed
		if self.collisiony < self.endY:
			self.collisiony += self.speed
		if self.collisiony > self.endY:
			self.collisiony -= self.speed
			
		if math.sqrt(pow(self.collisionx - self.endX, 2) + pow(self.collisiony - self.endY, 2)) < 20:
			self.exists = False
			
			
	def draw(self):
		pygame.draw.line(Display.DISPLAYSURF, Display.BLACK, (self.collisionx, self.collisiony), (self.collisionx+10, self.collisiony), 2)
		
		
	def update(self):
		if self.exists:
			self.draw()
			self.move()