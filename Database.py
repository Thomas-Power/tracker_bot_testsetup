import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#"CREATE TABLE portfolio_actions (action_date TIMESTAMP, username VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));"

#Implementation of required functions for data retrieval and verification using MySQL server

#postgresql://root:password@/portfolio_actions?unix_sock=cloudsql/trackerbot-319119:northamerica-northeast1:my-ptsql/.s.PGSQL.5432
class Database:
    #replace variables with appropriate credentials
    def __init__(self):
        load_dotenv()
        conn = engine = create_engine('sqlite:///sqlite3.db')
        self.cursor = conn.connect()
        self.cursor.execute("CREATE TABLE portfolio_actions (action_date TIMESTAMP, username VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));")
    
    def update_position(self, user, action, amount, ticker, price):
        sql = "INSERT INTO portfolio_actions (action_date, username, action, amount, ticker) VALUES (current_timestamp, %s, %s, %s, %s)"
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