import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (22, 226, 15)

class Enemy:
	num_enemies = 0
	listEnemies = []
	def __init__(self, size):
		self.x = 450
		self.y = 450
		self.size = size
		health = 10
		self.color = GREEN
		self.speed = 5
		Enemy.num_enemies += 1
		Enemy.listEnemies.append(self)
		
	def update(self, PlayerObj):
		for enemy in Enemy.listEnemies:
			if enemy.x >= SCREEN_WIDTH or enemy.x <= 0 or enemy.y >= SCREEN_HEIGHT or enemy.y <= 0:
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
			pygame.draw.circle(DISPLAYSURF, GREEN, (enemy.x, enemy.y), enemy.size)
				
				
	def delete(self):
		Enemy.num_enemies -= 1
		Enemy.listEnemies.remove(self)
		del self