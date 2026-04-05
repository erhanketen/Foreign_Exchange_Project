import random
import app.DB.DB as db

""" EXCHANGES FUNCTIONS """

def generate_exchange_id():
    num = random.randint(100_000_000,999_999_999)
    exchange_id = "exchange_" + str(num)

    while True:
        if isExchangeIdUnique(exchange_id):
            return exchange_id

def isExchangeIdUnique(exchange_id):
    if db.DB_connection.isIdUnique(exchange_id,"exchanges"):
        return True
    else:
        return False



