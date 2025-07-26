import requests

def convert(amount, from_curr, to_curr):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    rates = requests.get(url).json()['rates']
    converted = amount * rates[to_curr]
    print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")

convert(100, 'USD', 'INR')
