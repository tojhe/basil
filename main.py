import os
from operation.trailing_operation import TrailingBuyOperator
from operation.buy_operation import LimitOperator

API_KEY = os.environ.get("PRIVATE_API_KEY")
API_SECRET = os.environ.get("PRIVATE_API_SECRET")

def trailing_buy():
    pass 

if __name__=='__main__':

    symbol=input("Ticker Symbol: ")
    price_order=float(input("Price Order: "))
    deviation = int(input("Price Deviation: "))

    trailing_buy_host = TrailingBuyOperator(api_key=API_KEY, api_secret=API_SECRET)
    trailing_buy_host.create_order(symbol=symbol, price_order=price_order, deviation=deviation)