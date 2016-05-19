'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys, os
import math
import random
from pygame.locals import *
import Display
import SpriteAnimation
import Player
import Input
import Room
import Enemy
import Weapon
import Combat
import functions
import time
import Spawnner
import Menu
import Inventory
import Beats
#		
# START GAME
#	
items = []
GlobalInventorySys = Inventory.Inventory(1, items)



def main():
	gameNotOver = True
	while gameNotOver:
		gameNotOver = runGame()
	print "GAME OVER"
	os.execl(sys.executable, sys.executable, *sys.argv)


def restart():
	main()
		


def attack(count, attacker, defender):
	pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (attacker.collisionx, attacker.collisiony), (attacker.weaponx, attacker.weapony+count), 1)

	'''We should consider getting a draw down, 
	background, then loot, then spawners, then enemies, then player?'''
	
def runGame():

	CombatSys = Combat.Combat()
	playerObj = Player.Player()
	dungeonObj = Room.Dungeon(playerObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	enemylist = []
	#spawnnerlist = []
	#SpawnnerOfPwnge = Spawnner.Spawnner(enemylist)
	#spawnnerlist.append(SpawnnerOfPwnge)
	
	while True:
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		dungeonObj.update()
		Menu.update(playerObj, dungeonObj)
		
		playerObj.update()
		playerObj.updateColliders()
		
		if len(dungeonObj.returnCurrentRoom().spawnnerlist) > 0:
			for spawnner in dungeonObj.returnCurrentRoom().spawnnerlist:
				spawnner.drawSpawnner()
				spawnner.update()
				if functions.objCollision(playerObj, spawnner):
					CombatSys.attack(playerObj, spawnner)
				if spawnner.isDead == True:
					dungeonObj.returnCurrentRoom().spawnnerlist.remove(spawnner)
		if len(dungeonObj.returnCurrentRoom().enemylist) > 0:
			for enemy in dungeonObj.returnCurrentRoom().enemylist:
				enemy.drawSelf()
				enemy.updateColliders()
				enemy.drawCollider()
				enemy.chaseObj(playerObj)
				if playerObj.isAttacking:
					if functions.objCollision(playerObj, enemy):
						CombatSys.attack(playerObj, enemy)
				if enemy.isDead == True:
					dungeonObj.returnCurrentRoom().enemylist.remove(enemy)


		if functions.worldInventory:
			for item in functions.worldInventory:
				#print "%s" % (item.name)
				item.drawAsLoot()
					
		
		


		#if functions.worldCoins > 0:
		#	print "%s worldCoins" % (functions.worldCoins)

		if functions.worldInventory:
			for item in functions.worldInventory:
				print "%s" % (item.name)
		if functions.worldCoins > 0:
			print "%s worldCoins" % (functions.worldCoins)
			
		# check if the player is alive
		if playerObj.isDead == True:
			return False

		# draw stuff		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		
		
#
#	END GAME
#

if __name__ == '__main__':
	main()
		
