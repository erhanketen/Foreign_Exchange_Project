from Classes.Token import Token
from DataBase.DB import DataBase
from API.api import get_rates

def main_exn(exchange_info):
    user_id = exchange_info["user_id"]
    wallet = get_wallet(user_id)
    exchanging = exchange(exchange_info,wallet)
    if not exchanging:
        return False
    else:
        return True

def get_wallet(user_id):
    wallet = DataBase.get_wallet(user_id)
    return wallet

def exchange(exchange_info, wallet):
    values = calculate_exchange_value(exchange_info)

    if not get_permission(values[1]):
        return False

    if check_wallet(wallet,values,exchange_info["from"]):
        confirm_exchange(values,wallet,exchange_info)
        return True
    else:
        return False

def calculate_exchange_value(exchange_info):
    rates = get_rates()
    from_rate = exchange_info["from"]
    to_rate = exchange_info["to"]
    value = exchange_info["value"]

    get_value = value
    payment_value = value * (rates[from_rate] / rates[to_rate])

    values = [get_value,payment_value]
    return values


def check_wallet(wallet , values , from_rate):
    from_rate_value = 0

    for i in wallet:
        if from_rate == i["token_rate"]:
            from_rate_value += i["value"]

    if from_rate_value >= values[1]:
        return True
    else:
        return False

def confirm_exchange(values,wallet,exchange_info):
    get_value = values[0]
    payment_value = values[1]

    for i in wallet:
        if i["token_rate"] == exchange_info["from"]:
            calculation = i["value"] - payment_value
            if calculation == 0:
                DataBase.rm_token(i["token_id"])
                wallet.remove(i)
                break
            elif calculation > 0:
                i["value"] = calculation
                break
            elif calculation < 0:
                payment_value -= i["value"]
                DataBase.rm_token(i["token_id"])
                wallet.remove(i)

    new_token = Token(exchange_info["to"],get_value,exchange_info["user_id"])
    DataBase.add_token(new_token.token)

    DataBase.update_wallet(wallet,exchange_info["user_id"])

def get_exchange_rates(rates,based_on):

    calculated_rates = {
        "EUR": rates[based_on] / 1,
        "USD" : rates[based_on] / rates["USD"],
        "GBP" : rates[based_on] / rates["GBP"],
        "JPY" : rates[based_on] / rates["JPY"],
        "CHF" : rates[based_on] / rates["CHF"],
        "CAD" : rates[based_on] / rates["CAD"],
        "AUD" : rates[based_on] / rates["AUD"],
        "CNY" : rates[based_on] / rates["CNY"],
        "TRY" : rates[based_on] / rates["TRY"],
        "SAR" : rates[based_on] / rates["SAR"],
        "NZD" : rates[based_on] / rates["NZD"]
    }

    return calculated_rates

def get_permission(payment):
    print("Total Payment: {}".format(payment))
    permission = input("Do you accept the exchanging (y/n): ")
    if permission == "y":
        return True
    else:
        return False


