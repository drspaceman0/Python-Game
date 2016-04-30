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
	
	playerObj = {
		'x': PLAYER_X,
		'y': PLAYER_Y,
		'moveUp': False,
		'moveDown': False,
		'moveLeft': False,
		'moveRight': False,
		'width': PLAYER_WIDTH,
		'height': PLAYER_HEIGHT,
		'color': RED
	}
	while True:
		DISPLAYSURF.fill(WHITE)
		
		# check for key input
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key in (K_LEFT, K_a):
					playerObj['moveLeft']= True
				elif event.key in (K_RIGHT, K_d):
					playerObj['moveRight']= True
				elif event.key in (K_DOWN, K_s):
					playerObj['moveDown']= True
				elif event.key in (K_UP, K_w):
					playerObj['moveUp']= True
				elif event.key == K_ESCAPE:
					terminate()
			elif event.type == KEYUP:
				# stop moving the player
				if event.key in (K_LEFT, K_a):
					playerObj['moveLeft']= False
				if event.key in (K_RIGHT, K_d):
					playerObj['moveRight']= False
				if event.key in (K_DOWN, K_s):
					playerObj['moveDown']= False
				if event.key in (K_UP, K_w):
					playerObj['moveUp']= False
				 
		# update player position
		if playerObj['moveRight']:
			playerObj['x'] += PLAYER_SPEED
		if playerObj['moveDown']:
			playerObj['y'] += PLAYER_SPEED
		if playerObj['moveLeft']:
			playerObj['x'] -= PLAYER_SPEED
		if playerObj['moveUp']:
			playerObj['y'] -= PLAYER_SPEED
		moveToOtherSide(playerObj)
		
		# draw player
		pygame.draw.rect(DISPLAYSURF, playerObj['color'], (playerObj['x'], playerObj['y'], playerObj['width'], playerObj['height']))
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def moveToOtherSide(playerObj):
	if playerObj['moveRight'] and playerObj['x'] >= SCREEN_WIDTH:
		playerObj['x'] = 0
	if playerObj['moveLeft'] and playerObj['x'] <= 0 - PLAYER_WIDTH:
		playerObj['x'] = SCREEN_WIDTH
	if playerObj['moveDown'] and playerObj['y'] >= SCREEN_HEIGHT:
		playerObj['y'] = 0
	if playerObj['moveUp'] and playerObj['y'] <= 0 - PLAYER_HEIGHT:
		playerObj['y'] = SCREEN_HEIGHT
		
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