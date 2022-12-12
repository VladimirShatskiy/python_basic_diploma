import telebot

from typing import Callable
from config_data import config
from handlers import default_handlers

bot = telebot.TeleBot(config.BOT_TOKEN)


def start_bot():
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower() == "привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text.lower() == 'help':
            default_handlers.help.bot_help(message)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши help")
    bot.polling(none_stop=True, interval=0)


def hotel_lower_price(city: str = None) -> dict:
    """
    Telegram: /lowprice
    ф-ция поиска отелей по минимальной цене в заданном городе

    вывод информации в bot
    ● название отеля,
    ● адрес,
    ● как далеко расположен от центра,
    ● цена,
    ● N фотографий отеля (если пользователь счёл необходимым их вывод)

    :param city: Название города
    :return: dict Список отелей
    """
    pass


def hotel_high_price(city: str = None) -> dict:
    """
    Telegram: /highprice
    ф-ция поиска отелей по максимальной стоимости в заданном городе

    вывод информации в bot
    ● название отеля,
    ● адрес,
    ● как далеко расположен от центра,
    ● цена,
    ● N фотографий отеля (если пользователь счёл необходимым их вывод)

    :param city: Название города
    :return: dict Список отелей
    """

    pass


def hotel_best_deal(city: str = None) -> dict:
    """
    Telegram: /bestdeal
    ф-ция поиска отелей по заданным условиям в городе
    условия
    ● Диапазон цен.
    ● Диапазон расстояния, на котором находится отель от центра.
    ● Количество отелей, которые необходимо вывести в результате

    вывод информации в bot
    ● название отеля,
    ● адрес,
    ● как далеко расположен от центра,
    ● цена,
    ● N фотографий отеля (если пользователь счёл необходимым их вывод)

    :param city: Название города
    :return: dict Список отелей
    """





def hotel_history() -> None:
    """
    telegram: /history
    выводит в бот историю
    ● Команду, которую вводил пользователь.
    ● Дату и время ввода команды.
    ● Отели, которые были найдены.
    :return: None
    """
    pass


def hotel_history_writer(func: str) -> Callable:
    """
    Обертка, записывает в ID файл пользователя информацию
    ● Команду, которую вводил пользователь.
    ● Дату и время ввода команды.
    ● Отели, которые были найдены.
    :param func: str
    :return: None
    """
    pass


if __name__ == '__main__':

    start_bot()
