import pygame
import Display
import SpriteAnimation

# player variables defaults
PLAYER_X = 10
PLAYER_Y = 10
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
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
		self.direction = 'down'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = Display.RED
		self.spriteObj = SpriteAnimation.SpriteAnimation(self.player_down)

	def movePlayer(self):
		if self.moveRight:
			self.x += PLAYER_SPEED
		if self.moveDown:
			self.y += PLAYER_SPEED
		if self.moveLeft:
			self.x -= PLAYER_SPEED
		if self.moveUp:
			self.y -= PLAYER_SPEED
		# update sprites
		self.updateSpriteList()
		# check if player needs to go to other side
		self.moveToOtherSide()
		# draw player
		self.spriteObj.update(self.x, self.y)
	
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
			