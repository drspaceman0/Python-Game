import Enemy
import Display
import Bullet
import random
import math
class GooEnemy(Enemy.Enemy):
	numGooEnemies = 0
	listGooEnemies = []
	
	def __init__(self, posx, posy, size):
		self.x = posx
		self.y = posy
		self.size = size
		self.health = size/4
		self.color = Display.GREEN
		self.speed = 5
		self.chase = False
		GooEnemy.numGooEnemies += 1
		GooEnemy.listGooEnemies.append(self)
		
		
	def update(self, PlayerObj):
		for gooenemy in GooEnemy.listGooEnemies:
			for bullet in Bullet.Bullet.listBullets:
				if GooEnemy.collision(gooenemy, bullet):
					bullet.delete()
					gooenemy.health-= 5
					if gooenemy.health < 0:
						gooenemy.death()
						PlayerObj.score += 1
						print "%s = Score" % (PlayerObj.score)
			if gooenemy.x >= Display.SCREEN_WIDTH or gooenemy.x <= 0 or gooenemy.y >= Display.SCREEN_HEIGHT or gooenemy.y <= 0:
				gooenemy.delete()
				continue
			#Determine if within chasing distance of player
			if abs(gooenemy.x -PlayerObj.x) < 50 or abs(gooenemy.y - PlayerObj.y) < 50 or abs(PlayerObj.x - gooenemy.x) < 50 or abs(PlayerObj.y - gooenemy.y) < 50:
				gooenemy.chase = True
			else:
				gooenemy.chase = False
			#Chase the player in the x direction
			#The random.randint part makes the enemies "twitch" more, but also bunch less
			if gooenemy.chase == True:
				if ((PlayerObj.x+20)+random.randint(-10, 10)) > gooenemy.x:
					gooenemy.x = gooenemy.x + gooenemy.speed
				if ((PlayerObj.x+20)+random.randint(-10, 10)) < gooenemy.x:
					gooenemy.x = gooenemy.x - gooenemy.speed
				#Then chase the player in the y direction
				if ((PlayerObj.y+20)+random.randint(-10, 10)) > gooenemy.y:
					gooenemy.y = gooenemy.y + gooenemy.speed
				if ((PlayerObj.y+20)+random.randint(-10, 10)) < gooenemy.y:
					gooenemy.y = gooenemy.y - gooenemy.speed
			gooenemy.drawEnemy()
			gooenemy.drainHealth(PlayerObj)
			
			
	def collision(obj1, obj2):
		if math.sqrt(pow(obj1.x - obj2.x, 2) + pow(obj1.y - obj2.y, 2)) < 30:
			return True
	
	def death(self):
		if self.size > 20:
			GooEnemy(self.x + 25, self.y+25, self.size/2)
			GooEnemy(self.x - 25, self.y-25, self.size/2)
			self.delete()
		else:
			self.delete()
			
			
	def delete(self):
		try:
			GooEnemy.numGooEnemies -= 1
			GooEnemy.listGooEnemies.remove(self)
			del self
		except ValueError:
			GooEnemy.numGooEnemies += 1
			
	def drainHealth(self, PlayerObj):
		if self.collision (PlayerObj):
			PlayerObj.health -= 1
			print "%s, player health" % (PlayerObj.health)