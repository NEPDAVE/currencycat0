import os

from flask import Flask, request, redirect, Response, render_template
from twilio.rest import TwilioRestClient
import twilio.twiml


from models import Quote
from currencycat import app

#Twilio number
#980 223 6739

major_pairs = ['EUR_USD', 'GBP_USD', 'USD_CHF', 'USD_JPY']

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

    if msg == "Hello":
        send(request.args['From'], instructions)
    elif msg == "Majors":
        for pair in major_pairs:
            quote = Quote(pair=pair)
            quote_msg = "{} = {}".format(pair, quote.quote)
            send(request.args['From'], quote_msg)
    elif msg == "Read":
        read_msg = "A great article on how to read currency pairs: {}".format(
            "http://www.investopedia.com/university/forexmarket/forex2.asp")
        send(request.args['From'], read_msg)
    else:
        quote = Quote(pair=msg)
        quote_msg = "{} = {}".format(msg, quote.quote)
        send(request.args['From'], quote_msg)

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
