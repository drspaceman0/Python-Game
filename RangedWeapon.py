'''Ranged Weapon Class
Player and enemies can use them
they show a reticle (small dot for now)
on their target, and fire in a straight line
'''
import pygame
import Display
import functions
import Projectile

class RangedWeapon:
	
	def __init__(self, owner):
		name = "Bow of stink"
		self.isRanged = True
		self.range = 0
		self.dot = 0
		self.currentTarget = 0
		self.owner = owner
		self.damage = owner.rangeDamage+1
		self.target = 0
		self.arrows = []
		self.noTarget = True
		self.numOfTarget = 0
	
	def drawReticle(self):
			pygame.draw.circle(Display.DISPLAYSURF, Display.RED, (self.target.collisionx, self.target.collisiony), 10)
	
	def cycleTargets(self, dung):
		if self.owner.isPlayer() == True: #If the player wishes to grab a new target
			if dung.returnCurrentRoom().hasSpawners: #Check if there is a spawner
				if dung.returnCurrentRoom().enemylist: #Check if there are enemies
					self.noTarget = False
					try:
						self.target = dung.returnCurrentRoom().enemylist[self.numOfTarget+1] #Attempt to grab next enemy
						self.numOfTarget += 1
						print "New target acquired"
					except IndexError:
						try:
							self.target = dung.returnCurrentRoom().enemylist[0]
							self.numOfTarget = 0
							print "New target acquired"
						except IndexError:
							print "No enemies to target"
			else:
				self.noTarget = True
						
		
	def shoot(self):
		if self.noTarget == False:
			self.arrows.append(Projectile.Projectile(self.owner.x, self.owner.y, self.target.x, self.target.y, self.damage))	
		else:
			self.arrows.append(Projectile.Projectile(self.owner.x, self.owner.y, 400, 400, self.damage))
			
	def update(self):
		if self.noTarget == False:
			self.drawReticle()
		if self.arrows:
			for arrow in self.arrows:
				arrow.update()
		else:
			pass
		
	
