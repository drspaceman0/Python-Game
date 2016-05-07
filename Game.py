'''
Move with left right up down arrow keys
Shoot with a s d w keys
'''

import pygame, sys
import math
import random
from pygame.locals import *
import Bullet
import Enemy
import Display
import SpriteAnimation
import Player
import Input
import Room
import Spawner
import GooEnemy
import BrickEnemy

#		
# START GAME
#	
def main():
	while True:
		runGame()		
	
def runGame():
	dungeonObj = Room.Dungeon()
	playerObj = Player.Player()
	playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
	dungeonObj.playerObj = playerObj
	
	EnemyGooSpawner = Spawner.Spawner()
	EnemyBrickSpawner = Spawner.Spawner()
	myfont = pygame.font.SysFont("monospace", 15)
	scoretext = myfont.render("Score = "+str(playerObj.score), 1, (0,0,0))
	
	while True:
		Display.DISPLAYSURF.fill(Display.WHITE)
		
		
		# check for key input
		Input.checkForInputs(playerObj)
				 
		playerObj.update()
		
		# update bullets if any exist
		if len(Bullet.Bullet.listBullets) > 0:
			Bullet.Bullet.update(Bullet.Bullet.listBullets[0])
		
		# update GooEnemies if any exist
		if len(GooEnemy.GooEnemy.listGooEnemies) > 0:
			GooEnemy.GooEnemy.update(GooEnemy.GooEnemy.listGooEnemies[0], playerObj)
			
		# update BrickEnemies if any exist
		if len(BrickEnemy.BrickEnemy.listBrickEnemies) > 0:
			BrickEnemy.BrickEnemy.update(BrickEnemy.BrickEnemy.listBrickEnemies[0], playerObj)
		
		dungeonObj.update()
		#Spawn enemies if need be 
		if roomObj.numGooEnemySpawns > 0:
			EnemyGooSpawner.updateGoo(playerObj.getQuadrant())
		if roomObj.numBrickEnemySpawns > 0:
			EnemyBrickSpawner.updateBrick(playerObj.getQuadrant())
	
		# draw stuff
		Display.DISPLAYSURF.blit(scoretext, (10, 10))
		pygame.display.update()
		Display.FPSCLOCK.tick(Display.FPS)
		
#
#	END GAME
#

if __name__ == '__main__':
	main()