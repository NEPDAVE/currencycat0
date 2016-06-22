from currencycat import models
from currencycat import db
from datetime import datetime


def seed_db():
    q = models.Quote(pair='EUR_USD', granularity='H4', count=5000)
    try:
        for candle in q.response['candles']:
            row = models.Candle()

            row.instrument = q.pair
            row.complete = candle['complete']
            row.closeMid = candle['closeMid']
            row.highMid = candle['highMid']
            row.lowMid = candle['lowMid']
            row.volume = candle['volume']
            row.openMid = candle['openMid']
            #FIXME convert this from a string to a DateTime object
            row.time = datetime.strptime(candle['time'],
                                         "%Y-%m-%dT%H:%M:%S.%fZ")
            row.granularity = q.granularity

            db.session.add(row)
        db.session.commit()
    except:
        db.session.rollback()
