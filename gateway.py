import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from tronpy import Tron

load_dotenv()

app = Flask(__name__)
client = Tron()

PRIVATE_KEY = os.getenv('TRON_PRIVATE_KEY')
WALLET = os.getenv('TRON_ADDRESS')

@app.route('/api/invoice', methods=['POST'])
def create_invoice():
    data = request.json
    amount = data.get('amount', 0)
    return jsonify({'address': WALLET, 'amount': amount, 'token': 'USDT'})

@app.route('/api/balance')
def balance():
    bal = client.get_account_balance(WALLET)
    return jsonify({'balance': str(bal)})

if __name__ == '__main__':
    app.run(port=5000)
