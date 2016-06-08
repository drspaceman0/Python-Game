import pygame
import random

global FPSCLOCK, DISPLAYSURF, FPS

# TODO: we need to update this so everything gets initialized in main, not upon module load
# Otherwise, things will get nasty with multi-player stuffs

TILE_SIZE = 48
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 672
GAME_SCREEN_START = 96
DIALOGUE_BOX_START = SCREEN_HEIGHT - GAME_SCREEN_START
# colors
RED = (255, 0, 0)
FIGHTERRED = (175, 8, 8)
ORANGE = (255, 153, 153)
DEMONORANGE = (249, 66, 4)
YELLOW = (255, 255, 0)
GREEN = (22, 226, 15)
ORCGREEN = (65, 135, 50)
GOOGREEN = (174, 252, 156)
GOBLINGREEN = (0, 255, 25)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)
PURPLE = (153, 0, 153)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
BLACK = (0, 0, 0)
GREY = (93, 95, 96)
GOLD = (246, 255, 0)

ROOM_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, TEAL, PURPLE, BROWN, GREY]

QUADRANTX = int(SCREEN_WIDTH/2)
QUADRANTY = int(SCREEN_HEIGHT/2)

PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48

is_fullscreen = 0

#pygame.init()
FPS = 30 # Frames Per Second
FPSCLOCK = pygame.time.Clock()

# TODO: this is where we'd start on the whole resizing business

# Last argument was 32, but according to the pygame docs, setting the depth is a unnecessary thing.
# This can also slow things down if it has to emulate the depth on a system.
# http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption('Game')

	
def returnRandomColor():
	randNum = random.randint(0, len(ROOM_COLORS) - 1)
	return ROOM_COLORS[randNum]

def fullscreen():
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF )

def resetWindow():
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
