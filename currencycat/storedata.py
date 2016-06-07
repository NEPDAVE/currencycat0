
import requests
import datetime
from datetime import timedelta
from collections import Counter

#"Sample URL to get history"
#"https://api-fxtrade.oanda.com/v1/candles?instrument=EUR_USD&start=2014-06-19T15%3A47%3A40Z&end=2014-06-19T15%3A47%3A50Z"




#authenticating with zendesk
with open('zendesk_email.txt', 'r') as e:
    email = e.read()

with open('zendesk_password.txt', 'r') as p:
    password = p.read()

zendesk_url = 'https://perka.zendesk.com/api/v2/'


class ReportingPeriod(object):
    def __init__(self, start=None, end=None, view_id=None):
        print "Initializing"
        self.start = start
        self.end = end
        self.format_start()
        self.format_end()
        self.view_id = view_id
        self.topic_counts = {}

from modles import Quote


    def format_start(self):
        start_date = datetime.date.today() - timedelta(days=self.start)
        formatted_start = start_date.strftime('%Y-%m-%d')

        return formatted_start

    def format_end(self):
        end_date = datetime.date.today() - timedelta(days=(self.end + 1))
        formatted_end = end_date.strftime('%Y-%m-%d')




i = RawApiReturn

i.instrument = json['instrument']
i.complete =  json['candles'][0]['complete']
i.closeMid = json['candles'][0]['closeMid']
i.highMid = json['candles'][0]['highMid']
i.lowMid = json['candles'][0]['lowMid']
i.volume = json['candles'][0]['volume']
i.openMid = json['candles'][0]['openMid']
i.time = json['candles'][0]['time']
i.granularity = json['granularity']
