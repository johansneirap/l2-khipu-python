import json
from credentials import receiverId, secret
from pykhipu.client import Client
from flask import Flask,jsonify, url_for

app= Flask(__name__)

client = Client(receiver_id=receiverId, secret=secret)

@app.route('/test-payment/<string:subject>/<string:currency>/<int:amount>')
def test_payment(subject,currency,amount):
    payment = client.payments.post(subject, currency, amount ,body="k pasa",picture_url='https://raw.githubusercontent.com/johansneirap/l2hubble/main/images/logo-hubble550.png',return_url='http://localhost:5000/waiting-confirm-payment',cancel_url='http://localhost:5000/cancel-payment')
    print(json.dumps(payment.__dict__))
    return json.dumps(payment.__dict__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/waiting-confirm-payment')
def wait_payment():
    return 'We are waiting for your payment validation. In few moments you will be redirected to L2 Hubble'

@app.route('/cancel-payment')
def cancel_payment():
    return 'Your purchase was canceled'

resp = client.payments.get_id('rsakehr7k9wr')
notfication_token = resp.notification_token

resp_payment = client.payments.get(notfication_token)
print(resp_payment.__dict__)

if (__name__)=="__main__":
    app.run(debug=True)
