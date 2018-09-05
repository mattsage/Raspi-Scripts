
import json
import requests

Litecoin = float(1.0246364) #Amount of Litecoin
LitePaid = float(45) #Initial Payment

Ripplecoin = float(13.957432) #Amount of Ripplecoin
RipplePaid = float(3.75) #Inital Payment

def litecoin():
        print("***************************************")
        lite = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=GBP&limit=5$        for coin in lite.json():
                print("Litecoin Current = £" + coin["price_gbp"])
                CurrentPrice = float(coin["price_gbp"])
                value = (CurrentPrice * Litecoin)
                print("Total Litecoin Value = £" + str(value))
                diff = format(value - LitePaid, '.2f')
                print ("Profit/Loss: £" + str(diff))

def ripple():
        print("***************************************")
        ripple = requests.get('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=GBP&limit=5$        for coin in ripple.json():
                print("Ripple Current =  £" + coin["price_gbp"])
                CurrentPrice = float(coin["price_gbp"])
                value = (CurrentPrice * Ripplecoin)
                print("Total Ripple Value = £" + str(value))
                diff = format(value - RipplePaid, '.2f')
                print ("Profit/Loss: £" + str(diff))
                print("***************************************")

litecoin()
ripple()
