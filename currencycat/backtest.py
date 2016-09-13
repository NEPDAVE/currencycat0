#!!!!!!#
#this looks like its working!!!!!!!!
#use the algorithm that you already have… create a new df with two columns…. “time” and “account balance,” these are the two things you needs too see an analyze. don’t worry about “last price paid” or anything like that… if you can do this and then plot the data using marplot lib and js you will be able to really start messing around.

#FIXME this is way too many imports....
import pandas as pd
import os
import psycopg2
import matplotlib as mpl
import matplotlib.pyplot as plt
from currencycat import db, database, models
from sqlalchemy import create_engine
from matplotlib import finance

from IPython.display import display

import matplotlib
import matplotlib.pyplot as plt

#This will create the df


class PrepareBacktest(object):
    def __init__(self, query, engine, width=None):
        self.query = query
        self.engine = engine
        self.width = None
        self.query_db
        self.calculate_statistics
        self.df = self.create_df()

    def query_db(self, query):
        raw_df = pd.read_sql_query(query, db.engine)
        return raw_df

    def calculate_statistics(self, width, raw_df):
        if not self.width:
            self.width = 20
        raw_df['mean'] = raw_df.closemid.rolling(window=width).mean()
        return raw_df.dropna(subset = ['mean'])
        #f['vwma'] = df.closemid.rolling(window=width).mean()
        #return df.dropna(subset=['vwma'])

    def create_df(self, width=None):
        if not self.width:
            self.width = 20
        raw_df = self.query_db(self.query)
        self.df = self.calculate_statistics(self.width, raw_df)


class Backtest(object):
    def __init__(self, df, account_balance):
        self.df = df
        self.account_balance = account_balance
        self.open_position = False
        self.price_paid = None
        self.account_balance_series = []
        self.time_series = []
        self.backtest_algorithm(account_balance)

    #where should this live? should it be imported?
    def buy_currency(closemid, mean):
        return closemid < mean

    def convert_to_base_currency(account_balance, closemid):
        account_balance = account_balance/closemid
        return account_balance

    def convert_to_counter_currency(account_balance, closemid):
        account_balance = account_balance*closemid
        return account_balance

    def backtest_algorithm(self):
        for closemid, time, mean in df[['closemid', 'time', 'mean']].itertuples(index=False):
            if open_position:
                if closemid <= (self.price_paid - (self.price_paid * .00007)):
                    self.account_balance = convert_to_counter(self.account_balance, closemid)
                    self.open_position = False
                elif closemid >= (self.price_paid + (self.price_paid * .00025)):
                    account_balance = convert_to_base(self.account_balance, closemid)
                    open_position = False
            elif buy_forex(closemid, mean):
                self.price_paid = closemid
                self.open_position = True
            else:
                self.open_position = False

            self.account_balance_series.append(self.account_balance)
            self.time_series.append(time)

#print len(account_balance_series)
#print len(time_series)

#print account_balance_series[:10]
#print time_series[:10]


#dates = matplotlib.dates.date2num(time_series)
#matplotlib.pyplot.plot_date(dates, account_balance_series)



df = PrepareBacktest('select * from Candles', db.engine)
data = Backtest(df, 100)

new_df = pd.DataFrame()

new_df['time'] = data.time_series
new_df['balance'] = data.account_balance_series




final = new_df.set_index('time')
final[['balance']].plot(figsize=(24,12))
