import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
import os

#"CREATE TABLE portfolio_actions (action_date TIMESTAMP, username VARCHAR(140), action VARCHAR(140), amount FLOAT(10), ticker VARCHAR(140), price FLOAT(10));"

#Implementation of required functions for data retrieval and verification using MySQL server
class Database:
    #replace variables with appropriate credentials
    def __init__(self):
        load_dotenv()
        db_config = {
            'pool_size': 5,
            'max_overflow': 2,
            'pool_timeout': 30,
            'pool_recycle': 1800,
        }

        conn = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="postgres+pg8000",
                username=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASS'),
                database=os.environ.get('DB_NAME'),
                query={
                    "unix_sock":"/cloudsql/{}/./s.PGSQL.5432".format(os.environ.get("CLOUD_SQL_CONNECTION_NAME"))
                }
            ),
            **db_config
        )
        conn.dialect.description_encoding = None
        self.cursor = conn.connect()
    
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