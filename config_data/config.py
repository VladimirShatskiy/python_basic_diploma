import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
X_RapidAPI_Host = "hotels4.p.rapidapi.com"
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
