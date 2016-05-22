""" Network Server """

import legume
import logging

import Network


class GameServer:
    def __init__(self):
        self._server = legume.Server()
        self._server.OnConnectRequest += self.on_connect_request
        self._server.OnMessage += self.on_message
        self.port = Network.PORT


    def on_connect_request(self, sender, args):
        pass

    def on_message(self, sender, msg):
        pass

    def run(self):
        self._server.listen(('', self.port))
        print('Listening on port %d' % self.port)
        self._server.update()
        self._server.disconnect()


if __name__ == '__main__':
    logging.basicConfig(filename='Server.log', level=logging.DEBUG)
    server = GameServer()
    server.run()