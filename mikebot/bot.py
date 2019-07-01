from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
#    user_data['emo'] = emo уже не нужно
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text)

def send_cat_picture(bot, update, user_data):
    cats_list = glob('cats_images/*cat*.jp*g')
    cat_pic = choice(cats_list)
    bot.send_photo(chat_id=update.message.chat_id, photo = open(cat_pic, 'rb'))

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Hello {} {}! You wrote: '{}'.".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: %s, chat id: %s, Message: %s",
                update.message.chat.username,
                update.message.chat.id,
                update.message.text
                )
    update.message.reply_text(user_text)

def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']

def main():
    mikebot = Updater(settings.TG_API_KEY, request_kwargs = settings.PROXY)

    logging.info('Bot is starting')

    dp = mikebot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mikebot.start_polling()
    mikebot.idle()

if __name__ == "__main__":
    main()
