import telebot
import json
import Game
from telebot import types
import requests

bot = telebot.TeleBot('5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Об игре")
    btn3 = types.KeyboardButton("Об авторе")
    markup.add(btn1, btn2, btn3)

    bot.send_message(chat_id,
                     text="Добро пожаловать, {0.first_name}! Пора погрузиться в мир детектива, мафии и головоломок.".format(
                         message.from_user), reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Об игре" or ms_text == "Игра" or ms_text == "об игре" or ms_text == "игра":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Об авторе")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)

        bot.send_message(chat_id, "Прототип игры-бродилки с уклоном в детектив", reply_markup=markup)

    elif ms_text == "Об авторе" or ms_text == "Автор" or ms_text == "автор" or ms_text == "об авторе":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Об игре")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)

        img = open('vse-o-stile-nuar-2.jpg', "rb")
        bot.send_photo(message.chat.id, img, caption="Автор немного устал и заколебался", reply_markup=markup)

    elif ms_text == "Начать игру" or ms_text == "начать игру":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Далее")
        markup.add(btn1)
        msg = bot.send_message(chat_id, "Как вас зовут?")
        bot.register_next_step_handler(msg, ask)

        img = open("image.jpg", "rb")
        bot.send_photo(chat_id, img,
                       caption='США, конец 19 века. Время не спокойное, полное мафиозных разборок, сухого закона и '
                               'романтизации убийств. Вы-незадачливый детектив в одном из городов, '
                               'которым управляет мафия. Но кто же вы?', reply_markup=markup)

    elif ms_text == "Далее" or ms_text == "далее":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Завтрак")
        btn2 = types.KeyboardButton(text="Подобрать гардероб")
        btn3 = types.KeyboardButton(text="Совет дня")
        btn4 = types.KeyboardButton(text="Идти сразу на работу")
        markup.add(btn1, btn2, btn3, btn4 )
        bot.send_message(chat_id,
                         'Новый день. Вы не так давно переехали в новый город и перевелись в другой департамент.'
                         'Большой город кружил голову и вызывал некоторую детскую радость в душе. Но счастливые '
                         'визги можно оставить на потом. '
                         'На новом рабочем месте уже есть работа. Но с чего вы начнёте день?',
                         reply_markup=markup)

    elif ms_text == "Совет дня" or ms_text == "совет дня":
        contents = requests.get("https://api.adviceslip.com/advice").json()
        urlSOVET = contents["slip"]["advice"]
        bot.send_message(chat_id, f"Вы берёте первую попавшуюся книгу или газет и наугад тыкаете пальцем в "
                                  f"фразу. \n\n "
                                  f"<b><i>{urlSOVET}</i></b> \n\n Хм, что же это значит?",
                         parse_mode="HTML")

    elif ms_text == "Идти сразу на работу" or ms_text == "идти сразу на работу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, "Вы спосокойно вышли из квартиры, но на лестничной площадке ваши соседи снова "
                                  "решили сыграть в карты. Они зовут вас сыграть. Присоединитесь?",
                         reply_markup=markup)
        btn1 = types.KeyboardButton(text="Присоединиться")
        btn2 = types.KeyboardButton(text="Отказаться и уйти")
        markup.add(btn1, btn2 )

    elif ms_text == "Присоединиться" or ms_text == "присоединиться":
        game21 = Game.newGame(chat_id, Game.Game21(jokers_enabled=True))
        text_game = game21.get_cards(2)
        bot.send_media_group(chat_id, media=game21.mediaCards)
        bot.send_message(chat_id, text=text_game)

    else:
        bot.send_message(chat_id, text="А енто зачем? Я не поняль " + ms_text)


def ask(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Приятно познакомиться, детектив " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота
print()
