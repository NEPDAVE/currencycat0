from apscheduler.schedulers.blocking import BlockingScheduler
from currencycat.database import seed_db


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job_m1():
    seed_db(pair='EUR_USD', count=1, granularity='M1')
    print('This job is run every minute.')


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

sched.start()
