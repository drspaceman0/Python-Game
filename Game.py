'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys
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
#		
# START GAME
#	

def main():
	while True:
		runGame()


def restart():
	while True:
		runGame()
		

		

	'''We should consider getting a draw down, 
	background, then loot, then spawners, then enemies, then player?'''
	
def runGame():
	CombatSys = Combat.Combat()
	playerObj = Player.Player()
	dungeonObj = Room.Dungeon(playerObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	enemylist = []
	spawnnerlist = []
	SpawnnerOfPwnge = Spawnner.Spawnner(enemylist)
	spawnnerlist.append(SpawnnerOfPwnge)
	
	while True:
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		dungeonObj.update()
		Menu.drawMenu(playerObj, dungeonObj)
		
		playerObj.update()
		playerObj.updateColliders()
		
		if len(spawnnerlist) > 0:
			for spawnner in spawnnerlist:
				spawnner.drawSpawnner()
				spawnner.update()
				if functions.objCollision(playerObj, spawnner):
					CombatSys.attack(playerObj, spawnner)
				if spawnner.isDead == True:
					spawnnerlist.remove(spawnner)
		if len(enemylist) > 0:
			for enemy in enemylist:
				enemy.drawSelf()
				enemy.updateColliders()
				enemy.drawCollider()
				enemy.chaseObj(playerObj)
				if functions.objCollision(playerObj, enemy):
					CombatSys.attack(playerObj, enemy)
				if enemy.isDead == True:
					enemylist.remove(enemy)
					
		
		
			
		# check if the player is alive
		if playerObj.isDead == True:
			restart()
		
		

		# draw stuff
		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		
		
#
#	END GAME
#

if __name__ == '__main__':
	main()
		
