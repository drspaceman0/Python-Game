import pygame
global FPSCLOCK, DISPLAYSURF, FPS


SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640
RED = (255, 0, 0)
ORANGE = (255, 153, 153)
YELLOW = (255, 255, 0)
GREEN = (22, 226, 15)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)
PURPLE = (153, 0, 153)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
BLACK = (0, 0, 0)


QUADRANTX = int(SCREEN_WIDTH/2)
QUADRANTY = int(SCREEN_HEIGHT/2)


pygame.init()
FPS = 30 # frames per second
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Game')

	
