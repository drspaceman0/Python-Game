import pygame
import math
import Display
import Player
import random
DOOR_WIDTH = Display.TILE_SIZE
DOOR_LENGTH = Display.TILE_SIZE



class Room:
	# sprite library
	wall_up_sprite = pygame.image.load('images\wall_up.png')
	wall_right_sprite = pygame.transform.rotate(wall_up_sprite, 90)
	wall_down_sprite = pygame.transform.rotate(wall_up_sprite, 180)
	wall_left_sprite = pygame.transform.rotate(wall_up_sprite, 270)
	wall_corner_sprite = pygame.image.load('images\wall_corner_upleft.png')
	wall_flipped_corner_sprite = pygame.transform.rotate(wall_corner_sprite, 180)
	door_up_sprite = pygame.image.load('images\door_up.png')
	door_right_sprite = pygame.transform.rotate(door_up_sprite, 90)
	door_down_sprite = pygame.transform.rotate(door_up_sprite, 180)
	door_left_sprite = pygame.transform.rotate(door_up_sprite, 270)
	tile_sprite = pygame.image.load('images\\tile.png')
	
	
	
	def __init__(self, index, playerObj, color):
		self.color = color
		self.width = Display.SCREEN_WIDTH
		self.height = Display.SCREEN_HEIGHT
		#x, y, True if player enters this door, connected room, 
		self.doors =   {'leftDoor': [0, Display.SCREEN_HEIGHT/2, None, 'leftDoor'],
						'rightDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH, Display.SCREEN_HEIGHT/2, None, 'rightDoor'],
						'upDoor': [Display.SCREEN_WIDTH/2, Display.GAME_SCREEN_START, None, 'upDoor'], 
						'downDoor': [Display.SCREEN_WIDTH/2, Display.SCREEN_HEIGHT - DOOR_LENGTH, None, 'downDoor']}
		self.entranceX = 0
		self.entranceY = 0
		self.currentRoom = True
		self.timeToChangeRoom = False
		self.roomIndexToChangeTo = 0
		self.index = index
		self.playerObj = playerObj
		Dungeon.numRooms += 1
	
	def update(self):
		self.drawRoom()
	
	def drawRoom(self):
		Display.DISPLAYSURF.fill(self.color)
		for x in xrange(0, Display.SCREEN_WIDTH, Display.TILE_SIZE):
			for y in xrange(Display.GAME_SCREEN_START, Display.SCREEN_HEIGHT, Display.TILE_SIZE):
				# upper wall
				if y == Display.GAME_SCREEN_START: 
					if x == 0: # northwest corner
						Display.DISPLAYSURF.blit(self.wall_corner_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x >= Display.SCREEN_WIDTH - Display.TILE_SIZE: # norheast corner
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_corner_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x < Display.SCREEN_WIDTH/2: #left part
						Display.DISPLAYSURF.blit(self.wall_up_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # right part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_up_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if x == Display.SCREEN_WIDTH/2 and self.doors['upDoor'][2] != None: 
						Display.DISPLAYSURF.blit(self.door_up_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# lower wall
				elif y == Display.SCREEN_HEIGHT - Display.TILE_SIZE: 
					if x == 0: # southwest corner
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_flipped_corner_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x == Display.SCREEN_WIDTH - Display.TILE_SIZE: # southeast corner
						Display.DISPLAYSURF.blit(self.wall_flipped_corner_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x < Display.SCREEN_WIDTH/2: #left part
						Display.DISPLAYSURF.blit(self.wall_down_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # right part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_down_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if x == Display.SCREEN_WIDTH/2 and self.doors['downDoor'][2] != None: 
						Display.DISPLAYSURF.blit(self.door_down_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# right wall
				elif x == Display.SCREEN_WIDTH - Display.TILE_SIZE: 
					if y < Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_right_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors['rightDoor'][2] != None:
						Display.DISPLAYSURF.blit(self.door_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# left wall
				elif x == 0: 
					if y >= Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_left_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors['leftDoor'][2] != None: 
						Display.DISPLAYSURF.blit(self.door_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# floor tiles
				else: 
					Display.DISPLAYSURF.blit(self.tile_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))	
	
	def getRoomEntranceForNextRoom(self, door):
		if door[3] == 'leftDoor': # if exit left door, enter next room through right door 
			door[2].entranceX = self.doors['rightDoor'][0] - Player.PLAYER_WIDTH
			door[2].entranceY = self.doors['rightDoor'][1]
		elif door[3] == 'rightDoor':
			door[2].entranceX = self.doors['leftDoor'][0] + Player.PLAYER_WIDTH
			door[2].entranceY = self.doors['leftDoor'][1]
		elif door[3] == 'upDoor':
			door[2].entranceX = self.doors['downDoor'][0]
			door[2].entranceY = self.doors['downDoor'][1] - Player.PLAYER_HEIGHT
		elif door[3] == 'downDoor':
			door[2].entranceX = self.doors['upDoor'][0]
			door[2].entranceY = self.doors['upDoor'][1] + Player.PLAYER_HEIGHT
		
class Dungeon:
	numRooms = 0
	listRooms = []
	def __init__(self, playerObj):
		self.playerObj = playerObj
		self.Room1 = Room(self.numRooms, self.playerObj, Display.TEAL)
		self.Room2 = Room(self.numRooms, self.playerObj, Display.PURPLE)
		self.Room3 = Room(self.numRooms, self.playerObj, Display.ORANGE)
		self.Room4 = Room(self.numRooms, self.playerObj, Display.GREY)
		self.Room5 = Room(self.numRooms, self.playerObj, Display.BROWN)
		self.connectRooms()
		self.listRooms.append(self.Room1)
		self.listRooms.append(self.Room2)
		self.listRooms.append(self.Room3)
		self.listRooms.append(self.Room4)
		self.listRooms.append(self.Room5)
		self.currRoomIndex = 0
		
	def update(self):
		if self.returnCurrentRoom().timeToChangeRoom:
			self.changeRoom()
		self.returnCurrentRoom().update()
			
	
	def changeRoom(self):
		self.returnCurrentRoom().timeToChangeRoom = False
		self.currRoomIndex = self.returnCurrentRoom().roomIndexToChangeTo
		self.playerObj.changePlayerPosition(self.returnCurrentRoom().entranceX, self.returnCurrentRoom().entranceY)
		self.returnCurrentRoom().currentRoom = True
		self.returnCurrentRoom().update()
	
	def connectRooms(self):
		self.Room1.doors['upDoor'][2] = self.Room2
		self.Room1.doors['leftDoor'][2] = self.Room3
		self.Room1.doors['rightDoor'][2] = self.Room4
		self.Room1.doors['downDoor'][2] = self.Room5
		self.Room2.doors['downDoor'][2] = self.Room1
		self.Room3.doors['rightDoor'][2] = self.Room1
		self.Room4.doors['leftDoor'][2] = self.Room1
		self.Room5.doors['upDoor'][2] = self.Room1
		
	def returnCurrentRoom(self):
		return self.listRooms[self.currRoomIndex]