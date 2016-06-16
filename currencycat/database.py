from currencycat import models
from currencycat import db


def seed_db():
    q = models.Quote(pair='EUR_USD', granularity='H4', count=50)
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
        row.time = candle['time']
        row.granularity = q.granularity

        db.session.add(row)
    db.session.commit()
