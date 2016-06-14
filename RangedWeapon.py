'''Ranged Weapon Class
Player and enemies can use them
they show a reticle (small dot for now)
on their target, and fire in a straight line
'''
import pygame
import Display
import functions
import Projectile
import math 

class RangedWeapon:
	
	def __init__(self, owner):
		self.name = "Bow of suckage"
		self.isRanged = True
		self.range = 0
		self.dot = 0
		self.owner = owner
		self.damage = owner.rangeDamage+1
		self.arrows = []
		
		
	def updateDamage(self):
		self.damage = self.owner.rangeDamage+1
	
	def drawReticle(self):
		reticlePos = pygame.mouse.get_pos()
		pygame.draw.circle(Display.DISPLAYSURF, Display.RED, (reticlePos[0], reticlePos[1]), 10)
						
		
	def shoot(self):
		reticlePos = pygame.mouse.get_pos()
		self.arrows.append(Projectile.Projectile(self.owner.x, self.owner.y, reticlePos[0], reticlePos[1], self.damage))
			
	def update(self):
		self.drawReticle()
		if self.arrows:
			for arrow in self.arrows:
				if arrow.exists == False:
					self.arrows.remove(arrow)
				arrow.update()
		else:
			pass
		
	
