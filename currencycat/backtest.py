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
    def __init__(self, query, width=None):
        self.query = query
        self.engine = db.engine
        self.width = None
        self.df = self.create_df()

    def create_df(self):
        if not self.width:
            self.width = 20
        #querying database
        df = pd.read_sql_query(self.query, self.engine)
        #Calculating statistics
        df['mean'] = df.closemid.rolling(window=self.width).mean()
        df = df.dropna(subset = ['mean'])
        #df['vwma'] = df.closemid.rolling(window=width).mean()
        #return df.dropna(subset=['vwma'])
        return df

class Backtest(object):
    def __init__(self, df, account_balance):
        self.df = df
        self.account_balance = account_balance
        self.buy_currency
        self.convert_to_base_currency
        self.convert_to_counter_currency
        self.open_position = False
        self.price_paid = None
        self.account_balance_series = []
        self.time_series = []
        self.backtest_algorithm()

    #where should this live? should it be imported?
    def buy_currency(self, closemid, mean):
        return closemid < mean

    def convert_to_base_currency(self, account_balance, closemid):
        account_balance = account_balance/closemid
        return account_balance

    def convert_to_counter_currency(self, account_balance, closemid):
        account_balance = account_balance*closemid
        return account_balance

    def backtest_algorithm(self):
        for closemid, time, mean in self.df[['closemid', 'time', 'mean']].itertuples(index=False):
            if self.open_position:
                if closemid <= (self.price_paid - (self.price_paid * .00007)):
                    self.account_balance = self.convert_to_counter_currency(self.account_balance, closemid)
                    self.open_position = False
                elif closemid >= (self.price_paid + (self.price_paid * .00025)):
                    self.account_balance = self.convert_to_base_currency(self.account_balance, closemid)
                    self.open_position = False
            elif self.buy_currency(closemid, mean):
                self.price_paid = closemid
                self.open_position = True
            else:
                self.open_position = False

            self.account_balance_series.append(self.account_balance)
            self.time_series.append(time)

        return self.df

#print len(account_balance_series)
#print len(time_series)

#print account_balance_series[:10]
#print time_series[:10]


#dates = matplotlib.dates.date2num(time_series)
#matplotlib.pyplot.plot_date(dates, account_balance_series)



df = PrepareBacktest('select * from Candles', db.engine)
data = Backtest(df.df, 100)

new_df = pd.DataFrame()

new_df['time'] = data.time_series
new_df['balance'] = data.account_balance_series

print type(data.time_series)
print type(data.account_balance_series)

new_df = new_df.set_index('time')
new_df[['balance']].plot(figsize=(24,12))
