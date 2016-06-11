""" User input handling """

from pygame import joystick
from pygame.locals import *
import pygame

import sys
import logging

import functions
import Display


POS_SENS 	= 0.2				# Positive sensitivity
NEG_SENS 	= -0.2  	# Negative sensitivity
HAT_UP 		= (0, 1)
HAT_DOWN 	= (0, -1)
HAT_LEFT 	= (-1, 0)
HAT_RIGHT 	= (1, 0)


# TODO: remapping of keybinds
# This could be accomplished with generalized actions that map to the actual key
# e.g event.key == moveleft, with moveleft being pygame.K_LEFT or whatever user sets
# More ideas: boolean array or dictionary of the current mapping set
# TODO: rumble?


class Input:

	def __init__(self):
		self.controllers = [] # TODO: map controllers to players
		self.num_controllers = 0
		self.players = []
		self._log = logging.getLogger(__name__)
		self._log.debug('Initialized Input')

	def initialize(self):
		""" Initialize input devices, notably Controllers/Joysticks """
		joystick.init()
		if joystick.get_count():
			self._log.info('%s Controllers found', joystick.get_count())
			self.num_controllers = joystick.get_count()
			self.controllers = [joystick.Joystick(x) for x in range(self.num_controllers)]
			for c in self.controllers:
				c.init()
				self._log.info('Initialized controller %s', c.get_name())
			self._log.info('Initialized all controllers')

	def update(self, playerObj, menuObject, dungObj):
		if self.num_controllers < joystick.get_count():
			self._log.error('Controller disconnected unexpectantly!')
			self.num_controllers = joystick.get_count()

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
				if event.key == K_x:
					menuObject.activateText()
				if event.key == K_SPACE:
					playerObj.isAttacking = 1
				if event.key == K_e:
					playerObj.pickup = True
					if functions.playerInventory:
						playerObj.isTrading = True
				if event.key == K_1:
					print "firing!"
					playerObj.rangedWeapon.shoot()
				if event.key == K_f:
					if Display.is_fullscreen:
						Display.resetWindow()
						Display.is_fullscreen = 0
					else:
						Display.fullscreen()
						Display.is_fullscreen = 1
				if event.key == K_s:
					functions.screenshot()
				if event.key == K_BACKSPACE:
					playerObj.isDead = True
				if event.key == K_ESCAPE:
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
				if event.key == K_LSHIFT:
					playerObj.rangedWeapon.cycleTargets(dungObj)


			elif event.type == JOYAXISMOTION:  # TODO: handle multiple controllers better
				for con in range(self.num_controllers):
					self._axis_movement(con, playerObj)

			elif event.type == JOYBUTTONDOWN:  # TODO: non 10-button controller handling
				if self.controllers[0].get_button(0):    # 'A'
					playerObj.usePotion()
				elif self.controllers[0].get_button(1):  # 'B'
					playerObj.isDead = True
				elif self.controllers[0].get_button(2):  # 'X'
					if playerObj.pickup:
						playerObj.pickup = False
						playerObj.isTrading = False
					else:
						playerObj.pickup = True
						if functions.playerInventory:
							playerObj.isTrading = True
				elif self.controllers[0].get_button(3):  # 'Y'
					playerObj.cycleWeapon()
				elif self.controllers[0].get_button(4):  # 'LB'
					functions.screenshot()
				elif self.controllers[0].get_button(5):  # 'RB'
					if Display.is_fullscreen:
						Display.resetWindow()
						Display.is_fullscreen = 0
					else:
						Display.fullscreen()
						Display.is_fullscreen = 1
				elif self.controllers[0].get_button(6):  # 'back' (the double window button thing)
					self._log.debug('Back button pressed, terminating game')
					self.terminate()
				elif self.controllers[0].get_button(7): # 'start' (triple lines button thing)
					self._log.debug('Pausing game')
					functions.paused = True
				elif self.controllers[0].get_button(8):  # 'LS' depression (maybe)
					pass
				elif self.controllers[0].get_button(9):  # 'RS' depression (maybe)
					pass
				else:
					self._log.error('Controller has more than 10 buttons! OMG!')

			elif event.type == JOYHATMOTION:  # TODO: non 1-hat controller handling
				hat = self.controllers[0].get_hat(0)
				if hat == HAT_UP:
					pass
				elif hat == HAT_DOWN:
					self._log.debug('Opening menu')
					menuObject.activateText()
				elif hat == HAT_RIGHT:
					pass  # TODO: fullscreen function
				elif hat == HAT_LEFT:
					pass

	"""
	Xbox 360
		Axis 0/1 	= LS
		Axis 2 		= LT/RT (0 is resting value)
			-1 to 0 = RT
			1 to 0 	= LT
		Axis 3/4	= RS

	Xbox ONE
		Axis 0/1	= LS
		Axis 2/3	= RS
		Axis 4		= LT	(-1 is resting value)
		Axis 5 		= RT	( -1 is resting value)
	"""
	def _axis_movement(self, con, playerObj):

		if self.controllers[con].get_numaxes() == 5:
			""" Xbox 360 and other "5 axis" controllers """
			LS_X = 0
			LS_Y = 1
			RS_X = 3
			RS_Y = 4
		elif self.controllers[con].get_numaxes() == 6:
			""" Xbox ONE and other "6 axis" controllers """
			LS_X = 0
			LS_Y = 1
			RS_X = 4
			RS_Y = 5
		else:
			self._log.error('Improper number of axis on controller [%s] %s.', con, self.controllers[con].get_name())
			return

		# Left stick
		if self.controllers[con].get_axis(LS_X) < NEG_SENS:  # Left stick, X-axis left
			playerObj.moveRight = False  # Not sure if necessary, but to be safe for now. SDL's pointless printing is wasting way more cycles anyhow.
			playerObj.moveLeft = True
			playerObj.direction = 'left'
		elif self.controllers[con].get_axis(LS_X) > POS_SENS:  # Left stick, X-axis right
			playerObj.moveLeft = False
			playerObj.moveRight = True
			playerObj.direction = 'right'
		elif NEG_SENS < self.controllers[con].get_axis(LS_X) < POS_SENS:  # Reset left stick, X-axis
			playerObj.moveLeft = False
			playerObj.moveRight = False
			playerObj.currentWeapon.spriteObj.resetSpriteList()
		if self.controllers[con].get_axis(LS_Y) < NEG_SENS:  # Left stick, Y-axis up
			playerObj.moveUp = True  # These are backward, don't ask me why
			playerObj.direction = 'up'
		elif self.controllers[con].get_axis(LS_Y) > POS_SENS:  # Left stick, Y-axis down
			playerObj.moveDown = True
			playerObj.direction = 'down'
		elif NEG_SENS < self.controllers[con].get_axis(LS_Y) < POS_SENS:  # Reset left stick, Y-axis
			playerObj.moveUp = False
			playerObj.moveDown = False
			playerObj.currentWeapon.spriteObj.resetSpriteList()

		if self.controllers[con].get_numaxes() == 5:
			if self.controllers[con].get_axis(2) < NEG_SENS: # RT pulled
				playerObj.isAttacking = 1
			elif self.controllers[con].get_axis(2) > POS_SENS: # LT pulled
				pass
			else: # resting state, reset stuff
				playerObj.isAttacking = 0
		else:
			if self.controllers[con].get_axis(2) < NEG_SENS:  # Left trigger,  resting state, reset stuff
				pass
			elif self.controllers[con].get_axis(2) > POS_SENS:  # Left trigger pulled
				pass

			if self.controllers[con].get_axis(3) < NEG_SENS:  # Right trigger, resting state, reset stuff
				playerObj.isAttacking = 0  # TODO: Why not True? Et tu?
			elif self.controllers[con].get_axis(3) > POS_SENS:  # Right trigger pulled
				playerObj.isAttacking = 1

		# Right Stick
		# Why is Y-axis 4 and X-axis 5? Again, don't ask me why man, I don't know what to believe anymore...
		if self.controllers[con].get_axis(RS_Y) >= POS_SENS:  # Right stick, Y-axis left
			pass
		elif self.controllers[con].get_axis(RS_Y) < POS_SENS:  # Right stick, Y-axis right
			pass
		if self.controllers[con].get_axis(RS_X) >= POS_SENS:  # Right stick, X-axis up
			pass
		elif self.controllers[con].get_axis(RS_X) < POS_SENS:  # Right stick, X-axis down
			pass


	@staticmethod
	def terminate():
		logging.info('User quit game\n\n\n')
		pygame.quit()
		sys.exit()
