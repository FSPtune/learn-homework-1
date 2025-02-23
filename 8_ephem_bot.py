"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь !")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def get_plannet_constellation(update, context):
    user_text = update.message.text
    planet_name = user_text.split()[1].capitalize()
    if hasattr(ephem, planet_name):
        planet = getattr(ephem, planet_name)(datetime.now())
        update.message.reply_text(f"Планета {planet_name} находится в созвездии {ephem.constellation(planet)}")
    else:
        update.message.reply_text(f"Извините, я не знаю такую планету! Попробуйте ещё раз.")


def main():
    mybot = Updater("    токен  вписать сюда       ", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, ))
    dp.add_handler(CommandHandler("planet", get_plannet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()