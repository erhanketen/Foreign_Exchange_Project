import requests
import os
from dotenv import load_dotenv

def get_rates():
    load_dotenv()

    FIXER_API_KEY = os.getenv("FIXER_API_KEY")

    if not FIXER_API_KEY:
        raise Exception("Fixer API key not set. Please set it in .env file.")

    response = requests.get("https://data.fixer.io/api/latest?access_key="+FIXER_API_KEY)

    rates = response.json()

    rates = rates["rates"]

    return rates

