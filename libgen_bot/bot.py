import logging, re

from telegram import MessageEntity
from  telegram.ext import Updater, MessageHandler, Filters, CommandHandler, RegexHandler

from handlers import start,search, fetch, search_with_out_command
from config import API_KEY



## Handlers


if __name__== '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, search_with_out_command)
    start_handler = CommandHandler('start', start)
    search_handler = CommandHandler('search', search, pass_args=True)
    test_handler = CommandHandler('test', search, pass_args=True)
    fetch_handler = RegexHandler(re.compile('/get[0-9A-F]{32}'), fetch, pass_chat_data=True)


    ## Add handlers to dispatcher
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_handler)
    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(fetch_handler)

    print('INFO: Starting bot... ')
    updater.start_polling()
    print('INFO: Bot has started')
