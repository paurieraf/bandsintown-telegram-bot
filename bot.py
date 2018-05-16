import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import logging

from app.bandsintown import BandsInTown
import app.responser as responser

load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

bands_in_town = BandsInTown()
#responser = Responser()


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    #artist_dict = bands_in_town.fetch_artist(update.message.text)
    #artist_event_dict = bands_in_town.fetch_artist_events(update.message.text)
    # update.message.reply_text(responser.create_artist_response(artist_dict))
    update.message.reply_text(update.message.text)


def get_artist_info(bot, update, args):
    artist_name = ''
    for arg in args:
        artist_name = artist_name + ' ' + arg

    artist_dict = bands_in_town.fetch_artist(artist_name.strip())
    update.message.reply_text(responser.create_artist_response(artist_dict))


def get_artist_events(bot, update, args):
    artist_name = ''
    for arg in args:
        artist_name = artist_name + ' ' + arg

    artist_events_list = bands_in_town.fetch_artist_events(artist_name.strip())

    update.message.reply_text(
        responser.create_artist_events_response(artist_events_list))


def get_artist_events_spain(bot, update, args):
    artist_name = ''
    for arg in args:
        artist_name = artist_name + ' ' + arg

    artist_events_list = bands_in_town.fetch_artist_events(
        artist_name.strip(), country="Spain")

    update.message.reply_text(
        responser.create_artist_events_response(artist_events_list))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.getenv('TELEGRAM_BOT_API'))

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("artist", get_artist_info,
                                  pass_args=True))
    dp.add_handler(CommandHandler("events", get_artist_events,
                                  pass_args=True))
    dp.add_handler(CommandHandler("events_spain", get_artist_events_spain,
                                  pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
