import os
import sqlalchemy
import requests

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from currencycat import db



#FIXME is this the best name for this class? You're also using it to get
#entire candels.
class Quote(object):
    def __init__(self, pair=None, count=None, granularity=None):
        self.pair = pair
        self.count = count
        self.granularity = granularity
        self.response = self.get_quotes()


    def get_quotes(self):
        headers = {"Authorization": "Bearer" + " " + os.environ['OANDA_TOKEN']}

        if not self.pair:
            self.pair = "EUR_USD"

        if not self.count:
            self.count = "1"

        if not self.granularity:
            self.granularity = "S5"

        params = {
            "instrument": self.pair,
            "count": self.count,
            "candleFormat": "midpoint",
            "granularity": self.granularity,
            "Timezone": "America/New_York"
            }

        url = "https://api-fxpractice.oanda.com/v1/candles"

        r = requests.get(url, params=params, headers=headers)

        self.quote = r.json()['candles'][0]['closeMid']

        return r.json()


class Candle(db.Model):
    __tablename__ = "Candles"

    #FIXME Oanda uses instrument instead of pair. Should I use their language?
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(db.String)
    complete = db.Column(db.Boolean)
    closeMid = db.Column(db.Float)
    highMid = db.Column(db.Float)
    lowMid = db.Column(db.Float)
    volume = db.Column(db.Integer)
    openMid = db.Column(db.Float)
    time = db.Column(db.DateTime)
    granularity = db.Column(db.String)
