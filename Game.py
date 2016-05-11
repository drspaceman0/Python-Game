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
#		
# START GAME
#	

def main():
	while True:
		runGame()


def restart():
	while True:
		runGame()
		

	
def runGame():
	CombatSys = Combat.Combat()
	playerObj = Player.Player()
	dungeonObj = Room.Dungeon(playerObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	enemylist = []
	VE0 = Enemy.VariableEnemy(0, 300, 300, 1, 2, 3)
	VE1 = Enemy.VariableEnemy(1, 400, 500)
	enemylist.append(VE0)
	enemylist.append(VE1)
	print "%s = length of list" % (len(enemylist))
	

	
	while True:
		myfont = pygame.font.SysFont("monospace", 15)
		scoretext = myfont.render("Score = "+str(playerObj.score), 1, (0,0,0))
		roomtext = myfont.render("Room = "+str(dungeonObj.currRoomIndex), 1, (0,0,0))
		healthtext = myfont.render("Health ="+str(playerObj.health), 1, Display.RED)
		
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		playerObj.update()
		playerObj.updateColliders()
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
			print "GGWP"
			restart()
		
		

		# draw stuff
		Display.DISPLAYSURF.blit(scoretext, (10, 10))
		Display.DISPLAYSURF.blit(roomtext, (10, 20))
		Display.DISPLAYSURF.blit(healthtext, (10, 30))
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		
		
#
#	END GAME
#

if __name__ == '__main__':
	main()
	
