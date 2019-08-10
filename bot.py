# -*- coding: utf-8 -*-

import telebot
import os
import random
import sched
import pyowm
import datetime
import time
import emoji

bot = telebot.TeleBot('955970689:AAGNqX-pUAwc__4tjbCLdVzav9OSTX8yoic')

def msg():
   bot.send_message(message.chat.id, 'Доброго ранку!Як спалося?')
   schedule.every(1).minutes.do(msg)
   schedule.every().day.at("09:30").do(msg)

   while 1:
       schedule.run_pending()
       for i in range(1):
           time.sleep(1)

#клавіатура
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)#1-автоматичний розмір,2-тимчасова
    user_markup.row('/start', '/help')
    user_markup.row('memes(images)', 'memes(video)')
    user_markup.row('/game')
    bot.send_message(message.from_user.id, 'Бот готовий до розмови!', reply_markup=user_markup)
#клавіатура
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Список команд :\n /start - розпачати діалог\n /help - список команд\n/jokes-кину тобі меми')

@bot.message_handler(commands=['game'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Вгадай число від 0-2000 і виграй від мене шоколадку!\nПиши до тих пір, поки бот не напише ти виграв!')

@bot.message_handler(commands=['jokes'])
def start_message(message):
    directory = "/memes(images)"
    all_files_in_directory = os.listdir(directory)
    random_file = random.choice(all_files_in_directory)
    img = open(directory + '/' + random_file, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    img.close()

@bot.message_handler(content_types=['text'])
def start_message(message):

    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'привіт!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
        #відправка фотографій рандомних
    elif message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'hello!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хелло':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хелло!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хеллов':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хеллов!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хело':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хело!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хелов':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'хелов!':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
        #відправка фотографій рандомних
    elif message.text.lower() == 'ти мене задовбав':
        bot.send_message(message.chat.id, 'Я багато чого довбав)')
    elif message.text.lower() == 'ти мене задовбав!':
        bot.send_message(message.chat.id, 'Я багато чого довбав)')
    elif message.text.lower() == 'ти мене задовбуєш!':
        bot.send_message(message.chat.id, 'Я багато чого довбав)')
    elif message.text.lower() == 'ти мене задовбуєш':
        bot.send_message(message.chat.id, 'Я багато чого довбав)')
        #відправка фотографій рандомних
    elif message.text.lower() == 'ти шо тупий':
        bot.send_message(message.chat.id, 'Це одна з твоїх найголовніших рис)')
        #відправка фотографій рандомних
    elif message.text.lower() == 'ти шо такий розумний?':
        bot.send_message(message.chat.id, 'Цієї риси тобі бракує =)')
    elif message.text.lower() == 'ти шо такий розумний':
        bot.send_message(message.chat.id, 'Цієї риси тобі бракує =)')
    elif message.text.lower() == 'пішов в дупу!':
        bot.send_message(message.chat.id, 'Практика показує, що я не зможу це зробити...')
    elif message.text.lower() == 'пішов в дупу':
        bot.send_message(message.chat.id, 'Практика показує, що я не зможу це зробити...')
    elif message.text.lower() == 'жаль':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'погано':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'добре':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'добре!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'іди в дупу!':
        bot.send_message(message.chat.id, 'Практика показує, що я не зможу це зробити...')
    elif message.text.lower() == 'іди в дупу':
        bot.send_message(message.chat.id, 'Практика показує, що я не зможу це зробити...')
    elif message.text.lower() == 'ну ти і розумний':
        bot.send_message(message.chat.id, 'Цієї риси тобі бракує =)')
    elif message.text.lower() == 'шо ти такий розумний?':
        bot.send_message(message.chat.id, 'Цієї риси тобі бракує =)')
    elif message.text.lower() == 'шо ти такий розумний':
        bot.send_message(message.chat.id, 'Цієї риси тобі бракує =)')
        #відправка фотографій рандомних
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Де?(Львів, Київ, Самбір,Старий Самбір, Одеса, Харків, Дніпро, Тернопільб Дрогобич, Рудки, Ралівка, Бісковичі, Хирів, Турка)')
        #Weather
    elif message.text.lower() == 'львів':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Lviv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = speed*3.6
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Львів зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
        #відправка фотографій рандомних
    elif message.text.lower() == 'самбір':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Sambir, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Самбір зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
    elif message.text.lower() == 'київ':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Kyiv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Київ зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
    elif message.text.lower() == 'дрогобич':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Drohobych, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Дрогобич зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'рудки':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Rudky, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Рудки зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'бісковичі':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Biskovychi, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Бісковичі зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'ралівка':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Ralevka, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Ралівка зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'хирів':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Khyriv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Хирів зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'турка':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Turka, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Турка зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'старий самбір':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Staryy Sambor, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Старий Самбір зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'харків':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Kharkiv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Харків зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'дніпро':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Dnipropetrovsk, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Старий Самбір зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'одеса':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Odessa, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Одеса зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'тернопіль':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Ternopil, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        speed = w.get_wind()["speed"]
        speed1 = round(speed*3.6, 2)
        humidity = w.get_humidity()
        bot.send_message(message.chat.id, 'В місті Тернопіль зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        bot.send_message(message.chat.id, 'Швидкість вітру: ' + str(speed1) + ' км/год')
        bot.send_message(message.chat.id, 'Вологість:' + str(humidity) + '%')
        #weather
    elif message.text.lower() == 'memes(images)':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
        #відправка фотографій рандомних
        #відпарвка відео
    elif message.text.lower() == 'memes(video)':
        directory = "memes(videos)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        video = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_message(message.chat.id, 'Зачекай будь ласка пару хвилин поки відео загрузиться')
        bot.send_video(message.from_user.id, video)
        video.close()
        #відпарвка відео
    elif message.text.lower() == 'мем':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемасики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемчики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемачики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусікі':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусіки':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусикі':
            directory = "memes(images)"
            all_files_in_directory = os.listdir(directory)
            random_file = random.choice(all_files_in_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    elif message.text.lower() == 'меми':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні меми':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні мемасики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні мемасики негайно':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'негайно мемасики':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемасики негайно':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'негайно меми':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'меми негайно':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'хочу мем':
        directory = "memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'йоу':
        bot.send_message( message.chat.id,'Йоу йоу')
    elif message.text.lower() == 'га':
        bot.send_message( message.chat.id,'Що?')
    elif message.text.lower() == 'гу':
        bot.send_message( message.chat.id,'Що?')
    elif message.text.lower() == 'го гуляти':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го гуляти!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов гуляти':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов гуляти!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го кататись':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го кататись!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов кататись':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов кататись!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го кататися':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го кататися!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов кататися':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов кататися!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гоо гуляти':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'го гуляти!':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоов гуляти':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоов гуляти!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гоо кататись':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоо кататись!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гов кататись':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоов кататись!':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоо кататися':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'гоо кататися!':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоов кататися':
        bot.send_message( message.chat.id,'Нооу')
    elif message.text.lower() == 'гоов кататися!':
        bot.send_message( message.chat.id,'Ноу')
    elif message.text.lower() == 'крутий бот':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'крутий бот!':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'круто':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'круто!':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'це круто':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'це круто!':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'йоу йоу':
        bot.send_message( message.chat.id,'Йоу йоу йоу')
    elif message.text.lower() == 'майнкрафт':
        bot.send_message( message.chat.id,'Ето моя жизнь!')
    elif message.text.lower() == 'майнкрафт!':
        bot.send_message( message.chat.id,'Ето моя жизнь!')
    elif message.text.lower() == 'minecraft':
        bot.send_message( message.chat.id,'Ето моя жизнь!')
    elif message.text.lower() == 'minecraft!':
        bot.send_message( message.chat.id,'Ето моя жизнь!')
    elif message.text.lower() == 'го майнкрафт':
        bot.send_message( message.chat.id,'Гоо!')
    elif message.text.lower() == 'го майнкрафт!':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го minecraft':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го minecraft!':
        bot.send_message( message.chat.id,'Гоооооо!')
    elif message.text.lower() == 'го майнкрафт':
        bot.send_message( message.chat.id,'Гооооо!')
    elif message.text.lower() == 'го майнкрафт!':
        bot.send_message( message.chat.id,'Гоооооооооо!')
    elif message.text.lower() == 'го minecraft':
        bot.send_message( message.chat.id,'Гооо!')
    elif message.text.lower() == 'го minecraft!':
        bot.send_message( message.chat.id,'Гоооо!')
    elif message.text.lower() == 'гов майнкрафт':
        bot.send_message( message.chat.id,'Гоо!')
    elif message.text.lower() == 'гов майнкрафт!':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'гов minecraft':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'гов minecraft!':
        bot.send_message( message.chat.id,'Гоооооо!')
    elif message.text.lower() == 'гов майнкрафт':
        bot.send_message( message.chat.id,'Гооооо!')
    elif message.text.lower() == 'гов майнкрафт!':
        bot.send_message( message.chat.id,'Гоооооооооо!')
    elif message.text.lower() == 'гов minecraft':
        bot.send_message( message.chat.id,'Гооо!')
    elif message.text.lower() == 'гов minecraft!':
        bot.send_message( message.chat.id,'Гоооо!')
    elif message.text.lower() == 'гов майнкрафт':
        bot.send_message( message.chat.id,'Гоо!')
    elif message.text.lower() == 'го в майнкрафт!':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го в minecraft':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го в minecraft!':
        bot.send_message( message.chat.id,'Гоооооо!')
    elif message.text.lower() == 'го в майнкрафт':
        bot.send_message( message.chat.id,'Гооооо!')
    elif message.text.lower() == 'го в майнкрафт!':
        bot.send_message( message.chat.id,'Гоооооооооо!')
    elif message.text.lower() == 'го в minecraft':
        bot.send_message( message.chat.id,'Гооо!')
    elif message.text.lower() == 'го в minecraft!':
        bot.send_message( message.chat.id,'Гоооо!')
    elif message.text.lower() == 'го у майнкрафт!':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го у minecraft':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'го у minecraft!':
        bot.send_message( message.chat.id,'Гоооооо!')
    elif message.text.lower() == 'го у майнкрафт':
        bot.send_message( message.chat.id,'Гооооо!')
    elif message.text.lower() == 'го у майнкрафт!':
        bot.send_message( message.chat.id,'Гоооооооооо!')
    elif message.text.lower() == 'го у minecraft':
        bot.send_message( message.chat.id,'Гооо!')
    elif message.text.lower() == 'го у minecraft!':
        bot.send_message( message.chat.id,'Гоооо!')
    elif message.text.lower() == 'гов в майнкрафт':
        bot.send_message( message.chat.id,'Гоо!')
    elif message.text.lower() == 'гов в майнкрафт!':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'гов в minecraft':
        bot.send_message( message.chat.id,'Гооооооо!')
    elif message.text.lower() == 'гов в minecraft!':
        bot.send_message( message.chat.id,'Гоооооо!')
    elif message.text.lower() == 'гов в майнкрафт':
        bot.send_message( message.chat.id,'Гооооо!')
    elif message.text.lower() == 'гов в майнкрафт!':
        bot.send_message( message.chat.id,'Гоооооооооо!')
    elif message.text.lower() == 'гов в minecraft':
        bot.send_message( message.chat.id,'Гооо!')
    elif message.text.lower() == 'гов в minecraft!':
        bot.send_message( message.chat.id,'Гоооо!')
    elif message.text.lower() == 'гов в майнкрафт':
        bot.send_message( message.chat.id,'Гоо!')
    elif message.text.lower() == 'мінекрафт':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'мінекрафт!':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'минекрафт':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'минекрафт!':
        bot.send_message( message.chat.id,'Ага)')
    elif message.text.lower() == 'йоу братан':
        bot.send_message( message.chat.id,'Йоу йоу')
    elif message.text.lower() == 'ну шо там?':
        bot.send_message( message.chat.id,'Та ніц)')
    elif message.text.lower() == 'ну шо там':
        bot.send_message( message.chat.id,'Та ніц, все ок)')
    elif message.text.lower() == 'шо там?':
        bot.send_message( message.chat.id,'Та ніц)')
    elif message.text.lower() == 'шо там':
        bot.send_message( message.chat.id,'Та ніц, все ок)')
    elif message.text.lower() == 'ти що робиш?':
        bot.send_message( message.chat.id,'Та ніц')
    elif message.text.lower() == 'ти що робиш':
        bot.send_message( message.chat.id,'Та ніц')
    elif message.text.lower() == 'ти шо робиш?':
        bot.send_message( message.chat.id,'Та ніц')
    elif message.text.lower() == 'ти шо робиш':
        bot.send_message( message.chat.id,'Та ніц')
    elif message.text.lower() == 'ким ти був створений?':
        bot.send_message( message.chat.id,'@feynom')
    elif message.text.lower() == 'ким ти був створений':
        bot.send_message( message.chat.id,'@feynom')
    elif message.text.lower() == 'йоу йоу йоу':
        bot.send_message( message.chat.id,'Йоу йоу йоу йоу')
    elif message.text.lower() == 'яка година?':
        bot.send_message( message.chat.id,'Зараз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено?':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено в останній раз':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено в останній раз?':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено в останній час':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе було запущено в останній час?':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе запустив розробник?':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли тебе запустив розробник':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли був запущений бот?':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'коли був запущений бот':
        bot.send_message( message.chat.id,'Було запущено в останній раз:' + str(time) )
    elif message.text.lower() == 'хай':
        bot.send_message(message.chat.id, 'Хай, бро!Як справи?')
    elif message.text.lower() == 'а у тебе?':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'а ти?':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'а ти':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'а у тебе':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'а в тебе':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'а в тебе?':
        bot.send_message(message.chat.id, 'Супер!')
    elif message.text.lower() == 'ага':
        pass
    elif message.text.lower() == 'ага!':
        pass
    elif message.text.lower() == 'агаа':
        pass
    elif message.text.lower() == 'агаа!':
        pass
    elif message.text.lower() == 'аагаа':
        pass
    elif message.text.lower() == 'аагаа!':
        pass
    elif message.text.lower() == 'ааггаа':
        pass
    elif message.text.lower() == 'ааггаа!':
        pass
    elif message.text.lower() == 'агга':
        pass
    elif message.text.lower() == 'агга!':
        pass
    elif message.text.lower() == 'чебурек':
        bot.send_message(message.chat.id, 'ага!')
    elif message.text.lower() == 'чебурек!':
        bot.send_message(message.chat.id, 'ага!')
    elif message.text.lower() == 'добрий':
        bot.send_message(message.chat.id, 'Як ся маєш?')
    elif message.text.lower() == 'ти шо?':
        bot.send_message(message.chat.id, 'Та нічо')
    elif message.text.lower() == 'ти шо':
        bot.send_message(message.chat.id, 'Та нічо')
    elif message.text.lower() == 'ти шо тупий?':
        bot.send_message(message.chat.id, 'На відміну від тебе ні)')
    elif message.text.lower() == 'супер':
        bot.send_message(message.chat.id, 'То добре')
    elif message.text.lower() == 'братуха':
        bot.send_message(message.chat.id, 'Я тобі не брат!')
    elif message.text.lower() == 'братан':
        bot.send_message(message.chat.id, 'Я тобі не брат!')
    elif message.text.lower() == 'брат':
        bot.send_message(message.chat.id, 'Я тобі не брат!')
    elif message.text.lower() == 'брат братан братуха':
        bot.send_message(message.chat.id, 'Я тобі не брат!')
    elif message.text.lower() == 'брат братан братуха!':
        bot.send_message(message.chat.id, 'Я тобі не брат!')
    elif message.text.lower() == 'чому?':
        bot.send_message(message.chat.id, 'Догадайся!')
    elif message.text.lower() == 'ти такий розумний?':
        bot.send_message(message.chat.id, 'Походу так)')
    elif message.text.lower() == 'ти такий розумний':
        bot.send_message(message.chat.id, 'Походу так)')
    elif message.text.lower() == 'чому':
        bot.send_message(message.chat.id, 'Догадайся!')
    elif message.text.lower() == 'найс':
        bot.send_message(message.chat.id, 'То добре')
    elif message.text.lower() == 'класно':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'норм':
        bot.send_message(message.chat.id, 'Добре')
    elif message.text.lower() == 'нормально':
        bot.send_message(message.chat.id, 'То добре')
    elif message.text.lower() == 'все погано':
        bot.send_message(message.chat.id, 'Вот печалька...')
    elif message.text.lower() == 'хм':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмм':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хммм':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмммм':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хм.':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмм.':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хммм.':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмммм.':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хм..':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмм..':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хммм..':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмммм':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хм...':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмм...':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хммм...':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хмммм...':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хи':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хии':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хиии':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'хииии':
        bot.send_message(message.chat.id, '...')
    elif message.text.lower() == 'погано':
        bot.send_message(message.chat.id, 'Вот печалька...')
    elif message.text.lower() == 'уляна зе бест':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'уляна іс бест':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'уляна найкраща':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'Уляна':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'уляна супер':
        bot.send_message(message.chat.id, 'ага')
    elif message.text.lower() == 'уляна зе бест!':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'уляна іс бест!':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'уляна найкраща!':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'Уляна!':
        bot.send_message(message.chat.id, 'Так так!')
    elif message.text.lower() == 'фе':
        pass
    elif message.text.lower() == 'фе!':
        pass
    elif message.text.lower() == 'фее':
        pass
    elif message.text.lower() == 'фее!':
        pass
    elif message.text.lower() == 'феее':
        pass
    elif message.text.lower() == 'феее!':
        pass
    elif message.text.lower() == 'фееее':
        pass
    elif message.text.lower() == 'фееее!':
        pass
    elif message.text.lower() == 'феееее':
        pass
    elif message.text.lower() == 'феееее!':
        pass
    elif message.text.lower() == 'фееееее':
        pass
    elif message.text.lower() == 'фееееее!':
        pass
    elif message.text.lower() == 'феееееее':
        pass
    elif message.text.lower() == 'феееееее!':
        pass
    elif message.text.lower() == 'ффе':
        pass
    elif message.text.lower() == 'ффе!':
        pass
    elif message.text.lower() == 'ффее':
        pass
    elif message.text.lower() == 'ффее!':
        pass
    elif message.text.lower() == 'ффеее':
        pass
    elif message.text.lower() == 'ффеее!':
        pass
    elif message.text.lower() == 'ффееее':
        pass
    elif message.text.lower() == 'ффееее!':
        pass
    elif message.text.lower() == 'ффеееее':
        pass
    elif message.text.lower() == 'ффеееее!':
        pass
    elif message.text.lower() == 'ффееееее':
        pass
    elif message.text.lower() == 'ффееееее!':
        pass
    elif message.text.lower() == 'ффеееееее':
        pass
    elif message.text.lower() == 'ффеееееее!':
        pass
    elif message.text.lower() == 'фффе':
        pass
    elif message.text.lower() == 'фффе!':
        pass
    elif message.text.lower() == 'фффее':
        pass
    elif message.text.lower() == 'фффее!':
        pass
    elif message.text.lower() == 'фффеее':
        pass
    elif message.text.lower() == 'фффеее!':
        pass
    elif message.text.lower() == 'фффееее':
        pass
    elif message.text.lower() == 'фффееее!':
        pass
    elif message.text.lower() == 'фффеееее':
        pass
    elif message.text.lower() == 'фффеееее!':
        pass
    elif message.text.lower() == 'фффееееее':
        pass
    elif message.text.lower() == 'фффееееее!':
        pass
    elif message.text.lower() == 'фффеееееее':
        pass
    elif message.text.lower() == 'фффеееееее!':
        pass
    elif message.text.lower() == 'ффффе':
        pass
    elif message.text.lower() == 'ффффе!':
        pass
    elif message.text.lower() == 'ффффее':
        pass
    elif message.text.lower() == 'ффффее!':
        pass
    elif message.text.lower() == 'ффффеее':
        pass
    elif message.text.lower() == 'ффффеее!':
        pass
    elif message.text.lower() == 'ффффееее':
        pass
    elif message.text.lower() == 'ффффееее!':
        pass
    elif message.text.lower() == 'ффффеееее':
        pass
    elif message.text.lower() == 'ффффеееее!':
        pass
    elif message.text.lower() == 'ффффееееее':
        pass
    elif message.text.lower() == 'ффффееееее!':
        pass
    elif message.text.lower() == 'ффффеееееее':
        pass
    elif message.text.lower() == 'ффффеееееее!':
        pass
    elif message.text.lower() == 'фффффе':
        pass
    elif message.text.lower() == 'фффффе!':
        pass
    elif message.text.lower() == 'фффффее':
        pass
    elif message.text.lower() == 'фффффее!':
        pass
    elif message.text.lower() == 'фффффеее':
        pass
    elif message.text.lower() == 'фффффеее!':
        pass
    elif message.text.lower() == 'фффффееее':
        pass
    elif message.text.lower() == 'фффффееее!':
        pass
    elif message.text.lower() == 'фффффеееее':
        pass
    elif message.text.lower() == 'фффффеееее!':
        pass
    elif message.text.lower() == 'фффффееееее':
        pass
    elif message.text.lower() == 'фффффееееее!':
        pass
    elif message.text.lower() == 'фффффеееееее':
        pass
    elif message.text.lower() == 'фффффеееееее!':
        pass
    elif message.text.lower() == 'фу':
        pass
    elif message.text.lower() == 'фу!':
        pass
    elif message.text.lower() == 'фу':
        pass
    elif message.text.lower() == 'фуу!':
        pass
    elif message.text.lower() == 'фууу':
        pass
    elif message.text.lower() == 'фууу!':
        pass
    elif message.text.lower() == 'фуууу':
        pass
    elif message.text.lower() == 'фуууу!':
        pass
    elif message.text.lower() == 'фууууу':
        pass
    elif message.text.lower() == 'фууууу!':
        pass
    elif message.text.lower() == 'фуууууу':
        pass
    elif message.text.lower() == 'фуууууу!':
        pass
    elif message.text.lower() == 'фууууууу':
        pass
    elif message.text.lower() == 'фууууууу!':
        pass
    elif message.text.lower() == 'ффу':
        pass
    elif message.text.lower() == 'ффу!':
        pass
    elif message.text.lower() == 'ффуу':
        pass
    elif message.text.lower() == 'ффуу!':
        pass
    elif message.text.lower() == 'ффууу':
        pass
    elif message.text.lower() == 'ффууу!':
        pass
    elif message.text.lower() == 'ффуууу':
        pass
    elif message.text.lower() == 'ффуууу!':
        pass
    elif message.text.lower() == 'ффууууу':
        pass
    elif message.text.lower() == 'ффууууу!':
        pass
    elif message.text.lower() == 'ффуууууу':
        pass
    elif message.text.lower() == 'ффуууууу!':
        pass
    elif message.text.lower() == 'ффууууууу':
        pass
    elif message.text.lower() == 'ффууууууу!':
        pass
    elif message.text.lower() == 'фффу':
        pass
    elif message.text.lower() == 'фффу!':
        pass
    elif message.text.lower() == 'фффуу':
        pass
    elif message.text.lower() == 'фффуу!':
        pass
    elif message.text.lower() == 'фффууу':
        pass
    elif message.text.lower() == 'фффууу!':
        pass
    elif message.text.lower() == 'фффуууу':
        pass
    elif message.text.lower() == 'фффуууу!':
        pass
    elif message.text.lower() == 'фффууууу':
        pass
    elif message.text.lower() == 'фффууууу!':
        pass
    elif message.text.lower() == 'фффуууууу':
        pass
    elif message.text.lower() == 'фффуууууу!':
        pass
    elif message.text.lower() == 'фффууууууу':
        pass
    elif message.text.lower() == 'фффууууууу!':
        pass
    elif message.text.lower() == 'ффффу':
        pass
    elif message.text.lower() == 'ффффу!':
        pass
    elif message.text.lower() == 'ффффуу':
        pass
    elif message.text.lower() == 'ффффуу!':
        pass
    elif message.text.lower() == 'ффффууу':
        pass
    elif message.text.lower() == 'ффффууу!':
        pass
    elif message.text.lower() == 'ффффуууу':
        pass
    elif message.text.lower() == 'ффффуууу!':
        pass
    elif message.text.lower() == 'ффффууууу':
        pass
    elif message.text.lower() == 'ффффууууу!':
        pass
    elif message.text.lower() == 'ффффуууууу':
        pass
    elif message.text.lower() == 'ффффуууууу!':
        pass
    elif message.text.lower() == 'ффффууууууу':
        pass
    elif message.text.lower() == 'ффффууууууу!':
        pass
    elif message.text.lower() == 'фффффу':
        pass
    elif message.text.lower() == 'фффффу!':
        pass
    elif message.text.lower() == 'фффффуу':
        pass
    elif message.text.lower() == 'фффффуу!':
        pass
    elif message.text.lower() == 'фффффууу':
        pass
    elif message.text.lower() == 'фффффууу!':
        pass
    elif message.text.lower() == 'фффффуууу':
        pass
    elif message.text.lower() == 'фффффуууу!':
        pass
    elif message.text.lower() == 'фффффууууу':
        pass
    elif message.text.lower() == 'фффффууууу!':
        pass
    elif message.text.lower() == 'фффффуууууу':
        pass
    elif message.text.lower() == 'фффффуууууу!':
        pass
    elif message.text.lower() == 'фффффууууууу':
        pass
    elif message.text.lower() == 'фффффууууууу!':
        pass
    elif message.text.lower() == 'як не гарно':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'як не гарно!':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'як негарно':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'як негарно!':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'не гарно':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'не гарно!':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'негарно':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'негарно!':
        bot.send_message(message.chat.id, '???')
    elif message.text.lower() == 'вжух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууух':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууухх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжуууххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууухххх':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вжжжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввжжжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'вввжжжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууух!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууухх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжуууххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'ввввжжжууухххх!':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == 'уляна супер!':
        bot.send_message(message.chat.id, 'ага')
    elif message.text.lower() == 'супер уляна!':
        bot.send_message(message.chat.id, 'ага')
    elif message.text.lower() == 'супер уляна':
        bot.send_message(message.chat.id, 'ага')
    elif message.text.lower() == 'поганий бот':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'бот поганий':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'найгірший бот':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'бот найгірший':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'поганий бот!':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'бот поганий!':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'найгірший бот!':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'бот найгірший!':
        bot.send_message(message.chat.id, 'Ні!')
    elif message.text.lower() == 'все задовбало':
        bot.send_message(message.chat.id, 'Вот печалька...')
    elif message.text.lower() == 'все задовбало!':
        bot.send_message(message.chat.id, 'Вот печалька...')
    elif message.text.lower() == 'добрий день':
        bot.send_message(message.chat.id, 'Як ся маєш?')
    elif message.text.lower() == 'добрий день!':
        bot.send_message(message.chat.id, 'Як ся маєш?')
    elif message.text.lower() == 'хай!':
        bot.send_message(message.chat.id, 'Хай, бро!Як справи?')
    elif message.text.lower() == 'хай':
        bot.send_message(message.chat.id, 'Хай, бро!Як справи?')
    elif message.text.lower() == 'лол':
        pass
    elif message.text.lower() == 'лол!':
        pass
    elif message.text.lower() == 'лол кек':
        pass
    elif message.text.lower() == 'кек лол':
        pass
    elif message.text.lower() == 'лол кек!':
        pass
    elif message.text.lower() == 'кек лол!':
        pass
    elif message.text.lower() == 'лул':
        pass
    elif message.text.lower() == 'лул!':
        pass
    elif message.text.lower() == 'кек':
        bot.send_message(message.chat.id, 'Лол кек чебурек=)')
    elif message.text.lower() == 'кек!':
        bot.send_message(message.chat.id, 'Лол кек чебурек=)')
    elif message.text.lower() == 'здоров':
        bot.send_message(message.chat.id, 'Добрий день панове!Як справи?')
    elif message.text.lower() == 'здоров!':
        bot.send_message(message.chat.id, 'Добрий день панове!Як справи?')
    elif message.text.lower() == 'хто ти?':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'як тебе звати':
        bot.send_message(message.chat.id, 'Мене звати FoBOT!')
    elif message.text.lower() == 'як тебе звати?':
        bot.send_message(message.chat.id, 'Мене звати FoBOT!')
    elif message.text.lower() == 'хто ти':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'хто ти є':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'хто ти є?':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'ти хто?':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'ти хто':
        bot.send_message(message.chat.id, 'Я FoBOT!')
    elif message.text.lower() == 'ух ти':
        pass
    elif message.text.lower() == 'ухх ти':
        pass
    elif message.text.lower() == 'уххх ти':
        pass
    elif message.text.lower() == 'ухххх ти':
        pass
    elif message.text.lower() == 'уххххх ти':
        pass
    elif message.text.lower() == 'ухххххх ти':
        pass
    elif message.text.lower() == 'уххххххх ти':
        pass
    elif message.text.lower() == 'ухххххххх ти':
        pass
    elif message.text.lower() == 'уххххххххх ти':
        pass
    elif message.text.lower() == 'ух ти!':
        pass
    elif message.text.lower() == 'ухх ти!':
        pass
    elif message.text.lower() == 'уххх ти!':
        pass
    elif message.text.lower() == 'ухххх ти!':
        pass
    elif message.text.lower() == 'уххххх ти!':
        pass
    elif message.text.lower() == 'ухххххх ти!':
        pass
    elif message.text.lower() == 'уххххххх ти!':
        pass
    elif message.text.lower() == 'ухххххххх ти!':
        pass
    elif message.text.lower() == 'уххххххххх ти!':
        pass
    elif message.text.lower() == 'ухти!':
        pass
    elif message.text.lower() == 'уххти!':
        pass
    elif message.text.lower() == 'ухххти!':
        pass
    elif message.text.lower() == 'уххххти!':
        pass
    elif message.text.lower() == 'ухххххти!':
        pass
    elif message.text.lower() == 'уххххххти!':
        pass
    elif message.text.lower() == 'ухххххххти!':
        pass
    elif message.text.lower() == 'уххххххххти!':
        pass
    elif message.text.lower() == 'ухххххххххти!':
        pass
    elif message.text.lower() == 'уухх ти':
        pass
    elif message.text.lower() == 'ууххх ти':
        pass
    elif message.text.lower() == 'уухххх ти':
        pass
    elif message.text.lower() == 'ууххххх ти':
        pass
    elif message.text.lower() == 'уухххххх ти':
        pass
    elif message.text.lower() == 'ууххххххх ти':
        pass
    elif message.text.lower() == 'уухххххххх ти':
        pass
    elif message.text.lower() == 'ууххххххххх ти':
        pass
    elif message.text.lower() == 'уух ти!':
        pass
    elif message.text.lower() == 'уухх ти!':
        pass
    elif message.text.lower() == 'ууххх ти!':
        pass
    elif message.text.lower() == 'уухххх ти!':
        pass
    elif message.text.lower() == 'ууххххх ти!':
        pass
    elif message.text.lower() == 'уухххххх ти!':
        pass
    elif message.text.lower() == 'ууххххххх ти!':
        pass
    elif message.text.lower() == 'уухххххххх ти!':
        pass
    elif message.text.lower() == 'ууххххххххх ти!':
        pass
    elif message.text.lower() == 'уухти!':
        pass
    elif message.text.lower() == 'ууххти!':
        pass
    elif message.text.lower() == 'уухххти!':
        pass
    elif message.text.lower() == 'ууххххти!':
        pass
    elif message.text.lower() == 'уухххххти!':
        pass
    elif message.text.lower() == 'ууххххххти!':
        pass
    elif message.text.lower() == 'уухххххххти!':
        pass
    elif message.text.lower() == 'ууххххххххти!':
        pass
    elif message.text.lower() == 'уухххххххххти!':
        pass
    elif message.text.lower() == 'ууухх ти':
        pass
    elif message.text.lower() == 'уууххх ти':
        pass
    elif message.text.lower() == 'ууухххх ти':
        pass
    elif message.text.lower() == 'уууххххх ти':
        pass
    elif message.text.lower() == 'ууухххххх ти':
        pass
    elif message.text.lower() == 'уууххххххх ти':
        pass
    elif message.text.lower() == 'ууухххххххх ти':
        pass
    elif message.text.lower() == 'уууххххххххх ти':
        pass
    elif message.text.lower() == 'ууух ти!':
        pass
    elif message.text.lower() == 'ууухх ти!':
        pass
    elif message.text.lower() == 'уууххх ти!':
        pass
    elif message.text.lower() == 'ууухххх ти!':
        pass
    elif message.text.lower() == 'уууххххх ти!':
        pass
    elif message.text.lower() == 'ууухххххх ти!':
        pass
    elif message.text.lower() == 'уууххххххх ти!':
        pass
    elif message.text.lower() == 'ууухххххххх ти!':
        pass
    elif message.text.lower() == 'уууххххххххх ти!':
        pass
    elif message.text.lower() == 'ууухти!':
        pass
    elif message.text.lower() == 'уууххти!':
        pass
    elif message.text.lower() == 'ууухххти!':
        pass
    elif message.text.lower() == 'уууххххти!':
        pass
    elif message.text.lower() == 'ууухххххти!':
        pass
    elif message.text.lower() == 'уууххххххти!':
        pass
    elif message.text.lower() == 'ууухххххххти!':
        pass
    elif message.text.lower() == 'уууххххххххти!':
        pass
    elif message.text.lower() == 'ууухххххххххти!':
        pass
    elif message.text.lower() == 'уууухх ти':
        pass
    elif message.text.lower() == 'ууууххх ти':
        pass
    elif message.text.lower() == 'уууухххх ти':
        pass
    elif message.text.lower() == 'ууууххххх ти':
        pass
    elif message.text.lower() == 'уууухххххх ти':
        pass
    elif message.text.lower() == 'ууууххххххх ти':
        pass
    elif message.text.lower() == 'уууухххххххх ти':
        pass
    elif message.text.lower() == 'ууууххххххххх ти':
        pass
    elif message.text.lower() == 'уууух ти!':
        pass
    elif message.text.lower() == 'уууухх ти!':
        pass
    elif message.text.lower() == 'ууууххх ти!':
        pass
    elif message.text.lower() == 'уууухххх ти!':
        pass
    elif message.text.lower() == 'ууууххххх ти!':
        pass
    elif message.text.lower() == 'уууухххххх ти!':
        pass
    elif message.text.lower() == 'ууууххххххх ти!':
        pass
    elif message.text.lower() == 'уууухххххххх ти!':
        pass
    elif message.text.lower() == 'ууууххххххххх ти!':
        pass
    elif message.text.lower() == 'уууухти!':
        pass
    elif message.text.lower() == 'ууууххти!':
        pass
    elif message.text.lower() == 'уууухххти!':
        pass
    elif message.text.lower() == 'ууууххххти!':
        pass
    elif message.text.lower() == 'уууухххххти!':
        pass
    elif message.text.lower() == 'ууууххххххти!':
        pass
    elif message.text.lower() == 'уууухххххххти!':
        pass
    elif message.text.lower() == 'ууууххххххххти!':
        pass
    elif message.text.lower() == 'уууухххххххххти!':
        pass
    elif message.text.lower() == 'ок':
        bot.send_message(message.chat.id, 'ОК')
    elif message.text.lower() == 'ok':
        bot.send_message(message.chat.id, 'ОК')
    elif message.text.lower() == 'хто тебе створив':
        bot.send_message(message.chat.id, 'Мій творець: @feynom')
    elif message.text.lower() == 'хто твій розробник?':
        bot.send_message(message.chat.id, 'Мій творець: @feynom')
    elif message.text.lower() == 'хто твій розробник':
        bot.send_message(message.chat.id, 'Мій творець: @feynom')
    elif message.text.lower() == 'хто тебе створив?':
        bot.send_message(message.chat.id, 'Мій творець: @feynom')
    elif message.text.lower() == 'як справи?':
        bot.send_message(message.chat.id, 'Норм')
    elif message.text.lower() == 'як справи':
        bot.send_message(message.chat.id, 'Норм')
    elif message.text.lower() == 'як ся маєш':
        bot.send_message(message.chat.id, 'Супер')
    elif message.text.lower() == 'як ся маєш?':
        bot.send_message(message.chat.id, 'Супер')
    elif message.text.lower() == 'як у тебе справи':
        bot.send_message(message.chat.id, 'Норм')
    elif message.text.lower() == 'як у тебе справи?':
        bot.send_message(message.chat.id, 'Норм')
    elif message.text.lower() == 'шо таке?':
        bot.send_message(message.chat.id, 'Та ніц')
    elif message.text.lower() == 'шо таке':
        bot.send_message(message.chat.id, 'Та ніц')
    elif message.text.lower() == 'що таке?':
        bot.send_message(message.chat.id, 'Та ніц')
    elif message.text.lower() == 'що таке':
        bot.send_message(message.chat.id, 'Та ніц')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'пока!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'допобачення!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'допобачення':
        bot.send_message(message.chat.id, 'Допобачення')
        #образи
    elif message.text.lower() == 'ти лох':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'лошара':
            bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'вася лох':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'вася лох!':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'лашара':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'ти тупий':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'тупий бот':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'ти говно':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'говно а не бот':
        bot.send_message(message.chat.id, 'САМ ТИ ГОВНО!')
    elif message.text.lower() == 'говно, а не бот':
        bot.send_message(message.chat.id, 'САМ ТИ ГОВНО!')
    elif message.text.lower() == 'говнобот':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'говно-бот':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот-говно':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот говно':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот гавно':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'ти тупий бот':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'ти тупий бот!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот-гавно':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'лошпєндос':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'лошпэндос':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'лашара!':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'ти тупий!':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'курка':
        bot.send_message(message.chat.id, 'Нэ')
    elif message.text.lower() == 'курка!':
        bot.send_message(message.chat.id, 'Нэ')
    elif message.text.lower() == 'тупий бот!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'ти говно!':
        bot.send_message(message.chat.id, 'САМ ТАКИЙ!')
    elif message.text.lower() == 'говно а не бот!':
        bot.send_message(message.chat.id, 'САМ ТИ ГОВНО!')
    elif message.text.lower() == 'говно, а не бот!':
        bot.send_message(message.chat.id, 'САМ ТИ ГОВНО!')
    elif message.text.lower() == 'говнобот!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'говно-бот!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот-говно!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот говно!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот гавно!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'бот-гавно!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'лошпєндос!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'лошпэндос!':
        bot.send_message(message.chat.id, 'ТОДІ НАПИШИ КРАЩИЙ!')
    elif message.text.lower() == 'странно':
        bot.send_message(message.chat.id, 'НЕА')
    elif message.text.lower() == 'странно!':
        bot.send_message(message.chat.id, 'НЕА')
    elif message.text.lower() == 'дивно':
        bot.send_message(message.chat.id, 'НЕА')
    elif message.text.lower() == 'дивно!':
        bot.send_message(message.chat.id, 'НЕА')
    elif message.text.lower() == 'йой':
        bot.send_message(message.chat.id, 'Йой')
    elif message.text.lower() == 'бубка':
        bot.send_message(message.chat.id, 'Йой')
    elif message.text.lower() == 'бубка на связі':
        bot.send_message(message.chat.id, 'Добрий день Валентин!')
    elif message.text.lower() == 'гусь':
        bot.send_message(message.chat.id, ' "Молчать" валік')
    elif message.text.lower() == 'гусяра':
        bot.send_message(message.chat.id, '"Молчать" валік')
    elif message.text.lower() == 'йой!':
        bot.send_message(message.chat.id, 'Йой')
    elif message.text.lower() == 'бубка!':
        bot.send_message(message.chat.id, 'Йой')
    elif message.text.lower() == 'бубка на связі!':
        bot.send_message(message.chat.id, 'Добрий день Валентин!')
    elif message.text.lower() == 'гусь!':
        bot.send_message(message.chat.id, ' "Молчать" валік')
    elif message.text.lower() == 'гусяра!':
        bot.send_message(message.chat.id, '"Молчать" валік')
    elif message.text.lower() == 'курка!':
        pass
    elif message.text.lower() == 'курка':
        pass
    elif message.text.lower() == 'шо вмієш':
        bot.send_message(message.chat.id, 'Багато чого')
    elif message.text.lower() == 'що вмієш':
        bot.send_message(message.chat.id, 'Багато чого')
    elif message.text.lower() == 'шо вмієш?':
        bot.send_message(message.chat.id, 'Багато чого')
    elif message.text.lower() == 'що вмієш?':
        bot.send_message(message.chat.id, 'Багато чого')
    elif message.text.lower() == 'чурка':
        bot.send_message(message.chat.id, 'Сам ти чурка')
    elif message.text.lower() == 'чурка!':
        bot.send_message(message.chat.id, 'Сам ти чурка')
    elif message.text.lower() == 'йов!':
        bot.send_message(message.chat.id, 'Йов!')
    elif message.text.lower() == 'йов':
        bot.send_message(message.chat.id, 'Йов!')
    elif message.text.lower() == 'добраніч':
        bot.send_message(message.chat.id, 'Гарних снів!')
    elif message.text.lower() == 'добраніч!':
        bot.send_message(message.chat.id, 'Гарних снів!')
    elif message.text.lower() == 'добрий ранок!':
        bot.send_message(message.chat.id, 'Як сни?')
    elif message.text.lower() == 'добрий ранок':
        bot.send_message(message.chat.id, 'Як сни?')
    elif message.text.lower() == 'голова болить!':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'голова болить':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'болить голова':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'болить голова!':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'мене голова болить!':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'мене голова болить':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'мене болить голова':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'мене болить голова!':
        bot.send_message(message.chat.id, 'Погано(')
    elif message.text.lower() == 'точно?':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'точно':
        pass
    elif message.text.lower() == 'точняк':
        pass
    elif message.text.lower() == 'точно приточно?':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'точно при точно?':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'я тобі подобаюсь':
        bot.send_message(message.chat.id, 'Не думаю, мене ніхто не бачив...')
    elif message.text.lower() == 'я тобі подобаюся':
        bot.send_message(message.chat.id, 'Не думаю, мене ніхто не бачив...')
    elif message.text.lower() == 'я тобі подобаюсь?':
        bot.send_message(message.chat.id, 'Неа...')
    elif message.text.lower() == 'я тобі подобаюся?':
        bot.send_message(message.chat.id, 'Неа...')
    elif message.text.lower() == 'я гарний?':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я гарна?':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я гарний':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я гарна':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я гарний!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'я гарна!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'я красива?':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я красивий?':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я красива!':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я красивий!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'я красива':
        bot.send_message(message.chat.id, 'Хз')
    elif message.text.lower() == 'я красивий':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'пс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'зараз приїду':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зараз приїду!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зара приїду':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зара приїду!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зараз буду':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зараз буду!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зара буду':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'зара буду!':
        bot.send_message(message.chat.id, 'Ага')
    elif message.text.lower() == 'псс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'псссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'пссссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссссс':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссссс.':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссссс..':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссссс...':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упсссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'упссссс....':
        bot.send_message(message.chat.id, 'Шо таке?')
    elif message.text.lower() == 'та ніц':
        pass
    elif message.text.lower() == 'та нічого':
        pass
    elif message.text.lower() == 'чом так?':
        bot.send_message(message.chat.id, 'Хз...')
    elif message.text.lower() == 'чом так':
        bot.send_message(message.chat.id, 'Хз...')
    elif message.text.lower() == 'чом так!':
        pass
    elif message.text.lower() == 'ага ага':
        pass
    elif message.text.lower() == 'ага ага ага':
        pass
    elif message.text.lower() == 'ага ага ага ага':
        pass
    elif message.text.lower() == 'ага ага ага ага ага':
        pass
    elif message.text.lower() == 'ага ага!':
        pass
    elif message.text.lower() == 'ага ага ага!':
        pass
    elif message.text.lower() == 'ага ага ага ага!':
        pass
    elif message.text.lower() == 'ага ага ага ага ага!':
        pass
    elif message.text.lower() == 'иги иги':
        pass
    elif message.text.lower() == 'иги':
        pass
    elif message.text.lower() == 'иги!':
        pass
    elif message.text.lower() == 'иги иги иги':
        pass
    elif message.text.lower() == 'иги иги иги иги':
        pass
    elif message.text.lower() == 'иги иги иги иги иги':
        pass
    elif message.text.lower() == 'иги иги!':
        pass
    elif message.text.lower() == 'иги иги иги!':
        pass
    elif message.text.lower() == 'иги иги иги иги!':
        pass
    elif message.text.lower() == 'иги иги иги иги иги!':
        pass
    elif message.text.lower() == 'ігі':
        pass
    elif message.text.lower() == 'ігі ігі ':
        pass
    elif message.text.lower() == 'ігі ігі ігі ':
        pass
    elif message.text.lower() == 'ігі ігі ігі ігі':
        pass
    elif message.text.lower() == 'ігі! ':
        pass
    elif message.text.lower() == 'ігі ігі! ':
        pass
    elif message.text.lower() == 'ігі ігі ігі! ':
        pass
    elif message.text.lower() == 'ігі ігі ігі ігі!':
        pass
    elif message.text.lower() == 'угу':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'угу!':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'угу угу':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'угу угу!':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'угу угу угу':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'угу угу угу!':
        bot.send_message(message.chat.id, 'Ага)')
    elif message.text.lower() == 'ух':
        pass
    elif message.text.lower() == 'ух!':
        pass
    elif message.text.lower() == 'ухх':
        pass
    elif message.text.lower() == 'ухх!':
        pass
    elif message.text.lower() == 'уххх':
        pass
    elif message.text.lower() == 'уххх!':
        pass
    elif message.text.lower() == 'ухххх':
        pass
    elif message.text.lower() == 'ухххх!':
        pass
    elif message.text.lower() == 'уххххх':
        pass
    elif message.text.lower() == 'уххххх!':
        pass
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'як дела?':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'як дела':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'как діла?':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'как діла':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'як діла?':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'як діла':
        bot.send_message(message.chat.id, 'Нормуль')
    elif message.text.lower() == 'понятно':
        pass
    elif message.text.lower() == 'понятно!':
        pass
    elif message.text.lower() == 'понятно.':
        pass
    elif message.text.lower() == 'понятно..':
        pass
    elif message.text.lower() == 'понятно...':
        pass
    elif message.text.lower() == 'буду йти':
        pass
    elif message.text.lower() == 'буду йти по франка':
        pass
    elif message.text.lower() == 'буду йти по  вулиці франка':
        pass
    elif message.text.lower() == 'буду йти по вул франка':
        pass
    elif message.text.lower() == 'буду йти по вул. франка':
        pass
    elif message.text.lower() == 'йти по франка':
        pass
    elif message.text.lower() == 'чого':
        bot.send_message(message.chat.id, '?')
    elif message.text.lower() == '?':
        pass
    elif message.text.lower() == '??':
        pass
    elif message.text.lower() == '???':
        pass
    elif message.text.lower() == '????':
        pass
    elif message.text.lower() == '?????':
        pass
    elif message.text.lower() == '??????':
        pass
    elif message.text.lower() == '???????':
        pass
    elif message.text.lower() == '????????':
        pass
    elif message.text.lower() == '?????????':
        pass
    elif message.text.lower() == '??????????':
        pass
    elif message.text.lower() == '???????????':
        pass
    elif message.text.lower() == '????????????':
        pass
    elif message.text.lower() == '!':
        pass
    elif message.text.lower() == '!!':
        pass
    elif message.text.lower() == '!!!':
        pass
    elif message.text.lower() == '!!!!':
        pass
    elif message.text.lower() == '!!!!!':
        pass
    elif message.text.lower() == '!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!!!!!':
        pass
    elif message.text.lower() == '!!!!!!!!!!!!':
        pass
    elif message.text.lower() == 'робиться':
        pass
    elif message.text.lower() == 'ку':
        bot.send_message(message.chat.id, 'ку ку')
    elif message.text.lower() == 'ку ку':
        bot.send_message(message.chat.id, 'ку ку ку')
    elif message.text.lower() == 'ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку')
    elif message.text.lower() == 'ку ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку')
    elif message.text.lower() == 'ку ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку')
    elif message.text.lower() == 'ку ку ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку')
    elif message.text.lower() == 'ку ку ку ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку ку')
    elif message.text.lower() == 'ку ку ку ку ку ку ку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку ку ку')
    elif message.text.lower() == 'к':
        pass
    elif message.text.lower() == 'куку':
        bot.send_message(message.chat.id, 'ку ку')
    elif message.text.lower() == 'кукуку':
        bot.send_message(message.chat.id, 'ку ку ку')
    elif message.text.lower() == 'кукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку')
    elif message.text.lower() == 'кукукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку')
    elif message.text.lower() == 'кукукукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку')
    elif message.text.lower() == 'кукукукукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку')
    elif message.text.lower() == 'кукукукукукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку ку')
    elif message.text.lower() == 'кукукукукукукукуку':
        bot.send_message(message.chat.id, 'ку ку ку ку ку ку ку ку')
    elif message.text.lower() == 'падає дощ в самборі':
        pass
    elif message.text.lower() == 'падає дощ в львові':
        pass
    elif message.text.lower() == 'падає дощ в києві':
        pass
    elif message.text.lower() == 'падає дощ в дрогобичі':
        pass
    elif message.text.lower() == 'так':
        pass
    elif message.text.lower() == 'так!':
        pass
    elif message.text.lower() == 'так так':
        pass
    elif message.text.lower() == 'так так!':
        pass
    elif message.text.lower() == 'так так так':
        pass
    elif message.text.lower() == 'так так так!':
        pass
    elif message.text.lower() == 'та':
        pass
    elif message.text.lower() == 'та!':
        pass
    elif message.text.lower() == 'та та':
        pass
    elif message.text.lower() == 'та та!':
        pass
    elif message.text.lower() == 'та та та':
        pass
    elif message.text.lower() == 'та та та!':
        pass
    elif message.text.lower() == 'о':
        pass
    elif message.text.lower() == 'о!':
        pass
    elif message.text.lower() == 'оо':
        pass
    elif message.text.lower() == 'оо!':
        pass
    elif message.text.lower() == 'ооо':
        pass
    elif message.text.lower() == 'ооо!':
        pass
    elif message.text.lower() == 'оооо':
        pass
    elif message.text.lower() == 'оооо!':
        pass
    elif message.text.lower() == 'ооооо':
        pass
    elif message.text.lower() == 'ооооо!':
        pass
    elif message.text.lower() == 'оооооо':
        pass
    elif message.text.lower() == 'оооооо!':
        pass
    elif message.text.lower() == 'ооооооо':
        pass
    elif message.text.lower() == 'ооооооо!':
        pass
    elif message.text.lower() == 'оооооооо':
        pass
    elif message.text.lower() == 'оооооооо!':
        pass
    elif message.text.lower() == 'опа':
        pass
    elif message.text.lower() == 'опа!':
        pass
    elif message.text.lower() == 'оопа':
        pass
    elif message.text.lower() == 'оопа!':
        pass
    elif message.text.lower() == 'ооопа':
        pass
    elif message.text.lower() == 'ооопа!':
        pass
    elif message.text.lower() == 'оооопа':
        pass
    elif message.text.lower() == 'оооопа!':
        pass
    elif message.text.lower() == 'ооооопа':
        pass
    elif message.text.lower() == 'ооооопа!':
        pass
    elif message.text.lower() == 'опаа':
        pass
    elif message.text.lower() == 'опаа!':
        pass
    elif message.text.lower() == 'опааа':
        pass
    elif message.text.lower() == 'опааа!':
        pass
    elif message.text.lower() == 'опаааа':
        pass
    elif message.text.lower() == 'опаааа!':
        pass
    elif message.text.lower() == 'опааааа':
        pass
    elif message.text.lower() == 'опааааа!':
        pass
    elif message.text.lower() == 'опаааааа':
        pass
    elif message.text.lower() == 'опаааааа!':
        pass
    elif message.text.lower() == 'падає дощ в самборі?':
        bot.send_message(message.chat.id, 'Напиши слово "погода"')
    elif message.text.lower() == 'падає дощ в львові?':
        bot.send_message(message.chat.id, 'Напиши слово "погода"')
    elif message.text.lower() == 'падає дощ в києві?':
        bot.send_message(message.chat.id, 'Напиши слово "погода"')
    elif message.text.lower() == 'падає дощ в дрогобичі?':
        bot.send_message(message.chat.id, 'Напиши слово "погода"')
    elif message.text.lower() == 'шо ти':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'що ти':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'шо ти?':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'що ти?':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'шо ти там':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'що ти там':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'шо ти там?':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'що ти там?':
        bot.send_message(message.chat.id, 'Та ніц)')
    elif message.text.lower() == 'гей':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'гей!':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'гейй':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'гейй!':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'геййй':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'геййй!':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'гейййй':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'гейййй!':
        bot.send_message(message.chat.id, 'Сам ти гей')
    elif message.text.lower() == 'хз':
        pass
    elif message.text.lower() == 'хзз':
        pass
    elif message.text.lower() == 'хззз':
        pass
    elif message.text.lower() == 'хзззз':
        pass
    elif message.text.lower() == 'вінник':
        pass
    elif message.text.lower() == 'винник':
        pass
    elif message.text.lower() == 'віник':
        pass
    elif message.text.lower() == 'виник':
        pass
    elif message.text.lower() == 'вінник!':
        pass
    elif message.text.lower() == 'винник!':
        pass
    elif message.text.lower() == 'віник!':
        pass
    elif message.text.lower() == 'виник!':
        pass
    elif message.text.lower() == 'ало':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоо':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алооо':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоооо':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алооооо':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоооооо':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'ало!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоо!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алооо!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоооо!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алооооо!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'алоооооо!':
        bot.send_message(message.chat.id, 'Ульооо')
    elif message.text.lower() == 'ти як там':
        bot.send_message(message.chat.id, 'Та нормально)')
    elif message.text.lower() == 'ти як там?':
        bot.send_message(message.chat.id, 'Та нормально))')
    elif message.text.lower() == 'ти шо там':
        bot.send_message(message.chat.id, 'Та нічо')
    elif message.text.lower() == 'ти шо там?':
        bot.send_message(message.chat.id, 'Та нічо)')
    elif message.text.lower() == 'ти шо там?':
        bot.send_message(message.chat.id, 'Та нічо)')
    elif message.text.lower() == 'пака':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'пака пака':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'па':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'па па':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'пака!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'пака пака!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'па!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'па па!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай бай!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай бай':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай бай бай':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'бай бай бай!':
        bot.send_message(message.chat.id, 'Допобачення')
    elif message.text.lower() == 'очі відкрий':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'відкрий свої очі':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'відкрий свої очі!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очі відкрий свої':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очі відкрий свої!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'відкрий собі очі':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'відкрий собі очі!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очі відкрий собі':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очі відкрий собі!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'тоді очко':
        bot.send_message(message.chat.id, 'Сам собі очко відкрий')
    elif message.text.lower() == 'очі відкрий!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'тоді очко!':
        bot.send_message(message.chat.id, 'Сам собі очко відкрий')
    elif message.text.lower() == 'відкрий очі':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очко тоді':
        bot.send_message(message.chat.id, 'Сам собі очко відкрий')
    elif message.text.lower() == 'відкрий очі!':
        bot.send_message(message.chat.id, 'У мене нема очей')
    elif message.text.lower() == 'очко тоді!':
        bot.send_message(message.chat.id, 'Сам собі очко відкрий')
    elif message.text.lower() == 'круть':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььььььь':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'круть!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутьььььььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text.lower() == 'крутььььььььььь!':
        bot.send_message(message.chat.id, 'Иги')
    elif message.text == '1169':
        bot.send_message(message.chat.id, 'Ти виграв!!!\nНапиши мені в Telegram число і я куплю тобі чоколядку.')
    else:
        bot.send_message(message.chat.id, 'Не розумію, попробуй написати без розділових знаків...')
@bot.message_handler(content_types=['sticker'])
def start_message(message):
    pass

@bot.message_handler(content_types=['emoji'])
def start_message(message):
    pass

@bot.message_handler(content_types=['gif'])
def start_message(message):
    pass

@bot.message_handler(content_types=['photo'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Ніц тут не вижу')

bot.polling(none_stop = True, interval=0, timeout=2500)
