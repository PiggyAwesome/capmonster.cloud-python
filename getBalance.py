import requests
import json

apikey = "ENTER YOUR KEY HERE"

response = requests.post("https://api.capmonster.cloud/getBalance", json = {

    "clientKey": apikey

})
errorId = json.loads(response.text)['errorId']
try:
 balance = json.loads(response.text)['balance']
except KeyError:
    print("Invalid api key! Error code:" + f"{errorId}")
print('$'+f'{balance}'+' left')
