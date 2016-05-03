import pygame
import Display

class Bullet:
	numBullets = 0
	listBullets = []
	def __init__(self,playerObj, dir):
		self.x = playerObj.x + playerObj.width/4
		self.y = playerObj.y + playerObj.height/4
		self.width = 5
		self.height = 5
		self.color = Display.BLACK
		self.speed = 20
		self.direction = dir
		Bullet.numBullets += 1
		Bullet.listBullets.append(self)
	
	def update(self):
		for bullet in Bullet.listBullets:
			if bullet.x >= Display.SCREEN_WIDTH or bullet.x <= 0 or bullet.y >= Display.SCREEN_HEIGHT or bullet.y <= 0:
				Bullet.delete(bullet)
				continue
			# get bullet position
			if bullet.direction == 'right':
				bullet.x += bullet.speed
			if bullet.direction == 'left':
				bullet.x -= bullet.speed
			if bullet.direction == 'down':
				bullet.y += bullet.speed
			if bullet.direction == 'up':
				bullet.y -= bullet.speed
			# draw bullet
			pygame.draw.rect(Display.DISPLAYSURF, bullet.color, (bullet.x, bullet.y, bullet.width, bullet.width))

	def delete(self):
		Bullet.numBullets -= 1
		Bullet.listBullets.remove(self)
		del self