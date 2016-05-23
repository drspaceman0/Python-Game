""" Game Networking Client """

from legume import client
import logging
from time import strftime

import Network
import Game


class GameClient:
    def __init__(self):
        self.running = 1
        self._client = client.Client() # Note: _ makes it clear this is "private", and not to be used outside of the class
        self._client.OnMessage += self.on_message
        self._logger = logging.getLogger(__name__)
        self._logger.debug('Initialized GameClient')

    def on_message(self, sender, msg):
        pass

    def send_chat_message(self, player_from, message):
        msg                     = Network.ChatMessage()
        msg.player_from.value   = player_from
        msg.message.value       = message
        msg.timestamp.value     = strftime("%H:%M:%S")
        self._logger.info('Sending chat message: \"%s\"', message)
        try:
            self._client.send_reliable_message(msg)
        except client.ClientError:
            self._logger.error('Could not send chat message')

    def connect(self, host='localhost'):
        self._logger.info('Connecting to %s', host)

    def run(self):
        self._logger.debug('run()')
        #Game.main()

if __name__ == '__main__':
    logging.basicConfig(filename='Client.log', level=logging.DEBUG)
    client = GameClient()
    client.run()