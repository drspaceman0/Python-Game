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
	VE0 = Enemy.VariableEnemy(300, 300)
	enemylist.append(VE0)
	

	
	while True:
		myfont = pygame.font.SysFont("monospace", 15)
		scoretext = myfont.render("Score = "+str(playerObj.score), 1, (0,0,0))
		roomtext = myfont.render("Room = "+str(dungeonObj.currRoomIndex), 1, (0,0,0))
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		playerObj.update()
		playerObj.updateColliders()
		if len(enemylist) > 0:
			VE0.drawSelf()
			VE0.updateColliders()
			VE0.drawCollider()
			VE0.chaseObj(playerObj)
			if functions.objCollision(playerObj, VE0):
				print "attack!"
				CombatSys.attack(playerObj, VE0)
			if VE0.isDead == True:
				enemylist.remove(VE0)
			
			
		
			
		# check if the player is alive
		if playerObj.isDead == True:
			print "GGWP"
			restart()
		
		

		# draw stuff
		Display.DISPLAYSURF.blit(scoretext, (10, 10))
		Display.DISPLAYSURF.blit(roomtext, (10, 20))
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		
		
#
#	END GAME
#

if __name__ == '__main__':
	main()
	
