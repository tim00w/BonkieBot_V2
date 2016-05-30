"""
use python structures:
- assert
- hash (or hashlib)
- logging (create custom logger)
- dataset (easy sql connectivity)
* some form of testing library

ik voeg een nieuqwe line toe
"""


# IMPORTS


from telegram import Emoji, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from delorean import Delorean
import logging
import dataset
import tokens


# CONSTANTS


LOGGER = logging.getLogger()
TOKEN = tokens.BonkieBot


# CLASSES


class Oefening:

    def __init__(self, naam):
        """
        DocString
        """
        self.naam = naam
        self.series = []
        self.opmerking = []
        
    def __str__(self):
        return "{}\n{}\n\n{}"
    
    def nieuwe_set(self, reps, gewicht):
        """
        DocString
        """
        self.series.append(Set(reps, gewicht))
        

    def opmerking(self, tekst):
        """
        DocString
        """
        self.opmerking.append(tekst)
        

class SuperSet:
    
    def __init__():
        """
        DocString
        """
        return

class Set:
    
    def __init__(self, herhalingen, gewicht):
        """
        DocString
        """
        self.herhalingen = herhalingen
        self.gewicht = gewicht
        
        
    def __str__(self):
        return 'SET'
    
    def __repr__(self):
        return "Set class: ({}, {})".format(self.herhalingen, self.gewicht)

class Training:
    
    def __init__():
        """
        DocString
        """
        return

class BonkieBot:
    """
    DocString
    """
    def __init__(self, logger=LOGGER, token=TOKEN, dbName='sqlite:///BonkieBot.db'):
        """
        DocString
        """
        assert type(token) is str, "Token is not a str: {}".format(token)
        assert type(dbName) is str, "dbName is not a str: {}".format(dbName)
        
        self.logger = logger
        self.db = dataset.connect(dbName)
        
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
    
    def addHandlers(self, handlers):
    """
    method: 
            addHandlers(self, handlers)
    input:
            Variable 'Handlers' is a list, containing one or more tuples with 3 fields: 
            (command, function, require_args)
    Description:
            Combines telegram command names (/'command') with designated python functions ('function').
            The 'require_args' variable (bool) describes whether the 'function' needs additional arguments to work.
            Telegram users provide these adittional variables (/'command' <arguments>).
    Output:
            None
    """
    assert type(handlers) is list, "'{}' is not a list of handlers.".format(handlers)
    assert len(handlers) > 0, "Handlers is an empty list: {}".format(handlers)
    assert type(handlers[0]) is tuple, "Handlers doesn't contain tuples: {}".format(handlers[0])
    
    for command, function, require_args in handlers:
        handler = CommandHandler(command, function, pass_args=require_args)
        self.dispatcher.add_handler(handler)


# FUNCTIONS


def start(bot, update):
    """
    DocString
    """
    return

def help(bot, update, args):
    """
    DocString
    """
    return

def vorige(bot, update, args):
    """
    DocString
    """
    return

def begin(bot, update, args):
    """
    DocString
    """
    return

def einde(bot, update, args):
    """
    DocString
    """
    return

def sql(bot, update, args):
    """
    DocString
    """
    return

def max(bot, update, args):
    """
    DocString
    """
    return

def beginTraining(bot, update, args):
    """
    DocString
    """
    return

def beginTraining(bot, update, args):
    """
    DocString
    """
    return

def eindeTraining(bot, update, args):
    """
    DocString
    """
    return

def vorigeTraining(bot, update, args):
    """
    DocString
    """
    return

def annuleer(bot, update):
    """
    DocString
    """
    return

def verwijder(bot, update):
    """
    DocString
    """
    return

def wijzig(bot, update, args):
    """
    DocString
    """
    return

def schema(bot, update, args):
    """
    DocString
    """
    return

def eenRm(bot, update, args):
    """
    DocString
    """
    return

def zoek(bot, update, args):
    """
    DocString
    """
    return

def authoriseer(bot, update, args):
    """
    DocString
    """
    return

def grafiek(bot, update, args):
    """
    DocString
    """
    return

def gewicht(bot, update, args):
    """
    DocString
    """
    return

def hartslag(bot, update, args):
    """
    DocString
    """
    return

def slaap(bot, update, args):