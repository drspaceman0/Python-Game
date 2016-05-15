import pygame, sys
import math
import random
import Display
import SpriteAnimation
import Player
import Weapon
import functions
import time
import Spawnner


#info bar stuff
infobar_sprite = pygame.image.load('images\\infobar.png')
full_heart_sprite = pygame.image.load('images\\100_heart.png')
threequarters_heart_sprite = pygame.image.load('images\\75_heart.png')
half_heart_sprite = pygame.image.load('images\\50_heart.png')
onequarter_heart_sprite = pygame.image.load('images\\25_heart.png')

# weapons
axe_sprite = pygame.image.load('images\\axe.png')


def drawMenu(playerObj, dungeonObj):
	
	Display.DISPLAYSURF.blit(infobar_sprite, pygame.Rect(0, 0, Display.SCREEN_WIDTH, Display.GAME_SCREEN_START))
	drawHearts(playerObj)
	Display.DISPLAYSURF.blit(axe_sprite, pygame.Rect(280, 18, Display.TILE_SIZE, Display.TILE_SIZE))
	
	myfont = pygame.font.SysFont("monospace", 15)
	scoretext = myfont.render("Score = "+str(playerObj.score), 1, Display.RED)
	roomtext = myfont.render("Room = "+str(dungeonObj.currRoomIndex), 1, Display.RED)
	healthtext = myfont.render("Health ="+str(playerObj.health), 1, Display.RED)
	
	Display.DISPLAYSURF.blit(scoretext, (450, 10))
	Display.DISPLAYSURF.blit(roomtext, (450, 20))
	Display.DISPLAYSURF.blit(healthtext, (450, 30))
	
	
def drawHearts(playerObj):
	healthBits = playerObj.health
	x = 0
	y = 5
	while healthBits >0:
		if healthBits >= 4:
			Display.DISPLAYSURF.blit(full_heart_sprite, pygame.Rect(x*29 + 5, y, 29, 24))
		elif healthBits == 3:
			Display.DISPLAYSURF.blit(threequarters_heart_sprite, pygame.Rect(x*29 + 5, y, 29, 24))
		elif healthBits == 2:
			Display.DISPLAYSURF.blit(half_heart_sprite, pygame.Rect(x*29 + 5, y, 29, 24))
		elif healthBits == 1:
			Display.DISPLAYSURF.blit(onequarter_heart_sprite, pygame.Rect(x*29 + 5, y, 29, 24))
		else:
			return
		x += 1
		healthBits -= 4