from BotRequests import BotRequests
import telebot

app = telebot.TeleBot('1899234700:AAF-8-vXDtSJ6jJHPnSfsCLfCVAGe3StKEw')

bot_requests = BotRequests()

@app.message_handler(commands=['update_position'])
def update_position(message):
    try:
        chat_dest = message.json["chat"]["id"]
        try:
            username = message.json["chat"]["first_name"]
            data = message.json["text"].split(" ")[1:]
            status = bot_requests.update_position(data, username)
            app.send_message(chat_dest, status)
        except:
            app.send_message(chat_dest, "Update unsuccessful")
    except:
        pass

@app.message_handler(commands=['show_user'])
def show_user(message):
    try:
        chat_dest = message.json["chat"]["id"]
        try:
            data =  message.json["text"].split(" ")[1].upper()
            address = bot_requests.show_user(data)
            app.reply_to(message, address)
            app.send_message(chat_dest, address)
        except:
            app.send_message(chat_dest, "Python error")
    except:
        pass

@app.message_handler(commands=['show_all'])
def show_all(message):
    try:
        chat_dest = message.json['chat']['id']
        try:
            address = bot_requests.show_all()
            #app.reply_to(message, address)
            app.send_message(chat_dest, address)
        except:
            #app.reply_to("Python error")
            app.send_message(chat_dest, "Python error")
    except:
        pass

@app.message_handler(commands=['show_ticker'])
def show_ticker(message):
    try:
        try:
            chat_dest = message.json["chat"]["id"]
            data =  message.json["text"].split(" ")[1].upper()
            address = bot_requests.show_ticker(data)
            #app.reply_to(message, address)
            app.send_message(chat_dest, address)
        except:
            #app.reply_to("Python error")
            app.send_message(chat_dest, "Python error")
    except:
        pass

if __name__ == '__main__':
    print("working")
    app.polling()