# -*- coding: utf-8 -*-
from config_cctx import *
from datetime import datetime
import time
import pprint
from constant import BTC_USDT

def tradeCoin():
    while(True):
        response = exchange.fetchOHLCV(
            symbol=BTC_USDT,
            timeframe='1m',
            params={"price": 'mark'}
        )
        length = len(response)
        print('----------------------------------------------------------')
        pprint.pprint(length)
        # for item in response:
        #     print("Price", datetime.fromtimestamp(item[0]/1000).strftime('%H:%M:%S %d-%m-%Y'), item)
        # exchange.create_market_buy_order(symbol, 0.1)
        # exchange.create_market_sell_order(symbol, 0.5)
        print('-----------------------------------------------------------')
        time.sleep(60)