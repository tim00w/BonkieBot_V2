import logging
from telegram import Emoji, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dataset
import logging
import tokens

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = tokens.BonkieBot


class BonkieBot:
    def __init__(self, token=TOKEN, db_name='sqlite:///BonkieBot.database'):
        """

        :type db_name: string
        """

        self.db = dataset.connect(db_name)
        self.state = self.db['state']
        self.context = self.db['context']
        self.values = self.db['values']

        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

        # handlers
        self.start_handler = CommandHandler('start', start)
        self.dispatcher.add_handler(self.start_handler)
        self.echo_handler = MessageHandler([Filters.text], echo)
        self.dispatcher.add_handler(self.echo_handler)
        self.caps_handler = CommandHandler('caps', caps, pass_args=True)
        self.dispatcher.add_handler(self.caps_handler)

        # tell updater to start working
        self.updater.start_polling()

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def set_value(bot, update):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    text = update.message.text
    chat_state = state.get(chat_id, None)

    # since the handler will also be called on messages, we need to check if the message is actually a command
    if chat_state == MENU and text[0] == '/':
        state[chat_id] = AWAIT_INPUT # set the state
        context[chat_id] = user_id # save the user id to context
        bot.sendMessate(chat_id=chat_id,
                        text="Please enter your settings value or send "
                        "/cancel to abort",
                        reply_markup=ForceReply())



def getToken(fileName='TOKEN.log'):
    with open(fileName, 'r') as f:
        tokenStr = f.read()
    return tokenStr


if __name__ == '__main__':
    bot = BonkieBot()