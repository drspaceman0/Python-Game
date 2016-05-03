'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys
import math
import random
from pygame.locals import *
import Bullet
import Enemy
import Display


# player variables
PLAYER_X = 10
PLAYER_Y = 10
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
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
		self.color = Display.RED
		self.spriteList = []
	
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
		self.spriteList.update(self.x, self.y)
		self.spriteList.draw(Display.DISPLAYSURF)
		
	def updateSpriteList(self, sprites):
		self.spriteList = sprites
	
	

		
		
def load_image(name):
    image = pygame.image.load(name)
    return image

# http://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
class Sprite(pygame.sprite.Sprite):

    def __init__(self):
		super(Sprite, self).__init__()
		self.counter = 0
		self.images = []
		self.images.append(load_image('images\player_idle1.png'))
		self.images.append(load_image('images\player_idle2.png'))
		# assuming both images are 64x64 pixels

		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self, x, y):
		self.counter += 1 
		self.rect = pygame.Rect(x, y, 64, 64) 
		if self.counter > 10: # after ten clicks switch sprites
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
			self.image = self.images[self.index]
#		
# START GAME
#	
def main():
	global FPSCLOCK, DISPLAYSURF, FPS
	PLAYER_X = 10
	PLAYER_Y = 10 
	while True:
		runGame()		
	
def runGame():
	
	mySprite = Sprite()
	myGroup = pygame.sprite.Group(mySprite)
	playerObj = Player()
	playerObj.updateSpriteList(myGroup)
	
	while True:
		Display.DISPLAYSURF.fill(Display.WHITE)
		
		# check for key input
		checkForInputs(playerObj)
				 
		# update player position
		playerObj.movePlayer()
		
		# update bullets if any exist
		if len(Bullet.Bullet.listBullets) > 0:
			Bullet.Bullet.update(Bullet.Bullet.listBullets[0])
		
		# update enemies if any exist
		if len(Enemy.Enemy.listEnemies) > 0:
			Enemy.Enemy.update(Enemy.Enemy.listEnemies[0], playerObj)
			
		# Bullet vs Enemy collision
		if len(Enemy.Enemy.listEnemies) > 0:
			Enemy.Enemy.bulletCollide(Enemy.Enemy.listEnemies[0], Bullet.Bullet.listBullets)
			
		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
#
#	END GAME
#

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
				Bullet.Bullet(playerObj, 'left')
			if event.key == K_d:
				Bullet.Bullet(playerObj, 'right')
			if event.key == K_s:
				Bullet.Bullet(playerObj, 'down')
			if event.key == K_w:
				Bullet.Bullet(playerObj, 'up')
			if event.key == K_p:
				Enemy.Enemy(400, 400, 40)
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
	if playerObj.moveRight and playerObj.x >= Display.SCREEN_WIDTH:
		playerObj.x = 0
	if playerObj.moveLeft and playerObj.x <= 0 - PLAYER_WIDTH:
		playerObj.x = Display.SCREEN_WIDTH
	if playerObj.moveDown and playerObj.y >= Display.SCREEN_HEIGHT:
		playerObj.y = 0
	if playerObj.moveUp and playerObj.y <= 0 - PLAYER_HEIGHT:
		playerObj.y = Display.SCREEN_HEIGHT
		
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