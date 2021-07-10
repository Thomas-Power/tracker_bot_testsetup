import pandas as pd
import mysql.connector

#"CREATE TABLE IF NOT EXISTS portfolio_actions (action_date DATETIME, user VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));"

#Implementation of required functions for data retrieval and verification using MySQL server
class Database:
    #replace variables with appropriate credentials
    def __init__(self):
        self.positions = "open_positions.csv"
        self.db = mysql.connector.connect(
			host="34.95.55.18",
			user="root",
			passwd="password",
			database="portfolio_actions"
		)
		self.cursor = self.db.cursor()
        
    def update_position(self, user, action, amount, ticker, price):
        sql = "INSERT INTO portfolio_actions (action_date, user, action, amount, ticker) VALUES (%s, %s, %s, %s, %s)"
		self.cursor.execute(sql, values)
		self.db.commit()
        return 200
		
    
    def show_positions(self, user=None):
        sql = "SELECT * FROM portfolio_actions"
		self.cursor.execute(sql, values)
		result = self.cursor.fetchall()
        df = pd.DataFrame(result)
        if user is not None:
            df = df.loc[df["user"]==user]
        df.groupby(["user","ticker"]).sum()["amount"]
        df.to_csv(user + "_" + self.positions, index=False)
        return self.db_url + user + "_" + self.positions
        
    def show_owns(self, ticker):
        sql = "SELECT * FROM portfolio_actions"
		self.cursor.execute(sql, values)
		result = self.cursor.fetchall()
        df = pd.DataFrame(result)
        df = df.loc[df["ticker"]==ticker]
        df.groupby(["user","ticker"]).sum()["amount"]
        df.to_csv(ticker + "_" + self.positions, index=False)
        return self.db_url + ticker + "_" + self.positions