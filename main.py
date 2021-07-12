from BotRequests import BotRequests
import telebot

bot = telebot.TeleBot('1899234700:AAF-8-vXDtSJ6jJHPnSfsCLfCVAGe3StKEw')

bot_requests = BotRequests()

@bot.message_handler(commands=['update_position'])
def update_position(message):
    chat_dest = message.json["chat"]["id"]
    try:
        username = message.json["chat"]["first_name"]
        data = message.json["text"].split(" ")[1:]
        status = bot_requests.update_position(data, username)
        bot.send_message(chat_dest, status)
    except:
        bot.send_message(chat_dest, "Update unsuccessful")

@bot.message_handler(commands=['show_user'])
def show_user(message):
    chat_dest = message['chat']['id']
    try:
    data =  message.json["text"].split(" ")[1].upper()
    address = bot_requests.show_user(data)
    bot.reply_to(message, address)
    bot.send_message(chat_dest, address)
    except:
        bot.send_message(chat_dest, "Python error")

@bot.message_handler(commands=['show_all'])
def show_all(message):
    #try:
    address = bot_requests.show_all()
    bot.reply_to(message, address)
    #bot.send_message(chat_dest, address)
    #except:
    #    bot.reply_to("Python error")
        #bot.send_message(chat_dest, "Python error")

@bot.message_handler(commands=['show_ticker'])
def show_ticker(message):
    #try:
    data =  message.json["text"].split(" ")[1].upper()
    address = bot_requests.show_ticker(data)
    bot.reply_to(message, address)
        #bot.send_message(chat_dest, address)
    #except:
    #    bot.reply_to("Python error")
        #bot.send_message(chat_dest, "Python error")

if __name__ == '__main__':
    print("working")
    bot.polling()