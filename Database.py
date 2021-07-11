import pandas as pd
import sqlalchemy
import os

#"CREATE TABLE portfolio_actions (action_date TIMESTAMP, username VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));"

#Implementation of required functions for data retrieval and verification using MySQL server

#postgresql://root:password@/portfolio_actions?unix_sock=cloudsql/trackerbot-319119:northamerica-northeast1:my-ptsql/.s.PGSQL.5432
class Database:
    #replace variables with appropriate credentials
    def __init__(self):
        self.db_url = ""
        self.engine = sqlalchemy.create_engine('sqlite:///database.db')
        with self.engine.connect("database.db") as con:
            con.execute("CREATE TABLE IF NOT EXISTS portfolio_actions (action_date TIMESTAMP, username VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));")
    
    def update_position(self, user, action, amount, ticker, price):
        with self.engine.connect("database.db") as con:
            sql = "INSERT INTO portfolio_actions (action_date, username, action, amount, ticker, price) VALUES (CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)"
            con.execute(sql, [user, action, amount, ticker, price])
            return "Success"
    
    def show_all(self):
        with self.engine.connect("database.db") as con:
            sql = "SELECT * FROM portfolio_actions"
            result = con.execute(sql)
            df = pd.DataFrame(result)
            df.columns = ["action_date", "username", "action", "amount", "ticker", "price"]
            df = df.groupby(["username","ticker"]).sum()["amount"]
            return pd.DataFrame(df).to_html()
    
    
    def show_user(self, user):
        with self.engine.connect("database.db") as con:
            sql = "SELECT * FROM portfolio_actions"
            result = con.execute(sql)
            df = pd.DataFrame(result)
            df.columns = ["action_date", "username", "action", "amount", "ticker", "price"]
            df = df.loc[df["username"]==user]
            df = df.groupby(["username","ticker"]).sum()["amount"]
            return pd.DataFrame(df.to_html()).to_html()

    def show_ticker(self, ticker):
        with self.engine.connect("database.db") as con:
            sql = "SELECT * FROM portfolio_actions"
            result = con.execute(sql)
            df = pd.DataFrame(result)
            df.columns = ["action_date", "username", "action", "amount", "ticker", "price"]
            df = df.loc[df["ticker"]==ticker]
            df = df.groupby(["user","ticker"]).sum()["amount"]
            return pd.DataFrame(df).to_html()