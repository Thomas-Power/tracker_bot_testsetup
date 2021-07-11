from BotRequests import BotRequests
from flask import Flask, request, jsonify

app = Flask(__name__)

bot_requests = BotRequests()


@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/update_position')
def update_position():
    try:
        data = request.args
        status = bot_requests.update_position(data)
        return status
    except:
        return "Update unsuccessful"

@app.route('/show_user')
def show_user():
    try:
        data = request.args
        address = bot_requests.show_user(data)
        return address
    except:
        return "Python error"

@app.route('/show_all')
def show_all():
    try:
        address = bot_requests.show_all()
        return address
    except:
        return "Python error"

@app.route('/show_ticker')
def show_ticker():
    try:
        data = request.args
        address = bot_requests.show_ticker(data)
        return address
    except:
        return "Python error"

if __name__ == '__main__':
    app.run(debug=True)