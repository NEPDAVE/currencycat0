import pandas as pd
from currencycat import db, database, models
from sqlalchemy import create_engine


def query_db(query):
    return pd.read_sql_query(query, db.engine)


def calculate_statistics(df, width=None):
    if not width:
        width = 20
    df['mean'] = df.closemid.rolling(window=width).mean()
    df.dropna(subset=['mean'])
    return df

#FIXME figure out how to calculate vwap.
def vwap():
    pass


#where should this live? should it be imported?
def buy_currency(closemid, mean):
    return closemid < mean


def convert_to_base_currency(account_balance, closemid):
    account_balance = account_balance/closemid
    return account_balance


def convert_to_counter_currency(account_balance, closemid):
    account_balance = account_balance*closemid
    return account_balance


def backtest_algorithm(df):
    for closemid, time, mean in df[['closemid', 'time', 'mean']].itertuples(
            index=False):
        if open_position:
            if closemid <= (price_paid - (price_paid * .00007)):
                account_balance = convert_to_counter_currency(
                        account_balance, closemid)
                open_position = False
            elif closemid >= (price_paid + (price_paid * .00025)):
                account_balance = convert_to_base_currency(
                        account_balance, closemid)
                open_position = False
        elif buy_currency(closemid, mean):
            price_paid = closemid
            open_position = True
        else:
            open_position = False

        #FIXME you need to be returning a df that you will cocatenate from
        #these two lists. Then you will be able to look at the chart.
        account_balance_series.append(account_balance)
        time_series.append(time)

    backtest_data = (account_balance_series, time_series)

    return backtest_data


def main(query):
    raw_df = query_db(query)
    df = calculate_statistics(raw_df)
    backtest_data = backtest_algorithm(df)
    print backtest_data
    return backtest_data


if __name__ == '__main__':
    main(query)
