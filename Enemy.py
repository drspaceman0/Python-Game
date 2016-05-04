import pygame
import Display
import Bullet
import math
import Player
import random



class Enemy:
	num_enemies = 0
	listEnemies = []
	def __init__(self, posx, posy, size):
		self.x = posx
		self.y = posy
		self.size = size
		self.health = size/4
		self.color = Display.GREEN
		self.speed = 5
		self.chase = False
		Enemy.num_enemies += 1
		Enemy.listEnemies.append(self)
		
	def update(self, PlayerObj):
		for enemy in Enemy.listEnemies:
			for bullet in Bullet.Bullet.listBullets:
				if Enemy.collision(enemy, bullet):
					bullet.delete()
					enemy.health-= 5
					if enemy.health < 0:
						enemy.death()
						PlayerObj.score += 1
						print "%s = Score" % (PlayerObj.score)
			if enemy.x >= Display.SCREEN_WIDTH or enemy.x <= 0 or enemy.y >= Display.SCREEN_HEIGHT or enemy.y <= 0:
				Enemy.delete(enemy)
				continue
			#Determine if within chasing distance of player
			if abs(enemy.x -PlayerObj.x) < 50 or abs(enemy.y - PlayerObj.y) < 50 or abs(PlayerObj.x - enemy.x) < 50 or abs(PlayerObj.y - enemy.y) < 50:
				enemy.chase = True
			else:
				enemy.chase = False
			#Chase the player in the x direction
			#The random.randint part makes the enemies "twitch" more, but also bunch less
			if enemy.chase == True:
				if ((PlayerObj.x+20)+random.randint(-10, 10)) > enemy.x:
					enemy.x = enemy.x + enemy.speed
				if ((PlayerObj.x+20)+random.randint(-10, 10)) < enemy.x:
					enemy.x = enemy.x - enemy.speed
				#Then chase the player in the y direction
				if ((PlayerObj.y+20)+random.randint(-10, 10)) > enemy.y:
					enemy.y = enemy.y + enemy.speed
				if ((PlayerObj.y+20)+random.randint(-10, 10)) < enemy.y:
					enemy.y = enemy.y - enemy.speed
				#Draw the enemies	
			pygame.draw.circle(Display.DISPLAYSURF, Display.GREEN, (enemy.x, enemy.y), enemy.size)
			
	
	def death(self):
		if self.size > 20:
			Enemy(self.x + 25, self.y+25, self.size/2)
			Enemy(self.x - 25, self.y-25, self.size/2)
			self.delete()
		else:
			self.delete()
			
			
	def collision(obj1, obj2):
		if math.sqrt(pow(obj1.x - obj2.x, 2) + pow(obj1.y - obj2.y, 2)) < 30:
			return True
		
				
	'''			
	def bulletCollide(self, bulletlist):
		for enemy in Enemy.listEnemies:
			for Bullet.Bullet.bullet in bulletlist:
				if Enemy.collision(enemy, Bullet.Bullet.bullet):
					Bullet.Bullet.bullet.delete()
					enemy.health -= 5
				if enemy.health <= 0:
					enemy.death()'''
	
	def delete(self):
		Enemy.num_enemies -= 1
		try:
			Enemy.listEnemies.remove(self)
		except ValueError:
			print "Delete enemy error"
		del self
		
