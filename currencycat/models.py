import os
import requests


class Quote(object):
    def __init__(self, count=None, pair=None):
        self.count = count
        self.pair = pair
        self.get_quotes()

    def get_quotes(self):
        headers = {"Authorization": "Bearer" + " " + os.environ['OANDA_TOKEN']}

        if not self.count:
            self.count = '1'

        params = {
            "instrument": self.pair,
            "count": self.count,
            "candleFormat": "midpoint",
            "granularity": "S5",
            "Timezone": "America/New_York"
            }

        URL = "https://api-fxpractice.oanda.com/v1/candles"

        r = requests.get(URL, params=params, headers=headers)

        self.quote = r.json()['candles'][0]['closeMid']
