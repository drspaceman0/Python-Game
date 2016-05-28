""" Network Server """

import legume
import logging
from time import strftime

import Game
import Network


class GameServer:
    def __init__(self):
        self._server = legume.Server()
        self._server.OnConnectRequest += self.on_connect_request
        self._server.OnMessage += self.on_message
        self.port = Network.PORT  # Port the server listens on

        self.player_count = 0

        self._log = logging.getLogger(__name__)
        self._log.debug('Initialized GameServer')

    def on_connect_request(self, sender, args):
        self._log.debug('on_connect_request: sender = %s, args = %s', sender, args)

    def on_message(self, sender, msg):
        self._log.debug('on_message: sender = %s, msg = %s', sender, msg)
        if msg.MessageTypeID == Network.ChatMessage.MessageTypeID:
            if msg.player_to == 'all':
                self._server.send_reliable_message_to_all(msg)
            else:
                p = self._server.get_peer_by_address(msg.player_to) # doing this by address for now, need to handle people typing player names
                p.send_reliable_message(msg)

        elif msg:
            self._log.error('Unknown message from client %s', sender)
        else:
            self._log.error('Empty message from client %s', sender)

    def run(self):
        self._server.listen(('', self.port)) # TODO: handle exception?
        self._log.info('Listening on port %d', self.port)

        while True:
            self._server.update()

        self._log.info('Server killed, disconnecting all clients...')
        self._server.disconnect_all()
        self._log.info('Disconnected')


if __name__ == '__main__':
    logging.basicConfig(filename='Server.log', level=logging.DEBUG)
    server = GameServer()
    server.run()
    logging.info('Server finished')
