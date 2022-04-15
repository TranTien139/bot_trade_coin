from config_cctx import *
import pprint
def getCurrentBalance():
    balance = exchange.fetch_balance()
    pprint.pprint(balance)