import os
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from currencycat import db

db.session

[u'instrument', u'candles', u'granularity']

{
  u'closeMid': 1.141445,
  u'complete': True,
  u'highMid': 1.141445,
  u'lowMid': 1.141415,
  u'openMid': 1.141415,
  u'time': u'2016-06-09T02:57:20.000000Z',
  u'volume': 2
  }


Base = declarative_base()

class Candle(Base):
    __tablename__ = "Candles"

    #FIXME Oanda uses instrument instead of pair. Should I use their language?
    uid = db.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(sqlalchemy.String)
    complete = db.Column(sqlalchemy.Boolean)
    closeMid = db.Column(sqlalchemy.Float)
    highMid = db.Column(sqlalchemy.Float)
    lowMid = db.Column(sqlalchemy.Float)
    volume = db.Column(sqlalchemy.Integer)
    openMid = db.Column(sqlalchemy.Float)
    time = db.Column(sqlalchemy.DateTime)
    granularity = db.Column(sqlalchemy.String)
