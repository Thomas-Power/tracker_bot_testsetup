from BotRequests import BotRequests
import telebot
import requests

bot = telebot.TeleBot(__name__)

bot_requests = BotRequests()

@bot.route('/update_position ?(.*)')
def update_position(message, cmd):
    chat_dest = message['chat']['id']
    try:
        username = message["user"]["username"]
        data = message["text"].split(" ")
        status = bot_requests.update_position(data, username)
        bot.send_message(chat_dest, status)
    except:
        bot.send_message(chat_dest, "Update unsuccessful")

@bot.route('/show_user')
def show_user():
    chat_dest = message['chat']['id']
    try:
        data = message["text"]
        address = bot_requests.show_user(data)
        bot.send_message(chat_dest, status)
    except:
        bot.send_message(chat_dest, "Python error")

@bot.route('/show_all')
def show_all():
    try:
        address = bot_requests.show_all()
        bot.send_message(chat_dest, address)
    except:
        return "Python error"

@bot.route('/show_ticker')
def show_ticker():
    try:
        data = message["text"]
        address = bot_requests.show_ticker(data)
        bot.send_message(chat_dest, address)
    except:
        return "Python error"

if __name__ == '__main__':
    app.config['api_key'] = '1899234700:AAF-8-vXDtSJ6jJHPnSfsCLfCVAGe3StKEw'
    app.poll(debug=True)