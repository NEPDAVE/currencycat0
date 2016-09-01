from apscheduler.schedulers.blocking import BlockingScheduler
from currencycat.database import seed_db
from rq import Queue
from worker import conn


top_pairs = [
    'USD_CAD', 'EUR_JPY', 'EUR_USD', 'EUR_CHF', 'USD_CHF', 'EUR_GBP',
    'GBP_USD', 'AUD_CAD', 'NZD_USD', 'GBP_CHF', 'AUD_USD', 'GBP_JPY',
    'USD_JPY', 'CHF_JPY', 'EUR_CAD', 'AUD/JPY', 'EUR_AUD', 'AUD_NZD'
    ]

sched = BlockingScheduler()

q = Queue(connection=conn)


@sched.scheduled_job('interval', minutes=1)
def timed_job_m1():
    for pair in top_pairs:
        print 'Adding {}: Granularity, M1'.format(pair)
        #seed_db(pair=pair, count=1, granularity='M1')
        job = q.enqueue(seed_db, pair=pair, count=1, granularity='M1')
        print job.result

'''
@sched.scheduled_job('interval', hours=1)
def timed_job_h1():
    seed_db(pair='EUR_USD', count=1, granularity='H1')
    print('This job is run every hour.')


@sched.scheduled_job('interval', hours=4)
def timed_job_h4():
    seed_db(pair='EUR_USD', count=1, granularity='H4')
    print('This job is run every four hours.')


@sched.scheduled_job('interval', hours=24)
def timed_job_d():
    seed_db(pair='EUR_USD', count=1, granularity='D')
    print('This job is run every 24 hours.')
'''
sched.start()
