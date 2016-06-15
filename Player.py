import pygame
import logging

import Display
import SpriteAnimation
import math
import Weapon
import Combat
import RangedWeapon
import functions


# player variables defaults
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
PLAYER_SPEED = 15


class Player:
	player_down = [functions.load_image('player_down1.png'), functions.load_image('player_down2.png')]
	player_up = [functions.load_image('player_up1.png'), functions.load_image('player_up2.png')]
	player_right = [functions.load_image('player_right1.png'), functions.load_image('player_right2.png')]
	player_left = [pygame.transform.flip(functions.load_image('player_right1.png'), True, False), pygame.transform.flip(functions.load_image('player_right2.png'), True, False)]
	
	def __init__(self, player_name="Hero"):
		self.x = Display.TILE_SIZE
		self.y = Display.GAME_SCREEN_START + Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
		
		self.colliderx = self.x #playersize/2
		self.collidery = self.y
		self.collisionx = self.x
		self.collisiony = self.y
		self.name = player_name
		self.level = 1
		self.experience = 0
		self.meleeExp = 0
		self.rangeExp = 0
		self.score = 0
		self.health = 20
		self.maxHealth = 20 #use for leveling and stuff
		self.stamina = 10
		self.maxStamina = 10 #use for leveling and stuff
		self.damage = 5
		self.rangeDamage = 1
		self.range = 50
		self.size = 48
		self.weaponx = 0
		self.weapony = 0
		self.direction = 'down'
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.isAttacking = 0
		self.isTrading = False
		self.pickup = False
		self.knocksBack = True
		self.dot = False
		self.dotCount = 3
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = Display.RED
		self.spriteObj = SpriteAnimation.SpriteAnimation(self.player_down, 10)
		self.dungeonObj = None
		self.currRoomObj = None
		self.isDead = False
		self.currentWeapon = Weapon.MeleeWeapon()
		self.rangedWeapon = RangedWeapon.RangedWeapon(self)
		self.arrows = 1
		self.lastFired = 0
		self.updateToWeaponStats()
		self.attackRect =  pygame.Rect(self.x, self.y, self.currentWeapon.range, self.currentWeapon.range)
		self.circle = pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.collisionx, self.collisiony), self.range, 1)
		self.logger = logging.getLogger(__name__)
		self.logger.debug('Player %s Initialized', self.name)
	
	def update(self):
		# update room if need be
		self.currRoomObj = self.dungeonObj.returnCurrentRoom()
		self.updateRects()
		self.movePlayer()
		# update sprites
		self.updateSpriteList()
		# draw player
		self.spriteObj.update(self.x, self.y, False, 0)
		# check if player should move to next room
		#self.checkForDoorCollision()
		self.collisionx = self.x+24
		self.collisiony = self.y+24
		#check for leveling
		self.checkExperience()
		#Check if the player is attacking
		if self.isAttacking == 1:
			self.updateAttackSprite()
			self.attack()
		#Perform additional combat checks
		if self.dot == True:
			self.takeEffectDamage()
		#Check ranged attacks
		self.rangedAttack()
	
	def updateRects(self):
		self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
		
	def attack(self):
		for enemy in self.dungeonObj.returnCurrentRoom().enemylist:
			Combat.attack(self, enemy, True)
		for spawnner in self.dungeonObj.returnCurrentRoom().spawnnerlist:
			Combat.attack(self, spawnner, True)
			
	def rangedAttack(self):
		if self.rangedWeapon.arrows:
			for projectile in self.rangedWeapon.arrows:
				for enemy in self.dungeonObj.returnCurrentRoom().enemylist:
					if projectile.exists == True:
						if functions.objCollision(projectile, enemy):
							enemy.health -= projectile.damage
							projectile.exists = False
							print "%s hit for %s damage!" % (enemy.name, projectile.damage)
							if enemy.health <= 0:
								enemy.death()
								self.experience += 4
								print "%s gained 4 Exp!" % (self.name) 
								self.rangeExp += 2
								print "%s has gained 2 ranged exp!" % (self.name)
				
	
	def movePlayer(self):
		if self.isAttacking == 1:
			return
		if self.moveRight and self.x + PLAYER_SPEED < Display.SCREEN_WIDTH - PLAYER_WIDTH:
			self.x += PLAYER_SPEED
			self.weaponx = self.collisionx+self.range
		if self.moveDown and self.y + PLAYER_SPEED < Display.SCREEN_HEIGHT - PLAYER_HEIGHT:
			self.y += PLAYER_SPEED
			self.weapony = self.collisiony
		if self.moveLeft and self.x - PLAYER_SPEED > 0:
			self.x -= PLAYER_SPEED
			self.weaponx = self.collisionx-self.range
		if self.moveUp and self.y - PLAYER_SPEED > Display.GAME_SCREEN_START:
			self.y -= PLAYER_SPEED
			self.weapony = self.collisiony - 10
		
	
	def updateSpriteList(self):
		if self.direction == 'right' and self.spriteObj.images != self.player_right:
			self.spriteObj.changeSprites(self.player_right)
			self.currentWeapon.spriteObj.changeSprites(self.currentWeapon.sprite_list_right)
		elif self.direction == 'left' and self.spriteObj.images != self.player_left:
			self.spriteObj.changeSprites(self.player_left)
			self.currentWeapon.spriteObj.changeSprites(self.currentWeapon.sprite_list_left)
		elif self.direction == 'up' and self.spriteObj.images != self.player_up:
			self.spriteObj.changeSprites(self.player_up)
			self.currentWeapon.spriteObj.changeSprites(self.currentWeapon.sprite_list_up)
		elif self.direction == 'down' and self.spriteObj.images != self.player_down:	
			self.spriteObj.changeSprites(self.player_down)
			self.currentWeapon.spriteObj.changeSprites(self.currentWeapon.sprite_list_down)
			
		#This circle will be our collision box where we draw our attack from 
		#pygame.draw.circle(Display.DISPLAYSURF, Display.BLACK, (self.colliderx, self.collidery), self.range, 1)
		#Draw Weapon
		#pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (self.collisionx, self.collisiony), (self.weaponx, self.weapony), 1)

	

	def changePlayerPosition(self, x, y):
		self.x = x
		self.y = y
	
	def collision(self, x, y):
		if math.sqrt(pow(self.x - x, 2) + pow(self.y - y, 2)) < 30:
			return True


	def death(self):
		self.logger.info('Player %s is dead', self.name)
		self.isDead = True
		print "Hero died..."
		print "Game Over"
		
	def updateToWeaponStats(self):
		self.range += self.currentWeapon.range
		self.damage += self.currentWeapon.damage
		
	def updateColliders(self):
		self.collisionx = self.x+24
		self.collisiony = self.y+24

	@staticmethod
	def isPlayer():
		return True

	def updateAttackSprite(self):	
		if self.currentWeapon.spriteObj.loops == 1:
			self.currentWeapon.spriteObj.loops = 0
			self.isAttacking = 0
			return
		if self.direction == 'left':
			self.attackRect = pygame.Rect(self.x - self.currentWeapon.range + self.width, self.y - self.currentWeapon.range + self.width, self.currentWeapon.range, self.currentWeapon.range)
			self.currentWeapon.spriteObj.update(self.x - self.currentWeapon.range + self.width, self.y - self.currentWeapon.range + self.width, False, 0)
		elif self.direction == 'right':
			self.attackRect = pygame.Rect(self.x, self.y, self.currentWeapon.range, self.currentWeapon.range)
			self.currentWeapon.spriteObj.update(self.x , self.y , False, 0)
		elif self.direction == 'up':
			self.attackRect = pygame.Rect(self.x , self.y - self.currentWeapon.range + self.height, self.currentWeapon.range, self.currentWeapon.range)
			self.currentWeapon.spriteObj.update(self.x , self.y - self.currentWeapon.range + self.height, False, 0)
		elif self.direction == 'down':
			self.attackRect = pygame.Rect(self.x - self.currentWeapon.range + self.width, self.y, self.currentWeapon.range, self.currentWeapon.range)
			self.currentWeapon.spriteObj.update(self.x - self.currentWeapon.range + self.width, self.y, False, 0)
		
	def usePotion(self):
		if functions.playerPotions:
			usedPotion = functions.playerPotions.pop()
			if usedPotion.isHealth == True:
				if self.health == self.maxHealth:
					print "Well, that was dumb..."
				self.health += usedPotion.size
				self.dot = False
				if self.health >= self.maxHealth:
					self.health = self.maxHealth
			elif usedPotion.isStamina == True:
				if self.stamina == maxStamina:
					print "What a dummie..."
				self.stamina += usedPotion.size
				if self.stamina >= maxStamina:
					self.stamina = maxStamina
			print "Used a %s! %s potions left..." % (usedPotion.name, len(functions.playerPotions))
		else:
			print "No potions... buy some from NPC friendly for the low low price of 100 Gold!"
			
	def damageOverTime(self, damage):
		self.dot = True
		
	def takeEffectDamage(self):
		if functions.gameTimer == 1:
			print "Hero takes effect damage of 1!"
			self.dotCount -= 1
			self.health -= 1
			if self.dotCount <= 0:
				self.dot = False

	def cycleWeapon(self):
		if functions.playerInventory:
			tempWeapon = self.currentWeapon
			self.currentWeapon = functions.playerInventory.pop(0)
			functions.playerInventory.append(tempWeapon)
			print "Hero equipped %s" % (self.currentWeapon.name)
		else:
			print "No other weapons!"
			
	#Level up the player. Simply give the player one new heart every 20 exp pts
	def checkExperience(self):
		if self.experience >= 20:
			self.maxHealth += 1
			self.health = self.maxHealth
			self.experience = 0
			self.level += 1
			print "Level gained!"
			
		elif self.meleeExp >= 14:
			print "Melee skill increased!"
			self.damage += 1
			self.meleeExp = 0
		
		elif self.rangeExp >= 14:
			print "Ranged skill increased!"
			self.rangeDamage += 1
			self.rangedWeapon.updateDamage()
			self.rangeExp = 0
		else:
			pass
	

