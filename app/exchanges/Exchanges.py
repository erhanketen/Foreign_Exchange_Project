import datetime
import Exchanges_funcs as exf

""" EXCHANGES CLASS """

class Exchanges:
    def __init__(self,exchange_user_id,tokens,rate_to_rate,value):
        self.exchange_id = exf.generate_exchange_id()
        self.exchange_user_id = exchange_user_id
        self.tokens = tokens
        self.rate_to_rate = rate_to_rate
        self.value = value
        self.status = self.check_status()
        self.exchanged_at = datetime.datetime.now()

    def get_exchange_info(self):
        return [self.exchange_id,self.exchange_user_id,self.tokens,self.status,self.exchanged_at]

    # This function checks if the exchange is acceptable or not.
    # If exchange is acceptable returns 'ACCEPTED', if it's not returns 'REJECTED'.
    def check_status(self):
        exchange_info = [self.exchange_id,self.exchange_user_id,self.tokens,self.rate_to_rate,self.value]
        return exf.db.DB_connection.check_exchange(exchange_info)


