import requests
import json

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert1(quote: str, base: str, amount: str):
        r = requests.get('https://v6.exchangerate-api.com/v6/794dc4f3271af8313b19a665/latest/USD')

        data = json.loads(r.content)['conversion_rates']

        if quote not in data:
            raise ConvertionException(f'Не удалось обработать валюту {quote}. \nВведите валюту из списка (/values)!')
        
        if base not in data:
            raise ConvertionException(f'Не удалось обработать валюту {base}. \nВведите валюту из списка (/values)!')  

        if quote == base:
            raise ConvertionException(f'Неудалось перевести валюту {base}. \nВведите разные наименования валют!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать данное количество валюты. \nКол-во  валюты должно быть числом!')
        
        if amount <= 0:
            raise ConvertionException(f'Не удалось обработать данное количество валюты. \nКол-во  валюты должно быть больше нуля!')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/794dc4f3271af8313b19a665/pair/{quote}/{base}/{amount}')

        total_base = json.loads(r.content)['conversion_result']

        return total_base
    
def show_all():
    r = requests.get('https://v6.exchangerate-api.com/v6/794dc4f3271af8313b19a665/latest/USD')
    data = json.loads(r.content)['conversion_rates']
    return data
