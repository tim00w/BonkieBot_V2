import telegram

# create instance of telegram.Bot
TOKEN = '192950506:AAH82PqBpMS2iISI2PZ3d9b3rF_00cnGzGc'
bot = telegram.Bot(token=TOKEN)
print(bot.getMe())

# see if credentials are successful
updates = bot.getUpdates()
print([u.message.text for u in updates])

# fetch text messages send to bot (no idea why not working right now
updates = bot.getUpdates()
print([u.message.photo for u in updates if u.message.photo])

# to reply messages you'll need the chat_id
chat_id = bot.getUpdates()[-1].message.chat_id

# post text message
bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that")

# post text message with markdown
bot.sendMessage(chat_id=chat_id, text="*bold* _italic_ [link](http://google.com).", parse_mode=telegram.ParseMode.MARKDOWN)

# post message with html
bot.sendMessage(chat_id=chat_id, text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)

# post an emoji :-)
bot.sendMessage(chat_id=chat_id, text=telegram.Emoji.PILE_OF_POO)

# post an image file via url
bot.sendPhoto(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')

# post an image file from dist
bot.sendPhoto(chat_id=chat_id, photo=open('tests/test.png', 'rb'))

# post voice file from disk
bot.sendVoice(chat_id=chat_id, voice=open('tests/telegram.ogg', 'rb'))

# to tell the user that something is happening on the bot's side
bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)

# To create custom keyboards
custom_keyboard = [[telegram.KeyboardButton(telegram.Emoji.THUMBS_UP_SIGN),
                    telegram.KeyboardButton(telegram.Emoji.THUMBS_DOWN_SIGN)]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.sendMessage(chat_id=chat_id, text="Stay here, I'll be back.", reply_markup=reply_markup)

# To hide custom keyboars
reply_markup = telegram.ReplayKeyboardHide()
bot.sendMessage(chat_id=chat_id, text="I'm back.", reply_markup=reply_markup)

# to download a file
file_id = message.voice.file_id
newFile = bot.getFile(file_id)
newFile.download('voice.ogg')

# there are many more API methods, to read full API documentation
pydoc telegram.Bot


# Extensions
from telegram.ext import Updater
updater = Updater(token=TOKEN)

# for quick access to Dispatcher used by Updater, we can introduce it locally
dispatcher = updater.dispatcher

# define a function that should process a specific type of update
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

# we want this function to be called on a Telegram message that contains the /start command
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Last step is to tell the Updater to start working
updater.start_polling()

# make echo function
def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

# add caps command
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
                         bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

# to enable our bot to respond to inline queries, we can add the following (also talk to botfather)
from telegram import InlineQueryResultArticle
def inline_caps(bot, update):
    query = bot.update.inline_query.query
    results = list()
    results.append(InlineQueryResultArticle(query.upper(), 'Caps', query.upper()))
    bots.answerInlineQuery(update.inline_query.id, results)


InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# make a regexHandler to recognize unrecognizable commands (add last to CommandHandler)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry I didn't understand that command.")

unknown_handler = RegexHandler(r'/.*', unknown)
dispatcher.add_handler(unknown_handler)

# to stop bot
update.stop()


# JobQueue allows to perform tasks with delay or periodically
from telegram.ext import Updater
u = Updater(TOKEN)
j = u.job_queue

# prevent autostart
def job1(bot):
    bot.sendMessage(chat_id='@examplechannel', text='One message every minute')
j.put(job1, 60, next_t=0, prevent_autostart=True)

# no repeated job
def job2(bot):
    bot.sendMessage(chat_id='@examplechannel', text='A single message with 30s delay')
j.put(job2, 30, repeat=False)

# JobQueue stops with updater
u.stop()

# can also stop JobQueue by itself
j.stop()

# use logger
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

