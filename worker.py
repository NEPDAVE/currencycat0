import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

#redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_url = os.getenv('REDISTOGO_URL', 'redis://redistogo:e17dc9d6670e6c9aae6f3ce4ffcd03be@catfish.redistogo.com:11215/')


conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
