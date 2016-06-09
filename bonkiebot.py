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
import postgresqldatabase as pdb
from delorean import Delorean  # TODO: check if i really need this, message also includes date + time
from pprint import pformat
import datetime
import logging
import dataset
import tokens
# TODO: import tokens & dbSettings from config file (config.py?)

# CONSTANTS


# log = logging.getLogger(__name__)  # TODO: find out best way to log info (replace 'logging' with custom 'log')
# log.setLevel(logging.DEBUG)
# log.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

TOKEN = tokens.BonkieBot # TODO: use other source for tokens



# CLASSES


class BonkieBot:
    """
    DocString
    """
    def __init__(self, token=TOKEN, enginestr=pdb.engineStr):
        """
        DocString
        """
        assert type(token) is str, "Token is not a str: {}".format(token)

        self.token = token
        self.database = dataset.connect(enginestr)  # TODO: perhaps use a database class? (look for in sqlalchemy)

        self.training = self.database['training']  # TODO: perhaps use a table class? (look for in sqlalchemy)
        self.gebruikers = self.database['gebruikers']  # TODO: perhaps use a table class? (look for in sqlalchemy)
        self.fitness = self.database['fitness']  # TODO: perhaps use a table class? (look for in sqlalchemy)
        self.schema = self.database['schema']  # TODO: perhaps use a table class? (look for in sqlalchemy)
        
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
            self.dispatcher.add_handler(handler)  # TODO: find out whether a list of added commands get saved
            # TODO: add help text (both short and long) to some variable that can be used by the 'help' command

    def start(self, bot, update):
        """
        says hi!

        says hi!  to the person speaking to him
        """  # TODO: use docstring as a guide for help function (start.__doc__)
        message = update.message.to_dict()

        chat_id = message['chat']['id']
        first_name = message['chat']['first_name']
        last_name = message['chat']['last_name']
        date = datetime.datetime.utcfromtimestamp(message['date'])

        gebruiker_id = hash(str(chat_id) + self.token)

        t = self.gebruikers
        gebruiker_data = {pdb.GEBRUIKER_ID: str(gebruiker_id),
                          pdb.TELEGRAM_CODE: chat_id,
                          pdb.VOORNAAM: first_name,
                          pdb.ACHTERNAAM: last_name,
                          pdb.DATUMTIJD: date}

        if t.find_one(gebruiker_id=gebruiker_id) is None:
            t.insert(gebruiker_data)
            # TODO: log something
        message_template = 'Hi {}!\n\n I am a Telegram-bot!'
        bot_message = message_template.format(first_name)
        bot.sendMessage(chat_id, text=bot_message)
        logging.debug(pformat(update.message.to_dict()))  # TODO: change logging to custom log
        return

    def help(self, bot, update, args):
        """
        DocString
        """  # TODO: use DocString as guide for help function
        template = "The following commands are present:\n{}"
        if args is None:
            bot_message = template.format('commandAndHalp')  # TODO: use command help files
        elif args in ['start', 'help']:  # TODO: use commands list
            bot_message = '{}'.format('commandAndHalp')  # TODO: use command help files
        else:
            bot_message = "That command isn't present.\n\n{}".format(template.format('commandAndHalp'))  # TODO: use command help files
        bot.sendMessage(update.message.chat_id, bot_message)
        return


# FUNCTIONS  # TODO: implement functions


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
    BBot.addHandlers([('start', BBot.start, False), ('help', BBot.help, True)])
    BBot.updater.start_polling()
    BBot.updater.idle()
