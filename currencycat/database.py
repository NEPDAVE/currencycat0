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
            row.closemid = candle['closeMid']
            row.highmid = candle['highMid']
            row.lowmid = candle['lowMid']
            row.volume = candle['volume']
            row.openmid = candle['openMid']
            row.time = datetime.strptime(candle['time'],
                                         "%Y-%m-%dT%H:%M:%S.%fZ")
            row.granularity = q.granularity

            db.session.add(row)
        db.session.commit()
        print 'stored {} candles'.format(len(q.response['candles']))
    except Exception as e:
        print 'ERROR: {}'.format(e)
        db.session.rollback()
