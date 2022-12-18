import telebot

from config_data import config
from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
import handlers

from telebot.types import Message

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
    print('jhjhjgjh')


if __name__ == '__main__':

    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )

    bot.infinity_polling()