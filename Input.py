""" User input handling """

from pygame import joystick
from pygame.locals import *
import pygame

import sys
import logging

import functions

# TODO: remapping of keybinds
# This could be accomplished with genericized actions that map to the actual key
# e.g event.key == moveleft, with moveleft being pygame.K_LEFT or whatever user sets

'''
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
				playerObj.isAttacking = 1
			if event.key == K_e:
				playerObj.pickup = True
				if functions.playerInventory:
					playerObj.isTrading = True
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
				playerObj.currentWeapon.spriteObj.resetSpriteList()
			if event.key == K_UP:
				playerObj.moveUp= False
			if event.key == K_SPACE:
				playerObj.isAttacking = 0
			if event.key == K_e:
				playerObj.pickup = False
				playerObj.isTrading = False
			if event.key == K_p:
				functions.paused = True
			if event.key == K_q:
				playerObj.usePotion()
			if event.key == K_TAB:
				playerObj.cycleWeapon()
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
'''
class Input:

	def __init__(self):
		self.controllers = [] # TODO: map controllers to players
		self.num_controllers = 0
		self._log = logging.getLogger(__name__)
		self._log.debug('Initialized Input')

	def initialize(self):
		""" Initialize input devices, notably Controllers/Joysticks """
		joystick.init()
		if joystick.get_count():
			self._log.info('%s Controllers found', joystick.get_count())
			self.controllers = [joystick.Joystick(x) for x in range(joystick.get_count())]
			for c in self.controllers:
				c.init()
				self._log.info('Initialized controller %s', c.get_name())
			self._log.info('Initialized all controllers')

	def update(self, playerObj, menuObject):
		""" Input event handler """
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()
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
					playerObj.isAttacking = 1
				elif event.key == K_e:
					playerObj.pickup = True
					if functions.playerInventory:
						playerObj.isTrading = True
				elif event.key == K_BACKSPACE:
					playerObj.isDead = True
				elif event.key == K_ESCAPE:
					self.terminate()
			elif event.type == KEYUP: # stop moving the player
				if event.key == K_LEFT:
					playerObj.moveLeft= False
				if event.key == K_RIGHT:
					playerObj.moveRight= False
				if event.key == K_DOWN:
					playerObj.moveDown= False
					playerObj.currentWeapon.spriteObj.resetSpriteList()
				if event.key == K_UP:
					playerObj.moveUp= False
				if event.key == K_SPACE:
					playerObj.isAttacking = 0
				if event.key == K_e:
					playerObj.pickup = False
					playerObj.isTrading = False
				if event.key == K_p:
					functions.paused = True
				if event.key == K_q:
					playerObj.usePotion()
				if event.key == K_TAB:
					playerObj.cycleWeapon()
			elif event.type == JOYAXISMOTION:
				print "axis motion"
			elif event.type == JOYBUTTONDOWN:
				print "button down"
			elif event.type == JOYHATMOTION:
				(x, y) = self.controllers[0].get_hat(0)
				if x == 1 and y == 0:
					pass
			elif event.type == JOYBUTTONUP:
				print "button up"

	@staticmethod
	def terminate():
		logging.info('User quit game')
		pygame.quit()
		sys.exit()
