# -*- coding: utf-8 -*-
from config_cctx import *
import time
import pprint
from constant import BTC_USDT
from balance import getCurrentBalance
from telegram import send_telegram_message

def tradeCoin():
    while(True):
        response = exchange.fetchOHLCV(
            symbol=BTC_USDT,
            timeframe='15m',
            params={"price": 'mark'}
        )
        length = len(response)
        print('----------------------------------------------------------')
        index = 4
        lastPrice = response[length - 1][index]
        secondPrice = response[length - 2][index]
        thirdPrice = response[length - 3][index]

        print (lastPrice, secondPrice, thirdPrice, lastPrice > secondPrice and secondPrice > thirdPrice, lastPrice < secondPrice and secondPrice < thirdPrice)

        if lastPrice > secondPrice and secondPrice > thirdPrice:
            pprint.pprint("Buy BTC")
            exchange.create_market_buy_order(BTC_USDT, 0.01)

        if lastPrice < secondPrice and secondPrice < thirdPrice:
            pprint.pprint("Sell BTC")
            exchange.create_market_sell_order(BTC_USDT, 0.01)

        balance = getCurrentBalance()
        print("Balance BTC/USDT " + str(balance['BTC']['total']) + ' / ' + str(balance['USDT']['total']))
        message = "Balance BTC={} , USDT={} và 3 giá BTC gần nhất là {} , {} , {}".format(str(balance['BTC']['total']), str(balance['USDT']['total']), lastPrice, secondPrice, thirdPrice)
        send_telegram_message(message)
        # for item in response:
        #     print("Price at: ", datetime.fromtimestamp(item[0]/1000).strftime('%H:%M:%S %d-%m-%Y'), item[index])

        print('-----------------------------------------------------------')
        time.sleep(60 * 15)