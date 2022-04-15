# -*- coding: utf-8 -*-
from config_cctx import *
from constant import BTC_USDT
import pprint

def getHistoryTrade():
    day = 24 * 60 * 60 * 1000
    start_time = exchange.parse8601('2022-03-01T00:00:00')
    now = exchange.milliseconds()
    all_trades = []
    while start_time < now:
        print('------------------------------------------------------------------')
        print('Fetching trades from', exchange.iso8601(start_time))
        end_time = start_time + day

        trades = exchange.fetch_my_trades(BTC_USDT, start_time, None, {
            'endTime': end_time,
        })
        if len(trades):
            last_trade = trades[len(trades) - 1]
            start_time = last_trade['timestamp'] + 1
            all_trades = all_trades + trades
        else:
            start_time = end_time

    print('Fetched', len(all_trades), 'trades')
    for i in range(0, len(all_trades)):
        trade = all_trades[i]
        print (i, trade['id'], trade['datetime'], trade['amount'])