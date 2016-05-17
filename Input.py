import pygame
import sys
from pygame.locals import *
import Game
import Player

# TODO: joystick

def checkForInputs(playerObj, menuObject):
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
			if event.key == K_x:
				menuObject.activateText()
			if event.key == K_SPACE:
				playerObj.isAttacking = True
				playerObj.attack = True
			if event.key == K_p:
				Player.hurt()	
			if event.key == K_BACKSPACE:
				playerObj.isDead = True
			if event.key == K_ESCAPE:
				terminate()
		elif event.type == KEYUP: # stop moving the player
			if event.key == K_LEFT:
				playerObj.moveLeft= False
			if event.key == K_RIGHT:
				playerObj.moveRight= False
			if event.key == K_DOWN:
				playerObj.moveDown= False
			if event.key == K_UP:
				playerObj.moveUp= False
			if event.key == K_SPACE:
				playerObj.isAttacking = False
				
def terminate():
	pygame.quit()
	sys.exit()

def checkForQuit():
	for event in pygame.event.get(pygame.QUIT): # get all the QUIT events
		terminate() # terminate if any QUIT events are present
	for event in pygame.event.get(pygame.KEYUP): # get all the KEYUP events
		if event.key == pygame.K_ESCAPE:
			terminate() # terminate if the KEYUP event was for the Esc key
		pygame.event.post(event) # put the other KEYUP event objects back
