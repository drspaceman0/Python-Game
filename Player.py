import pygame
import Display
import SpriteAnimation
import Room
import math

# player variables defaults
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
PLAYER_SPEED = 10

class Player:
	player_down = [pygame.image.load('images\player_down1.png'), pygame.image.load('images\player_down2.png')]
	player_up = [pygame.image.load('images\player_up1.png'), pygame.image.load('images\player_up2.png')]
	player_right = [pygame.image.load('images\player_right1.png'), pygame.image.load('images\player_right2.png')]
	player_left = [pygame.transform.flip(pygame.image.load('images\player_right1.png'), True, False), pygame.transform.flip(pygame.image.load('images\player_right2.png'), True, False)]
	
	def __init__(self):
		self.x = PLAYER_X
		self.y = PLAYER_Y
		self.score = 0
		self.health = 20
		self.damage = 5
		self.direction = 'down'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = Display.RED
		self.spriteObj = SpriteAnimation.SpriteAnimation(self.player_down)
		self.dungeonObj = None
		self.currRoomObj = None
	
	def update(self):
		# update room if need be
		self.currRoomObj = self.dungeonObj.returnCurrentRoom()
		self.movePlayer()
		# update sprites
		self.updateSpriteList()
		# check if player needs to go to other side
		self.moveToOtherSide()
		# draw player
		self.spriteObj.update(self.x, self.y)
		# check if player should move to next room
		self.checkForDoorCollision()
	
	def movePlayer(self):
		if self.moveRight and self.x + PLAYER_SPEED < Display.SCREEN_WIDTH - PLAYER_WIDTH:
			self.x += PLAYER_SPEED
		if self.moveDown and self.y + PLAYER_SPEED < Display.SCREEN_HEIGHT - PLAYER_HEIGHT:
			self.y += PLAYER_SPEED
		if self.moveLeft and self.x - PLAYER_SPEED > 0:
			self.x -= PLAYER_SPEED
		if self.moveUp and self.y - PLAYER_SPEED > 0:
			self.y -= PLAYER_SPEED
		
	
	def updateSpriteList(self):
		if self.direction == 'right' and self.spriteObj.images != self.player_right:
			self.spriteObj.changeSprites(self.player_right)
		elif self.direction == 'left' and self.spriteObj.images != self.player_left:
			self.spriteObj.changeSprites(self.player_left)
		if self.direction == 'up' and self.spriteObj.images != self.player_up:
			self.spriteObj.changeSprites(self.player_up)
		elif self.direction == 'down' and self.spriteObj.images != self.player_down:
			self.spriteObj.changeSprites(self.player_down)


	def moveToOtherSide(self):
		if self.moveRight and self.x >= Display.SCREEN_WIDTH:
			self.x = 0
		if self.moveLeft and self.x <= 0 - PLAYER_WIDTH:
			self.x = Display.SCREEN_WIDTH
		if self.moveDown and self.y >= Display.SCREEN_HEIGHT:
			self.y = 0
		if self.moveUp and self.y <= 0 - PLAYER_HEIGHT:
			self.y = Display.SCREEN_HEIGHT

	def changePlayerPosition(self, x, y):
		self.x = x
		self.y = y
	
	def checkForDoorCollision(self):
		for door in self.currRoomObj.doors.values():
			if self.collision(door[0], door[1]):
				door[2] = True
			else:
				door[2] = False
			
	def collision(self, x, y):
		if math.sqrt(pow(self.x - x, 2) + pow(self.y - y, 2)) < 30:
			return True
		
	def getQuadrant(self):
			#Check quadrant 1
			if self.x < Display.QUADRANTX and self.y < Display.QUADRANTY:
				return 1
			#Check quadrant 2
			if self.x > Display.QUADRANTX and self.y < Display.QUADRANTY:
				return 2
			#Check Q 3
			if self.x < Display.QUADRANTX and self.y > Display.QUADRANTY:
				return 3
			#Check Q 4
			if self.x > Display.QUADRANTX and self.y > Display.QUADRANTY:
				return 4
				

	def stillAlive(self):
		if self.health <= 0:
			return False
		else:
			return True
