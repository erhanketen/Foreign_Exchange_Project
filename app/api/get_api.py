import requests

def get_api():
    api_key = "1d981d1252340d565ad10af6a83f8711"
    api_link = "https://data.fixer.io/api/latest?access_key="+api_key

    response = requests.get(api_link)

    responce = response.json()

    return responce