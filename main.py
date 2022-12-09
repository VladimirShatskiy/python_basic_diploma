import telebot

from typing import Callable
bot = telebot.TeleBot('5941899011:AAERS5iHo5oqBew2hBchG7PTRpYLt-9CXzI') # telegram @MyVeryFirstBot


def start_bot():
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower() == "привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text.lower() == 'help':
            hotel_help(message)
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


def hotel_help(message) -> None:
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
