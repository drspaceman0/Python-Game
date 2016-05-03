import pygame
import Display
import Bullet


class Enemy:
	num_enemies = 0
	listEnemies = []
	def __init__(self, posx, posy, size):
		self.x = posx
		self.y = posy
		self.size = size
		health = size/2
		self.color = Display.GREEN
		self.speed = 5
		Enemy.num_enemies += 1
		Enemy.listEnemies.append(self)
		
	def update(self, PlayerObj):
		for enemy in Enemy.listEnemies:
			for bullet in Bullet.Bullet.listBullets:
				if bullet.collision(enemy.x, enemy.y):
					bullet.delete()
					enemy.delete()
			if enemy.x >= Display.SCREEN_WIDTH or enemy.x <= 0 or enemy.y >= Display.SCREEN_HEIGHT or enemy.y <= 0:
				Enemy.delete(enemy)
				continue
			#Chase the player in the x direction
			if (PlayerObj.x > enemy.x):
				enemy.x = enemy.x + enemy.speed
			if (PlayerObj.x < enemy.x):
				enemy.x = enemy.x - enemy.speed
			#Then chase the player in the y direction
			if (PlayerObj.y > enemy.y):
				enemy.y = enemy.y + enemy.speed
			if (PlayerObj.y < enemy.y):
				enemy.y = enemy.y - enemy.speed
			#Draw the enemies	
			pygame.draw.circle(Display.DISPLAYSURF, Display.GREEN, (enemy.x, enemy.y), enemy.size)
				
				
	def delete(self):
		Enemy.num_enemies -= 1
		Enemy.listEnemies.remove(self)
		del self
		
