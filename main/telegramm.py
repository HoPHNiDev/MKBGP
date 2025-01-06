import telebot

token = '' #Token of the bot from @BotFather
user_id = 1 #User ID of the reciever, it could be user/chat/channel
bot = telebot.TeleBot(token)

def send_message(text):
    try:
        bot.send_message(user_id, text, parse_mode="Markdown")
        return True
    except:
        return False
