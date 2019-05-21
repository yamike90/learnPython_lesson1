from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


def greet_user(bot, update):
    text = '/start is called'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Hello {}! You wrote: '{}'.".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, chat id: %s, Message: %s",
                update.message.chat.username,
                update.message.chat.id,
                update.message.text
                )
    update.message.reply_text(user_text)

def main():
    mikebot = Updater(settings.TG_API_KEY, request_kwargs = settings.PROXY)

    logging.info('Bot is starting')

    dp = mikebot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mikebot.start_polling()
    mikebot.idle()

main()
