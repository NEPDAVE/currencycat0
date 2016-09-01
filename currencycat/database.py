from currencycat import models
from currencycat import db
from datetime import datetime


def seed_db(pair=None, count=None, granularity=None):
    q = models.Quote(pair=pair, count=count, granularity=granularity)
    try:
        for candle in q.response['candles']:
            #FIXME do you want to think about checking if the value is already
            #in the db before moving onto the next candle? If your pinging the
            #system at right at the top of the hour, is there a chance that it
            #could send you the quote for the previouse period instead of the
            #newest?
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
