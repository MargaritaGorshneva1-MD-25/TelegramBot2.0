import telebot
import json
from telebot import types

bot = telebot.TeleBot('5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk')  # Создаем экземпляр бота

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):                                                                                                     
    chat_id = message.chat.id                                                                                           
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)                                                            
    btn1 = types.InlineKeyboardButton("Начать игру")                                                                          
    btn2 = types.InlineKeyboardButton("Об игре")                                                                              
    btn3 = types.InlineKeyboardButton("Об авторе")                                                                            
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
        markup = types.InlineKeyboardMarkup(resize_keyboard=True)                                                        
        bot.send_message(chat_id, "Прототип игры-бродилки с уклоном в детектив")                                        
        btn1 = types.InlineKeyboardButton("Начать игру")                                                                      
        btn2 = types.InlineKeyboardButton("Об авторе")                                                                        
        back = types.InlineKeyboardButton("Назад")                                                                            
        markup.add(btn1, btn2, back)                                                                                    
                                                                                                                        
    elif ms_text == "Об авторе" or ms_text == "Автор" or ms_text == "автор" or ms_text == "об авторе":                  
        markup = types.InlineKeyboardMarkup(resize_keyboard=True)                                                        
        bot.send_message(chat_id, "Автор немного устал и заколебался")                                                  
        img = open('vse-o-stile-nuar-2.jpg', 'rb')                                                                      
        bot.send_photo(message.chat.id, img)                                                                            
                                                                                                                        
        btn1 = types.InlineKeyboardButton("Начать игру")                                                                      
        btn2 = types.InlineKeyboardButton("Об авторе")                                                                        
        back = types.InlineKeyboardButton("Назад")                                                                            
        markup.add(btn1, btn2, back)                                                                                    
                                                                                                                        
    elif ms_text == "Начать игру" or ms_text == "начать игру":                                                          
        markup = types.InlineKeyboardMarkup(resize_keyboard=True)                                                        
        bot.send_message(chat_id, 'США, конец 19 века. Время не спокойное, полное мафиозных разборок, сухого закона и ' 
                                  'романтизации убийств. Вы-незадачливый детектив в одном из городов, '                 
                                  'которым управляет мафия. Но кто же вы?')                                             
        img = open("image.jpg", "rb")                                                                                   
        bot.send_photo(message.chat.id, img)                                                                            
        btn1 = types.InlineKeyboardButton(text="Мужчина")                                                               
        btn2 = types.InlineKeyboardButton(text="Девушка")
        btn3 = types.InlineKeyboardButton(text="Рандом")
        markup.add(btn1, btn2, btn3)
        
    elif ms_text == "Девушка" or ms_text == "девушка":                                                                  
        msg = bot.send_message(chat_id, "Как вас зовут?")                                                               
        bot.register_next_step_handler(msg, ask)
        
    elif ms_text == "Рандом" or ms_text == "рандом":
        msg = bot.send_message(chat_id, 'Новый день. Вы не так давно переехали в новый город и перевелись в другой департамент.' 
                                  'Большой город кружил голову и вызывал некоторую детскую радость в душе. Но счастливые визги можно оставить на потом.'                 
                                  'На новом рабочем месте уже есть работа. Но с чего вы начнёте день?')
        btn1 = types.InlineKeyboardButton(text="Завтрак")                                                               
        btn2 = types.InlineKeyboardButton(text="Подобрать гардероб")
        btn3 = types.InlineKeyboardButton(text="Совет дня")
        markup.add(btn1, btn2, btn3)
        
    elif ms_text == "Совет дня" or ms_text == "совет дня":
        msg = bot.send_message(chat_id, "Вы берёте первую попавшуюся книгу или газет и наугад тыкаете пальцем в фразу. Хм, что же это значит?")
        contents = requests.get("https://api.adviceslip.com/advice").json()
        urlSOVET = contents["url"]
        bot.send_message(message.chat.id, ms_text = urlSOVET)
    
    else:                                                                                                               
        bot.send_message(chat_id, text="А енто зачем? Я не поняль " + ms_text)                                          
                                                                                                                        
                                                                                                                        
def ask(message):                                                                                                       
    chat_id = message.chat.id                                                                                           
    ms_text = message.text                                                                                              
    bot.send_message(chat_id, text="Приятно познакомиться, детектив" + ms_text)
                                                                                                                        
# -----------------------------------------------------------------------                                               
bot.polling(none_stop=True, interval=0)  # Запускаем бота                                                               
                                                                                                                        
print()
