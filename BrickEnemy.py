import Enemy
import Display
import Bullet
import random
import math
import pygame
MINSIZE = 20

class BrickEnemy(Enemy.Enemy):
	numBrickEnemies = 0
	listBrickEnemies = []
	
	def __init__(self, posx, posy, size):
		self.x = posx
		self.y = posy
		self.size = size
		self.health = 1
		self.color = Display.RED
		self.speed = 8
		self.chase = False
		BrickEnemy.numBrickEnemies += 1
		BrickEnemy.listBrickEnemies.append(self)
		
		
	def update(self, PlayerObj):
		for brickenemy in BrickEnemy.listBrickEnemies:
			for bullet in Bullet.Bullet.listBullets:
				if BrickEnemy.collision(brickenemy, bullet):
					bullet.delete()
					brickenemy.health-= PlayerObj.damage
					if brickenemy.health < 0:
						brickenemy.death()
						PlayerObj.score += 1
						print "%s = Score" % (PlayerObj.score)
			if brickenemy.x >= Display.SCREEN_WIDTH or brickenemy.x <= 0 or brickenemy.y >= Display.SCREEN_HEIGHT or brickenemy.y <= 0:
				brickenemy.delete()
				continue
			#Determine if within chasing distance of player
			if abs(brickenemy.x -PlayerObj.x) < 100 or abs(brickenemy.y - PlayerObj.y) < 100 or abs(PlayerObj.x - brickenemy.x) < 100 or abs(PlayerObj.y - brickenemy.y) < 100:
				brickenemy.chase = True
			else:
				brickenemy.chase = False
			#Chase the player in the x direction
			#The random.randint part makes the enemies "twitch" more, but also bunch less
			if brickenemy.chase == True:
				if ((PlayerObj.x+20)+random.randint(-10, 10)) > brickenemy.x:
					brickenemy.x = brickenemy.x + brickenemy.speed
				if ((PlayerObj.x+20)+random.randint(-10, 10)) < brickenemy.x:
					brickenemy.x = brickenemy.x - brickenemy.speed
				#Then chase the player in the y direction
				if ((PlayerObj.y+20)+random.randint(-10, 10)) > brickenemy.y:
					brickenemy.y = brickenemy.y + brickenemy.speed
				if ((PlayerObj.y+20)+random.randint(-10, 10)) < brickenemy.y:
					brickenemy.y = brickenemy.y - brickenemy.speed
			brickenemy.drawEnemy()
			brickenemy.drainHealth(PlayerObj)
			
			
	def collision(obj1, obj2):
		if math.sqrt(pow(obj1.x - obj2.x, 2) + pow(obj1.y - obj2.y, 2)) < 30:
			return True
	
	def drawEnemy(self):
		#Draw the enemies	
		pygame.draw.rect(Display.DISPLAYSURF, self.color, (self.x, self.y, self.size, self.size))
	
	def death(self):
		if self.size > 20:
			BrickEnemy(self.x + 25, self.y+25, self.size/2)
			BrickEnemy(self.x - 25, self.y-25, self.size/2)
			self.delete()
		else:
			self.delete()
			
			
	def delete(self):
		try:
			BrickEnemy.numBrickEnemies -= 1
			BrickEnemy.listBrickEnemies.remove(self)
			del self
		except ValueError:
			BrickEnemy.numBrickEnemies += 1
			
	def drainHealth(self, PlayerObj):
		if self.collision (PlayerObj):
			PlayerObj.health -= 1
			print "%s, player health" % (PlayerObj.health)