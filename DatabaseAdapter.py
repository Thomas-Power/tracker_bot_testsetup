import json
import pandas as pd
from Database import Database

#Adapter class, used to verify and prepare data for input and output from database 
#and keep actual database implementation independent from greater system
class DatabaseAdapter:
    def __init__(self):
        self.db = Database()

    def update_position(self, user, action, amount, ticker, price):
        return self.db.update_position(user, action, amount, ticker, price)
      
    def show_all(self):
        return self.db.show_all()
      
    def show_user(self, user):
        return self.db.show_positions(user)
        
    def show_ticker(self, ticker):
        return self.db.show_ticker(ticker)