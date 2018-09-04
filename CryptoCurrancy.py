import json
import requests

lite = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=GBP&limit=5')
for coin in lite.json():
    print("Litecoin = £" + coin["price_gbp"])

ripple = requests.get('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=GBP&limit=5')
for coin in ripple.json():
    print("Ripple =  £" + coin["price_gbp"])
