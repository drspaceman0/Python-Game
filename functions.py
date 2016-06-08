""" Functions, variables, and objects shared between many classes stored here"""


#from pygame.locals import *

import logging
import math
import pygame
from os import path

#import Enemy
#import Display


IMAGE_DIR = 'images'


# Keep track of dead enemies loot and whatnot.
worldInventory = []
worldCoins = []
playerCoins = []
playerInventory = [] #This is done in the player class, but might be smoother here...
playerPotions = []

# Keep track of player stats
worldEnemiesKilled = 0
worldDeaths = 0

# "Timer"
gameTimer = 0

#Game Menu
paused = False
def pauseMenu():
	import Display
	font = pygame.font.SysFont("comicsansms",115)
	text = font.render("Pause", 1, (0,0,0))	
    
	while pauseMenu:
		for event in pygame.event.get():  # TODO: is there a better way?
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					return
			elif event.type == pygame.JOYBUTTONDOWN:
				return
					
		Display.DISPLAYSURF.fill(Display.WHITE)
		Display.DISPLAYSURF.blit(text, (100, 200))
		pygame.display.update()
		Display.FPSCLOCK
	


def objCollision(obj1, obj2):
	if math.sqrt(pow(obj1.collisionx - obj2.collisionx, 2) + pow(obj1.collisiony - obj2.collisiony, 2)) < obj1.range:
		return True

def rectCollision(rect1, rect2):
	if rect1.x >= rect2.x and rect1.x <= rect2.x + rect2.width and rect1.y >= rect2.y and rect1.y <= rect2.y + rect2.height or rect2.x >= rect1.x and rect2.x <= rect1.x + rect1.width and rect2.y >= rect1.y and rect2.y <= rect1.y + rect1.height:
		return True

def spawnEnemy(playerObj, x, y, verb, noun, adjective):
	logging.debug('spawnEnemy')
	from Enemy import VariableEnemy
	return VariableEnemy(playerObj, x, y, verb, noun, adjective)

def moveCoinFromWorldToPlayerInv(coin):
	#worldInventory.remove(coin)
	if coin not in playerCoins:
		playerCoins.append(coin)
			
def movePotionFromWorldToPlayerInv(potion):
	if potion not in playerInventory:
		playerPotions.append(potion)
	
def printPlayerStats():
	logging.debug('printPlayerStats')
	total = 0
	if playerCoins:
		for coin in playerCoins:
			total += coin.value
	print "%s gold held!" % total
	print "%s enemies slain by Hero" % worldEnemiesKilled
	print "Hero sucked %s times!" % worldDeaths
	
def updateItems(player):
	if worldInventory:
		for item in worldInventory:
				item.drawAsLoot()
				if player.pickup:
					if objCollision(player, item):
						print "Hero picked %s up!" % item.name
						worldInventory.remove(item)
						item.pickup()
						
def updateCoins(player):
	if worldCoins:
		for coin in worldCoins:
			coin.drawSelf()
			if player.pickup:
				if objCollision(player, coin):
					print "Hero acquired %s gold!" % (coin.value)
					worldCoins.remove(coin)
					coin.pickup()

def load_image(image_name):
	return pygame.image.load(path.join(IMAGE_DIR, image_name))
