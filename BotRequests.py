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
    def update_position(self, data):
        #try:
        user = data.get("username")
        action = data.get("action").lower()
        amount = data.get("amount")
        ticker = data.get("ticker").lower()
        price = data.get("price")
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
       
    def show_user(self, data):
        #try:
        user = data.get("username")
        return self.db.show_user(user)
        #except:
        #    return 404
        
    def show_ticker(self, data):
        #try:
        ticker = data.get("ticker")
        return self.db.show_ticker(ticker)
        #except:
        #    return 404