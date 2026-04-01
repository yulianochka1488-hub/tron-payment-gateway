# TRON Payment Gateway

Simple payment gateway for accepting USDT TRC20 payments.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
python3 gateway.py
```

## Features
- Auto-detect incoming USDT transfers
- Webhook notifications
- Multi-currency support
- Rate limiting

## API

```
POST /api/invoice - Create new invoice
GET /api/invoice/:id - Check payment status
POST /api/webhook - Payment callback
```

## License
MIT
