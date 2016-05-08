'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys
import math
import random
from pygame.locals import *
import Bullet
#import Enemy
import Display
import SpriteAnimation
import Player
import Input
import Room
import Spawner
import GooEnemy
import BrickEnemy
import labledEnemy
import LabelMaker
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
	LE = labledEnemy.labledEnemy()
	

	
	while True:
		myfont = pygame.font.SysFont("monospace", 15)
		scoretext = myfont.render("Score = "+str(playerObj.score), 1, (0,0,0))
		roomtext = myfont.render("Room = "+str(dungeonObj.currRoomIndex), 1, (0,0,0))
		# check for key input
		Input.checkForInputs(playerObj)
		dungeonObj.update() 
		playerObj.update()
		
		# update bullets if any exist
		if len(Bullet.Bullet.listBullets) > 0:
			Bullet.Bullet.update(Bullet.Bullet.listBullets[0])
		# update GooEnemies if any exist, then attack the player
		if len(GooEnemy.GooEnemy.listGooEnemies) > 0:
			GooEnemy.GooEnemy.update(GooEnemy.GooEnemy.listGooEnemies[0], playerObj)
		# update BrickEnemies if any exist, then attack the player
		if len(BrickEnemy.BrickEnemy.listBrickEnemies) > 0:
			BrickEnemy.BrickEnemy.update(BrickEnemy.BrickEnemy.listBrickEnemies[0], playerObj)
			
		LE.update(playerObj)
			
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