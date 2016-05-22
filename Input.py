""" User input handling """

import pygame
from pygame.locals import *

import sys
import logging

# TODO: remapping of keybinds
# This could be accomplished with genericized actions that map to the actual key
# e.g event.key == moveleft, with moveleft being pygame.K_LEFT or whatever user sets

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
			if event.key == K_e:
				playerObj.pickup = True
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
			if event.key == K_e:
				playerObj.pickup = False
			if event.key == K_q:
				playerObj.usePotion()
		elif event.type == pygame.JOYAXISMOTION:
			print "axis motion"
		elif event.type == pygame.JOYBALLMOTION:
			print "ball motion"
		elif event.type == pygame.JOYHATMOTION:
			print "hat motion"
		elif event.type == pygame.JOYBUTTONUP:
			print "button up"
		elif event.type == pygame.JOYBUTTONDOWN:
			print "button down"

def terminate():
	logging.info('Quit game')
	pygame.quit()
	sys.exit()

def listControllers(controllers):
	print "Controller names:"
	for controller in controllers:
		print "\t", controller.get_name()
