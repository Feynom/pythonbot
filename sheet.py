import telebot
import os
import random
import sched, time
import pyowm

bot = telebot.TeleBot('955970689:AAGNqX-pUAwc__4tjbCLdVzav9OSTX8yoic')

#клавіатура

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)#1-автоматичний розмір,2-тимчасова
    user_markup.row('/start', '/help','/timerminutes')
    user_markup.row('memes(images)', 'memes(video)', '/timerhours')
    bot.send_message(message.from_user.id, 'Бот готовий до розмови!', reply_markup=user_markup)
#клавіатура
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Список команд :\n /start - розпачати діалог\n /help - список команд\n/jokes-кину тобі меми\n/timer - відлік часу')

@bot.message_handler(commands=['jokes'])
def start_message(message):
    directory = "C:/python/memes(images)"
    all_files_in_directory = os.listdir(directory)
    random_file = random.choice(all_files_in_directory)
    img = open(directory + '/' + random_file, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    img.close()

@bot.message_handler(commands=['timerminutes'])
def start_message(message):
    bot.send_message(message.chat.id, 'Скільки хвилин?\nХвилини мають бути кратні числу "5"\nПриклад:X хвилин,\nде Х - кількість хвилин')

@bot.message_handler(commands=['timerhours'])
def start_message(message):
    bot.send_message(message.chat.id, 'Скільки годин?\nМаксимум до 24 годин\nПриклад: 1 година,2 години, 24 година...')

@bot.message_handler(content_types=['text'])
def start_message(message):
    #timer
    #if message.text.lower() == '5 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(300):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '1 хвилин' or message.text.lower() == '1 хвилина':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(60):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='10 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='15 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(900):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='20 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(1200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='25 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(1500):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='30 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(1800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='35 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(2100):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='40 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(2400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='45 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(2700):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='50 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(3000):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='55 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(3300):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() =='60 хвилин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(3600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '1 година':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(3600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '2 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(7200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '3 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(10800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '4 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(14400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '5 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(18000):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '6 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(21600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '7 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(25200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '8 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(28800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '9 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(32400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '10 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(36000):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '11 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(39600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '12 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(43200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '13 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(46800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '14 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(50400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '15 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(54000):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '16 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(57600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '17 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(61200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '18 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(64800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '19 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(68400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '20 годин':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(72000):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '21 година':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(75600):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '22 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(79200):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '23 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(82800):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #elif message.text.lower() == '24 години':
        bot.send_message(message.chat.id, 'Таймер запущено!')
        for i in range(86400):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
        for i in range(2):
            time.sleep(1)
        bot.send_message(message.chat.id, 'Час вийшов!')
    #timer
    elif message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Привіт!\nЯк справи?')
    elif message.text.lower() == 'привіт!':
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
        bot.send_message(message.chat.id, 'Де ти проживаєш?(Львів, Київ, Самбір, Дрогобич)')
        #Weather
    elif message.text.lower() == 'львів':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Lviv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        bot.send_message(message.chat.id, 'В місті Львів зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        #weather
        #відправка фотографій рандомних
    elif message.text.lower() == 'самбір':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Sambir, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        bot.send_message(message.chat.id, 'В місті Самбір зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
    elif message.text.lower() == 'київ':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Kyiv, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        bot.send_message(message.chat.id, 'В місті Київ зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
    elif message.text.lower() == 'дрогобич':
        owm = pyowm.OWM('e55341dec41c58f9e967307794300466', language = "ru")
        observation = owm.weather_at_place('Drohobych, UA')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        bot.send_message(message.chat.id, 'В місті Дрогобич зараз: ' + w.get_detailed_status())
        bot.send_message(message.chat.id, 'Температура в районі  ' + str(temp) + ' градусів')
        #weather
        #відправка фотографій рандомних
        #weather
        #відправка фотографій рандомних
        #weather
        #відправка фотографій рандомних
        #weather
        #відправка фотографій рандомних
    elif message.text.lower() == 'memes(images)':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
        #відправка фотографій рандомних
        #відпарвка відео
    elif message.text.lower() == 'memes(video)':
        directory = "C:/python/memes(videos)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        video = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_message(message.chat.id, 'Зачекай будь ласка пару хвилин поки відео загрузиться')
        bot.send_video(message.from_user.id, video)
        video.close()
        #відпарвка відео
    elif message.text.lower() == 'мем':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемасики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемчики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемачики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусікі':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусіки':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемусикі':
            directory = "C:/python/memes(images)"
            all_files_in_directory = os.listdir(directory)
            random_file = random.choice(all_files_in_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    elif message.text.lower() == 'меми':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні меми':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні мемасики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'потрібні мемасики негайно':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'негайно мемасики':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'мемасики негайно':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'негайно меми':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'меми негайно':
        directory = "C:/python/memes(images)"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower() == 'хочу мем':
        directory = "C:/python/memes(images)"
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
    elif message.text.lower() == 'лул':
        pass
    elif message.text.lower() == 'лул!':
        pass
    elif message.text.lower() == 'кек':
        bot.send_message(message.chat.id, 'Лол кек чебкре=)')
    elif message.text.lower() == 'кек!':
        bot.send_message(message.chat.id, 'Лол кек чебкре=)')
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
    else:
        bot.send_message(message.chat.id, 'Не розумію, попробуй написати без знаку оклику або без крапки в кінці, можливо допоможе...')

bot.polling(none_stop = True, interval=0, timeout=100)
