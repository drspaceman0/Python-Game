import pygame
import Display
import SpriteAnimation
import Room
import math
import Weapon
import Combat
import Enemy

# player variables defaults
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
PLAYER_SPEED = 15

PlayerCombat = Combat.Combat()
class Player:
	player_down = [pygame.image.load('images\player_down1.png'), pygame.image.load('images\player_down2.png')]
	player_up = [pygame.image.load('images\player_up1.png'), pygame.image.load('images\player_up2.png')]
	player_right = [pygame.image.load('images\player_right1.png'), pygame.image.load('images\player_right2.png')]
	player_left = [pygame.transform.flip(pygame.image.load('images\player_right1.png'), True, False), pygame.transform.flip(pygame.image.load('images\player_right2.png'), True, False)]
	
	def __init__(self):
		self.x = Display.TILE_SIZE
		self.y = Display.GAME_SCREEN_START + Display.TILE_SIZE
		self.colliderx = self.x #playersize/2
		self.collidery = self.y
		self.name = "Hero"
		self.score = 0
		self.health = 20
		self.damage = 1
		self.range = 50
		self.size = 48
		self.weaponx = 0
		self.weapony = 0
		self.direction = 'down'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.isAttacking = False
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = Display.RED
		self.spriteObj = SpriteAnimation.SpriteAnimation(self.player_down)
		self.dungeonObj = None
		self.currRoomObj = None
		self.isDead = False
		self.currentWeapon = Weapon.MeleeWeapon()
		self.updateToWeaponStats()
		self.circle = pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.colliderx, self.collidery), self.range, 1)
	
	
	def update(self):
		# update room if need be
		self.currRoomObj = self.dungeonObj.returnCurrentRoom()
		self.movePlayer()
		# update sprites
		self.updateSpriteList()
		# draw player
		self.spriteObj.update(self.x, self.y, False)
		# check if player should move to next room
		#self.checkForDoorCollision()
		self.colliderx = self.x+24
		self.collidery = self.y+24
		if self.isAttacking == True:
			self.attack()
	
	def movePlayer(self):
		if self.moveRight and self.x + PLAYER_SPEED < Display.SCREEN_WIDTH - PLAYER_WIDTH:
			self.x += PLAYER_SPEED
			self.weaponx = self.colliderx+self.range
		if self.moveDown and self.y + PLAYER_SPEED < Display.SCREEN_HEIGHT - PLAYER_HEIGHT:
			self.y += PLAYER_SPEED
			self.weapony = self.collidery
		if self.moveLeft and self.x - PLAYER_SPEED > 0:
			self.x -= PLAYER_SPEED
			self.weaponx = self.colliderx-self.range
		if self.moveUp and self.y - PLAYER_SPEED > Display.GAME_SCREEN_START:
			self.y -= PLAYER_SPEED
			self.weapony = self.collidery - 10
		
	
	def updateSpriteList(self):
		if self.direction == 'right' and self.spriteObj.images != self.player_right:
			self.spriteObj.changeSprites(self.player_right)
		elif self.direction == 'left' and self.spriteObj.images != self.player_left:
			self.spriteObj.changeSprites(self.player_left)
		if self.direction == 'up' and self.spriteObj.images != self.player_up:
			self.spriteObj.changeSprites(self.player_up)
		elif self.direction == 'down' and self.spriteObj.images != self.player_down:
			self.spriteObj.changeSprites(self.player_down)
		#This circle will be our collision box where we draw our attack from 
		#pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.colliderx, self.collidery), self.range, 1)
		#Draw Weapon
		pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (self.colliderx, self.collidery), (self.weaponx, self.weapony), 1)


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
		
	def collision(self, x, y):
		if math.sqrt(pow((self.x) - x, 2) + pow((self.y) - y, 2)) < 30:
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
					
	def death(self):
		self.isDead = True
		print "Hero died..."
		print "Game Over"
		
	def updateToWeaponStats(self):
		self.range += self.currentWeapon.range
		self.damage += self.currentWeapon.damage
		
	def updateColliders(self):
		self.collisionx = self.x+24
		self.collisiony = self.y+24
	
	def isPlayer(self):
		return True
		
	def attack(self):
		for count in range (-20, 30):
			pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (self.colliderx, self.collidery), (self.weaponx, self.weapony+count), 1)
		