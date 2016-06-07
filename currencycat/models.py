import os
import requests


class Quote(object):
    def __init__(self, pair=None, count=None, granularity=None):
        self.count = count
        self.pair = pair
        self.granularity = granularity
        self.response = self.get_quotes()


    def get_quotes(self):
        headers = {"Authorization": "Bearer" + " " + os.environ['OANDA_TOKEN']}

        if not self.count:
            self.count = "1"

        if not self.granularity:
            self.count = "S5"

        params = {
            "instrument": self.pair,
            "count": self.count,
            "candleFormat": "midpoint",
            "granularity": self.granularity,
            "Timezone": "America/New_York"
            }

        URL = "https://api-fxpractice.oanda.com/v1/candles"

        r = requests.get(URL, params=params, headers=headers)

        self.quote = r.json()['candles'][0]['closeMid']

        return r.json()
