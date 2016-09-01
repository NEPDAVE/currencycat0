import os

from redis import Redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

conn = Redis()
#redis_url = 'localhost'
#conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
