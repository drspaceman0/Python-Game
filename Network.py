""" Core networking functionality """

# Get from: https://pypi.python.org/pypi/Legume
from legume import messages

from subprocess import Popen
import os
import logging


# Network defaults
PORT = 12999
MSGID = messages.BASE_MESSAGETYPEID_USER

def start_server():
    logging.debug('Starting a new server process')
    return Popen(["python", os.path.dirname(__file__) + "/" + "Server.py"])

def start_client():
    logging.debug('Starting a new client process')
    return Popen(["python", os.path.dirname(__file__) + "/" + "Client.py"])

class ChatMessage(messages.BaseMessage):
    MessageTypeID = MSGID + 10
    MessageValues = {
        'player_from'   : 'varstring',
        'player_to'     : 'varstring',
        'message'       : 'varstring',
        'timestamp'     : 'varstring' # length could probably be specified using string <len> for this
    }
messages.message_factory.add(ChatMessage)

