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
import Room

class NPC:
	NPC_sprite = pygame.image.load('images\\friendly.png')
	
	def __init__(self, x, y, roomObj, text):
		self.dialogue = text
		self.collisionx = x
		self.collisiony = y
		self.width = 48
		self.height = 48
		self.range = 48
		self.roomObj = roomObj
		pass
		
	def update(self):
		self.drawNPC()
		if self.checkPlayerCollision():
			self.roomObj.text = self.dialogue
		else:
			self.roomObj.text = ""
	
	def checkPlayerCollision(self):
		if functions.objCollision(self, self.roomObj.playerObj):
			return True
		else:
			return False
	
	def drawNPC(self):
		pygame.draw.rect(Display.DISPLAYSURF, Display.BLUE, pygame.Rect(self.collisionx, self.collisiony, self.width, self.height))
		Display.DISPLAYSURF.blit(self.NPC_sprite, pygame.Rect(self.collisionx, self.collisiony, self.width, self.height))	