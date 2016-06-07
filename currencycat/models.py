import os
import requests


class Quote(object):
    def __init__(self, pair=None, count=None, granularity=None):
        self.pair = pair
        self.count = count
        self.granularity = granularity
        self.response = self.get_quotes()


    def get_quotes(self):
        headers = {"Authorization": "Bearer" + " " + os.environ['OANDA_TOKEN']}

        if not self.pair:
            self.pair = "EUR_USD"

        if not self.count:
            self.count = "1"

        if not self.granularity:
            self.granularity = "S5"

        params = {
            "instrument": self.pair,
            "count": self.count,
            "candleFormat": "midpoint",
            "granularity": self.granularity,
            "Timezone": "America/New_York"
            }

        url = "https://api-fxpractice.oanda.com/v1/candles"

        r = requests.get(url, params=params, headers=headers)

        self.quote = r.json()['candles'][0]['closeMid']

        return r.json()
