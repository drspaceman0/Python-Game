"""
Ranged Weapon Class
Player and enemies can use them
they show a reticle (small dot for now)
on their target, and fire in a straight line
"""
import pygame
import Display
import functions
import Projectile

class RangedWeapon:
	
	def __init__(self, owner):
		self.name = "Bow of suckage"
		self.isRanged = True
		self.range = 0
		self.dot = 0
		self.owner = owner
		self.damage = owner.rangeDamage+1
		self.arrows = []
		self.playerPosX = 0
		self.playerPosY = 0
		
		
	def updateDamage(self):
		self.damage = self.owner.rangeDamage+1

	@staticmethod
	def drawReticle():
		reticlePos = pygame.mouse.get_pos()
		pygame.draw.circle(Display.DISPLAYSURF, Display.WHITE, (reticlePos[0], reticlePos[1]), 10)
		
	def aimAtPlayer(self, playerObj):
		self.playerPosX = playerObj.collisionx
		self.playerPosY = playerObj.collisiony
		pygame.draw.circle(Display.DISPLAYSURF, Display.WHITE, (playerObj.collisionx, playerObj.collisiony), 10)
		
	def attackPlayer(self):
			if self.owner.arrows > 0:
				self.arrows.append(Projectile.Projectile(self.owner.x, self.owner.y, self.playerPosX, self.playerPosY, self.damage))
				self.owner.arrows -= 1
		
	def shoot(self):
		reticlePos = pygame.mouse.get_pos()
		#reticlePos = Input.get_current_pos()
		self.arrows.append(Projectile.Projectile(self.owner.x, self.owner.y, reticlePos[0], reticlePos[1], self.damage))
			
	def update(self, playerObj):
		if self.owner.isPlayer():
			self.drawReticle()
		if self.arrows:
			for arrow in self.arrows:
				if not self.owner.isPlayer():
					if functions.objCollision(arrow, playerObj):
						playerObj.health -= arrow.damage
						print "Oh no! %s takes %s damage from an arrow!" % (playerObj.name, arrow.damage)
						arrow.exists = False
				if not arrow.exists:
					self.arrows.remove(arrow)
				arrow.update()
