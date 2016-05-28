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
        self._log = logging.getLogger(__name__)
        self._log.debug('Initialized GameClient')

    def on_message(self, sender, msg):
        if msg.MessageTypeID == Network.ChatMessage.MessageTypeID:
            self._log.info('Chat message from %s: \"%s\"', msg.player_from, msg.message)
            print "(%s) %s: %s" % (msg.timestamp, msg.player_from, msg.message)

    def send_chat_message(self, player_from, message):
        msg                     = Network.ChatMessage()
        msg.player_from.value   = player_from
        msg.message.value       = message
        msg.timestamp.value     = strftime("%H:%M:%S")
        self._log.info('Sending chat message: \"%s\"', message)
        try:
            self._client.send_reliable_message(msg)
        except client.ClientError:
            self._log.error('Could not send chat message')

    def connect(self, host='localhost'):
        self._log.info('Attempting to connect to server %s', host)
        try:
            self._client.connect(host)
            return True
        except client.ClientError, e:
            self._log.exception(e)
            self._log.info('Could not connect to server %s!', host)
            return False


    def run(self):
        self._log.debug('run()')
        if not self.connect():
            logging.error('Connection failed, killing client')
            return

        #Game.main()

if __name__ == '__main__':
    logging.basicConfig(filename='Client.log', level=logging.DEBUG)
    client = GameClient()
    client.run()
    logging.info('Client finished')