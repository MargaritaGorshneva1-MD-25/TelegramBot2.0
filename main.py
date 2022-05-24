import telebot
from telebot import types
bot = telebot.TeleBot('5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk')  # Создаем экземпляр бота

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Об игре")
    btn3 = types.KeyboardButton("Об авторе")
    markup.add(btn1, btn2, btn3)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Об игре" or ms_text == "Игра" or ms_text == "об игре" or ms_text == "игра":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, "Прототип игры-бродилки с уклоном в детектив")
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Об авторе")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)

    elif ms_text == "Об авторе" or ms_text == "Автор" or ms_text == "автор" or ms_text == "об атворе":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, "Автор немного устал и заколебался")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Не надо мне писать", url="https://vk.com/id333170468")
        key1.add(btn1)
        img = open('Мафиози.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Об авторе")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)

    elif ms_text == "Начать игру" or ms_text == "начать игру":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, "США, конец 19 века. Время не спокойное, полное мафиозных разборок, сухого закона и романтизации убийств. Вы-незадачливый детектив в одном из городов, которым управляет мафия. Но кто же вы?")
        btn1 = types.InlineKeyboardButton(text="Мужчина")
        btn2 = types.InlineKeyboardButton(text="Девушка")
        markup.add(btn1, btn2)
        img = open('scale_1200.webp', 'rb')
        bot.send_photo(message.chat.id, img)
        if ms_text == "Девушка":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(chat_id, "И как же зовут леди?")
            bot.register_next_step_handler(message, add_user)


    else:
        bot.send_message(chat_id, text="А енто зачем? Я не поняль " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()