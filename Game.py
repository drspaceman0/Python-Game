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
import Potions

items = []



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
	functions.printPlayerStats()
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
				if playerObj.isAttacking:
					if functions.objCollision(playerObj, spawnner):
						CombatSys.attack(playerObj, spawnner, playerObj.currentWeapon.spriteObj.rect, pygame.Rect(spawnner.x, spawnner.y, spawnner.size, spawnner	.size))
				if spawnner.isDead:
					p = Potions.Potion()
					p.setDrawInfo(spawnner.x, spawnner.y)
					functions.worldInventory.append(p)
					dungeonObj.returnCurrentRoom().spawnnerlist.remove(spawnner)
		if dungeonObj.returnCurrentRoom().hasSpawners:
			for enemy in dungeonObj.returnCurrentRoom().enemylist:
				enemy.drawSelf()
				enemy.updateColliders()
				enemy.drawCollider()
				enemy.chaseObj(playerObj)
				if playerObj.isAttacking:
					CombatSys.attack(playerObj, enemy, playerObj.currentWeapon.spriteObj.rect, pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size))
				if enemy.isDead:
					playerObj.score += 1
					dungeonObj.returnCurrentRoom().enemylist.remove(enemy)

		if functions.worldInventory:
			for item in functions.worldInventory:
				print "%s" % item.name
				item.drawAsLoot()
				if playerObj.pickup == True:
					if functions.objCollision(playerObj, item) == True:
						print "pickup %s" % (item.name)
						functions.worldInventory.remove(item)
						item.pickup()
						
		if functions.worldCoins:
			for coin in functions.worldCoins:
				coin.drawSelf()
				if playerObj.pickup == True:
					if functions.objCollision(playerObj, coin) == True:
						print "pickup coin"
						functions.worldCoins.remove(coin)
						coin.pickup()
			
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
