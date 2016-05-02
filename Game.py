'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys
from pygame.locals import *

# canvas variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (22, 226, 15)

# player variables
PLAYER_X = 10
PLAYER_Y = 10
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10

class Player:
	def __init__(self):
		self.x = PLAYER_X
		self.y = PLAYER_Y
		self.direction = 'right'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = RED
	
	def movePlayer(self):
		if self.moveRight:
			self.x += PLAYER_SPEED
		if self.moveDown:
			self.y += PLAYER_SPEED
		if self.moveLeft:
			self.x -= PLAYER_SPEED
		if self.moveUp:
			self.y -= PLAYER_SPEED
		# check if player needs to go to other side
		moveToOtherSide(self)
		# draw player
		pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.width, self.width))
	
	
class Bullet:
	numBullets = 0
	listBullets = []
	def __init__(self,playerObj, dir):
		self.x = playerObj.x + playerObj.width/2 - 2
		self.y = playerObj.y + playerObj.height/2 - 2
		self.width = 10
		self.height = 10
		self.color = BLACK
		self.speed = 20
		self.direction = dir
		Bullet.numBullets += 1
		Bullet.listBullets.append(self)
	
	def update(self):
		for bullet in Bullet.listBullets:
			if bullet.x >= SCREEN_WIDTH or bullet.x <= 0 or bullet.y >= SCREEN_HEIGHT or bullet.y <= 0:
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
			pygame.draw.rect(DISPLAYSURF, bullet.color, (bullet.x, bullet.y, bullet.width, bullet.width))

	def delete(self):
		Bullet.numBullets -= 1
		Bullet.listBullets.remove(self)
		del self
		
		
		
		
class Enemy:
	num_enemies = 0
	list_enemies = []
	def __init__(self, size):
		self.x = 450
		self.y = 450
		self.size = 20
		health = 10
		self.color = GREEN
		self.speed = 5
		Enemy.num_enemies += 1
		Enemy.list_enemies.append(self)
		
	def update(self, PlayerObj):
		for enemy in Enemy.list_enemies:
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
		Enemy.list_enemies.remove(self)
		del self
		
		

	

def main():
	global FPSCLOCK, DISPLAYSURF, FPS

	pygame.init()
	FPS = 30 # frames per second
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption('Game')
	PLAYER_X = 10
	PLAYER_Y = 10
	while True:
		runGame()		
	
def runGame():
	playerObj = Player()

	while True:
		DISPLAYSURF.fill(WHITE)
		
		# check for key input
		checkForInputs(playerObj)
				 
		# update player position
		playerObj.movePlayer()
		
		# update bullets if any exist
		if len(Bullet.listBullets) > 0:
			Bullet.update(Bullet.listBullets[0])
			
			
		# update enemies if any exist
		if len(Enemy.list_enemies) > 0:
			Enemy.update(Enemy.list_enemies[0], playerObj)
					
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def checkForInputs(playerObj):
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				playerObj.moveLeft= True
				playerObj.direction = 'left'
			if event.key == K_RIGHT:
				playerObj.moveRight= True
				playerObj.direction = 'right'
			if event.key == K_DOWN:
				playerObj.moveDown= True
				playerObj.direction = 'down'
			if event.key == K_UP:
				playerObj.moveUp= True
				playerObj.direction = 'up'
			if event.key == K_a:
				Bullet(playerObj, 'left')
			if event.key == K_d:
				Bullet(playerObj, 'right')
			if event.key == K_s:
				Bullet(playerObj, 'down')
			if event.key == K_w:
				Bullet(playerObj, 'up')
			if event.key == K_p:
				Enemy(4)
			if event.key == K_ESCAPE:
				terminate()
		elif event.type == KEYUP:
			# stop moving the player
			if event.key == K_LEFT:
				playerObj.moveLeft= False
			if event.key == K_RIGHT:
				playerObj.moveRight= False
			if event.key == K_DOWN:
				playerObj.moveDown= False
			if event.key == K_UP:
				playerObj.moveUp= False
		
def moveToOtherSide(playerObj):
	if playerObj.moveRight and playerObj.x >= SCREEN_WIDTH:
		playerObj.x = 0
	if playerObj.moveLeft and playerObj.x <= 0 - PLAYER_WIDTH:
		playerObj.x = SCREEN_WIDTH
	if playerObj.moveDown and playerObj.y >= SCREEN_HEIGHT:
		playerObj.y = 0
	if playerObj.moveUp and playerObj.y <= 0 - PLAYER_HEIGHT:
		playerObj.y = SCREEN_HEIGHT
		
def terminate():
	pygame.quit()
	sys.exit()

def checkForQuit():
     for event in pygame.event.get(QUIT): # get all the QUIT events
         terminate() # terminate if any QUIT events are present
     for event in pygame.event.get(KEYUP): # get all the KEYUP events
         if event.key == K_ESCAPE:
             terminate() # terminate if the KEYUP event was for the Esc key
         pygame.event.post(event) # put the other KEYUP event objects back
		 
if __name__ == '__main__':
	main()