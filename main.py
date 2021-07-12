from BotRequests import BotRequests
import telebot
import requests

bot = telebot.TeleBot('1899234700:AAF-8-vXDtSJ6jJHPnSfsCLfCVAGe3StKEw')

bot_requests = BotRequests()

@bot.message_handler(commands=['update_position'])
def update_position(message, cmd):
    chat_dest = message['chat']['id']
    try:
        username = message["user"]["username"]
        data = message["text"].split(" ")
        status = bot_requests.update_position(data, username)
        bot.reply_to(status)
        #bot.send_message(chat_dest, status)
    except:
        bot.send_message(chat_dest, "Update unsuccessful")

@bot.message_handler(commands=['show_user'])
def show_user():
    chat_dest = message['chat']['id']
    try:
        data = message["text"]
        address = bot_requests.show_user(data)
        bot.reply_to(address)
        #bot.send_message(chat_dest, address)
    except:
        bot.reply_to("Python error")
        #bot.send_message(chat_dest, "Python error")

@bot.message_handler(commands=['show_all'])
def show_all():
    try:
        address = bot_requests.show_all()
        bot.send_message(chat_dest, address)
    except:
        bot.reply_to("Python error")
        #bot.send_message(chat_dest, "Python error")

@bot.message_handler(commands=['show_ticker'])
def show_ticker():
    try:
        data = message["text"]
        address = bot_requests.show_ticker(data)
        bot.reply_to(address)
        #bot.send_message(chat_dest, address)
    except:
        bot.reply_to("Python error")
        #bot.send_message(chat_dest, "Python error")

if __name__ == '__main__':
    bot.polling()