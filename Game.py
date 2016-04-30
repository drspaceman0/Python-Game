import pygame, sys
from pygame.locals import *

# canvas variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# player variables
PLAYER_X = 10
PLAYER_Y = 10
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10
def main():
	global FPSCLOCK, DISPLAYSURF, FPS, SCREEN_WIDTH, SCREEN_HEIGHT

	pygame.init()
	FPS = 30 # frames per second
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption('Game')
	PLAYER_X = 10
	PLAYER_Y = 10
	while True:
		runGame()

def runGame():
	global PLAYER_X, PLAYER_Y
	
	moveUp = False
	moveDown = False
	moveLeft = False
	moveRight = False
	while True:
		DISPLAYSURF.fill(WHITE)
		
		# check for key input
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key in (K_LEFT, K_a):
					moveLeft = True
				elif event.key in (K_RIGHT, K_d):
					moveRight = True
				elif event.key in (K_DOWN, K_s):
					moveDown = True
				elif event.key in (K_UP, K_w):
					moveUp = True
				elif event.key == K_ESCAPE:
					terminate()
			elif event.type == KEYUP:
				# stop moving the player
				if event.key in (K_LEFT, K_a):
					moveLeft = False
				if event.key in (K_RIGHT, K_d):
					moveRight = False
				if event.key in (K_DOWN, K_s):
					moveDown = False
				if event.key in (K_UP, K_w):
					moveUp = False
				 
		# update player position
		if moveRight:
			PLAYER_X += PLAYER_SPEED
		if moveDown:
			PLAYER_Y += PLAYER_SPEED
		if moveLeft:
			PLAYER_X -= PLAYER_SPEED
		if moveUp:
			PLAYER_Y -= PLAYER_SPEED
		moveToOtherSide(moveLeft, moveRight, moveUp, moveDown)
		
		# draw player
		pygame.draw.rect(DISPLAYSURF, RED, (PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT))
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def moveToOtherSide(moveLeft, moveRight, moveUp, moveDown):
	global PLAYER_X, PLAYER_Y
	if moveRight and PLAYER_X >= SCREEN_WIDTH:
		PLAYER_X = 0
	if moveLeft and PLAYER_X <= 0 - PLAYER_WIDTH:
		PLAYER_X = SCREEN_WIDTH
	if moveDown and PLAYER_Y >= SCREEN_HEIGHT:
		PLAYER_Y = 0
	if moveUp and PLAYER_Y <= 0 - PLAYER_HEIGHT:
		PLAYER_Y = SCREEN_HEIGHT
		
def terminate():
	pygame.quit()
	sys.exit()

def checkForQuit():
     for event in pygame.event.get(QUIT): # get all the QUIT events
         terminate() # terminate if any QUIT events are present
     for event in pygame.event.get(KEYUP): # get all the KEYUP events
         if event.key == K_ESCAPE:
             terminate() # terminate if the KEYUP event was for the Esc key
         pygame.event.post(event) # put the other KEYUP event objects back
		 
if __name__ == '__main__':
	main()