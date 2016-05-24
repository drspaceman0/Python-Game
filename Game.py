"""
Move with left right up down arrow keys
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
import Audio
import functions
import Potions


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
	logging.debug('restart')
	main()
		
def attack(count, attacker, defender): #TODO: where is this being used, and why isn't defender being used in it?
	pygame.draw.aaline(Display.DISPLAYSURF, Display.BLACK, (attacker.collisionx, attacker.collisiony), (attacker.weaponx, attacker.weapony+count), 1)

def runGame():
	playerObj = Player.Player("Hero")
	audioObj = Audio.GameAudio()
	audioObj.load_music('music\Damnation.mp3')
	#audioObj.play_next_song()

	dungeonObj = Room.Dungeon(playerObj, 10)
	menuObject = Menu.Menu(playerObj, dungeonObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj	#This line and the last are hella confusing....
	dungeonObj.menuObject = menuObject
	logging.debug('Finished initializations for runGame')

	while True:
		if functions.gameTimer == 30:
			functions.gameTimer = 0
		# check for key input
		Input.checkForInputs(playerObj, menuObject)
		dungeonObj.update() 
		menuObject.update()
		playerObj.update()
		playerObj.updateColliders()
		audioObj.update()
		
		if dungeonObj.returnCurrentRoom().hasSpawners:
			for spawnner in dungeonObj.returnCurrentRoom().spawnnerlist:
				spawnner.drawSpawnner()
				spawnner.update()
				if spawnner.isDead:
					dungeonObj.returnCurrentRoom().spawnnerlist.remove(spawnner)
		if dungeonObj.returnCurrentRoom().hasSpawners:
			for enemy in dungeonObj.returnCurrentRoom().enemylist:
				enemy.update()


		functions.updateItems(playerObj)
		functions.updateCoins(playerObj)
			
		# check if the player is alive
		if playerObj.isDead:
			logging.info('Player %s is dead', playerObj.name)
			return False

		# draw stuff		
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		functions.gameTimer += 1


if __name__ == '__main__':
	logging.basicConfig(filename='Game.log',level=logging.DEBUG) # add filemode='w' to overwrite previous log files
	main()
	logging.debug('Exited main')
