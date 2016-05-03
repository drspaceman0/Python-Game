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
import SpriteAnimation
import Player
import Input

				 

	
<<<<<<< HEAD
=======
	

		
		
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
>>>>>>> 8c0a8f5fd8073ade00b9cffc4bba49d1d0785ed9
#		
# START GAME
#	
def main():
	while True:
		runGame()		
	
def runGame():
	
	mySprite = SpriteAnimation.SpriteAnimation()
	myGroup = pygame.sprite.Group(mySprite)
	playerObj = Player.Player()
	playerObj.updateSpriteList(myGroup)
	
	while True:
		Display.DISPLAYSURF.fill(Display.WHITE)
		
		# check for key input
		Input.checkForInputs(playerObj)
				 
		# update player position
		playerObj.movePlayer()
		
		# update bullets if any exist
		if len(Bullet.Bullet.listBullets) > 0:
			Bullet.Bullet.update(Bullet.Bullet.listBullets[0])
		
		# update enemies if any exist
		if len(Enemy.Enemy.listEnemies) > 0:
			Enemy.Enemy.update(Enemy.Enemy.listEnemies[0], playerObj)
		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
#
#	END GAME
#

if __name__ == '__main__':
	main()