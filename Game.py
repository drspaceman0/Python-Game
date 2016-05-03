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