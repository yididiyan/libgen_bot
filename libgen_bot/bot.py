import logging

from telegram import MessageEntity
from  telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from handlers import start,search, test
from config import API_KEY



## Handlers 


if __name__== '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

    updater = Updater(API_KEY)
    dispather = updater.dispatcher


    search_handler = CommandHandler('search', test, pass_args=True)
    test_handler = CommandHandler('test', test, pass_args=True)

    ## Add handlers to dispatcher
    dispather.add_handler(search_handler)
    dispather.add_handler(test_handler)
    
    print('INFO: Starting bot... ')
    updater.start_polling()
    print('INFO: Bot has started')
    