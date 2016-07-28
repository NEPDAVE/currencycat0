import pandas as pd
from currencycat import db
from datetime import datetime


def latest_closemid(instrument, granularity):
    query = """
    SELECT closemid, time FROM candles
    where instrument = '{}' and granularity = '{}'
    ORDER BY time DESC
    LIMIT 1;
    """.format(instrument, granularity)

    series = pd.read_sql_query(query, db.engine).iloc[0]

    return series.closemid, series.time


def average_closemid(instrument, granularity, days):
    granularity_keys = {"H2": 2, "H3": 3, "H4": 4, "H6": 6, "H8": 8, "H12": 12,
                        "D": 24}
    limit = (24 * days)/granularity_keys[granularity]

    query = """
    SELECT closemid, time FROM candles
    where instrument = '{}' and granularity = '{}'
    ORDER BY time DESC
    LIMIT '{}';
    """.format(instrument, granularity, limit)

    df = pd.read_sql_query(query, db.engine).sort_values('time')

    return df.closemid.mean(), df.iloc[0].time, df.iloc[-1].time


def buy_forex(instrument, granularity, days, percent_lower):
    average = average_closemid(instrument, granularity, days)
    latest = latest_closemid(instrument, granularity)

    print latest[0], average[0], average[0] * (1 - percent_lower)

    return latest[0] < average[0] * (1 - percent_lower)
