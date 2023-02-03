import telebot

token = '5943512620:AAFSladkS80Tvhc45i4mVCr2ZumOo5y_X2c'
user_id = -1001822113373
bot = telebot.TeleBot(token)

# 1002820269


def send_message(text):
    try:
        bot.send_message(user_id, text, parse_mode="Markdown")
        return True
    except:
        return False
