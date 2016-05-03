import Display


# player variables defaults
PLAYER_X = 10
PLAYER_Y = 10
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
PLAYER_SPEED = 10

class Player:
	def __init__(self):
		self.x = PLAYER_X
		self.y = PLAYER_Y
		self.score = 0
		self.direction = 'right'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = Display.RED
		self.spriteList = []
	
	def movePlayer(self):
		if self.moveRight:
			self.x += PLAYER_SPEED
		if self.moveDown:
			self.y += PLAYER_SPEED
		if self.moveLeft:
			self.x -= PLAYER_SPEED
		if self.moveUp:
			self.y -= PLAYER_SPEED
		# check if player needs to go to other side
		self.moveToOtherSide()
		# draw player
		self.spriteList.update(self.x, self.y)
		self.spriteList.draw(Display.DISPLAYSURF)
		
	def updateSpriteList(self, sprites):
		self.spriteList = sprites
	
	def moveToOtherSide(self):
		if self.moveRight and self.x >= Display.SCREEN_WIDTH:
			self.x = 0
		if self.moveLeft and self.x <= 0 - PLAYER_WIDTH:
			self.x = Display.SCREEN_WIDTH
		if self.moveDown and self.y >= Display.SCREEN_HEIGHT:
			self.y = 0
		if self.moveUp and self.y <= 0 - PLAYER_HEIGHT:
			self.y = Display.SCREEN_HEIGHT