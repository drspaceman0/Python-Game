"""
Move with left right up down arrow keys
Shoot with a s d w keys
"""

import pygame
from pygame import joystick

import sys
import os
import logging

import Display
import SpriteAnimation
import Player
import Input
import Room
import Enemy
import Weapon
import Combat
import Spawnner
import Menu
import Inventory
import Beats
import functions


items = []
GlobalInventorySys = Inventory.Inventory(1, items)


def main():
	if joystick.get_count():
		logging.info('Controllers found')
		print joystick.get_count(), "joysticks detected"
		joystick.init() # initialize all connected controllers
		controllers = [joystick.Joystick(x) for x in range(joystick.get_count())]
		Input.listControllers(controllers)
			
	gameNotOver = True	
	while gameNotOver:
		gameNotOver = runGame()
	print "GAME OVER"
	logging.info('GAME OVER')
	os.execl(sys.executable, sys.executable, *sys.argv) # Glorious hack

def restart():
	logging.debug('restart()')
	main()
		
def attack(count, attacker, defender):
	pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (attacker.collisionx, attacker.collisiony), (attacker.weaponx, attacker.weapony+count), 1)

def runGame():
	CombatSys = Combat.Combat()
	playerObj = Player.Player()
	dungeonObj = Room.Dungeon(playerObj, 10)
	menuObject = Menu.Menu(playerObj, dungeonObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	dungeonObj.menuObject = menuObject
	
	while True:
		# check for key input
		Input.checkForInputs(playerObj, menuObject)
		dungeonObj.update() 
		dungeonObj.update() # duplicate?
		menuObject.update()
		
		playerObj.update()
		playerObj.updateColliders()
		
		if dungeonObj.returnCurrentRoom().hasSpawners:
			for spawnner in dungeonObj.returnCurrentRoom().spawnnerlist:
				spawnner.drawSpawnner()
				spawnner.update()
				if functions.objCollision(playerObj, spawnner):
					CombatSys.attack(playerObj, spawnner)
				if spawnner.isDead:
					dungeonObj.returnCurrentRoom().spawnnerlist.remove(spawnner)
		if dungeonObj.returnCurrentRoom().hasSpawners:
			for enemy in dungeonObj.returnCurrentRoom().enemylist:
				enemy.drawSelf()
				enemy.updateColliders()
				enemy.drawCollider()
				enemy.chaseObj(playerObj)
				if playerObj.isAttacking:
					if functions.objCollision(playerObj, enemy):
						CombatSys.attack(playerObj, enemy)
				if enemy.isDead:
					dungeonObj.returnCurrentRoom().enemylist.remove(enemy)


		if functions.worldInventory:
			for item in functions.worldInventory:
				print "%s" % item.name
				item.drawAsLoot()
					
		#if functions.worldCoins > 0:
		#	print "%s worldCoins" % (functions.worldCoins)

		if functions.worldCoins > 0:
			pygame.draw.circle(Display.DISPLAYSURF, Display.GOLD, (100, 100), 10)
			print "%s worldCoins" % functions.worldCoins
			
		# check if the player is alive
		if playerObj.isDead:
			logging.info('Player is dead')
			return False

		# draw stuff		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)


if __name__ == '__main__':
	logging.basicConfig(filename='Game.log',level=logging.DEBUG) # add filemode='w' to overwrite previous log files
	main()
	logging.debug('Exited main')
