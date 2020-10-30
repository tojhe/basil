from binance.client import Client


class BaseOperator():

    def __init__(self, api_key, api_secret):
        '''
        Base Operator to connect client and start all activity
        params: api_key (str): Binance account API Key
        params: api_secret(str): API Secret to match applied API Key
        '''
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = None

    def connect(self):
        self.client = Client(api_key=self.api_key, api_secret=self.api_secret)