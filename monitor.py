import os
import time
from tronpy import Tron
from dotenv import load_dotenv

load_dotenv()
client = Tron()
addr = os.getenv('TRON_ADDRESS')

while True:
    try:
        info = client.get_account(addr)
        print(f'Balance: {info}')
    except Exception as e:
        print(f'Error: {e}')
    time.sleep(30)
