import os

from flask import Flask, request, redirect, Response, render_template
from twilio.rest import TwilioRestClient
import twilio.twiml

from models import Quote
from currencycat import app, analysis

#Twilio number
#980 223 6739

#help email
#api@oanda.com
#list of all available rates in the USA
#https://www.oanda.com/resources/legal/united-states/legal/margin-rates
#curl command to get all instruments
#curl -X GET "https://api-fxtrade.oanda.com/v1/instruments?accountId=8500841"

major_pairs = ['EUR_USD', 'GBP_USD', 'USD_CHF', 'USD_JPY']
all_pairs = [
    'AUD_CAD', 'AUD_CHF', 'AUD_HKD', 'AUD_JPY', 'AUD_NZD', 'AUD_SGD',
    'AUD_USD', 'CAD_CHF', 'CAD_HKD', 'CAD_JPY', 'CAD_SGD', 'CHF_HKD',
    'CHF_JPY', 'CHF_ZAR', 'EUR_AUD', 'EUR_CAD', 'EUR_CHF', 'EUR_CZK',
    'EUR_DKK', 'EUR_GBP', 'EUR_HKD', 'EUR_HUF', 'EUR_JPY', 'EUR_NOK',
    'EUR_NZD', 'EUR_PLN', 'EUR_SEK', 'EUR_SGD', 'EUR_TRY', 'EUR_USD',
    'EUR_ZAR', 'GBP_AUD', 'GBP_CAD', 'GBP_CHF', 'GBP_HKD', 'GBP_JPY',
    'GBP_NZD', 'GBP_PLN', 'GBP_SGD', 'GBP_USD', 'GBP_ZAR', 'HKD_JPY',
    'NZD_CAD', 'NZD_CHF', 'NZD_HKD', 'NZD_JPY', 'NZD_SGD', 'NZD_USD',
    'SGD_CHF', 'SGD_HKD', 'SGD_JPY', 'TRY_JPY', 'USD_CAD', 'USD_CHF',
    'USD_CNH', 'USD_CZK', 'USD_DKK', 'USD_HKD', 'USD_HUF', 'USD_JPY',
    'USD_MXN', 'USD_NOK', 'USD_PLN', 'USD_SAR', 'USD_SEK', 'USD_SGD',
    'USD_THB', 'USD_TRY', 'USD_ZAR', 'ZAR_JPY'
    ]

@app.route("/quote")
def receive():

    instructions = """
Hello! Please text one of these pairs for a real time Forex Quote:
{}

Text 'Majors' If you would like a quote for all the Major pairs.

Text 'Read' for a great article on how to read currency pairs.
""".format(", ".join(major_pairs))

    print request.args
    msg = request.args.get("Body", "None")
    print msg

    msg = msg.lower()

    if msg == "hello":
        send(request.args['From'], instructions)
    elif msg == "majors":
        quote_msg = ""
        for pair in major_pairs:
            quote = Quote(pair=pair)
            majors_quote = "{} = {}".format(pair, quote.quote)
            quote_msg += str(majors_quote) + "\n"
        send(request.args['From'], quote_msg)
    elif msg == "read":
        read_msg = "A great article on how to read currency pairs: {}".format(
            "http://www.investopedia.com/university/forexmarket/forex2.asp")
        send(request.args['From'], read_msg)
    elif msg.upper() in all_pairs:
        quote = Quote(pair=msg.upper())
        quote_msg = "{} = {}".format(msg.upper(), quote.quote)
        send(request.args['From'], quote_msg)
    elif msg == "buy?":
        decision = buy_forex("EUR_USD", "H4", 5, .01)
        send(request.args['From'], str(decision))
    else:
        send(request.args['From'], """
            Sorry, please try again. Text 'Hello' for instructions
            """)
    return msg


def send(recipient, message):
    """Respond to incoming calls with a simple text message."""

    # put your own credentials here
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']

    client = TwilioRestClient(account_sid, auth_token)

    client.messages.create(
        to=recipient,
        from_="+19802236739",
        body=message,
    )


#return render_template('index.html', **paramapp.route("/")
@app.route("/")
def index():

    params = {q: Quote(pair=q).quote for q in major_pairs}

    return render_template('about.html', **params)
