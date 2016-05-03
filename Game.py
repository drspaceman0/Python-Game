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


	
	
def collision(obj1, obj2):
	if math.sqrt(pow(obj1.x - obj2.x, 2) + pow(obj1.y - obj2.y, 2)) < 30:
		return True	

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
	
	mySprite = SpriteAnimation.SpriteAnimation()
	myGroup = pygame.sprite.Group(mySprite)
	playerObj = Player.Player()
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
			
			
		#Hacked way to check for collision. For loops don't work the way you'd think
		countb = 0
		counte = 0
		if countb < len(Bullet.Bullet.listBullets):
			if counte < len(Enemy.Enemy.listEnemies):
				if collision(Bullet.Bullet.listBullets[countb], Enemy.Enemy.listEnemies[counte]) == True:
					Bullet.Bullet.listBullets[countb].delete()
					Enemy.Enemy.listEnemies[counte].delete()
				else:
					countb += 1
					counte += 1
		
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
				Enemy.Enemy(300, 300, 40)
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