import sys
import pandas as pd
import time
import json
import os
from DatabaseAdapter import DatabaseAdapter


class BotRequests:
    def __init__(self):
        self.db = DatabaseAdapter()
    
#https://trackerbot-service-test-gmnto3bl6a-nn.a.run.app//update_position?username=me&action=bought&amount=100&ticker=BTC&price=40000    
    def update_position(self, data, username):
        #try:
        user = username
        action = data[0].lower()
        amount = data[1]
        ticker = data[2].lower()
        price = data[3]
        if action == "buy":
            action =="bought"
        if action == "sell":
            action == "sold"
        if action == "sold":
            amount = amount*-1
        return self.db.update_position(user, action, amount, ticker, price)
        #except:
        #    return 404
       
    def show_all(self):
        #try:
        return self.db.show_all()
        #except:
        #    return 404
       
    def show_user(self, user):
        #try:
        return self.db.show_user(user)
        #except:
        #    return 404
        
    def show_ticker(self, ticker):
        #try:
        return self.db.show_ticker(ticker)
        #except:
        #    return 404