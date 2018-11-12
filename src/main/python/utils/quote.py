import requests

def _get_quote():
  response = requests.get('https://talaikis.com/api/quotes/random/')
  return response.json()['quote']
