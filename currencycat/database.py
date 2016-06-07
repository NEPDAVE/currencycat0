import os

from sqlalchemy import create_engine

def get_connection():
    url = os.environ['DATABASE_URL']
    return create_engine(url)
