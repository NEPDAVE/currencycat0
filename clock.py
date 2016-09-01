from apscheduler.schedulers.blocking import BlockingScheduler
from currencycat.database import seed_db

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=30)
def timed_job():
    seed_db(pair='EUR_USD', count=1, granularity='M1')
    print('This job is run every three seconds.')

sched.start()
