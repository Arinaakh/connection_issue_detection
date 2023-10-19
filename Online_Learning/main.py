import requests
import secrets
import json

url = 'https://pro-api.coinmarketcap.com/v1/exchange/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}
r = requests.get(url)
