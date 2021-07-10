import sys
sys.path.append('./fintech-lab')
import pandas as pd
import time
import json
import os
from DatabaseAdapter import DatabaseAdapter


class BotRequests:
    def __init__(self):
        self.db = DatabaseAdapter()
    
    def update_position(self, data):
        try:
            user = data.get("user_name")
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
        except:
            return 404
        return self.db.update_position(user, action, amount, ticker, price)
        
    def show_positions(self, data):
        try:
            user = data.get("user_name")
        except:
            return 404
        return self.db.get_positions_url(user)
        
    def show_owns(self, data):
        try:
            ticker = data.get("ticker")
        except:
            return 404
        return self.db.show_owns(ticker)