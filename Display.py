import pygame
global FPSCLOCK, DISPLAYSURF, FPS


SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640
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


QUADRANTX = int(SCREEN_WIDTH/2)
QUADRANTY = int(SCREEN_HEIGHT/2)


pygame.init()
FPS = 30 # frames per second
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Game')

	
