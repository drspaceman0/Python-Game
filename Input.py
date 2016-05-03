import pygame, sys
from pygame.locals import *
import Game
import Player
import Bullet
import Enemy

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