import pygame, sys
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
			elif event.key == K_RIGHT:
				playerObj.moveRight= True
				playerObj.direction = 'right'
			elif event.key == K_DOWN:
				playerObj.moveDown= True
				playerObj.direction = 'down'
			elif event.key == K_UP:
				playerObj.moveUp= True
				playerObj.direction = 'up'
			elif event.key == K_x:
				menuObject.activateText()
			elif event.key == K_SPACE:
				playerObj.isAttacking = True
				playerObj.attack()
			elif event.key == K_p:
				Player.hurt()	
			elif event.key == K_BACKSPACE:
				playerObj.isDead = True
			elif event.key == K_ESCAPE:
				terminate()
		elif event.type == KEYUP: # stop moving the player
			if event.key == K_LEFT:
				playerObj.moveLeft= False
			elif event.key == K_RIGHT:
				playerObj.moveRight= False
			elif event.key == K_DOWN:
				playerObj.moveDown= False
			elif event.key == K_UP:
				playerObj.moveUp= False
			elif event.key == K_a:
				bulletDir['left'] = False
			elif event.key == K_d:
				bulletDir['right'] = False
			elif event.key == K_s:
				bulletDir['down'] = False
			elif event.key == K_w:
				bulletDir['up'] = False
			elif event.key == K_SPACE:
				playerObj.isAttacking = False
				
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
