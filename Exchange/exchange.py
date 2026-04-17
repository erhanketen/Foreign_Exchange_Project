import Classes
import DataBase
from API.api import get_rates

def main(exchange_info):
    user_id = exchange_info["user_id"]
    wallet = get_wallet(user_id)

def get_wallet(user_id):
    wallet = DataBase.DB_connection.DataBase.get_wallet(user_id)
    return wallet

def exchange(exchange_info, wallet):
    exchange_value = calculate_exchange_value(exchange_info)

    if check_wallet(wallet,exchange_value):
        exchange = confirm_exchange(exchange_value,wallet,exchange_info)
        return exchange
    else:
        exchange = reject_exchange()
        return exchange

def calculate_exchange_value(exchange_info):
    rates = get_rates()
    from_rate = exchange_info["from"]
    to_rate = exchange_info["to"]
    value = exchange_info["value"]

    exchange_value = value * (rates[to_rate] / rates[from_rate])

    return exchange_value


def check_wallet(wallet , exchange_value):
    pass

def confirm_exchange(exchange_value,wallet,exchange_info):
    pass

def reject_exchange():
    pass