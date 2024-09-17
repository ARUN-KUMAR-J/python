from currency_converter import CurrencyConverter

def convert(amount,from_curr,to_curr):
    c=CurrencyConverter()
    try:
        result=c.convert(amount,from_curr,to_curr)
        print(f'{amount} {from_curr} is equal to {result} {to_curr}')
    except Exception as e:
        print(e)
amount=int(input("Enter amount:"))
from_currency=input("From currency:")
to_currency=input("To currency:")
convert(amount,from_currency,to_currency)