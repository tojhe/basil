from .start_operation import BaseOperator
from binance.client import Client
import logging
import time

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class TrailingBuyOperator(BaseOperator):
    '''
    Operator for trailing buy
    '''

    def __init__(self, api_key, api_secret):
        BaseOperator.__init__(self, api_key=api_key, api_secret=api_secret)
        self.connect()

        self.price_order = None
        self.present_price = None
        self.buy_condition = None
        self.buy_condition_activate_price = None
        self.deviation = None
        self.trailing_buy_state = False
        self.bought_stop = False

    def _update_buy_condition(self, price, deviation=1):
        self.buy_condition = price*((100+deviation)/100)

    def _actor(self, symbol):
        '''
            Primary logic for monitoring price and executing trailing buy operations
            params: symbol(str) - ticker symbol
        '''
        # check price
        self.present_price = float(self.client.get_symbol_ticker(symbol=symbol)["price"])

        # when trailing buy already activated
        if self.trailing_buy_state:
            # buy token when present price matched/surpassed Buy Condition price
            if self.present_price >= self.buy_condition:
                # Action Buy at present_price
                # TODO: send message to open order operator
                logging.info(f"Buy executed, Price:{self.present_price}, Buy Condition:{self.buy_condition} \n")
                self.bought_stop = True

            # update to better/lower buy condition
            elif self.present_price < self.buy_condition_activate_price:
                self._update_buy_condition(price=self.present_price, deviation=self.deviation)
                self.buy_condition_activate_price = self.present_price
                logging.info(f"Buy Condition Updated, Price:{self.present_price}, Buy Condition:{self.buy_condition}")

            # continue monitoring                
            else:
                logging.info(f"No action taken, Price:{self.present_price}, Buy Condition:{self.buy_condition} \n")

        # when trailing buy still dormant
        elif not self.trailing_buy_state:
            # activate trailing buy if price order met
            if self.present_price <= self.price_order:
                self.trailing_buy_state = True
                self._update_buy_condition(price=self.present_price, deviation=self.deviation)
                self.buy_condition_activate_price = self.present_price
                logging.info(f"First Buy Condtion Updated, Price:{self.present_price}, Buy Condition:{self.buy_condition}")

            # wait for trailing buy activation
            else:
                logging.info(f"Waiting, Price:{self.present_price}, Price Order:{self.price_order}")
                
    def create_order(self, symbol, price_order, deviation=1):
        '''
            Create an order with trailing buy
            params: symbol (str) - ticker symbol
            params: price_order (float) - input price for order
            params: deviation (int) - price deviation for trailing percentage
        '''
        self.deviation = deviation
        self.price_order = price_order
        while not self.bought_stop:
            self._actor(symbol=symbol)
            time.sleep(2)
        
        self.bought_stop = False