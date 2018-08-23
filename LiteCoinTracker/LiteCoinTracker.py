import json
import requests

r = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=GBP&limit=10')
for coin in r.json():
    print("£" + coin["price_gbp"])
