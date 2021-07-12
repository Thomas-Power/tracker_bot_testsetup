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
        user = username.upper()
        action = data[0].lower()
        amount = data[1]
        ticker = data[2].upper()
        price = data[3]
        if action == "buy":
            return self.db.update_position(user, "bought", amount, ticker, price)
        if action == "bought":
            return self.db.update_position(user, "bought", amount, ticker, price)
        if action == "sell":
            return self.db.update_position(user, "sold", str(float(amount)*-1), ticker, price)
        if action == "sold":
            return self.db.update_position(user, "sold", str(float(amount)*-1), ticker, price)
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