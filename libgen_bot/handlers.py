'''
Command handlers, MessageHandlers here 

'''

from libgen import api
from emoji import emojize
from telegram.parsemode import ParseMode
from telegram import ChatAction


def start(bot, update):
    import ipdb ; ipdb.set_trace()
    bot.send_message(chat_id=update.messsage.chat_id, text='Im the bot you have been looking for quite sometime!!')

def search(bot, update, args):
    query_text = ' '.join(args)
    
    
    results = api.search(query_text)
    # import ipdb ; ipdb.set_trace()
    bot.send_message(chat_id=update.message.chat_id, text=(emojize_book_list(results) if results  else 'No results Found!!'), parse_mode=ParseMode.HTML)

def fetch(bot, update):
    pass

def emojize_book_list(books):
    return '\n'.join(map(lambda book: emojize(':blue_book:' + book['title'] + book['author'] + '</br><a href="/get' + book['md5'] + '">[/get'+ book['md5'] +']</a>') , books))

def test(bot, update, args):
    results = api.search(' '.join(args))
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text=(emojize_book_list(results) if results  else 'No results Found!!'), parse_mode=ParseMode.HTML)



