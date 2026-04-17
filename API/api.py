import requests

def get_rates():
    api_key = "1d981d1252340d565ad10af6a83f8711"

    response = requests.get("https://data.fixer.io/api/latest?access_key="+api_key)

    rates = response.json()

    rates = rates["rates"]

    return rates

