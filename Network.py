""" Core networking functionality """

import legume # Get from: https://pypi.python.org/pypi/Legume
from subprocess import Popen
import os
import logging

PORT = 12999


class ChatMessage(legume.messages.BaseMessage):
    MessageTypeID = 2
    MessageValues = {
        'from'      : 'int',
        'message'   : 'varstring'
    }

class PlayerJoin(legume.messages.BaseMessage):
    MessageTypeID = 100
    MessageValues = {
        'player_name'       : 'string 32',
        'player_model_id'   : 'int',
        'start_x'           : 'float',
        'start_y'           : 'float'
    }

def start_server():
    return Popen(["python", os.path.dirname(__file__) + "/" + "Server.py"])

def start_client():
    return Popen(["python", os.path.dirname(__file__) + "/" + "Client.py"])







