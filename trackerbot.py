from BotRequests import BotRequests
from flask import Flask, request, jsonify

app = Flask(__name__)

bot_requests = BotRequests()

@app.route('/update_position')
def update_position():
    data = request.args
    status = bot_requests.update_position(data)
    return status

@app.route('/show_positions')
def show_positions():
    data = request.args
    address = bot_requests.show_positions(data)
    return address

@app.route('/show_positions')
def show_owns():
    data = request.args
    address = bot_requests.show_positions(data)
    return address
    
if __name__ == '__main__':
    app.run(debug=True)