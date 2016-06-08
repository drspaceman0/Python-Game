""" Main game logic. Where the magic happens. """

import pygame

from sys import executable, argv
from os import execl
import logging

import Display
import Player
from Input import Input
from Room import Dungeon
import Menu
import Audio
import functions

GAME_ICON =  'slithering_python.png' # 'player_down1.png'

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_icon(pygame.transform.scale(functions.load_image(GAME_ICON), (32, 32)))
		pygame.display.set_caption('Python-Game')
		self.playerObj = Player.Player()
		self.audioObj = Audio.GameAudio()
		self.inputObj = Input()
		self._log = logging.getLogger(__name__)
		self._log.debug('Initialized Game')

	def run(self):

		# Initialize Input and Audio
		self.inputObj.initialize()
		self.audioObj.load_music('music\Damnation.mp3')
		self.audioObj.play_next_song()
		# Run the game
		gameNotOver = True
		while gameNotOver:
			gameNotOver = self.runGame()

		# Finishing up
		print "GAME OVER"
		self._log.info('GAME OVER')
		functions.printPlayerStats()
		self.restart()

	def restart(self):
		self._log.debug('restart')
		execl(executable, executable, *argv) # TODO: do this properly, otherwise it will crash and burn badly

	def runGame(self):
		self.playerObj = Player.Player()
		dungeonObj =  Dungeon(self.playerObj, 10)
		menuObject = Menu.Menu(self.playerObj, dungeonObj)
		self.playerObj.dungeonObj = dungeonObj # temporary, need a better way to pass dungeon info to playerobj
		dungeonObj.playerObj = self.playerObj	#This line and the last are hella confusing....
		dungeonObj.menuObject = menuObject
		self._log.debug('Finished initializations for runGame')

		while True:
			if functions.paused:
				functions.pauseMenu()
				functions.paused = False
			if functions.gameTimer == 30:
				functions.gameTimer = 0
			self.inputObj.update(self.playerObj, menuObject)
			dungeonObj.update()
			menuObject.update()
			self.playerObj.update()
			self.playerObj.updateColliders()
			self.audioObj.update()

			if dungeonObj.returnCurrentRoom().hasSpawners:
				for spawnner in dungeonObj.returnCurrentRoom().spawnnerlist:
					spawnner.drawSpawnner()
					spawnner.update()
					if spawnner.isDead:
						dungeonObj.returnCurrentRoom().spawnnerlist.remove(spawnner)
			if dungeonObj.returnCurrentRoom().hasSpawners:
				for enemy in dungeonObj.returnCurrentRoom().enemylist:
					enemy.update()

			functions.updateItems(self.playerObj)
			functions.updateCoins(self.playerObj)

			if self.playerObj.isDead:
				self._log.info('Player %s is dead', self.playerObj.name)
				return False

			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
			functions.gameTimer += 1

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	logging.basicConfig(filename='Game.log',level=logging.DEBUG)
	game = Game()
	game.run()
	logging.debug('Finished Game')
