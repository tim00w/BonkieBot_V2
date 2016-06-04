"""
use python structures:
- assert
- hash (or hashlib)
- logging (create custom logger)
- dataset (easy sql connectivity)
* some form of testing library

"""


# IMPORTS


from telegram import Emoji, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from delorean import Delorean
from pprint import pformat
import sqlitedatabase as db
import datetime
import logging
import dataset
import tokens


# CONSTANTS


LOGGER = logging.getLogger()  # TODO: find out best way to log info

TOKEN = tokens.BonkieBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
# CLASSES


class BonkieBot:
    """
    DocString
    """
    def __init__(self, logger=LOGGER, token=TOKEN, dbName='TestBonkieBot.db'):
        """
        DocString
        """
        assert type(token) is str, "Token is not a str: {}".format(token)
        assert type(dbName) is str, "dbName is not a str: {}".format(dbName)

        self.token = token
        self.logger = logger
        self.database = dataset.connect('sqlite:///{}'.format(dbName))

        self.training = self.database['training']
        self.gebruikers = self.database['gebruikers']
        self.fitness = self.database['fitness']
        self.schema = self.database['schema']
        
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

    
        for command, function, require_args in handlers:
            handler = CommandHandler(command, function, pass_args=require_args)
            self.dispatcher.add_handler(handler)

    def start(self, bot, update):
        """
        DocString
        """
        message = update.message.to_dict()

        chat_id = message['chat']['id']
        first_name = message['chat']['first_name']
        last_name = message['chat']['last_name']
        date = datetime.datetime.utcfromtimestamp(message['date'])

        gebruiker_id = hash(str(chat_id) + self.token)

        t = self.gebruikers
        gebruiker_data = {db.GEBRUIKER_ID: str(gebruiker_id),
                          db.TELEGRAM_CODE: chat_id,
                          db.VOORNAAM: first_name,
                          db.ACHTERNAAM: last_name,
                          db.DATUMTIJD: date}
        t.insert(gebruiker_data)



        bot.sendMessage(chat_id, text='Hi {}!\n\n I am a Telegram-bot!'.format(first_name))
        logging.debug(pformat(update.message.to_dict()))




# FUNCTIONS



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
    """
    DocString
    """
    return

if __name__ == '__main__':
    BBot = BonkieBot()
    BBot.addHandlers([('start', BBot.start, False)])
    BBot.updater.start_polling()
    BBot.updater.idle()
