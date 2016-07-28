import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
print os.environ['DATABASE_URL']
db = SQLAlchemy(app)

import currencycat.views
