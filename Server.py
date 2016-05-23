""" Network Server """

import legume
import logging
from time import strftime

import Network


class GameServer:
    def __init__(self):
        self._server = legume.Server()
        self._server.OnConnectRequest += self.on_connect_request
        self._server.OnMessage += self.on_message
        self.port = Network.PORT
        self._logger = logging.getLogger(__name__)
        self._logger.debug('Initialized GameServer')

    def on_connect_request(self, sender, args):
        self._logger.debug('on_connect_request: sender = %s, args = %s', sender, args)
        pass

    def on_message(self, sender, msg):
        self._logger.debug('on_message: sender = %s, msg = %s', sender, msg)
        pass

    def run(self):
        self._server.listen(('', self.port))
        self._logger.info('Listening on port %d', self.port)

        self._server.update()

        self._logger.info('Disconnecting...')
        self._server.disconnect()
        self._logger.info('Disconnected')


if __name__ == '__main__':
    logging.basicConfig(filename='Server.log', level=logging.DEBUG)
    server = GameServer()
    server.run()