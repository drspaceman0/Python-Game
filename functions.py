""" Functions shared between many classes stored here"""

import math
import Enemy
import pygame
import Display

#keep track of dead enemies loot and whatnot.
worldInventory = []
worldCoins = []
playerCoins = []
playerInventory = [] #This is done in the player class, but might be smoother here...

#Keep track of player stats
worldEnemiesKilled = 0
worldDeaths = 0


def objCollision(obj1, obj2):
	if math.sqrt(pow(obj1.collisionx - obj2.collisionx, 2) + pow(obj1.collisiony - obj2.collisiony, 2)) < obj1.range:
		return True

def rectCollision(rect1, rect2):
	if rect1.colliderect(rect2):
		return True
	else:
		return False

def spawnEnemy(x,y):
	return Enemy.VariableEnemy(x,y)
	
def moveCoinFromWorldToPlayerInv(coin):
		#worldInventory.remove(coin)
		if coin not in playerCoins:
			playerCoins.append(coin)
			
def movePotionFromWorldToPlayerInv(potion):
	if potion not in playerInventory:
		playerInventory.append(potion)
	
	
	
def printPlayerStats():
	total = 0
	if playerCoins:
		for coin in playerCoins:
			total += coin.value
	print "%s gold held!" % (total)
	print "%s enemies slain by Hero" % (worldEnemiesKilled)
	print "Hero sucked %s times!" % (worldDeaths)
	
	
