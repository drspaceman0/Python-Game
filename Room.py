import pygame
import math
import Display
import Enemy

class Room:
	numRooms = 0
	listRooms = []
	def __init__(self):
		self.width = SCREEN_WIDTH
		self.height = SCREEN_HEIGHT