import pygame
import math
import Display
import Enemy
import Player
import Spawner

DOOR_WIDTH = 50
DOOR_LENGTH = 100



class Room:
	
	def __init__(self, index, spawnGoo, spawnBrick, playerObj):
		self.width = Display.SCREEN_WIDTH
		self.height = Display.SCREEN_HEIGHT
		'''
		self.spawnGoo = False #spawnGoo
		self.spawnBrick = False #spawnBrick
		if self.spawnGoo:
			EnemyGooSpawner = Spawner.Spawner()
		if self.spawnBrick:
			EnemyBrickSpawner = Spawner.Spawner()
		'''
								  #x, y, True if player enters this door 
		self.doors = {'leftDoor': [0, int(Display.SCREEN_HEIGHT/2), False, None], 'rightDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH, int(Display.SCREEN_HEIGHT/2), False, None]}
		self.entranceX = 25
		self.entranceY = 25
		self.beginRoom = True
		self.timeToChangeRoom = False
		self.roomIndexToChangeTo = 0
		self.index = index
		self.playerObj = playerObj
		Dungeon.numRooms += 1
		
	def update(self):
		self.updateDoors()
		if self.beginRoom:
			self.beginRoom = False
		'''
		if self.spawnGoo:
			EnemyGooSpawner.updateGoo(playerObj.getQuadrant())
		if self.spawnBrick:
			EnemyBrickSpawner.updateBrick(playerObj.getQuadrant())
		'''
	
	def updateDoors(self):
		for door in self.doors.values():
			# check if door has room connected to it, if not, skip and dont draw
			if door[3] == None:
				continue
			# draw door
			pygame.draw.rect(Display.DISPLAYSURF, Display.BROWN, (door[0], door[1], DOOR_WIDTH, DOOR_LENGTH))
			# check if player hsa entered door
			if door[2]:
				self.roomIndexToChangeTo = door[3].index
				self.getRoomEntranceForNextRoom(door)
				self.timeToChangeRoom = True
				
	
	def getRoomEntranceForNextRoom(self, door):
		if door[0] > 0:
			door[3].entranceX = DOOR_WIDTH + 30
		else:
			door[3].entranceX = Display.SCREEN_WIDTH - DOOR_WIDTH - 50
		door[3].entranceY = door[1]
	
	#def exitRoom(self):
		#if math.sqrt(pow(self.playerObj.x - 300, 2) + pow(self.playerObj.y - 300, 2)) < 30:
		#	return True
		
class Dungeon:
	numRooms = 0
	listRooms = []
	def __init__(self, playerObj):
		self.playerObj = playerObj
		self.Room1 = Room(self.numRooms, 0,0, self.playerObj)
		self.Room2 = Room(self.numRooms, 1,1, self.playerObj)
		self.connectRooms()
		self.listRooms.append(self.Room1)
		self.listRooms.append(self.Room2)
		self.currRoomIndex = 0
		
		
		
	def update(self):
		if self.returnCurrentRoom().timeToChangeRoom:
			self.changeRoom()
		self.returnCurrentRoom().update()
		
			
	
	def changeRoom(self):
		self.returnCurrentRoom().timeToChangeRoom = False
		self.currRoomIndex = self.returnCurrentRoom().roomIndexToChangeTo
		self.playerObj.changePlayerPosition(self.returnCurrentRoom().entranceX, self.returnCurrentRoom().entranceY)
		self.returnCurrentRoom().update()
	
	def connectRooms(self):
		self.Room1.doors['rightDoor'][3] = self.Room2
		self.Room2.doors['leftDoor'][3] = self.Room1
		
	def returnCurrentRoom(self):
		return self.listRooms[self.currRoomIndex]
	
		
		