import json
import requests
from tkinter import *
import os
import main

api_key = "YOUR_KEY_HERE"
api_host = "YOUR_HOST_HERE"

def convert(cmb1, cmb2, value, result):

    currency_1 = cmb1.get()
    currency_2 = cmb2.get()
    amount = value.get()

    if(len(currency_1) == 0 or len(currency_2) == 0):
        return

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    converted_amount = data['result']['convertedAmount']

    symbol = ""

    if os.path.exists(main.mydir+"/app/symbols.json") == True:
        with open(main.mydir+'/app/symbols.json') as json_file:
            data = json.load(json_file)
            symbol = data[currency_2]

    formatted = symbol+" {:,.2f}".format(converted_amount)

    result['text'] = formatted

def loadCurrencys():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)
    symbol = []

    for symbols in data:
        symbol.append(symbols["symbol"])

    return symbol