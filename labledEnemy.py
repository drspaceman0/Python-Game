import Game
import pygame
import Display
import random


class labledEnemy:
	numLabledEnemies = 0
	listLabledEnemies = []

	def __init__(self):
		self.x = 500
		self.y = 500
		self.label = "Viscous Goo"
		self.speed = 2
		self.color = Display.BLACK
		self.size = 20
		self.font = pygame.font.SysFont("monospace", 12)
		self.text = self.font.render(self.label, 1, (0,0,0))
		
	def update(self, playerObj):
		if ((playerObj.x+20)+random.randint(-10, 10)) > self.x:
			self.x = self.x + self.speed
		if ((playerObj.x+20)+random.randint(-10, 10)) < self.x:
			self.x = self.x - self.speed
		if ((playerObj.y+20)+random.randint(-10, 10)) > self.y:
			self.y = self.y + self.speed
		if ((playerObj.y+20)+random.randint(-10, 10)) < self.y:
			self.y = self.y - self.speed
		self.draw()
			
			
	def draw(self):	
		pygame.draw.circle(Display.DISPLAYSURF, self.color, (self.x, self.y), self.size)
		Display.DISPLAYSURF.blit(self.text, (self.x - self.size*1.5, (self.y - self.size*1.5)))
		
