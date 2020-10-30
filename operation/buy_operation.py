from .start_operation import BaseOperator
from binance.client import Client
import logging
import time

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class LimitOperator(BaseOperator):

    def __init__(self, api_key, api_secret):
        BaseOperator.__init__(self, api_key=api_key, api_secret=api_secret)
        self.connect()
    
    def market_buy(self, symbol, quantity=None, quoteOrderQty=None):
        '''
        Buy order at market price
        '''
        if quantity:
            self.client.order_market_buy(symbol=symbol, quantity=quantity)
        elif quoteOrderQty:
            self.client.order_market_buy(symbol=symbol, quoteOrderQty=quoteOrderQty)
        else:
            raise Exception ("No quantity indicated")

        logging.info("Buy order filled")