""" User input handling """

from pygame import joystick
from pygame.locals import *
import pygame

import logging

import functions
import Display


# Controller sensitivity to axis position changes
POS_SENS 	= 0.2		# Positive sensitivity
NEG_SENS 	= -0.2  	# Negative sensitivity
HAT_UP 		= (0, 1)
HAT_DOWN 	= (0, -1)
HAT_LEFT 	= (-1, 0)
HAT_RIGHT 	= (1, 0)
POS_CHANGE_PER_TICK = 2

# Possible actions
MOVE_LEFT 		= 10
MOVE_RIGHT 		= 11
MOVE_DOWN 		= 12
MOVE_UP 		= 13
NO_MOVE_LEFT	= 14
NO_MOVE_RIGHT	= 15
NO_MOVE_DOWN	= 16
NO_MOVE_UP		= 17

PICKUP_OBJECT 	= 30
NO_PICKUP_OBJECT = 31
USE_POTION		= 32

NORMAL_ATTACK 	= 50
RANGED_ATTACK	= 51
SWITCH_WEAPON	= 52
NO_NORMAL_ATTACK = 53
NO_RANGED_ATTACK = 54
CONTINIOUS_RANGED_ATTACK = 55

RESTART_MATCH 	= 100
RESTART_GAME 	= 101
QUIT_GAME		= 102
OPEN_MENU 		= 103
SET_FULLSCREEN 	= 104
TAKE_SCREENSHOT = 105
PAUSE_GAME		= 106



# TODO: remapping of keybinds
# This could be accomplished with generalized actions that map to the actual key
# e.g event.key == moveleft, with moveleft being pygame.K_LEFT or whatever user sets
# More ideas: boolean array or dictionary of the current mapping set
# TODO: rumble?


class Input:
	def __init__(self):
		self.controllers = [] 	# TODO: map controllers to players
		self.vPosX = [] 			# Virtual positions of each controller on the screen
		self.vPosY = []
		self.num_controllers = 0

		# Default action mappings
		# TODO: seperate map with user-readable entries
		self.action_mappings = { "KEY_DOWN_LEFT" : 		MOVE_LEFT,
								 "KEY_DOWN_RIGHT" : 	MOVE_RIGHT,
								 "KEY_DOWN_UP" : 		MOVE_UP,
								 "KEY_DOWN_DOWN" : 		MOVE_DOWN,
								 "KEY_DOWN_X" : 		OPEN_MENU,
								 "KEY_DOWN_SPACE" : 	NORMAL_ATTACK,
								 "KEY_DOWN_E" : 		PICKUP_OBJECT,
								 "KEY_DOWN_1" : 		RANGED_ATTACK,
								 "KEY_DOWN_F" : 		SET_FULLSCREEN,
								 "KEY_DOWN_P" : 		PAUSE_GAME,
								 "KEY_DOWN_Q" : 		USE_POTION,
								 "KEY_DOWN_S" : 		TAKE_SCREENSHOT,
								 "KEY_DOWN_TAB" : 		SWITCH_WEAPON,
								 "KEY_DOWN_BACKSPACE" :	RESTART_MATCH,
								 "KEY_DOWN_ESCAPE" : 	QUIT_GAME,
								 "KEY_UP_LEFT" : 		NO_MOVE_LEFT,
								 "KEY_UP_RIGHT" : 		NO_MOVE_RIGHT,
								 "KEY_UP_UP" : 			NO_MOVE_UP,
								 "KEY_UP_DOWN" : 		NO_MOVE_DOWN,
								 "KEY_UP_SPACE" : 		NO_NORMAL_ATTACK,
								 "KEY_UP_E" :			NO_PICKUP_OBJECT,
								 "MOUSE_PRESSED" : 		CONTINIOUS_RANGED_ATTACK,
								 "JOY_A" : 				USE_POTION,
								 "JOY_B" : 				RESTART_MATCH,
								 "JOY_X" : 				PICKUP_OBJECT,
								 "JOY_Y" : 				SWITCH_WEAPON,
								 "JOY_LB" : 			TAKE_SCREENSHOT,
								 "JOY_RB" : 			SET_FULLSCREEN,
								 "JOY_BACK" : 			QUIT_GAME,
								 "JOY_START" : 			PAUSE_GAME,
								 "JOY_LS" : 			0,
								 "JOY_RS" : 			0,
								 "JOY_HAT_UP" : 		0,
								 "JOY_HAT_DOWN" : 		OPEN_MENU,
								 "JOY_HAT_RIGHT" : 		SET_FULLSCREEN,
								 "JOY_HAT_LEFT" : 		0 }
		self.players = []
		self._log = logging.getLogger(__name__)
		self._log.debug('Initialized Input')

	def initialize_controllers(self):
		""" Initialize Controllers/Joysticks """
		joystick.init()
		if joystick.get_count():
			self._log.info('%s Controllers found', joystick.get_count())
			self.num_controllers = joystick.get_count()
			self.controllers = [joystick.Joystick(x) for x in range(self.num_controllers)]
			for c in self.controllers:
				self.vPosX.append(0)
				self.vPosY.append(0)
				c.init()
				self._log.info('Initialized controller %s', c.get_name())
			self._log.info('Initialized all controllers')

	def update(self, playerObj, menuObject):
		""" Pulls events from the event queue """
		if self.num_controllers < joystick.get_count():
			self._log.error('A controller disconnected unexpectantly! Attempting to reinitialize all controllers...')
			self.initialize_controllers()

		# Input event handler
		for event in pygame.event.get():
			action = 0

			if event.type == QUIT:
				action = QUIT_GAME

			elif event.type == KEYDOWN:
				if event.key == K_LEFT:
					action = self.action_mappings["KEY_DOWN_LEFT"]
				elif event.key == K_RIGHT:
					action = self.action_mappings["KEY_DOWN_RIGHT"]
				elif event.key == K_DOWN:
					action = self.action_mappings["KEY_DOWN_DOWN"]
				elif event.key == K_UP:
					action = self.action_mappings["KEY_DOWN_UP"]
				elif event.key == K_x:
					action = self.action_mappings["KEY_DOWN_X"]
				elif event.key == K_SPACE:
					action = self.action_mappings["KEY_DOWN_SPACE"]
				elif event.key == K_e:
					action = self.action_mappings["KEY_DOWN_E"]
				elif event.key == K_TAB:
					action = self.action_mappings["KEY_DOWN_TAB"]
				elif event.key == K_p:
					action = self.action_mappings["KEY_DOWN_P"]
				elif event.key == K_q:
					action = self.action_mappings["KEY_DOWN_Q"]
				elif event.key == K_1:
					action = self.action_mappings["KEY_DOWN_1"]
				elif event.key == K_f:
					action = self.action_mappings["KEY_DOWN_F"]
				elif event.key == K_s:
					action = self.action_mappings["KEY_DOWN_S"]
				elif event.key == K_BACKSPACE:
					action = self.action_mappings["KEY_DOWN_BACKSPACE"]
				elif event.key == K_ESCAPE:
					action = self.action_mappings["KEY_DOWN_ESCAPE"]

			elif event.type == KEYUP: # stop moving the player
				if event.key == K_LEFT:
					action = self.action_mappings["KEY_UP_LEFT"]
				elif event.key == K_RIGHT:
					action = self.action_mappings["KEY_UP_RIGHT"]
				elif event.key == K_DOWN:
					action = self.action_mappings["KEY_UP_DOWN"]
				elif event.key == K_UP:
					action = self.action_mappings["KEY_UP_UP"]
				elif event.key == K_SPACE:
					action = self.action_mappings["KEY_UP_SPACE"]
				elif event.key == K_e:
					action = self.action_mappings["KEY_UP_E"]

			elif event.type == JOYAXISMOTION:  # TODO: multiple controllers
				self._axis_movement(0, playerObj)
				#for con in range(self.num_controllers):
				#	self._axis_movement(con, self.players[con])

			elif event.type == JOYBUTTONDOWN:  # TODO: non 10-button controller handling
				if self.controllers[0].get_button(0):    # 'A'
					action = self.action_mappings["JOY_A"]
				elif self.controllers[0].get_button(1):  # 'B'
					action = self.action_mappings["JOY_B"]
				elif self.controllers[0].get_button(2):  # 'X'
					action = self.action_mappings["JOY_X"]
				elif self.controllers[0].get_button(3):  # 'Y'
					action = self.action_mappings["JOY_Y"]
				elif self.controllers[0].get_button(4):  # 'LB'
					action = self.action_mappings["JOY_LB"]
				elif self.controllers[0].get_button(5):  # 'RB'
					action = self.action_mappings["JOY_RB"]
				elif self.controllers[0].get_button(6):  # 'back' (the double window button thing)
					action = self.action_mappings["JOY_BACK"]
				elif self.controllers[0].get_button(7): # 'start' (triple lines button thing)
					action = self.action_mappings["JOY_START"]
				elif self.controllers[0].get_button(8):  # 'LS' depression (maybe)
					action = self.action_mappings["JOY_LS"]
				elif self.controllers[0].get_button(9):  # 'RS' depression (maybe)
					action = self.action_mappings["JOY_RS"]
				else:
					self._log.error('Controller has more than 10 buttons! OMG!')

			elif event.type == JOYBUTTONUP:
				action = NO_PICKUP_OBJECT  # ugly ass hack

			elif event.type == JOYHATMOTION:  # TODO: non 1-hat controller handling
				hat = self.controllers[0].get_hat(0)
				if hat == HAT_UP:
					action = self.action_mappings["JOY_HAT_UP"]
				elif hat == HAT_DOWN:
					action = self.action_mappings["JOY_HAT_DOWN"]
				elif hat == HAT_RIGHT:
					action = self.action_mappings["JOY_HAT_RIGHT"]
				elif hat == HAT_LEFT:
					action = self.action_mappings["JOY_HAT_LEFT"]

			self._perform_action(action=action, playerObj=playerObj, menuObject=menuObject)

			if pygame.mouse.get_pressed():
				self._perform_action(self.action_mappings["MOUSE_PRESSED"], playerObj, menuObject)

	def _perform_action(self, action, playerObj, menuObject):
		if action == MOVE_LEFT:
			playerObj.moveLeft = True
			playerObj.direction = 'left'
		elif action == MOVE_RIGHT:
			playerObj.moveRight = True
			playerObj.direction = 'right'
		elif action == MOVE_DOWN:
			playerObj.moveDown = True
			playerObj.direction = 'down'
		elif action == MOVE_UP:
			playerObj.moveUp = True
			playerObj.direction = 'up'
		elif action == NO_MOVE_LEFT:
			playerObj.moveLeft = False
		elif action == NO_MOVE_RIGHT:
			playerObj.moveRight = False
		elif action == NO_MOVE_DOWN:
			playerObj.moveDown = False
			playerObj.currentWeapon.spriteObj.resetSpriteList()
		elif action == NO_MOVE_UP:
			playerObj.moveUp = False

		elif action == NORMAL_ATTACK:
			playerObj.isAttacking = 1
		elif action == NO_NORMAL_ATTACK:
			playerObj.isAttacking = 0
		elif action == RANGED_ATTACK:
			if playerObj.arrows > 0:
				playerObj.arrows -= 1
				print "Firing!"
				playerObj.rangedWeapon.shoot()
			else:
				print "No arrows!"
		elif action == CONTINIOUS_RANGED_ATTACK:
			if pygame.time.get_ticks() > playerObj.lastFired + 500 and playerObj.arrows > 0:
				playerObj.rangedWeapon.shoot()
				playerObj.lastFired = pygame.time.get_ticks()
				playerObj.arrows -= 1
			else:
				if playerObj.arrows < 1:
					print "No arrows!"
				else:
					print "Notching arrow!"
		elif action == SWITCH_WEAPON:
			playerObj.cycleWeapon()
		elif action == USE_POTION:
			playerObj.usePotion()
		elif action == PICKUP_OBJECT:
			playerObj.pickup = True
			if functions.playerInventory:
				playerObj.isTrading = True
		elif action == NO_PICKUP_OBJECT:
			playerObj.pickup = False
			playerObj.isTrading = False

		elif action == OPEN_MENU:
			self._log.debug('Opening menu')
			menuObject.activateText()
		elif action == PAUSE_GAME:
			if functions.paused:
				self._log.debug('Resuming game')
				functions.paused = False
			else:
				self._log.debug('Pausing game')
				functions.paused = True
		elif action == TAKE_SCREENSHOT:
			self._log.info('Taking screenshot')
			functions.screenshot()
		elif action == SET_FULLSCREEN:
			if Display.is_fullscreen:
				self._log.debug('Exiting fullscreen')
				Display.resetWindow()
				Display.is_fullscreen = 0
			else:
				self._log.debug('Entering fullscreen')
				Display.fullscreen()
				Display.is_fullscreen = 1

		elif action == RESTART_MATCH:
			self._log.info('Restarting match')
			playerObj.isDead = True
		elif action == QUIT_GAME:
			self._log.info('Quitting game')
			functions.terminate()

	# TODO: axis movement mapping
	def _axis_movement(self, con, playerObj):
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

		if self.controllers[con].get_numaxes() == 5:
			""" Xbox 360 and other '5 axis' controllers """
			LS_X = 0
			LS_Y = 1
			RS_X = 3
			RS_Y = 4
		elif self.controllers[con].get_numaxes() == 6:
			""" Xbox ONE and other '6 axis' controllers """
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
		if self.controllers[con].get_axis(RS_Y) >= POS_SENS:  # Right stick, Y-axis down
			self.vPosY[con] += POS_CHANGE_PER_TICK
		elif self.controllers[con].get_axis(RS_Y) < POS_SENS:  # Right stick, Y-axis up
			self.vPosY[con] -= POS_CHANGE_PER_TICK
		if self.controllers[con].get_axis(RS_X) >= POS_SENS:  # Right stick, X-axis right
			self.vPosX[con] += POS_CHANGE_PER_TICK
		elif self.controllers[con].get_axis(RS_X) < POS_SENS:  # Right stick, X-axis left
			self.vPosX[con] -= POS_CHANGE_PER_TICK

	# TODO: not sure how to do this without passing a input object everywhere yet
	def get_current_pos(self):
		"""
		Gets current position on the screen.
		If mouse: 		simply return current position of mouse
		If controller: 	return current virtual position being tracked by Input
		"""
		if self.vPosX and self.vPosY:
			return self.vPosX[0], self.vPosY[0] # TODO: multiple players
		else:
			return pygame.mouse.get_pos()
