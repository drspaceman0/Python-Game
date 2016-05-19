import pygame
import math
import Display
import Player
import random
DOOR_WIDTH = Display.TILE_SIZE
DOOR_LENGTH = Display.TILE_SIZE

UP_DOOR = 0
RIGHT_DOOR = 1
DOWN_DOOR = 2
LEFT_DOOR = 3
UP_DOOR_CORDS = [Display.SCREEN_WIDTH/2, Display.GAME_SCREEN_START]
RIGHT_DOOR_CORDS = [Display.SCREEN_WIDTH-DOOR_WIDTH, Display.SCREEN_HEIGHT/2]
DOWN_DOOR_CORDS = [Display.SCREEN_WIDTH/2, Display.SCREEN_HEIGHT - DOOR_LENGTH]
LEFT_DOOR_CORDS = [0, Display.SCREEN_HEIGHT/2]


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
	
	
	
	def __init__(self, dungeonObject, color):
		self.color = color
		self.width = Display.SCREEN_WIDTH
		self.height = Display.SCREEN_HEIGHT
		self.x = 0
		self.y = 0
		#x, y, True if player enters this door, connected room, 
		
		#self.doors =   {'leftDoor': [0, Display.SCREEN_HEIGHT/2, None, 'leftDoor'],
		#				'rightDoor': [Display.SCREEN_WIDTH-DOOR_WIDTH, Display.SCREEN_HEIGHT/2, None, 'rightDoor'],
		#				'upDoor': [Display.SCREEN_WIDTH/2, Display.GAME_SCREEN_START, None, 'upDoor'], 
		#				'downDoor': [Display.SCREEN_WIDTH/2, Display.SCREEN_HEIGHT - DOOR_LENGTH, None, 'downDoor']}
		self.doors = [-1, -1, -1, -1]
		Dungeon.listDoors.extend(self.doors) 
		self.currentRoom = True
		self.index = dungeonObject.numRooms
		self.playerObj = dungeonObject.playerObj
		self.dungeonObject = dungeonObject
		Dungeon.numRooms += 1
	
	def update(self):
		self.drawRoom()
		self.checkPlayerDoorCollision()
		
		
	def checkPlayerDoorCollision(self):
		if self.doors[LEFT_DOOR] >= 0 and self.playerObj.collision(LEFT_DOOR_CORDS[0], LEFT_DOOR_CORDS[1]):
			self.changeRoom(RIGHT_DOOR_CORDS[0] - Player.PLAYER_WIDTH, RIGHT_DOOR_CORDS[1], LEFT_DOOR)
			
		if self.doors[RIGHT_DOOR] >= 0 and self.playerObj.collision(RIGHT_DOOR_CORDS[0], RIGHT_DOOR_CORDS[1]):
			self.changeRoom(LEFT_DOOR_CORDS[0] + Player.PLAYER_WIDTH, LEFT_DOOR_CORDS[1], RIGHT_DOOR)
			
		if self.doors[DOWN_DOOR] >= 0 and self.playerObj.collision(DOWN_DOOR_CORDS[0], DOWN_DOOR_CORDS[1]):
			self.changeRoom(UP_DOOR_CORDS[0], UP_DOOR_CORDS[1] + Player.PLAYER_HEIGHT, DOWN_DOOR)
			
		if self.doors[UP_DOOR] >= 0 and self.playerObj.collision(UP_DOOR_CORDS[0], UP_DOOR_CORDS[1]):
			self.changeRoom(DOWN_DOOR_CORDS[0], DOWN_DOOR_CORDS[1] - Player.PLAYER_HEIGHT, UP_DOOR)
			
	
	def changeRoom(self, x, y, door):
		self.playerObj.changePlayerPosition(x, y)
		self.dungeonObject.currRoomIndex = self.doors[door]
		
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
					if x == Display.SCREEN_WIDTH/2 and self.doors[UP_DOOR] != -1: 
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
					if x == Display.SCREEN_WIDTH/2 and self.doors[DOWN_DOOR] != -1: 
						Display.DISPLAYSURF.blit(self.door_down_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# right wall
				elif x == Display.SCREEN_WIDTH - Display.TILE_SIZE: 
					if y < Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_right_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors[RIGHT_DOOR] != -1:
						Display.DISPLAYSURF.blit(self.door_right_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# left wall
				elif x == 0: 
					if y >= Display.SCREEN_HEIGHT/2: # upper part
						Display.DISPLAYSURF.blit(self.wall_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					else: # lower part
						Display.DISPLAYSURF.blit(pygame.transform.flip(self.wall_left_sprite, False, True), pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
					# draw door if it exists
					if y == Display.SCREEN_HEIGHT/2 and self.doors[LEFT_DOOR] != -1: 
						Display.DISPLAYSURF.blit(self.door_left_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))
				# floor tiles
				else: 
					Display.DISPLAYSURF.blit(self.tile_sprite, pygame.Rect(x, y, Display.TILE_SIZE, Display.TILE_SIZE))	

					
	
class Dungeon:
	numRooms = 0
	listRooms = []
	listDoors = []
	def __init__(self, playerObj):
		self.playerObj = playerObj
		self.maxRooms = 12	
		self.currRoomIndex = 0
		for i in xrange(0, self.maxRooms):
			self.listRooms.append(Room(self, Display.returnRandomColor()))
			if self.numRooms > 1:
				self.connectRoom(self.listRooms[self.numRooms - 1])
		#self.printAllDoors()
		#self.printAllCords()
		
	def returnListRooms(self):
		return self.listRooms
		
	def update(self):
		#if self.returnCurrentRoom().timeToChangeRoom:
		#	self.changeRoom()
		self.returnCurrentRoom().update()
	
	def printAllDoors(self):
		for i in xrange(0, self.numRooms):
			print self.listDoors[i*4 : i*4 + 4]
	
	def printAllCords(self):
		for i in xrange(0, self.numRooms):
			print "(" + str(self.listRooms[i].x) + ", " + str(self.listRooms[i].y) + ")"
	
	def roomHasSpecificDoorFree(self, room, door):
		if room.doors[door] == -1:
			return True
		else:
			return False
	
	def returnRandomFreeDoor(self, room):
		if self.roomHasFreeDoors(room):
			randInt = random.randint(0, 3)
			while True:
				if room.doors[randInt] == -1:
					return randInt
				randInt += 1
				if randInt >= 4:
					randInt = 0
			
	def roomHasFreeDoors(self, room):
		for i in xrange(0, 3):
			if room.doors[i] == -1:
				return True
		return False
	
	def oppositeDoor(self, door):
		if door == LEFT_DOOR:
			return RIGHT_DOOR
		elif door == RIGHT_DOOR:
			return LEFT_DOOR
		elif door == UP_DOOR:
			return DOWN_DOOR
		elif door == DOWN_DOOR:
			return UP_DOOR
	
	def connectableRoom(self, room, door):
		for i in xrange(0, self.numRooms):
			if room.index != i and self.listDoors[room.index * 4 + door] == -1 and self.listDoors[i * 4 + self.oppositeDoor(door)] == -1:
				return self.listRooms[i]
		return None
	
	def assignRoomToGrid(self, newRoom, oldRoom, door):
		if door == LEFT_DOOR:
			newRoom.x = oldRoom.x + 1
			newRoom.y = oldRoom.y
		elif door == RIGHT_DOOR:
			newRoom.x = oldRoom.x - 1
			newRoom.y = oldRoom.y
		elif door == UP_DOOR:
			newRoom.x = oldRoom.x 
			newRoom.y = oldRoom.y + 1
		elif door == DOWN_DOOR:
			newRoom.x = oldRoom.x 
			newRoom.y = oldRoom.y - 1
			
	def connectRoom(self, room1):
		if self.roomHasFreeDoors(room1):
			# give each room a grid
			
			door = self.returnRandomFreeDoor(room1)
			room2 = self.connectableRoom(room1, door)
			if room2 == None:
				# couldnt find a connecting room, which should be impossible
				print "wtf"
				exit(1)
			room1.doors[door] = room2.index
			room2.doors[self.oppositeDoor(door)] = room1.index
			self.assignRoomToGrid(room1, room2, door)
			self.listDoors[room1.index*4 + door] = room2.index # assign room to door
			self.listDoors[room2.index*4 + self.oppositeDoor(door)] = room1.index
		
		
		#self.Room1.doors['upDoor'][2] = self.Room2
		
	def returnCurrentRoom(self):
		return self.listRooms[self.currRoomIndex]