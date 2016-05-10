import pygame, sys
from pygame.locals import *
import Game
import Player

bulletDir = {'left': False, 'right': False, 'up': False, 'down': False} 

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
			'''if event.key == K_a:
				bulletDir['left'] = True
			if event.key == K_d:
				bulletDir['right'] = True
			if event.key == K_s:
				bulletDir['down'] = True
			if event.key == K_w:
				bulletDir['up'] = True
			'''
			if event.key == K_SPACE:
				Player.attack()
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
			if event.key == K_a:
				bulletDir['left'] = False
			if event.key == K_d:
				bulletDir['right'] = False
			if event.key == K_s:
				bulletDir['down'] = False
			if event.key == K_w:
				bulletDir['up'] = False
	updateBullets(playerObj)

def updateBullets(playerObj):
	if bulletDir['left']:
		Bullet.Bullet(playerObj, 'left')
	if bulletDir['right']:
		Bullet.Bullet(playerObj, 'right')
	if bulletDir['up']:
		Bullet.Bullet(playerObj, 'up')
	if bulletDir['down']:
		Bullet.Bullet(playerObj, 'down')
				
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