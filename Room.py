import pygame
import math
import Display
import Enemy
import Player
import Spawner
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
	
	def __init__(self, index, spawnGoo, spawnBrick, playerObj, color):
		self.color = color
		self.width = Display.SCREEN_WIDTH
		self.height = Display.SCREEN_HEIGHT
		self.spawnGoo = spawnGoo
		self.spawnBrick = spawnBrick
		if self.spawnGoo:
			self.EnemyGooSpawner = Spawner.Spawner()
		if self.spawnBrick:
			self.EnemyBrickSpawner = Spawner.Spawner()

								  #x, y, True if player enters this door 
		self.doors = {'leftDoor': [0, Display.SCREEN_HEIGHT/2, False, None], 'rightDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH, Display.SCREEN_HEIGHT/2, False, None], 'upDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH/2, DOOR_LENGTH, False, None], 'downDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH/2, Display.SCREEN_HEIGHT - DOOR_LENGTH, False, None]}
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
		self.updateDoors()
		if self.spawnGoo and self.currentRoom:
			self.EnemyGooSpawner.updateGoo(self.playerObj.getQuadrant())
		if self.spawnBrick and self.currentRoom:
			self.EnemyBrickSpawner.updateBrick(self.playerObj.getQuadrant())
	
	def drawRoom(self):
		Display.DISPLAYSURF.fill(self.color)
		for x in xrange(0, Display.SCREEN_WIDTH, Display.TILE_SIZE):
			for y in xrange(0, Display.SCREEN_HEIGHT, Display.TILE_SIZE):
				# upper wall
				if y == 0: 
					if x == 0: # northwest corner
						Display.DISPLAYSURF.blit(self.wall_corner_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x > Display.SCREEN_WIDTH - Display.TILE_SIZE: # norheast corner
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_corner_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					elif x < Display.SCREEN_WIDTH/2: #left part
						Display.DISPLAYSURF.blit(self.wall_up_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # right part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_up_sprite, True, False), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if x == Display.SCREEN_WIDTH/2 and self.doors['upDoor'][3] != None: 
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
					if x == Display.SCREEN_WIDTH/2 and self.doors['downDoor'][3] != None: 
						Display.DISPLAYSURF.blit(self.door_down_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# right wall
				elif x == Display.SCREEN_WIDTH - Display.TILE_SIZE: 
					if y < Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_right_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors['rightDoor'][3] != None:
						Display.DISPLAYSURF.blit(self.door_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# left wall
				elif x == 0: 
					if y >= Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_left_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors['leftDoor'][3] != None: 
						Display.DISPLAYSURF.blit(self.door_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# floor tiles
				else: 
					Display.DISPLAYSURF.blit(self.tile_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					
	def updateDoors(self):
		for door in self.doors.values():
			# check if door has room connected to it, if not, skip and dont draw
			if door[3] == None:
				continue
			# check if player hsa entered door
			if door[2]:
				self.currentRoom = False
				self.roomIndexToChangeTo = door[3].index
				self.getRoomEntranceForNextRoom(door)
				self.timeToChangeRoom = True
				
	
	def getRoomEntranceForNextRoom(self, door):
		if door[0] == 0 and door[1] == Display.SCREEN_HEIGHT/2: # left door
			door[3].entranceX = Display.SCREEN_WIDTH - DOOR_WIDTH - 30
			door[3].entranceY = door[1]
		elif door[0] == Display.SCREEN_WIDTH and door[1] == Display.SCREEN_HEIGHT/2: # right door
			door[3].entranceX = DOOR_WIDTH + 30
			door[3].entranceY = door[1]
		elif door[0] == Display.SCREEN_WIDTH/2 and door[1] == 0: # upper door
			door[3].entranceX = door[0]
			door[3].entranceY = Display.SCREEN_HEIGHT - DOOR_LENGTH - 30
		elif door[0] == Display.SCREEN_WIDTH/2 and door[1] == Display.SCREEN_HEIGHT: # lower door
			door[3].entranceX = door[0]
			door[3].entranceY = DOOR_LENGTH + 30
	
		
class Dungeon:
	numRooms = 0
	listRooms = []
	def __init__(self, playerObj):
		self.playerObj = playerObj
		self.Room1 = Room(self.numRooms, False, True, self.playerObj, Display.TEAL)
		self.Room2 = Room(self.numRooms, True, False, self.playerObj, Display.PURPLE)
		self.Room3 = Room(self.numRooms, True, True, self.playerObj, Display.ORANGE)
		self.Room4 = Room(self.numRooms, False, False, self.playerObj, Display.GREY)
		self.Room5 = Room(self.numRooms, False, True, self.playerObj, Display.BROWN)
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
		self.Room1.doors['upDoor'][3] = self.Room2
		self.Room1.doors['leftDoor'][3] = self.Room3
		self.Room1.doors['rightDoor'][3] = self.Room4
		self.Room1.doors['downDoor'][3] = self.Room5
		self.Room2.doors['downDoor'][3] = self.Room1
		self.Room3.doors['rightDoor'][3] = self.Room1
		self.Room4.doors['leftDoor'][3] = self.Room1
		self.Room5.doors['upDoor'][3] = self.Room1
		
	def returnCurrentRoom(self):
		print self.currRoomIndex
		return self.listRooms[self.currRoomIndex]
	
		
		