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
import LabelMaker
import hypotheticalenemy
import Weapon
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

	playerObj = Player.Player()
	dungeonObj = Room.Dungeon(playerObj)
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	VE0 = hypotheticalenemy.VariableEnemy(100, 100)
	VE1 = hypotheticalenemy.VariableEnemy(200, 200)
	VE2 = hypotheticalenemy.VariableEnemy(300, 300)
	VE3 = hypotheticalenemy.VariableEnemy(400, 400)
	W0 = Weapon.MeleeWeapon()
	W1 = Weapon.MeleeWeapon()
	W2 = Weapon.MeleeWeapon()
	W0.printName()
	W1.printName()
	W2.printName()
	

	
	while True:
		myfont = pygame.font.SysFont("monospace", 15)
		scoretext = myfont.render("Score = "+str(playerObj.score), 1, (0,0,0))
		roomtext = myfont.render("Room = "+str(dungeonObj.currRoomIndex), 1, (0,0,0))
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		playerObj.update()
		
		
		VE0.updateName()	
		VE1.updateName()	
		VE2.updateName()	
		VE3.updateName()	
		VE0.drawSelf()
		VE1.drawSelf()
		VE2.drawSelf()
		VE3.drawSelf()
		
		
			
		# check if the player is alive
		if playerObj.stillAlive() == False:
			print "dead"

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