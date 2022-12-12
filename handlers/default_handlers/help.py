from telebot.types import Message
from main import bot


def bot_help(message) -> None:
    """
    Telegram: /help
    Вывод информации по функциям и подсказкам
    :return: None
    """
    str_help = "Я пока в стадии разрабoтки \n\n" \
               "в самое ближайшее время можно будет с помощью меня узнать\n" \
               "1. Tоп самых дешёвых отелей в городе (команда /lowprice).\n" \
               "2. Tоп самых дорогих отелей в городе (команда /highprice).\n" \
               "3. Tоп отелей, наиболее подходящих по цене и расположению от центра (команда /bestdeal)\n" \
               "4. Узнать историю поиска отелей (команда /history)\n"
    bot.send_message(message.from_user.id, str_help)