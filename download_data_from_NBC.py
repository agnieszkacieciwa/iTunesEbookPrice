import requests

def get_nbp_exchange_rate(currency_code):
    # Adres URL API NBP dla kursu walut
    url = f'https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/?format=json'

    try:
        # Wysyłanie zapytania do API
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy nie wystąpiły błędy

        # Parsowanie odpowiedzi JSON
        data = response.json()

        # Wyodrębnianie kursu waluty
        if 'rates' in data and len(data['rates']) > 0:
            rate = data['rates'][0]['mid']
            return rate
        else:
            return None  # Brak kursu

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas komunikacji z NBP API: {e}')
        return None

currency_code = 'USD'
exchange_rate = get_nbp_exchange_rate(currency_code)

if exchange_rate:
    print(f"Kurs waluty {currency_code}: {exchange_rate}")
else:
    print(f"Nie udało się pobrać kursu waluty {currency_code}.")
