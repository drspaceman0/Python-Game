""" Network Client """

import legume
import logging
import pygame

import Network
import Game


class GameClient:
    def __init__(self):
        self.running = 1
        self._client = legume.Client() # Note: _ makes it clear this is "private", and not to be used outside of the class
        self._client.OnMessage += self.on_message

    def on_message(self, sender, msg):
        pass

    def connect(self, host='localhost'):
        pass

    def run(self):
        pass

if __name__ == '__main__':
    logging.basicConfig(filename='Client.log', level=logging.DEBUG)
    client = GameClient()
    client.run()