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
		self.dung = 0
	
	def drawReticle(self):
			pygame.draw.circle(Display.DISPLAYSURF, Display.RED, (self.target.collisionx, self.target.collisiony), 10)
	
	def cycleTargets(self, dung):
		self.dung = dung
		if self.owner.isPlayer() == True: #If the player wishes to grab a new target
			if self.dung.returnCurrentRoom().hasSpawners: #Check if there is a spawner
				if self.dung.returnCurrentRoom().enemylist: #Check if there are enemies
					self.noTarget = False
					try:
						self.target = self.dung.returnCurrentRoom().enemylist[self.numOfTarget+1] #Attempt to grab next enemy
						self.numOfTarget += 1
						print "New target acquired"
					except IndexError:
						try:
							self.target = self.dung.returnCurrentRoom().enemylist[0]
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
				if arrow.exists == False:
					self.arrows.remove(arrow)
				if self.dung.returnCurrentRoom().enemylist:
					for enemy in self.dung.returnCurrentRoom().enemylist:
						if math.sqrt(pow(arrow.x - enemy.x, 2) + pow(arrow.y - enemy.y, 2)) < 30:
							enemy.health -= self.damage
							print "%s has been hit with an arrow for %s damage!" % (enemy.name, self.damage)
							if enemy.health <= 0:
								enemy.death()
								self.cycleTargets(self.dung)
				arrow.update()
		else:
			pass
		
	
