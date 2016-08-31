from database import seed_db
from apscheduler.schedulers.blocking import BlockingScheduler

top_pairs = [
    'USD_CAD', 'EUR_JPY', 'EUR_USD', 'EUR_CHF', 'USD_CHF', 'EUR_GBP',
    'GBP_USD', 'AUD_CAD', 'NZD_USD', 'GBP_CHF', 'AUD_USD', 'GBP_JPY',
    'USD_JPY', 'CHF_JPY', 'EUR_CAD', 'AUD/JPY', 'EUR_AUD', 'AUD_NZD'
    ]

"""
Example:
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
sched.start()
"""

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1440)
def seed_top_pairs(top_pairs, granularity='D'):
    for pair in top_pairs:
        seed_db(pair=pair, count=1, granularity=granularity)


@sched.scheduled_job('interval', minutes=240)
def seed_top_pairs(top_pairs, granularity='H4'):
    for pair in top_pairs:
        seed_db(pair=pair, count=1, granularity=granularity)


@sched.scheduled_job('interval', minutes=60)
def seed_top_pairs(top_pairs, granularity='H'):
    for pair in top_pairs:
        seed_db(pair=pair, count=1, granularity=granularity)


@sched.scheduled_job('interval', minutes=1)
def seed_top_pairs(top_pairs, granularity='M1'):
    for pair in top_pairs:
        seed_db(pair=pair, count=1, granularity=granularity)

sched.start()
