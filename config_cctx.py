# -*- coding: utf-8 -*-
import ccxt
import os
import dotenv
dotenv.load_dotenv()
print('CCXT Version:', ccxt.__version__)

exchange = ccxt.binance({
    'apiKey': os.environ.get('apiKey'),
    'secret': os.environ.get('secret'),
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot'
    }
})
exchange.set_sandbox_mode(True) # uncomment for mainnet
exchange.verbose = True  # uncomment for debugging